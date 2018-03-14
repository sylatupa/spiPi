$(document).ready(function () {
    jQuery('#westPanel h4').click(
        function () {
            $(this).next().slideToggle();
        });
    jQuery('#eastPanel h4').click(
    function () {
        $(this).next().slideToggle();
    });
//	$("#graphPanel").dialog();	
//	$gp = document.getElementById('graphPanel').parentNode
//    	jQuery($gp).css('display', 'none');
//	jQuery($gp).css('width', 'auto');
});
function fullScreenMap() {
        $mc = jQuery('#myMap_container');
        $mr = jQuery('#myMap_root');
        $mp = jQuery('#myMap');
        $cp = jQuery('#centerPanel');
}
function toggleGraphPanel() {
    if (jQuery($gp).css('display') == "block")
        { jQuery($gp).css('display', 'none'); }
    else
        jQuery($gp).css('display', 'block');
}
function toggleBaseMaps() {
    if (jQuery('#basemap').animate().css('display') == "block") {
        jQuery('#basemap').animate().css('display', 'none');
        jQuery('#basemap').dialog('close');
    }
    else {
        jQuery('#basemap').animate().css('display', 'block');
        jQuery('#basemap').dialog({position:'top'});
    }
}
function toggleDrawing() {
    if (jQuery('#drawing').animate().css('display') == "block") {
        jQuery('#drawing').animate().css('display', 'none');
        jQuery('#drawing').dialog('close');
    }
    else {
        jQuery('#drawing').animate().css('display', 'block');
        jQuery('#drawing').dialog({position:['left','bottom']});
    }
}
function toggleIdentify() {
    if (jQuery('#identify').animate().css('display') == "block") {
        jQuery('#identify').animate().css('display', 'none');
        jQuery('#identify').dialog('close');
    }
    else {
        jQuery('#identify').animate().css('display', 'block');
        jQuery('#identify').dialog({position:['right','bottom']});
    }
}
function toggleLocate() {
    if (jQuery('#locate').animate().css('display') == "block") {
        jQuery('#locate').animate().css('display', 'none');
        jQuery('#locate').dialog('close');
    }
    else {
        jQuery('#locate').animate().css('display', 'block');
        jQuery('#locate').dialog({position:[400,150]});
    }
}
function toggleFindRoute() {
    if (jQuery('#findRoute').animate().css('display') == "block") {
        jQuery('#findRoute').animate().css('display', 'none');
        jQuery('#findRoute').dialog('close');
    }
    else {
        jQuery('#findRoute').animate().css('display', 'block');
        jQuery('#findRoute').dialog({position:[100,150]});
    }
}
function toggleLegend() {
    if (jQuery('#mapLegend').animate().css('display') == "block") {
        jQuery('#mapLegend').animate().css('display', 'none');
        jQuery('#mapLegend').dialog('close');
    }
    else {
        jQuery('#mapLegend').animate().css('display', 'block');
        jQuery('#mapLegend').dialog({position:['right','150']});
    }
}
function toggleLayerList() {
    if (jQuery('#layerList').animate().css('display') == "block") {
        jQuery('#layerList').animate().css('display', 'none');
        jQuery('#layerList').dialog('close');
    }
    else {
        jQuery('#layerList').animate().css('display', 'block');
        jQuery('#layerList').dialog({position:['left','150']});
    }
}


