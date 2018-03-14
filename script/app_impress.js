function app_impress() {
      JSOND = {
	1:"<p><span class='have'>have</span> <span class='you'>you</span> <span class='noticed'>noticed</span> <span class='its'>it's</span> <span class='in'>in</span> <b>3D<sup>*</sup></b>?</p>        <span class='footnote'>* beat that, prezi ;)</span>",
	2:"<q>!Don't you think that presentations given <strong>in modern browsers</strong> shouldn't <strong>copy the limits</strong> of 'classic' slide decks?</q>",
	3:"<q>Would you like to <strong>impress your audience</strong> with <strong>stunning visualization</strong> of your talk?</q>",
	4:"<span class='try'>then you should try</span>        <h1>impress.js<sup>*</sup></h1>        <span class='footnote'><sup>*</sup> no rhyme intended</span>",
        5:"<p>It's a <strong>presentation tool</strong> <br/>        inspired by the idea behind <a href='http://prezi.com'>prezi.com</a> <br/>        and based on the <strong>power of CSS3 transforms and transitions</strong> in modern browsers.</p>",
        6:"<p>visualize your <b>big</b> <span class='thoughts'>thoughts</span></p>",
	7:"<p>and <b>tiny</b> ideas</p>",
	8:"<p>by <b class='positioning'>positioning</b>, <b class='rotating'>rotating</b> and <b class='scaling'>scaling</b> them on an infinite canvas</p>",
    	9:"<p>the only <b>limit</b> is your <b class='imagination'>imagination</b></p>",
    	10:"<p>want to know more?</p>       <q><a href='http://github.com/bartaz/impress.js'>use the source</a>, Luke!</q>",
    	11:"<p>one more thing...</p>",
    	12:"<p><span class='have'>have</span> <span class='you'>you</span> <span class='noticed'>noticed</span> <span class='its'>it's</span> <span class='in'>in</span> <b>3D<sup>*</sup></b>?</p>        <span class='footnote'>* beat that, prezi ;)</span>"
      };

      for(var i=1; i < 12; i++) {
	var div = document.createElement('div')
	document.body.appendChild(div)
	div.setAttribute('data-x',200)
      document.getElementById(i).innerHTML = JSOND[i]
      };
    

}

