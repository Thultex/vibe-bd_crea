#!/usr/bin/env python3
"""Bereinigt und erweitert die allgemeinen BlinkRead-Wortlisten (WL)."""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path


LISTEN = Path(__file__).resolve().parents[1]
REPO = LISTEN.parents[1]
KORPORA = REPO / "z_wortlisten" / "korpora"
HISTORISCHE_100K = (
    KORPORA
    / "2026_local-haeufigkeitsliste_102k"
    / "leibnitz-100k.txt"
)
BRANDENBURG = (
    KORPORA
    / "2024_brandenburg-grundwortschatz_685"
    / "grundwortschatz-brandenburg-2024.txt"
)
LOKALE_HAEUFIGKEIT = (
    KORPORA
    / "2021_local-wortfrequenz-pos_864k"
    / "worte-2-6.tsv"
)
VERSION = "1.02"

WORTDATEIEN = {
    2: "de_2_Zeichen.txt",
    3: "de_3_Zeichen.txt",
    4: "de_4_Zeichen.txt",
    5: "de_5_Zeichen.txt",
    6: "de_6_Zeichen.txt",
    7: "de_7_Zeichen.txt",
    8: "de_8_Zeichen.txt",
    9: "de_9-10_Zeichen.txt",
    10: "de_9-10_Zeichen.txt",
}

# Personen, Orte, Marken, Parteien, Vereine und Institutionen aus dem alten
# Nachrichtenkorpus. Ein Treffer entfernt immer den ganzen Eintrag.
GESPERRTE_WOERTER = {
    "aachen", "adidas", "afrika", "airbus", "aldi", "alejandro", "alexander",
    "alfred", "amazon", "amerika", "amsterdam", "andreas", "angela", "anna",
    "apple", "asien", "athen", "audi", "augsburg", "axel", "bayern", "beate",
    "becker", "belgien", "benjamin", "berlin", "berliner", "berlins", "bernd",
    "bertelsmann", "bielefeld", "bill", "birgit", "bochum", "bonn", "boris",
    "borussia", "brandenburg", "braunschweig", "bremen", "bremer", "brüssel",
    "bundesliga", "bundestag", "bundeswehr", "bush", "catterfeld", "cdu",
    "charlotte", "china", "christian", "christine", "claudia", "coca-cola",
    "cologne", "daimler", "david", "dell", "dennis", "deutsche", "deutscher",
    "deutschland", "dieter", "dortmund", "dresden", "dynamo", "düsseldorf",
    "düsseldorfer", "e.on", "ebay", "eisbären", "emil", "emma", "erfurt",
    "ericsson", "essen", "europa", "facebook", "fdp", "fifa", "fischer",
    "ford", "frank", "frankfurt", "franz", "freiburg", "fortuna", "gelsenkirchen",
    "george", "gerd", "google", "göttingen", "greifswald", "gysi", "hamburg",
    "hamburger", "hannover", "hans", "heesters", "heidelberg", "heike", "heinz",
    "helmut", "hertha", "hessen", "heute-journal", "hoeneß", "honda", "hsv",
    "ibm", "ikea", "indien", "ingolstadt", "instagram", "italien", "japan",
    "jens", "joachim", "johannes", "jürgen", "kaiserslautern", "karin", "karlsruhe",
    "karlsruher", "kassel", "kathrin", "kiel", "klaus", "kohl", "köln", "kölner",
    "leipzig", "lidl", "london", "lufthansa", "lübeck", "lüneburg", "madrid",
    "magdeburg", "manfred", "maria", "markus", "martin", "martina", "mcdonald's",
    "mcdonalds", "mercedes", "merkel", "merz", "michael", "microsoft", "münchen",
    "münchner", "münster", "nike", "nintendo", "nokia", "nürnberg", "olympia",
    "olympisch", "olympische", "opel", "osnabrück", "otto", "paris", "paul",
    "peter", "peugeot", "philipp", "porsche", "potsdam", "prag", "ralf", "rewe",
    "rheinland", "robert", "rostock", "rtl", "ruhrgebiet", "russland", "sabine",
    "saarland", "samsung", "sandra", "schalke", "schleswig-holstein", "schmidt",
    "schneider", "schröder", "schweiz", "siemens", "sony", "spd", "stefan",
    "steffi", "stuttgart", "sven", "telekom", "thomas", "thüringen", "tina",
    "tobias", "toyota", "türkei", "twitter", "udo", "uwe", "valverde", "vatikan",
    "volkswagen", "wagner", "wien", "wolfgang", "würzburg", "yahoo", "yvonne",
    "zalando", "zdf", "zürich",
}

# Weitere kurze oder mehrdeutige Eigennamen aus den Einzelwortlisten. Sie
# stehen getrennt, damit die kompakte Hauptliste lesbar bleibt.
GESPERRTE_WOERTER.update("""
albert alex alpen andrea anton australien bayer beck berger brasilien christoph
daniel dax dänemark dirk england ernst erwin eva felix finnland florian frankreich
fritz georg gerhard günter hagen harald harry holger horst huber irak iran irland
islam israel jakob james jan jena jesus jochen johann jones jörg josef julia kanada
karl katrin katja kevin kieler köhler kurt lisa lkw löw ludwig mainz marc marco mark
mario matthias mexiko meyer monika moskau obama olaf oliver ostsee patrick peking petra
pkw polen portugal rainer roland rolf rom roman roth rudolf schmid schulz schweden
sebastian simon spanien st stephan susanne tecdax tim tokio tom ulrich ungarn usd vfl
volker walter weber werder werner wiener willi york
aachener albrecht arcandor barbara bernhard bochumer brigitte budapest chemnitz chinesen
christen christus clinton cottbus dietrich dresdner duisburg europäer europas eurozone
ferrari franken franzose gabriel gabriele georgien griechen günther hamilton hartmut
heinrich herbert hermann hoffmann hongkong indianer infineon israelis istanbul japaner
kroatien lehmann londoner lübecker mainzer mallorca mannheim norbert pakistan postbank
reinhard renault richard rumänien rüttgers sachsen salzburg schäuble schwaben schwerin
seehofer serbien shanghai spanier spd-chef steffen stoiber südkorea thailand thorsten
tübingen wilhelm williams windows zürcher
amerikaner augsburger barcelona bayerische berlusconi bundesbank bundesrat darmstadt
demokraten deutschen dortmunder ebit-marge elisabeth engländer franzosen friedrich
göppingen hollywood italiener javascript katharina klinsmann lafontaine leipziger
leverkusen münchener nordkorea oldenburg österreich reutlingen schumacher schweizer
selbstmord siegfried steinbrück steinmeier südafrika thüringer tschechien us-börsen
us-dollar washington wiesbaden wolfsburg
nazis pfennig
amerikaner augsburger barcelona berlusconi bundesbank bundesrat darmstadt demokraten
dortmunder elisabeth engländer franzosen friedrich göppingen italiener katharina
klinsmann lafontaine leipziger leverkusen münchener nordkorea oldenburg österreich
reutlingen schumacher schweizer siegfried steinbrück steinmeier südafrika thüringer
tschechien washington wiesbaden wolfsburg zimmermann
composite javascript
max
""".split())

NEUE_WOERTER = """
ab am an da du eh Ei er es im in ja je ob oh Öl Po so um wo zu
Ast Axt Bad Ball Bau Bär Beet Bein Berg Bild Birne Blatt Blut Boot Brot Buch Bus Dach
Dampf Decke Dieb Ding Dorf Draht Ei Eis Eule Fach Fass Fell Feld Fels Feuer Fisch Fluss
Frosch Fuß Gabel Gang Garten Gas Glas Gras Hahn Hals Hand Hase Haus Heft Herd Holz Horn
Hose Hund Huhn Igel Jacke Kamm Kanne Karte Käfer Keks Kerze Kiste Kleid Knie Knopf Koch
Kohle Korb Krug Kuh Laden Lampe Laub Löwe Luft Maus Mehl Messer Milch Mond Moos Mütze
Nadel Nagel Nase Nest Netz Ofen Ohr Paket Pfad Pferd Pilz Pinsel Rad Regen Ring Rock Rohr
Rose Sack Saft Salz Sand Schaf Schal Schiff Schuh Seife Seil Senf Sofa Sonne Stall Stein
Stern Stift Stuhl Suppe Tasse Teich Teller Topf Tor Turm Uhr Vase Vogel Wald Wand Wanne
Wasser Weg Weide Wiese Wind Wolf Wolle Wurm Zahn Zaun Zelt Ziege Zug
alt arm blank blau braun breit bunt dick dünn eng fest flach glatt grau grün hart heiß
hell hoch kalt klar klein kurz lang laut leer leise nass neu offen rau rund sauber schief
schnell schwer spitz stark still tief trocken warm weich weiß wild
backen baden bauen bellen biegen bohren braten fallen fegen füllen geben graben halten
hämmern heben holen hüpfen kaufen kleben kochen lachen laufen legen lesen malen mähen
nähen öffnen packen pflanzen pusten reiben rollen rufen sägen sammeln schieben schneiden
schreiben schwimmen sehen sitzen spielen springen stehen tragen trinken waschen werfen
winken ziehen
Abend Ampel Anker Apfel Amsel Bagger Balkon Banane Besen Beutel Biene Birke Bohne Brille
Bürste Butter Eimer Ente Erbse Esel Faden Feder Fenster Flasche Gabel Gans Gießkanne
Glocke Gurke Hammer Harke Hecke Herdplatte Hocker Insel Kachel Kanne Kappe Karren Keller
Kirsche Kissen Klammer Koffer Kuchen Leiter Löffel Lupe Mantel Mauer Möhre Muschel Nuss
Pappe Pfanne Pflaster Pfütze Rasen Raupe Regal Reifen Riegel Rinde Roller Salat Schale
Scheune Schere Schirm Schlitten Schrank Schraube Socke Spiegel Spinne Tasche Taube Topf
Treppe Trommel Tüte Waffel Walze Wippe Wolke Zange Zebra Ziegel Zwiebel
Badewanne Backblech Bleistift Brotdose Brotmesser
Feuerholz Fußmatte Gartenbank Gartentor Handbesen
Haustür Holzbrett Kinderbett Kochlöffel Müllbeutel
Obstschale Pappkarton Regenjacke Sandkasten
Sonnenhut Teekanne Vogelhaus Wasserhahn Wäschekorb Werkzeug
Zahnbürste Zeitung Zeltplane
""".split()

# Kurze, konkrete Ergänzungen außerhalb des historischen Bestands. Die
# Brandenburger Grundwörter bis sechs Zeichen werden zusätzlich dynamisch
# eingelesen, damit die amtliche Referenz nicht im Skript dupliziert wird.
NEUE_KURZWOERTER = """
au ha hm na
Aal Aas Ass Boa Deo Fee Fön Hai Klo Lid Oma Opa Sau Ski Tau Wal Wok Öse
fit rar roh zäh
Ahle Alge Boje Bock Brei Damm Düse Eber Elch Farn Floh Garn Harz Hefe Ibis Kanu
Keil Klee Kohl Kran Laib Laus Lehm Luke Mais Mast Mohn Moor Mops Möwe Muli Pfau
Pult Rebe Reis Riff Rübe Saat Säge Teer Tuch Tube Uhu Wels Zopf Kiwi
äsen faul fein flau froh lahm matt müde nett reif rosa säen wach zart
Acker Ahorn Angel Blase Borke Brett Daune Dohle Dolch Eiche Euter Falke Fasan
Feile Feger Garbe Hafer Honig Hirse Iltis Kamel Kelle Klaue Klotz Kröte Lachs
Laken Leine Linse Luchs Molch Nelke Otter Pfahl Pudel Quark Ranke Sirup Spatz
Speck Speer Spule Toast Truhe Wachs Wespe Zeder
atmen eckig eilen flink frech kauen nagen sauer tauen toben
Ameise Becher Dattel Eichel Fichte Fliese Fohlen Gitter Hummel Kessel
Kiefer Korken Kreide Krücke Lärche Marder Nudeln Oliven Qualle Ranzen Raspel
Rechen Rüssel Schilf Sichel Spaten Storch
angeln bissig blasen brauen heulen kehren kneten lecken melken rudern salzig
stumpf wühlen zottig zupfen
""".split()

# Manuell geprüfte, kurze Ergänzungen aus der lokalen POS-/Häufigkeitsliste.
# Die Quelle enthält auch Flexionsformen, Satzanfänge und Fachsprache; deshalb
# werden nur diese allgemein verständlichen Einträge übernommen.
NEUE_LOKALE_WOERTER = """
ah tu
bei kam gab ins sei zog hin lag her sah per gar bot tun ums mag tot bat via las
hob Lok tut lud dir wog Jet Kot wem Alm Heu ach wen Huf arg war
eine nahm ging trat fand dazu nahe lebt fiel will oben trug lief fort traf fuhr
rein legt jene sagt sang wies Bass rief sank wahr samt Male half litt flog quer
warf aufs Stab baut treu halb Null Funk Zoll ruft grob fing Blei Vieh ruht gebe
hebt Kalk Watt Deck Maul Leib Mine Korn Gase Tank Zink fern rege Bart kahl Darm
hing warb Sarg Lama Loge riss egal Zinn Joch
""".split()

NICHT_UEBERNEHMEN = {"fleiss"}

def normalisieren(text: str) -> str:
    return " ".join(text.replace("\ufeff", "").strip().split())


def tokens(text: str) -> list[str]:
    return re.findall(r"[A-Za-zÄÖÜäöüß]+(?:[-'][A-Za-zÄÖÜäöüß]+)*", text)


def ist_gesperrt(text: str) -> bool:
    if any(ch.isdigit() for ch in text):
        return True
    for token in tokens(text):
        if token.casefold() in GESPERRTE_WOERTER:
            return True
        if len(token) >= 2 and token.isupper():
            return True
    return False


def lesen(path: Path) -> list[str]:
    if not path.exists():
        return []
    return [normalisieren(line) for line in path.read_text(encoding="utf-8-sig").splitlines()]


def historische_raenge() -> dict[str, int]:
    raenge: dict[str, int] = {}
    for rang, wort in enumerate(lesen(HISTORISCHE_100K), 1):
        raenge.setdefault(wort.casefold(), rang)
    return raenge


def brandenburg_woerter() -> dict[str, str]:
    return {wort.casefold(): wort for wort in lesen(BRANDENBURG)}


def lokale_haeufigkeiten() -> dict[str, int]:
    haeufigkeiten: dict[str, int] = {}
    zeilen = LOKALE_HAEUFIGKEIT.read_text(encoding="utf-8-sig").splitlines()
    for zeile in zeilen[1:]:
        teile = zeile.split("\t")
        if len(teile) < 2:
            continue
        wort, anzahl = teile[:2]
        try:
            wert = int(anzahl)
        except ValueError:
            continue
        schluessel = wort.casefold()
        haeufigkeiten[schluessel] = max(haeufigkeiten.get(schluessel, 0), wert)
    return haeufigkeiten


def eindeutig(zeilen: list[str]) -> list[str]:
    ergebnis: list[str] = []
    gesehen: set[str] = set()
    for zeile in zeilen:
        schluessel = zeile.casefold()
        if zeile and schluessel not in gesehen:
            gesehen.add(schluessel)
            ergebnis.append(zeile)
    return ergebnis


def schreiben(path: Path, zeilen: list[str]) -> None:
    path.write_text("\n".join(zeilen) + "\n", encoding="utf-8", newline="\n")


def fortschritt(label: str, aktuell: int, gesamt: int) -> None:
    if gesamt < 20:
        return
    intervall = max(1, gesamt // 20)
    if aktuell not in {1, gesamt} and aktuell % intervall:
        return
    breite = 28
    gefuellt = round(breite * aktuell / gesamt)
    balken = "#" * gefuellt + "-" * (breite - gefuellt)
    ende = "\n" if aktuell == gesamt else "\r"
    print(f"{label:<12} [{balken}] {aktuell:>4}/{gesamt}", end=ende, flush=True)


def planen() -> dict:
    wortdateien = sorted(set(WORTDATEIEN.values()))
    dateinamen = wortdateien + ["de_Spezial_Doppelkonsonanten.txt"]
    vorher = {name: lesen(LISTEN / name) for name in dateinamen}
    nachher: dict[str, list[str]] = {name: [] for name in dateinamen}
    gesehen: dict[str, set[str]] = {name: set() for name in dateinamen}
    entfernt: list[tuple[str, str, str]] = []
    verschoben: list[tuple[str, str, str]] = []
    ergaenzt: list[tuple[str, str, int | None, bool, int | None]] = []
    raenge = historische_raenge()
    brandenburg = brandenburg_woerter()
    lokale_werte = lokale_haeufigkeiten()
    gesamt = sum(len(v) for v in vorher.values())
    aktuell = 0

    # Falsch einsortierte Alteinträge werden anhand ihrer wirklichen Länge
    # verschoben; dadurch werden sie nicht nur wegen eines alten Ablagefehlers
    # verworfen.
    for dateiname in wortdateien:
        for wort in vorher[dateiname]:
            aktuell += 1
            fortschritt("Analysiere", aktuell, gesamt)
            zielname = WORTDATEIEN.get(len(wort))
            if not wort:
                entfernt.append((dateiname, wort, "leer"))
                continue
            if ist_gesperrt(wort):
                entfernt.append((dateiname, wort, "gesperrt"))
                continue
            if not zielname:
                entfernt.append((dateiname, wort, "keine passende Wortlänge"))
                continue
            schluessel = wort.casefold()
            if schluessel in gesehen[zielname]:
                entfernt.append((dateiname, wort, "Dublette"))
                continue
            gesehen[zielname].add(schluessel)
            nachher[zielname].append(wort)
            if zielname != dateiname:
                verschoben.append((wort, dateiname, zielname))

    spezialname = "de_Spezial_Doppelkonsonanten.txt"
    for wort in vorher[spezialname]:
        aktuell += 1
        fortschritt("Analysiere", aktuell, gesamt)
        schluessel = wort.casefold()
        if not wort or ist_gesperrt(wort):
            entfernt.append((spezialname, wort, "leer oder gesperrt"))
        elif schluessel in gesehen[spezialname]:
            entfernt.append((spezialname, wort, "Dublette"))
        else:
            gesehen[spezialname].add(schluessel)
            nachher[spezialname].append(wort)

    kurze_grundwoerter = [
        wort
        for wort in brandenburg.values()
        if 2 <= len(wort) <= 6 and wort.casefold() not in NICHT_UEBERNEHMEN
    ]
    for wort in (
        NEUE_WOERTER
        + NEUE_KURZWOERTER
        + NEUE_LOKALE_WOERTER
        + kurze_grundwoerter
    ):
        dateiname = WORTDATEIEN.get(len(wort))
        if not dateiname or ist_gesperrt(wort):
            continue
        schluessel = wort.casefold()
        if schluessel not in gesehen[dateiname]:
            gesehen[dateiname].add(schluessel)
            nachher[dateiname].append(wort)
            ergaenzt.append(
                (
                    dateiname,
                    wort,
                    raenge.get(schluessel),
                    schluessel in brandenburg,
                    lokale_werte.get(schluessel),
                )
            )

    return {
        "vorher": vorher,
        "nachher": nachher,
        "entfernt": entfernt,
        "verschoben": verschoben,
        "ergaenzt": ergaenzt,
    }


def vorschau(plan: dict) -> None:
    print("\nÄnderungsvorschau")
    print(f"1/3 Entfernen ({len(plan['entfernt'])})")
    for dateiname, wort, grund in plan["entfernt"]:
        print(f"  - {dateiname}: {wort!r} ({grund})")
    print(f"2/3 Verschieben ({len(plan['verschoben'])})")
    for wort, quelle, ziel in plan["verschoben"]:
        print(f"  - {wort!r}: {quelle} -> {ziel}")
    print(f"3/3 Ergänzen ({len(plan['ergaenzt'])})")
    for dateiname, wort, rang, in_brandenburg, lokale_anzahl in plan["ergaenzt"]:
        quellen = [
            f"Rang {rang} in historischer 100k-Liste"
            if rang else "nicht in historischer 100k-Liste"
        ]
        if in_brandenburg:
            quellen.append("Grundwortschatz Brandenburg 2024")
        if lokale_anzahl is not None:
            quellen.append(f"lokale Häufigkeit {lokale_anzahl}")
        print(f"  + {dateiname}: {wort} [{'; '.join(quellen)}]")


def backup_anlegen(plan: dict) -> Path:
    backup_root = LISTEN / "backups"
    zeitstempel = datetime.now().strftime("%Y%m%d-%H%M%S")
    ziel = backup_root / zeitstempel
    nummer = 2
    while ziel.exists():
        ziel = backup_root / f"{zeitstempel}-{nummer}"
        nummer += 1
    ziel.mkdir(parents=True)
    dateien = [name for name in plan["vorher"] if (LISTEN / name).exists()]
    for nr, dateiname in enumerate(dateien, 1):
        shutil.copy2(LISTEN / dateiname, ziel / dateiname)
        fortschritt("Backup", nr, len(dateien))
    (ziel / "README.txt").write_text(
        "Automatisches Backup vor build_wordlists.py\n"
        f"Version: {VERSION}\n"
        f"Entfernen: {len(plan['entfernt'])}\n"
        f"Verschieben: {len(plan['verschoben'])}\n"
        f"Ergänzen: {len(plan['ergaenzt'])}\n",
        encoding="utf-8",
        newline="\n",
    )
    return ziel


def anwenden(plan: dict) -> int:
    geaenderte_dateien = [
        name for name in plan["nachher"]
        if plan["vorher"][name] != plan["nachher"][name]
    ]
    for nr, dateiname in enumerate(geaenderte_dateien, 1):
        schreiben(LISTEN / dateiname, plan["nachher"][dateiname])
        fortschritt("Schreibe", nr, len(geaenderte_dateien))
    return len(geaenderte_dateien)


def pruefe_daten(daten: dict[str, list[str]]) -> list[str]:
    fehler: list[str] = []
    for dateiname, zeilen in sorted(daten.items()):
        if len(zeilen) != len({zeile.casefold() for zeile in zeilen}):
            fehler.append(f"{dateiname}: enthält Dubletten")
        for nr, zeile in enumerate(zeilen, 1):
            if not zeile:
                fehler.append(f"{dateiname}:{nr}: leere Zeile")
            if ist_gesperrt(zeile):
                fehler.append(f"{dateiname}:{nr}: gesperrter Eintrag {zeile!r}")
        if dateiname.startswith("de_") and "Phrasen" not in dateiname and dateiname != "de_Spezial_Doppelkonsonanten.txt":
            erlaubte_laengen = {9, 10} if dateiname == "de_9-10_Zeichen.txt" else {
                laenge for laenge, name in WORTDATEIEN.items() if name == dateiname
            }
            for nr, wort in enumerate(zeilen, 1):
                if len(wort) not in erlaubte_laengen:
                    fehler.append(
                        f"{dateiname}:{nr}: {len(wort)} statt erwarteter Länge: {wort!r}"
                    )
    return list(dict.fromkeys(fehler))


def pruefen() -> list[str]:
    dateinamen = set(WORTDATEIEN.values()) | {"de_Spezial_Doppelkonsonanten.txt"}
    daten = {
        name: lesen(LISTEN / name)
        for name in sorted(dateinamen)
        if (LISTEN / name).exists()
    }
    return pruefe_daten(daten)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="BlinkRead-Einzelwörter sichern, bereinigen, ergänzen und prüfen."
    )
    parser.add_argument("--check", action="store_true", help="nur den Bestand prüfen")
    parser.add_argument(
        "--apply", action="store_true", help="angezeigte Änderungen sichern und anwenden"
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    args = parser.parse_args()

    if not LISTEN.is_dir() or LISTEN.is_symlink():
        print(f"FEHLER: ungültiges BlinkRead-Verzeichnis: {LISTEN}", file=sys.stderr)
        return 1
    if not args.check:
        for referenz in (HISTORISCHE_100K, BRANDENBURG, LOKALE_HAEUFIGKEIT):
            if not referenz.is_file():
                print(f"FEHLER: Referenzliste fehlt: {referenz}", file=sys.stderr)
                return 1

    if not args.check:
        plan = planen()
        vorschau(plan)
        hat_aenderungen = plan["vorher"] != plan["nachher"]
        if not hat_aenderungen:
            print("Keine Änderungen nötig; es wurde kein Backup angelegt.")
        elif not args.apply:
            print("Vorschau beendet; mit --apply sichern und anwenden.")
            return 0
        else:
            planfehler = pruefe_daten(plan["nachher"])
            if planfehler:
                print("\n".join(f"FEHLER: {text}" for text in planfehler), file=sys.stderr)
                print("Nicht angewendet: Der geplante Zielbestand ist ungültig.", file=sys.stderr)
                return 1
            backup = backup_anlegen(plan)
            anzahl = anwenden(plan)
            print(f"Backup: {backup.relative_to(LISTEN)}")
            print(
                f"Angewendet: {len(plan['entfernt'])} entfernt, "
                f"{len(plan['verschoben'])} verschoben, {len(plan['ergaenzt'])} ergänzt "
                f"in {anzahl} Dateien."
            )
    fehler = pruefen()
    if fehler:
        print("\n".join(f"FEHLER: {fehlertext}" for fehlertext in fehler), file=sys.stderr)
        return 1
    print("WL-Prüfung: keine Dubletten, Sperrtreffer oder falschen Wortlängen.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
