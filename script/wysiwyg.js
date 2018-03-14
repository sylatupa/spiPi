var colorPalette = ['000000', 'FF9966', '6699FF', '99FF66', 'CC0000', '00CC00', '0000CC', '333333', '0066FF', 'FFFFFF'];
var forePalette = $('.fore-palette');
var backPalette = $('.back-palette');

for (var i = 0; i < colorPalette.length; i++) {
  forePalette.append('<a href="#" data-command="forecolor" data-value="' + '#' + colorPalette[i] + '" style="background-color:' + '#' + colorPalette[i] + ';" class="palette-item"></a>');
  backPalette.append('<a href="#" data-command="backcolor" data-value="' + '#' + colorPalette[i] + '" style="background-color:' + '#' + colorPalette[i] + ';" class="palette-item"></a>');
}

$('.toolbar a').click(function(e) {
  var command = $(this).data('command');
  if (command == 'toggle') {
   doToggleView()
   //document.execCommand('formatBlock', false, command);
  }  
  if (command == 'h1' || command == 'h2' || command == 'p') {
    document.execCommand('formatBlock', false, command);
  }
  if (command == 'forecolor' || command == 'backcolor') {
    document.execCommand($(this).data('command'), false, $(this).data('value'));
  }
  if (command == 'createlink' || command == 'insertimage') {
    url = prompt('Enter the link here: ', 'http:\/\/');
    document.execCommand($(this).data('command'), false, url);
  } else document.execCommand($(this).data('command'), false, null);
});


var viewMode = 1; // WYSIWYG
// Other code exists here
par = $('#paragraph')
console.log(par.text())
//console.log(par.html())

editor = $('#editor')
//editor.text(par.html())
function doToggleView()
{
  console.log('her')
  if(viewMode == 1)
  {
    iHTML = editor.html()
    console.log(iHTML)
    editor.text(iHTML)
    // Hide all controls
    editor.focus();
    viewMode = 2; // Code
  }
  else
  {
    iText = editor.text();
    editor.html(iText);
    editor.focus();
    viewMode = 1; // WYSIWYG
  }
}
