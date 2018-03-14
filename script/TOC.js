      var toc, br, header;
      var h4;
      var newA;
      var TOCArray;
      function tocBuilder() {

	toc = document.getElementById("toc");
	br = document.createElement('br');
	$h5Array = jQuery("h5"); 				//JQUERY

	for (i = 0; i < $h5Array.length ; i++) {
	  var h5Children = $h5Array[i].children;
	  for (j = 0; j < $h5Array[i].children.length; j++) {

	    console.log(j);
	    if(h5Children[j].tagName == "SPAN") {

	      if(h5Children[j].id.indexOf("heading3") !== -1) {

		newDiv = document.createElement('div');
		var innerHtml = h5Children[j].innerHTML;

		var aIdName = "id"+innerHtml;
		newDiv.setAttribute('id',aIdName);
		newDiv.innerHTML = innerHtml;

		toc.appendChild(newDiv);
		newDiv = document.getElementById(aIdName);
		newDiv.setAttribute('onclick', 'document.getElementById(\''+h5Children[j].id +'\').scrollIntoView()');
	      }
	    }
	  }
	}

      }
