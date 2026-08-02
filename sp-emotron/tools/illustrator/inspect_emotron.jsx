#target illustrator

(function () {
    var projectRoot = File($.fileName).parent.parent.parent;
    var source = File(projectRoot.fsName + "/files/emotron.ai");
    var reportFile = File(projectRoot.fsName + "/files/Emotron.layers.txt");
    var documentRef = null;

    for (var index = 0; index < app.documents.length; index += 1) {
        if (app.documents[index].fullName && app.documents[index].fullName.fsName === source.fsName) {
            documentRef = app.documents[index];
            break;
        }
    }
    if (!documentRef) documentRef = app.open(source);

    function clean(value) {
        return String(value).replace(/[\r\n\t]+/g, " ");
    }

    function bounds(item) {
        try {
            return item.geometricBounds.join(",");
        } catch (_) {
            return "";
        }
    }

    var lines = [];
    lines.push("DOCUMENT\t" + clean(documentRef.name));
    lines.push("ARTBOARDS\t" + documentRef.artboards.length);
    for (var layerIndex = 0; layerIndex < documentRef.layers.length; layerIndex += 1) {
        var layer = documentRef.layers[layerIndex];
        lines.push("LAYER\t" + layerIndex + "\t" + clean(layer.name) + "\tvisible=" + layer.visible + "\tlocked=" + layer.locked + "\tpageItems=" + layer.pageItems.length + "\tgroups=" + layer.groupItems.length + "\ttexts=" + layer.textFrames.length + "\tpaths=" + layer.pathItems.length + "\tcompound=" + layer.compoundPathItems.length + "\tplaced=" + layer.placedItems.length);
        for (var textIndex = 0; textIndex < layer.textFrames.length; textIndex += 1) {
            var textFrame = layer.textFrames[textIndex];
            lines.push("TEXT\t" + layerIndex + "\t" + textIndex + "\t" + clean(textFrame.contents) + "\t" + bounds(textFrame));
        }
        for (var groupIndex = 0; groupIndex < layer.groupItems.length; groupIndex += 1) {
            var group = layer.groupItems[groupIndex];
            lines.push("GROUP\t" + layerIndex + "\t" + groupIndex + "\t" + clean(group.name) + "\t" + bounds(group) + "\titems=" + group.pageItems.length + "\tgroups=" + group.groupItems.length + "\tpaths=" + group.pathItems.length + "\tcompound=" + group.compoundPathItems.length + "\ttexts=" + group.textFrames.length);
            for (var groupTextIndex = 0; groupTextIndex < group.textFrames.length; groupTextIndex += 1) {
                var groupText = group.textFrames[groupTextIndex];
                lines.push("GTEXT\t" + layerIndex + "\t" + groupIndex + "\t" + groupTextIndex + "\t" + clean(groupText.contents) + "\t" + bounds(groupText));
            }
        }
        for (var placedIndex = 0; placedIndex < layer.placedItems.length; placedIndex += 1) {
            var placed = layer.placedItems[placedIndex];
            var placedFile = "<missing>";
            try {
                placedFile = clean(placed.file);
            } catch (_) {}
            lines.push("PLACED\t" + layerIndex + "\t" + placedIndex + "\t" + clean(placed.name) + "\t" + bounds(placed) + "\t" + placedFile);
        }
    }

    reportFile.encoding = "UTF-8";
    reportFile.open("w");
    reportFile.write(lines.join("\n"));
    reportFile.close();
    alert("Ebenenbericht erstellt: " + reportFile.fsName);
}());
