#pragma once
#include "gd.h"

char* generateMandelbrot(int size, int* len);
int calcEscapeForPixel(double x0, double y0);
gdImagePtr createImage(int** iterationCount, int size, int* histogram);
void HsvToRgb(double h, double s, double v, int* r, int* g, int* b);
void freeImage(char* ptr);
