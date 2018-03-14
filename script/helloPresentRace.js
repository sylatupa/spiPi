/*Tips
// Sweet  ?? JAVASCRIPT
//  Math.min(centerX, centerY);
// var now = new Date();
// now.getHours() now.getMinutes() now.getSeconds() / 60) / 60;

//Sweet ?? PROCESSINGjs
// Build in functions   
// 		function drawArm(position, lengthScale, weight) {      } 
// Built ins
// 		processing.width processing.height processing.strokeWeight(weight); 
// 		processing.line(x1,y1,x2,y2); processing.background(224);
// 		processing.loadImage("pjs.png");
 */

/*
 * 1) Make a function that will be called by the Processing object, which then attatches to the canvas
 */
var box_w = 8;
var box_h = 8;
var col_gap = 1;
var slot_gap = 3;
var brick_start = 90;
var width = 300;
var height 
var brick_end = width;
var slides = 1;
var gravita = 0.03;
var randomData = new Array();
var slots = new Array();
var frames = 200
function sketchProc(processing) {
	/*
	 *  3) Make an override for processing.setup
	 */ 
	processing.setup = function() {
		processing.size(960,800);
		processing.fill(144);
		processing.stroke(processing.color(44,48,32));
		processing.text("here", 10,10,50,50);
	};
	/* 3) Make an override for processing.draw */ 
	processing.draw = function() {
		processing.background('#FFFFFF');
		RandomDataGenerator(processing);
		for (i = 0; i < randomData.length; i++) {
			randomData[i].draw();
		}
		for(i = 0; i < slots.length; i++) {
			slots[i].draw();
		}
	};
}
function addData() {
	randomData.push(new RandomDataGenerator().getRandomData());
}
function getSlot(randomData) {
	for (i = 0; i<slots.length; i++) {
		if(slots[i].name == randomData)
			{ return slots[i]; }
		else 
			{ return null }
	}
}
function RandomDataGenerator(processing) {
	this.getRandomData = function () {
		return Math.floor(Math.random()*100);
	}
	this.getRandomDataSlot = function (randomData) {
		if(randomData >= 90) { return 90 }
		if(randomData < 90 && randomData >= 80) { return 80 }
		if(randomData < 80 && randomData >= 79) { return 70 }
		return randomData  
	}
	var data = getRandomData()
	if (data > 98) {
		var a = new RandomData(processing);
		a.setData(data, randomData.length);
		randomData.push(a);
	}
}
function RandomData(processing) {
	this.processing = processing;
	this.randomData = {};
	this.index;
	this.slot;
	this.pos_y;
	this.vel_y;
	this.slot_index;
	this.col_x;
	this.frames;

	this.setData = function(dataIn, i) {
		this.randomData = dataIn;
		this.frames = 0;
		this.pos_y = brick_start;
		this.vel_y = 0;
		this.slot = getSlot(this.randomData) || new Slot(this.randomData, this.processing);
		this.index = i;
		this.col_x = this.slot.inc(this);
		this.slot_index = this.slot.rD.length -1; 		
	};
	this.draw = function() {
		this.processing.fill(this.slot.get_color());
		this.frames = (this.frames <= frames && this.pos_y > this.brick_start + 30) ? this.frames + 1 : this.frames;
		this.update = (this.frames < frames);
		if (this.update) {
			for (k = 0; k < this.slot_index; k++) {
				tempRD = this.slot.rD[k];
				if(this.col_x == tempRD.col_x && Math.abs(this.pos_y - tempRD.pos_y) < (box_h+2)) {
					this.pos_y = tempRD.pos_y - (box_h + 1);
					this.update = false;
					break;
				}
			}
		}
		processing.rect(this.slot.get_pos_x(this.col_x), this.pos_y, box_w, box_h);
		if (this.update && this.pos_y < brick_end) {
			this.vel_y += gravita;
			this.pos_y += this.vel_y;
		}
	};
}
function Slot(randomData, processing) {
	this.processingTemp = processing;
	this.last_col = 0;
	this.color;  
	this.name = new RandomDataGenerator().getRandomDataSlot(randomData);
	this.index = slots.length;
	this.prev_slot = slots[this.index-1];
	this.rD = new Array();
	if(this.prev_slot) {
		this.pos_x = this.prev_slot.get_pos_x(this.prev_slot.last_col) + box_w + slot_gap;
	}
	else {
		this.pos_x = 0;
	}

	this.inc = function(randomData) {
		if(Math.floor(this.rD.length/20) > this.last_col) {
			for(i = index+1; i < slots.length;i++) {
				slots[i].pos_x += (box_w + col_gap);
				this.last_col ++;
			}
		}
		this.rD.push(randomData);
		return this.last_col;
	};
	this.get_color 	= function() {
		return this.processingTemp.color(this.index * 10,125,255);
	};
	this.get_pos_x = function(col) {
		return this.pos_x + (box_w + col_gap) * col;
	};
	this.draw = function() {
		this.processingTemp.fill(this.get_color());
	//	this.processingTemp.text(this.name, this.pos_x, brick_end + 20, this.get_pos_x(this.last_col+1) - this.pos_x, 13);
	}; //end draw()
	slots.push(this);
	console.log("slot: " + this.name , " x: " , this.pos_x , " y: " , this.pos_y , " text: " , this.get_pos_x(this.last_col+1) - this.pos_x );
} //end Slots object
// ATTACH TO CANVAS
var p = new Processing("presents", sketchProc);
p.size(frames,frames)
// p.exit(); to detach it
