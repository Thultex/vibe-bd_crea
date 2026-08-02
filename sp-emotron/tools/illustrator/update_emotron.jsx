#target illustrator

(function () {
    var projectRoot = File($.fileName).parent.parent.parent;
    var source = File(projectRoot.fsName + "/files/emotron.ai");
    var assetRoot = Folder(projectRoot.fsName + "/files/openmoji");
    var reportFile = File(projectRoot.fsName + "/files/Emotron.update.txt");
    var documentRef = null;
    var lines = [];

    for (var documentIndex = 0; documentIndex < app.documents.length; documentIndex += 1) {
        try {
            if (app.documents[documentIndex].fullName.fsName === source.fsName) {
                documentRef = app.documents[documentIndex];
                break;
            }
        } catch (_) {}
    }
    if (!documentRef) documentRef = app.open(source);
    documentRef.activate();

    function layerByName(name) {
        for (var index = 0; index < documentRef.layers.length; index += 1) {
            if (documentRef.layers[index].name === name) return documentRef.layers[index];
        }
        throw new Error("Ebene fehlt: " + name);
    }

    function unlock(item) {
        try { item.locked = false; } catch (_) {}
        try { item.hidden = false; } catch (_) {}
    }

    function removeMissingPlacedItems() {
        var removed = 0;
        for (var layerIndex = 0; layerIndex < documentRef.layers.length; layerIndex += 1) {
            var layer = documentRef.layers[layerIndex];
            unlock(layer);
            for (var itemIndex = layer.placedItems.length - 1; itemIndex >= 0; itemIndex -= 1) {
                var placed = layer.placedItems[itemIndex];
                var missing = false;
                try {
                    missing = !placed.file || !placed.file.exists;
                } catch (_) {
                    missing = true;
                }
                if (missing) {
                    unlock(placed);
                    placed.remove();
                    removed += 1;
                }
            }
        }
        lines.push("Fehlende Verknüpfungen entfernt: " + removed);
    }

    function clearLayer(layer) {
        unlock(layer);
        for (var index = layer.pageItems.length - 1; index >= 0; index -= 1) {
            unlock(layer.pageItems[index]);
            layer.pageItems[index].remove();
        }
    }

    function setCenterAndSize(item, centerX, centerY, targetSize) {
        var bounds = item.geometricBounds;
        var width = bounds[2] - bounds[0];
        var height = bounds[1] - bounds[3];
        var percentage = Math.min(targetSize / width, targetSize / height) * 100;
        item.resize(percentage, percentage, true, true, true, true, percentage, Transformation.CENTER);
        bounds = item.geometricBounds;
        width = bounds[2] - bounds[0];
        height = bounds[1] - bounds[3];
        item.left = centerX - width / 2;
        item.top = centerY + height / 2;
    }

    function addSvg(layer, variant, filename, centerX, centerY, targetSize, opacity) {
        var file = File(assetRoot.fsName + "/" + variant + "/" + filename);
        if (!file.exists) throw new Error("OpenMoji fehlt: " + file.fsName);
        var group = layer.groupItems.createFromFile(file);
        group.name = filename;
        setCenterAndSize(group, centerX, centerY, targetSize);
        group.opacity = opacity;
    }

    var centerX = 357.5;
    var centerY = 362.5;
    var radii = [88, 155, 220];
    var branches = [
        { angle: 135, files: ["3_freude_1_zufrieden.svg", "3_freude_2_froehlich.svg", "3_freude_3_begeistert.svg"] },
        { angle: 90, files: ["2_zuneigung_1_freundlich.svg", "2_zuneigung_2_zugewandt.svg", "2_zuneigung_3_verbunden.svg"] },
        { angle: 45, files: ["1_neugier_1_interessiert.svg", "1_neugier_2_neugierig.svg", "1_neugier_3_fasziniert.svg"] },
        { angle: 0, files: ["8_angst_1_besorgt.svg", "8_angst_2_aengstlich.svg", "8_angst_3_panisch.svg"] },
        { angle: -45, files: ["7_trauer_1_bedrueckt.svg", "7_trauer_2_traurig.svg", "7_trauer_3_trauernd.svg"] },
        { angle: -90, files: ["6_scham_1_verlegen.svg", "6_scham_2_befangen.svg", "6_scham_3_beschaemt.svg"] },
        { angle: -135, files: ["5_ekel_1_abgeneigt.svg", "5_ekel_2_angeekelt.svg", "5_ekel_3_uebel.svg"] },
        { angle: 180, files: ["4_wut_1_gereizt.svg", "4_wut_2_veraergert.svg", "4_wut_3_wuetend.svg"] }
    ];
    var combinations = [
        { angle: 112.5, file: "2-3_dankbarkeit.svg" },
        { angle: 67.5, file: "1-2_bewunderung.svg" },
        { angle: 22.5, file: "8-1_ueberraschung.svg" },
        { angle: -22.5, file: "7-8_aufgeben.svg" },
        { angle: -67.5, file: "6-7_reue.svg" },
        { angle: -112.5, file: "5-6_unbehagen.svg" },
        { angle: -157.5, file: "4-5_abwertung.svg" },
        { angle: 157.5, file: "3-4_streitlust.svg" }
    ];

    function radians(degrees) {
        return degrees * Math.PI / 180;
    }

    function rebuildEmojiLayer(layerName, variant, opacity) {
        var layer = layerByName(layerName);
        clearLayer(layer);
        addSvg(layer, variant, "0_neutral.svg", centerX, centerY, 72, opacity);
        for (var branchIndex = 0; branchIndex < branches.length; branchIndex += 1) {
            var branch = branches[branchIndex];
            for (var levelIndex = 0; levelIndex < radii.length; levelIndex += 1) {
                var radius = radii[levelIndex];
                var x = centerX + Math.cos(radians(branch.angle)) * radius;
                var y = centerY + Math.sin(radians(branch.angle)) * radius;
                addSvg(layer, variant, branch.files[levelIndex], x, y, 72, opacity);
            }
        }
        for (var combinationIndex = 0; combinationIndex < combinations.length; combinationIndex += 1) {
            var combination = combinations[combinationIndex];
            var comboX = centerX + Math.cos(radians(combination.angle)) * 278;
            var comboY = centerY + Math.sin(radians(combination.angle)) * 278;
            addSvg(layer, variant, combination.file, comboX, comboY, 54, opacity);
        }
        lines.push(layerName + ": " + layer.groupItems.length + " OpenMoji-Gruppen");
    }

    var names = [
        "freundlich", "zugewandt", "verbunden", "Bewunderung",
        "interessiert", "neugierig", "fasziniert", "Überraschung",
        "ausgeglichen",
        "besorgt", "ängstlich", "panisch", "Aufgeben",
        "bedrückt", "traurig", "trauernd", "Reue",
        "verlegen", "befangen", "beschämt", "Unbehagen",
        "abgeneigt", "angeekelt", "übel", "Abwertung",
        "gereizt", "verärgert", "wütend", "Streitlust",
        "fröhlich", "zufrieden", "begeistert", "Dankbarkeit"
    ];
    var emojiNames = [
        "freundlich", "zugewandt", "verbunden", "Bewunderung",
        "interessiert", "neugierig", "fasziniert", "Überraschung",
        "besorgt", "ängstlich", "panisch", "Aufgeben",
        "bedrückt", "traurig", "trauernd", "Reue",
        "verlegen", "befangen", "beschämt", "Unbehagen",
        "abgeneigt", "angeekelt", "übel", "Abwertung",
        "gereizt", "verärgert", "wütend", "Streitlust",
        "begeistert", "fröhlich", "zufrieden", "Dankbarkeit"
    ];

    function textFramesFor(layer, expectedCount) {
        if (layer.textFrames.length === expectedCount) return layer.textFrames;
        for (var groupIndex = 0; groupIndex < layer.groupItems.length; groupIndex += 1) {
            if (layer.groupItems[groupIndex].textFrames.length === expectedCount) {
                return layer.groupItems[groupIndex].textFrames;
            }
        }
        throw new Error(layer.name + " enthält nicht " + expectedCount + " Textfelder");
    }

    function setTexts(layerName, values) {
        var layer = layerByName(layerName);
        unlock(layer);
        var frames = textFramesFor(layer, values.length);
        for (var index = 0; index < values.length; index += 1) frames[index].contents = values[index];
        lines.push(layerName + ": " + values.length + " Namen");
    }

    var palette = {
        "90": "#f4b56d",
        "45": "#83d4cf",
        "0": "#c2a8dc",
        "-45": "#6381d7",
        "-90": "#bfe36f",
        "-135": "#6f9f68",
        "180": "#ef938b",
        "135": "#f5df6f"
    };

    function rgb(hex, strength) {
        var red = parseInt(hex.substr(1, 2), 16);
        var green = parseInt(hex.substr(3, 2), 16);
        var blue = parseInt(hex.substr(5, 2), 16);
        var color = new RGBColor();
        color.red = Math.round(255 + (red - 255) * strength);
        color.green = Math.round(255 + (green - 255) * strength);
        color.blue = Math.round(255 + (blue - 255) * strength);
        return color;
    }

    function nearestAngle(value) {
        var choices = [90, 45, 0, -45, -90, -135, 180, 135];
        var best = choices[0];
        var bestDistance = 999;
        for (var index = 0; index < choices.length; index += 1) {
            var distance = Math.abs(value - choices[index]);
            distance = Math.min(distance, 360 - distance);
            if (distance < bestDistance) {
                best = choices[index];
                bestDistance = distance;
            }
        }
        return best;
    }

    function colorPaths(layerName, faded) {
        var layer = layerByName(layerName);
        unlock(layer);
        var paths = [];
        for (var index = 0; index < layer.pathItems.length; index += 1) paths.push(layer.pathItems[index]);
        for (var groupIndex = 0; groupIndex < layer.groupItems.length; groupIndex += 1) {
            var group = layer.groupItems[groupIndex];
            for (var pathIndex = 0; pathIndex < group.pathItems.length; pathIndex += 1) paths.push(group.pathItems[pathIndex]);
        }
        var branchPaths = {};
        for (var pathItemIndex = 0; pathItemIndex < paths.length; pathItemIndex += 1) {
            var path = paths[pathItemIndex];
            var bounds = path.geometricBounds;
            var x = (bounds[0] + bounds[2]) / 2;
            var y = (bounds[1] + bounds[3]) / 2;
            var angle = Math.atan2(y - centerY, x - centerX) * 180 / Math.PI;
            var key = String(nearestAngle(angle));
            if (!branchPaths[key]) branchPaths[key] = [];
            branchPaths[key].push({ item: path, radius: Math.sqrt(Math.pow(x - centerX, 2) + Math.pow(y - centerY, 2)) });
        }
        var strengths = [0.25, 0.43, 0.68, 1.0];
        for (var key in branchPaths) {
            if (!branchPaths.hasOwnProperty(key)) continue;
            branchPaths[key].sort(function (left, right) { return left.radius - right.radius; });
            for (var itemIndex = 0; itemIndex < branchPaths[key].length; itemIndex += 1) {
                var level = Math.min(itemIndex, strengths.length - 1);
                var strength = strengths[level] * (faded ? 0.3 : 1);
                var item = branchPaths[key][itemIndex].item;
                if (item.filled) item.fillColor = rgb(palette[key], strength);
            }
        }
        lines.push(layerName + ": " + paths.length + " Farbflächen");
    }

    removeMissingPlacedItems();
    rebuildEmojiLayer("emoji_svg color", "color", 100);
    rebuildEmojiLayer("emoji_svg sw", "sw", 100);
    rebuildEmojiLayer("emoji_svg color faded", "color", 30);
    setTexts("names", names);
    setTexts("names for emoji", emojiNames);
    setTexts("names for emoji - front", emojiNames);
    colorPaths("Color", false);
    colorPaths("Color faded", true);

    layerByName("emoji_svg color").visible = true;
    layerByName("emoji_svg sw").visible = false;
    layerByName("emoji_svg color faded").visible = false;
    layerByName("Color").visible = true;
    layerByName("Color faded").visible = false;
    documentRef.save();

    reportFile.encoding = "UTF-8";
    reportFile.open("w");
    reportFile.write(lines.join("\n"));
    reportFile.close();
    alert("Emotron aktualisiert und gespeichert.\n" + lines.join("\n"));
}());
