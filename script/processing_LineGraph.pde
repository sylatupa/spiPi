//GLOBAL VARIABLES
	bool verbose = false;	
	//Canvas Variables
	int width = 600;
	int height = 400;
	int margin = 15;

	//Bargraph Variables
	int lineThickness=1;
	String[] yAxis = new String[20];
	//Data Variables
	int baseYear = 1970;
	//String[] dateSet = ["9/13/1990 12:00:00 AM", "7/10/1998 12:00:00 AM", "6/24/2000 12:00:00 AM", "5/17/2004 12:00:00 AM", "6/25/2004 12:00:00 AM", "6/12/2005 12:00:00 AM", "11/26/2005 12:00:00 AM", "3/5/2006 12:00:00 AM", "5/5/2006 12:00:00 AM", "5/28/2006 12:00:00 AM", "6/12/2006 12:00:00 AM", "7/6/2006 12:00:00 AM", "3/16/2007 12:00:00 AM", "4/30/2007 12:00:00 AM", "6/11/2007 12:00:00 AM", "7/21/2007 12:00:00 AM", "8/4/2007 12:00:00 AM", "11/7/2007 12:00:00 AM", "4/6/2008 12:00:00 AM", "4/6/2008 12:00:00 AM", "5/5/2008 12:00:00 AM", "6/1/2008 12:00:00 AM", "6/25/2008 12:00:00 AM", "7/12/2008 12:00:00 AM", "4/8/2009 12:00:00 AM", "5/12/2009 12:00:00 AM", "6/17/2009 12:00:00 AM", "9/13/2009 12:00:00 AM"];
	//Int[] levelSet = [85, 0, 0, 25, 28, 26, 0, 12, 28, 13, 20, 13, 27, 26, 21, 28, 30, 20, 22, 22, 18, 16, 25, 20, 20, 15, 23, 16];
	Int[] levelSet = WaterLevel;
	Int[] dateSet = InspectionDate;
	String[] dateArray = dateTimeToDate(dateSet);	//use as label
	String[] totalDays = dateToTotalDays(dateArray);
	int length = levelSet.length; 
	Int[] normalTotalDays = normalizeArray(totalDays);
	Int[] normalLevelSet = normalizeArray(levelSet);
	Int[] flippedNormalLevelSet = flipSet(normalLevelSet);

	int[] Y=new int[length];
	if(verbose){
	println("levelset" + "   |   " + "waterLevels" + "   |   " + "inspectiondate" +"   |   "+"totaldays"+"    |  " + "normaltotaldays" + "   |   " +"normalLevelSet" + "   |   " + "flippedNormalLevel");
	for(int i=0;i<length;i++){
		println(levelSet[i] + "       |      " + WaterLevel[i] + "      |     " + InspectionDate[i] +"   |   " +totalDays[i]+"    |   " + normalTotalDays[i] + "   |   " +normalLevelSet[i]+ "   |       " +flippedNormalLevelSet[i]);
			}
	}
//END GLOBAL VARIABLES
void setup() {
	background(125);
	size(width,height);
	//framerate(15);
//  	println("Hello ErrorLog!");
	noLoop();
	PFont fontA = loadFont("courier");
	textFont(fontA, 14);  
	smooth();
}
void draw(){
	//pointMatrix();
	grid();	
	drawBar();
}
void drawBar() {
	strokeWeight(2);

	color c = color(0,126,255,60);
	fill(c);
	//rectMode(CORNERS);
	beginShape();
	vertex(margin,height-margin);

	for(int i=0; i<=length-1; i++){
		//ellipse(margin+normalTotalDays[i]*width,flippedNormalLevelSet[i]*height -margin, 5,5);
		//stroke(0,233,233);
		if(verbose){
			println((margin+(normalTotalDays[i]*width)) + " " + (margin+(flippedNormalLevelSet[i]*height)));
		}
		vertex((margin+(normalTotalDays[i]*width)),(margin+(flippedNormalLevelSet[i]*height)));
		//rect(margin+normalTotalDays[i]*width,flippedNormalLevelSet[i]*height -margin,5+margin+normalTotalDays[i]*width, height-margin);
		text(str(levelSet[i]).substring(0,5), margin+(normalTotalDays[i]*width-3), margin+(flippedNormalLevelSet[i]*height));
	}
	vertex((margin+(normalTotalDays[length-1]*width)),(height-margin));
	vertex(margin, height-margin);
	endShape();
	fill(0,0,0);
	for(int i=0; i<=length-1; i++){
		text(str(levelSet[i]).substring(0,5), margin+(normalTotalDays[i]*width-3), margin+(flippedNormalLevelSet[i]*height));
	}

}
void grid() {
  strokeWeight(1.5);
  stroke(0,233,233);
  line(0.9*margin,height-0.9*margin,0.9*margin,0.9*margin); //vertical line
  line(0.9*margin,height-0.9*margin,width-margin,height-0.9*margin); //horizontal line
  for(int i=margin; i<height-margin;i+=40){
		line(0.9*margin-4,height-2*margin-i,0.9*margin+4,height-2*margin-i); //vertical tick marks
  }
  strokeWeight(.5);
  for(int i=margin; i<height-margin;i+=40){
	line(0.9*margin,height-2*margin+i,width-margin,height-2*margin+i);
  }
  String[] yAxisNormal =normalizeArray(yAxis);
	String[] yAxisNormalFlipped = flipSet(yAxisNormal);
	for(int i=margin; i<height-margin;i+=40){
  }
}

void pointMatrix(){
	textSize(10);
	for(i=0; i < width; i= i + 50){
		for( j=0; j < height; j = j+50){
			k = k + 1;
		String numberPoint = "|"+i+ ","+ j+"|"; 
		strokeWeight(10);
		stroke(10);
		point(i , j);
		strokeWeight(1);
		stroke(0, 60, 80);
		fill(255,255,255);
		text(numberPoint, i-7, j+5);
		//System.out.println(i + " " + j + " "+ k);
		}
	}
}

String[] dateTimeToDate(String[] dateArrayOriginal){
	String[] dateArray = new String[dateArrayOriginal.length];
	for (int i=0; i <= dateArrayOriginal.length-1 ; i++) {
		String tempString = str(dateArrayOriginal[i]);
		String[] stringArray = split(tempString," ");
		//text(stringArray[0], 222, 50+(15*i));	
		dateArray[i] = stringArray[0];
	}		
		return(dateArray);
}

Int[] dateToTotalDays(String dateArray[]){
	Int[] totalDayArray = new totalDayArray[dateArray.length];
	for(int i=0; i<=totalDayArray.length-1;i++){
		String[] monthDayYearArray = split(dateArray[i], "/");
		int month = int(monthDayYearArray[0]);
		int day = int(monthDayYearArray[1]);
		int year = int(monthDayYearArray[2]);
		//println(str(month)+" "+str(day)+" "+ str(year));
		totalDayArray[i] = getDays(month,day,year);
		text(str(totalDayArray[i]), 5, 15*i);
	}
	return(totalDayArray);
}
Int getDays(int month, int day, int year){
	int numberOfYears = year-baseYear;
	int days = numberOfYears * 365;
	//adds up all the days until the month is reached
	for(int i = 1; i <= 12; i++){
		if(i == month){
			break;
		}
		if ((i==1) || (i==3) || (i==5) || (i==7) || (i==8) || (i==10) || (i==12)) {
			days += 31;
		}
		if (i==2) {
			days += 28;
		}
		if ((i==4) || (i==6) || (i==9) || (i==11)) {
			days += 30;
		} 
	}
	days += int(day);
	return(days)
}

Int[] normalizeArray(int[] dataArray) {
	Int[] normedArray = new Int[dataArray.length];
	Int maxNum = max(dataArray);
	for(int i=0; i <= dataArray.length-1; i++){
		normedArray[i] =  norm(dataArray[i], 0, maxNum);
		//println(dataArray[i] + " " + normedArray[i]);
	}
	return(normedArray);
}
Int[] flipSet(verticalArray){
	Int[] flippedArray = new Int[verticalArray.length];
		for(int i =0; i < verticalArray.length; i++){
			flippedArray[i] = 1-verticalArray[i];
		}
		return(flippedArray)
}
