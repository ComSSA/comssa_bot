#include <png.h>
//#include <zlib.h>

#define TESTING

#include "images.h"

#ifdef TESTING
int main() {
    return 0;
}
#endif

png_bytep makeEmptyPng(png_image* data) {
    png_bytep buffer;
    buffer = malloc(PNG_IMAGE_SIZE(*data));

    return buffer;
}
