// Document elements that are not available until after all the Java script is run
// if it has jQuery styling--that is loaded now.
function hello() {
console.log("hey", "hey");
}
function postLoadView() {
	jQuery('#layerList h4').click(function () { $(this).next().slideToggle(); })
}

