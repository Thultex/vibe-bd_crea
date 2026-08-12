'use strict';

const fs = require('fs');
const path = require('path');

const toolRoot = __dirname;
const repoRoot = path.resolve(toolRoot, '..', '..', '..');
const sourcePath = path.join(toolRoot, 'index.html');
const swPath = path.join(toolRoot, 'sw.js');
const shareRoot = path.join(repoRoot, 'share', 'apps', 'emotronic');
const audioRoot = path.join(repoRoot, 'assets', 'audio', 'emotronic');

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

function read(file) {
  return fs.readFileSync(file);
}

function sameBytes(left, right, label) {
  assert(Buffer.compare(read(left), read(right)) === 0, `${label} ist nicht bytegleich`);
}

const html = read(sourcePath).toString('utf8');
for (const match of html.matchAll(/<script>([\s\S]*?)<\/script>/g)) {
  new Function(match[1]);
}

const dataStart = html.indexOf('const APP_META=');
const dataEnd = html.indexOf('let audioCtx=null;');
assert(dataStart >= 0 && dataEnd > dataStart, 'Datentabellen nicht gefunden');
const data = new Function(
  `${html.slice(dataStart, dataEnd)};return {APP_META,APP_CONFIG,base,order,combos,comboOverview,soundPatterns,specialSoundPatterns,SHARE_BASE_KEYS,SHARE_COMBO_KEYS,sharedStateNumber,sharedStateItem,encodeCompactHistory,decodeCompactHistory,encodeCompactScore,decodeCompactScore,replayEmojiText};`
)();

const keyboardStart = html.indexOf('const keyboardEmotionMap=');
const keyboardEnd = html.indexOf('function currentGridKey()', keyboardStart);
assert(keyboardStart >= 0 && keyboardEnd > keyboardStart, 'Tastaturtabellen nicht gefunden');
const keyboard = new Function(
  `${html.slice(keyboardStart, keyboardEnd)};return {keyboardEmotionMap,keyGrid};`
)();

const expectedGrid = [
  'joy', 'affection', 'curiosity',
  'anger', 'neutral', 'fear',
  'disgust', 'shame', 'sadness'
];
assert(JSON.stringify(data.order) === JSON.stringify(expectedGrid), 'Das sichtbare Rad ist nicht korrekt an der Y-Achse gespiegelt');
assert(JSON.stringify(keyboard.keyGrid.flat()) === JSON.stringify(expectedGrid), 'Pfeiltastengitter stimmt nicht mit dem Rad überein');
const digitCodes = ['Digit7', 'Digit8', 'Digit9', 'Digit4', 'Digit5', 'Digit6', 'Digit1', 'Digit2', 'Digit3'];
assert(JSON.stringify(digitCodes.map(code => keyboard.keyboardEmotionMap[code])) === JSON.stringify(expectedGrid), 'Zifferntasten stimmen nicht mit dem Rad überein');
assert((html.match(/const choices=\{joy:'Leicht',neutral:'Normal',sadness:'Profi'\}/g) || []).length === 2, 'Simon-Auswahl liegt nicht auf Freude, Neutral und Trauer');
assert((html.match(/const selection=\{joy:'easy',neutral:'normal',sadness:'pro'\}/g) || []).length === 2, 'Simon-Moduszuordnung liegt nicht auf Freude, Neutral und Trauer');
assert(!html.includes('powerOffAndClearHistoryFromNeutral'), 'Neutral darf den Ausschalter nicht auslösen');
assert(html.includes("state.selected='neutral';state.displayKey='neutral';state.intensity=0"), 'Neutral ist nicht als wiederholt wählbarer Grundzustand umgesetzt');
assert(/cancelReplayToReady\(\);\r?\n state\.powerArmed=true;/.test(html), 'Der erste Ausschalter-Klick wechselt nicht zu Bereit und leert die Historie');
assert(html.includes('function gameBonusTiming(extraMs=0)'), 'Modusabhängige Dauer der Simon-Zwischenanimation fehlt');
assert(html.includes('function showGameBonusFrame(stage,text,index)'), 'Dynamische Simon-Zwischenanimation fehlt');
assert(html.includes('game-bonus-milestone'), 'Hervorhebung der Simon-Zehnerschritte fehlt');

const expectedBase = {
  curiosity: ['Neugier', ['interessiert', 'neugierig', 'fasziniert'], ['1F60F', '1FAE2', '1F929'], '#83d4cf'],
  affection: ['Zuneigung', ['freundlich', 'zugewandt', 'verbunden'], ['1F609', '1F917', '1F970'], '#f4b56d'],
  joy: ['Freude', ['zufrieden', 'fröhlich', 'begeistert'], ['1F60C', '1F60A', '1F602'], '#f5df6f'],
  anger: ['Wut', ['gereizt', 'verärgert', 'wütend'], ['1F612', '1F620', '1F92C'], '#ef938b'],
  disgust: ['Ekel', ['abgeneigt', 'angeekelt', 'übel'], ['1F62C', '1F616', '1F922'], '#6f9f68'],
  shame: ['Scham', ['verlegen', 'befangen', 'beschämt'], ['1F605', '1F633', '1FAE3'], '#bfe36f'],
  sadness: ['Trauer', ['bedrückt', 'traurig', 'trauernd'], ['1F641', '1F622', '1F62D'], '#6381d7'],
  fear: ['Angst', ['besorgt', 'ängstlich', 'panisch'], ['1F61F', '1F628', '1F631'], '#c2a8dc'],
  neutral: ['Neutral', ['ausgeglichen'], ['1F610'], '#ddd9d0']
};
for (const [key, [category, labels, codes, color]] of Object.entries(expectedBase)) {
  const item = data.base[key];
  assert(item, `Grundemotion fehlt: ${key}`);
  assert(item.category === category, `Falscher Emotionsname für ${key}`);
  assert(JSON.stringify(item.labels) === JSON.stringify(labels), `Falsche Gefühlswörter für ${category}`);
  assert(JSON.stringify(item.codes) === JSON.stringify(codes), `Falsche Emojis für ${category}`);
  assert(item.color === color, `Falsche Basisfarbe für ${category}`);
}

const expectedCombos = {
  'curiosity|affection': ['Bewunderung', 'affection', '1F60D', 'bewunderung'],
  'affection|joy': ['Dankbarkeit', 'joy', '1F979', 'dankbarkeit'],
  'joy|anger': ['Streitlust', 'anger', '1F608', 'streitlust'],
  'anger|disgust': ['Abwertung', 'disgust', '1F644', 'abwertung'],
  'disgust|shame': ['Unbehagen', 'shame', '1F623', 'unbehagen'],
  'shame|sadness': ['Reue', 'sadness', '1F61E', 'reue'],
  'sadness|fear': ['Aufgeben', 'fear', '1F629', 'aufgeben'],
  'fear|curiosity': ['Überraschung', 'curiosity', '1F632', 'ueberraschung']
};
for (const [pair, [name, anchor, code, audioName]] of Object.entries(expectedCombos)) {
  assert(data.combos[pair]?.name === name, `Falsche Sekundäremotion für ${pair}`);
  assert(data.combos[pair]?.code === code, `Falsches Gesichts-Emoji für ${name}`);
  assert(data.combos[pair]?.audioName === audioName, `Falscher Audio-Name für ${name}`);
  assert(data.comboOverview[anchor] === pair, `${name} liegt nicht auf ${data.base[anchor].category}`);
  assert(!/\s/.test(name), `${name} ist nicht einwortig`);
}

for (const [key, levels] of Object.entries(data.soundPatterns)) {
  if (key === 'neutral') continue;
  const counts = levels.map(notes => notes.length);
  assert(counts[0] === 2 && counts[1] === 3 && counts[2] >= 3 && counts[2] <= 4, `${key} überschreitet die gemeinsamen Grenzen 2/3/4`);
}
assert(JSON.stringify(data.soundPatterns.anger.map(notes => notes.length)) === JSON.stringify([2, 3, 4]), 'Wut verwendet nicht 2/3/4 Töne');
assert(JSON.stringify(data.soundPatterns.anger[1]) === JSON.stringify([330, 196, 277]), 'Mittlere Wut-Stufe ist nicht dynamisch gestimmt');
assert(JSON.stringify(data.soundPatterns.sadness) === JSON.stringify([[392, 330], [440, 370, 294], [440, 349, 294, 220]]), 'Trauer ist nicht dunkel gestimmt');

const emojiOwners = [];
for (const [key, item] of Object.entries(data.base)) {
  for (const code of item.codes) emojiOwners.push([code, key]);
}
for (const [key, item] of Object.entries(data.combos)) emojiOwners.push([item.code, key]);
const seenEmoji = new Set();
for (const [code, owner] of emojiOwners) {
  assert(!seenEmoji.has(code), `Doppeltes Emoji ${code} bei ${owner}`);
  seenEmoji.add(code);
}

const words = [];
for (const item of Object.values(data.base)) words.push(item.category, ...item.labels);
for (const item of Object.values(data.combos)) words.push(item.name);
const normalizedWords = words.map(word => word.toLocaleLowerCase('de-DE'));
assert(new Set(normalizedWords).size === normalizedWords.length, 'Emotions- oder Gefühlswort ist doppelt');

const asciiOwners = [];
for (const [key, item] of Object.entries(data.base)) {
  const expectedLevels = key === 'neutral' ? 1 : 3;
  assert(item.ascii.length === expectedLevels, `Falsche Zahl ASCII-Stufen für ${item.category}`);
  item.ascii.forEach((frames, index) => {
    assert(frames.length === 3, `ASCII-Animation für ${item.category} Stufe ${index + 1} hat nicht drei Frames`);
    asciiOwners.push([frames.at(-1), `${item.category} ${index + 1}`]);
  });
}
for (const item of Object.values(data.combos)) {
  assert(item.ascii.length === 3, `ASCII-Animation für ${item.name} hat nicht drei Frames`);
  asciiOwners.push([item.ascii.at(-1), item.name]);
}
const seenAscii = new Set();
for (const [motif, owner] of asciiOwners) {
  assert(/^[\x20-\x7e]+$/.test(motif), `ASCII-Motiv für ${owner} enthält Nicht-ASCII-Zeichen`);
  assert(motif.length <= 7, `ASCII-Motiv für ${owner} ist zu breit`);
  assert(!seenAscii.has(motif), `Doppeltes ASCII-Motiv ${motif} bei ${owner}`);
  seenAscii.add(motif);
}
for (const motion of ['curiosity','affection','joy','fear','neutral','anger','sadness','shame','disgust','bewunderung','dankbarkeit','streitlust','abwertung','unbehagen','reue','aufgeben','ueberraschung']) {
  assert(html.includes(`ascii-${motion}`), `Eigene ASCII-Bewegung fehlt: ${motion}`);
}

const compactStates = [
  { key: 'neutral', intensity: 0 },
  ...data.SHARE_BASE_KEYS.flatMap(key => [1, 2, 3].map(intensity => ({ key, intensity }))),
  ...data.SHARE_COMBO_KEYS.map(combo => ({ combo, colorParts: data.combos[combo].partners }))
];
assert(compactStates.length === 33, 'Kurzcode bildet nicht genau 33 Zustände ab');
const compactCode = data.encodeCompactHistory(compactStates, 40);
assert(compactCode.length === compactStates.length, 'Kurzcode verwendet nicht genau ein Zeichen pro Zustand');
assert(/^[0-9a-w]+$/.test(compactCode), 'Kurzcode ist nicht reines Base36 im Bereich 0-w');
const compactRoundTrip = data.decodeCompactHistory(compactCode, 40);
assert(compactRoundTrip?.length === compactStates.length, 'Kurzcode-Verlauf lässt sich nicht vollständig lesen');
compactStates.forEach((state, index) => {
  assert(data.sharedStateNumber(compactRoundTrip[index]) === data.sharedStateNumber(state), `Kurzcode-Rückweg weicht an Position ${index} ab`);
});
const normalScore = { type: 'score', score: 123, mode: 'normal', sequence: [{ key: 'joy', level: 2 }, { combo: true, first: 'curiosity', second: 'affection' }] };
const normalScoreCode = data.encodeCompactScore(normalScore);
assert(normalScoreCode === '3f~2p', 'Normaler Score enthält redundante Angaben');
assert(JSON.stringify(data.decodeCompactScore(normalScoreCode)) === JSON.stringify(normalScore), 'Normaler Score-Kurzcode ist nicht verlustfrei');
const proScore = { ...normalScore, mode: 'pro' };
assert(data.encodeCompactScore(proScore) === '3f.p~2p', 'Abweichender Modus wird nicht knapp codiert');
const emojiReplayText = data.replayEmojiText([
  { key: 'joy', intensity: 2 },
  { key: 'neutral', intensity: 0 },
  { combo: 'anger|disgust', colorParts: ['anger', 'disgust'] }
]);
assert(emojiReplayText === '😊 😐 🙄', 'Replay-Emojis werden nicht in zeitlicher Reihenfolge als Text erzeugt');
assert(data.APP_CONFIG?.share?.multiTapMs === 520, 'Zeitfenster für Mehrfachtipps weicht vom Standard ab');
assert(html.includes('state.phoneTapCount===3') && html.includes('shareSlowReplayFromPhone()'), 'Telefon-Dreifachtipp teilt keinen Slow-Replay');
assert(html.includes('if(taps===2)shareReplayFromPhone();else if(taps===1)runPhoneSingleTap()'), 'Telefon-Einzel- und Doppeltipp werden nicht verzögert unterschieden');
assert(html.includes('if(doubled){event.preventDefault();shareReplayEmojisFromWifi();return}'), 'Wifi-/Sender-Doppeltipp teilt keine Replay-Emojis');
assert(html.includes("/^#(share|replay|slow|score)="), 'Ausgeschriebene Fragmentnamen fehlen');
assert(html.includes('if(!payload)payload=decodeSharePayload(value)'), 'Alte lange Links werden nicht als Rückfall gelesen');
for (const fragment of ['#share=', '#score=']) {
  assert(html.includes(fragment), `Ausgeschriebener Kurzlink fehlt: ${fragment}`);
}
assert(html.includes("fragmentOverride==='slow'?'slow':'replay'"), 'Replay und Slow werden nicht ausgeschrieben erzeugt');
for (const fragment of ['#e=', '#r=', '#s=', '#g=']) {
  assert(!html.includes(fragment), `Fragmentname wurde unerwünscht abgekürzt: ${fragment}`);
}
assert(data.APP_CONFIG?.replay?.maxItems === 24, 'Normaler Replay-Verlauf ist nicht auf 24 Schritte begrenzt');
assert(html.includes('state.history.splice(0,state.history.length-APP_CONFIG.replay.maxItems)'), 'Älteste Replay-Schritte werden bei neuer Eingabe nicht entfernt');
assert(data.APP_CONFIG?.audio?.soundSet === 'classic', 'Klassische Web-Audio-Synthese ist nicht Standard');
assert(data.APP_CONFIG?.audio?.assetRoot === '../../../assets/audio/emotronic', 'WAV-Basispfad ist nicht für Quelle und Laufzeitspiegel gemeinsam');
assert(html.includes("set!=='8-bit_soft'"), 'Soft-WAV ist nicht als einzige auswählbare Alternative begrenzt');
assert(html.includes("if(set==='classic'){fallback();return}"), 'Direkte Auswahl der klassischen Synthese fehlt');
assert(html.includes('function playSoundAsset(id,synthFallback)'), 'WAV-Wiedergabe mit Synthese-Fallback fehlt');
for (const prefix of ['emotion_', 'combo_', 'special_']) assert(html.includes(`playSoundAsset(\`${prefix}`), `WAV-Zuordnung fehlt: ${prefix}`);
const audioStart = html.indexOf('const soundPatterns=');
const audioEnd = html.indexOf('let state=', audioStart);
assert(audioStart >= 0 && audioEnd > audioStart, 'Audio-Laufzeitcode nicht gefunden');
const playedAudioUrls = [];
class TestAudio {
  constructor(url) { this.url = url; playedAudioUrls.push(url); }
  addEventListener() {}
  play() { return Promise.resolve(); }
}
const classicRuntime = new Function(
  'APP_CONFIG', 'Audio',
  `${html.slice(audioStart, audioEnd)};return {playEmotionSound};`
)(data.APP_CONFIG, TestAudio);
classicRuntime.playEmotionSound('anger', 2);
assert(playedAudioUrls.length === 0, 'Klassischer Standard versucht unerwartet eine WAV-Datei abzuspielen');
const audioRuntime = new Function(
  'APP_CONFIG', 'Audio',
  `${html.slice(audioStart, audioEnd)};return {playEmotionSound,playComboSound,playSpecialSound};`
 )({ ...data.APP_CONFIG, audio: { ...data.APP_CONFIG.audio, soundSet: '8-bit_soft' } }, TestAudio);
audioRuntime.playEmotionSound('anger', 2);
audioRuntime.playComboSound(data.combos['anger|disgust']);
audioRuntime.playSpecialSound('lifeGain');
assert(playedAudioUrls[0]?.endsWith('/8-bit_soft/emotion_anger_2.wav'), 'Soft-Emotions-WAV wird nicht korrekt aufgelöst');
assert(playedAudioUrls[1]?.endsWith('/8-bit_soft/combo_abwertung.wav'), 'Soft-Kombi-WAV wird nicht korrekt aufgelöst');
assert(playedAudioUrls[2]?.endsWith('/8-bit_soft/special_life_gain.wav'), 'Soft-Spezial-WAV wird nicht korrekt aufgelöst');

const { version, revision } = data.APP_META;
assert(html.includes(`Emotronic v${version}`), 'Codekopf und APP_META-Version weichen ab');
assert(html.includes(`Aktuelle Revision: ${revision}`), 'Codekopf und APP_META-Revision weichen ab');
const snapshotPath = path.join(toolRoot, `Emotronic-v${version}.html`);
assert(fs.existsSync(snapshotPath), 'Versionierter Snapshot fehlt');
sameBytes(sourcePath, snapshotPath, 'Snapshot');
sameBytes(sourcePath, path.join(shareRoot, 'index.html'), 'Öffentlicher HTML-Spiegel');
sameBytes(swPath, path.join(shareRoot, 'sw.js'), 'Öffentlicher Service-Worker-Spiegel');
assert(read(swPath).toString('utf8').includes(`\${CACHE_PREFIX}${revision}`), 'Cache-Version stimmt nicht mit der Revision überein');

const manifest = JSON.parse(read(path.join(audioRoot, 'manifest.json')).toString('utf8'));
assert(manifest.defaultPlayback === 'classic', 'Audio-Manifest nennt die klassische Synthese nicht als Standard');
assert(manifest.optionalSet === '8-bit_soft', 'Audio-Manifest nennt Soft nicht als einzige Laufzeitalternative');
assert(JSON.stringify(manifest.sets) === JSON.stringify(['8-bit_soft']), 'Audio-Manifest enthält weitere WAV-Sets neben Soft');
assert(manifest.sounds.length === 40, 'Audio-Manifest enthält nicht 40 Klänge');
const manifestById = new Map(manifest.sounds.map(sound => [sound.id, sound]));
for (const [key, levels] of Object.entries(data.soundPatterns)) {
  levels.forEach((notes, index) => {
    const sound = manifestById.get(`emotion_${key}_${index + 1}`);
    assert(sound && JSON.stringify(sound.notes) === JSON.stringify(notes), `Audio-Manifest weicht bei ${key} Stufe ${index + 1} ab`);
  });
}
for (const item of Object.values(data.combos)) {
  assert(manifestById.has(`combo_${item.audioName}`), `Kombi-WAV fehlt: ${item.audioName}`);
}
const expectedWavs = new Set(manifest.sounds.map(sound => `${sound.id}.wav`));
for (const setName of manifest.sets) {
  const setPath = path.join(audioRoot, setName);
  const actualWavs = fs.readdirSync(setPath).filter(name => name.endsWith('.wav'));
  assert(actualWavs.length === expectedWavs.size && actualWavs.every(name => expectedWavs.has(name)), `Soundset ${setName} weicht vom Manifest ab`);
  for (const name of actualWavs) {
    const wav = read(path.join(setPath, name));
    assert(wav.length > 44 && wav.toString('ascii', 0, 4) === 'RIFF' && wav.toString('ascii', 8, 12) === 'WAVE', `Ungültige WAV-Datei: ${setName}/${name}`);
  }
}

console.log(`Emotronic v${version}: Modell, Kurzlinks, Spiegelung, Emojis, Kombis, Audio, Cache und Laufzeitspiegel OK`);
