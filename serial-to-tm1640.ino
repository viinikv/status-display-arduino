#include "TM1638.h"
#include "TM1640.h"
#define LCDLEN 16

// connect the module data line to pin 7, clock to pin 8
TM1640 module(7, 8);
char text[LCDLEN * 2 + 1];
unsigned short dots;

void setup()
{
	memset(text, ' ', LCDLEN);
	text[LCDLEN * 2] = 0;
	Serial.begin(9600);
}

// read text from serial, output to 7-segment led module
// right-aligns the text and converts periods to dots between characters
// (by default periods are their own characters and leave the 7-segment part empty)
void loop()
{
	int c, i;
	dots = 0;
	// read LCDLEN + 1 characters, the last one gets ignored
	for (i = 0; i < LCDLEN + 1; i++){
		for (;;) {
			if (!Serial.available()){
				continue;
			}
			c = Serial.read();
			if (c != -1) {
				break;
			}
		}
		// now c is a proper received character
		if (c == '\n'){
			break;
		} else if (c == '.') {
			dots = dots | (1 << (LCDLEN - i));
			i--;
		} else {
			text[LCDLEN + i] = c;
		}
	}
	text[LCDLEN + i] = 0;
	dots = dots >> LCDLEN - i;

	module.setDisplayToString(&text[i], dots);
}
