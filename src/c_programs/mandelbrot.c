#include "gd.h"
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "mandelbrot.h"


#define MAX_ITERATIONS 100

#define HUE 260.0
#define SATURATION 0.6

#define COMPRESSION_LEVEL 9

char* generateMandelbrot(int size, int* len) {
    /* Generates a mandelbrot image of size sizexsize, creates a PNG file in a buffer, and returns a pointer to it. */
    /* len is a pointer that will be written to with the length of the file. */
    /* Based largely off of the code at https://en.wikipedia.org/wiki/Plotting_algorithms_for_the_Mandelbrot_set */
    int** iterationCount;
    int* histogram;
    int x, y, escapeNum;
    double size_d, x_trans, y_trans;
    gdImagePtr im;
    FILE* output;

    /* Allocating table */
    iterationCount = malloc(size * sizeof(int*));
    for(x = 0; x < size; x++) {
        iterationCount[x] = malloc(size * sizeof(int));
    }
    /* Also initialising everything to 0 */
    histogram = calloc(MAX_ITERATIONS, sizeof(int));

    /* Filling table */
    /* size - 1 so that the min value of x/size_d is 0, and max value is 1. */
    size_d = (double)size - 1.0;

    for(x = 0; x < size; x++) {
        for(y = 0; y < size; y++) {
            /* Need to scale the coordinates to fall between the set x: (-2.5 - 1), y: (-1 - 1) */
            x_trans = (double)x / size_d * 3.5 - 2.5;
            y_trans = (double)y / size_d * 2.0 - 1.0;
            escapeNum = calcEscapeForPixel(x_trans, y_trans);
            iterationCount[x][y] = escapeNum;
            histogram[escapeNum]++;
        }
    }

    /* Adding histogram up */
    for(x = 1; x < MAX_ITERATIONS; x++) {
        histogram[x] += histogram[x - 1];
    }

    /* Creating image */
    im = createImage(iterationCount, size, histogram);

    /* Saving */
    gdImagePngPtrEx(im, len, COMPRESSION_LEVEL);

    /* Freeing */
    gdImageDestroy(im);
    for(x = 0; x < size; x++) {
        free(iterationCount[x]);
    }
    free(iterationCount);
    free(histogram);
}

int calcEscapeForPixel(double x0, double y0) {
    int i;
    double x, y, x2, y2;

    i = 0;
    x = y = x2 = y2 = 0.0;

    while(x2 + y2 <= 4.0 && i < MAX_ITERATIONS) {
        y = 2.0 * x * y + y0;
        x = x2 - y2 + x0;

        x2 = x * x;
        y2 = y * y;

        i++;
    }

    return i;
}

gdImagePtr createImage(int** iterationCount, int size, int* histogram) {
    int r, g, b, x, y, total, colour, cur;
    double v, total_d;
    gdImagePtr im;

    total = histogram[MAX_ITERATIONS - 1];
    total_d = (double)total;

    im = gdImageCreateTrueColor(size, size);

    for(x = 0; x < size; x++) {
        for(y = 0; y < size; y++) {
            /* Calculating needed colour */
            cur = histogram[iterationCount[x][y]];
            if(iterationCount[x][y] == MAX_ITERATIONS) {
                /* Just use solid black */
                colour = gdImageColorExact(im, 0, 0, 0);
            }
            else {
                v = (double)cur / total_d;
                HsvToRgb(HUE, SATURATION, v, &r, &g, &b);
                /* For truecolor images, shouldn't have to allocate colors */
                colour = gdImageColorExact(im, r, g, b);
            }

            gdImageSetPixel(im, x, y, colour);
        }
    }

    return im;
}

void HsvToRgb(double h, double s, double v, int* r, int* g, int* b) {
    /* Converts HSV to RBG for good colours.
     * Based on https://www.rapidtables.com/convert/color/hsv-to-rgb.html as that gave the only explanation I could understand */
    double C, X, m;
    double pre_r, pre_g, pre_b;

    C = v * s;
    X = C * (1 - abs(fmod((h / 60.0), 2.0) - 1.0));
    m = v - C;

    if (h <= 60.0) {
        pre_r = C;
        pre_g = X;
        pre_b = 0.0;
    }
    else if (h <= 120.0) {
        pre_r = X;
        pre_g = C;
        pre_b = 0.0;
    }
    else if (h <= 180.0) {
        pre_r = 0.0;
        pre_g = C;
        pre_b = X;
    }
    else if (h <= 240.0) {
        pre_r = 0.0;
        pre_g = X;
        pre_b = C;
    }
    else if (h <= 300.0) {
        pre_r = X;
        pre_g = 0.0;
        pre_b = C;
    }
    else {
        pre_r = C;
        pre_g = 0.0;
        pre_b = X;
    }
    *r = (int)((pre_r + m) * 255.0);
    *g = (int)((pre_g + m) * 255.0);
    *b = (int)((pre_b + m) * 255.0);
}

void freeImage(char* ptr) {
    gdFree(ptr);
}
