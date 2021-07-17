# distutils: sources = c_programs/mandelbrot.c
# distutils: include_dirs = c_programs/

import cython
from errors.errors import MemoryError

cdef extern from "mandelbrot.h":
    char* generateMandelbrot(int size, int* len)
    void freeImage(char* ptr)

def generate_mandelbrot(size: cython.int) -> bytes:
    length: cython.int = -1
    raw_image: cython.p_char
    py_image: bytes

    raw_image = generateMandelbrot(size, &length)

    if length <= -1 or raw_image is NULL:
        raise MemoryError("Not enough memory")
    
    # This will make cython copy length bytes, starting at the position pointed to by raw_image, to a python bytes object
    # Cython doesn't support wrapping a section of memory in a bytes container, so this is the best option
    py_image = raw_image[:length]
    # After it's copied, the C memory can be cleaned up however
    freeImage(raw_image)

    return py_image
