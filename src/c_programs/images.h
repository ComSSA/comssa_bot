#pragma once
#include "gd.h"

#ifdef TESTING
int main();
#endif

void generateMandelBrot(int size);
int calcEscapeForPixel(double x0, double y0);
gdImagePtr createImage(int** iterationCount, int size, int* histogram);
void HsvToRgb(double h, double s, double v, int* r, int* g, int* b);
