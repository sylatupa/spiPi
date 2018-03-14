var eventPoint;
function MouseHandler(e) {
    eventPoint = e;
    var msg = "Mouse: ";
    var mp = e.mapPoint
    var mpGeographic = esri.geometry.webMercatorToGeographic(e.mapPoint);
    eventPoint = e.mapPoint;
    msg += " Clicked at: <br />";
    msg += "Lat_x:" + mpGeographic.x + "  Long_y:" + mpGeographic.y;
    //e.shiftKey; e.ctrlKey; + e.altKey;
    document.getElementById("labelMapCoords").innerHTML = msg;
}

function HoverHandler(e) {
    map.graphics.remove(mouseXY);
    var mpGeographic = esri.geometry.webMercatorToGeographic(e.mapPoint);
    var symbol = new esri.symbol.SimpleMarkerSymbol();
    var point = new esri.geometry.Point(e.mapPoint.x, e.mapPoint.y, new esri.SpatialReference({ wkid: 102100 }))
    mouseX = mpGeographic.x.toString();
    mouseY = mpGeographic.y.toString();
    mouseText = new esri.symbol.TextSymbol(mouseX.substring(0,7) +"\n"+mouseY.substring(0,5));
    mouseText = mouseText.setOffset(50,5);
//    mouseText.setFont(font);    
    mouseXY = new esri.Graphic(point, symbol);
    mouseXY.setSymbol(mouseText);
    map.graphics.add(mouseXY);
    //msg += "Lat:" + mpGeographic.x + "  Long:" + mpGeographic.y;
    //e.shiftKey, e.ctrlKey, e.altKey;
}
function updateExtent() {
	dojo.byId("currentextent").innerHTML = "<b>Current Extent JSON:</b> " + dojo.toJson(map.extent.toJson());
        dojo.byId("currentextent").innerHTML += "<br/><b>Current Zoom level:</b> " + map.getLevel();
}

