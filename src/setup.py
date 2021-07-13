from setuptools import Extension, setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize(
        [Extension(
            "cogs.example.mandelbrot",
            ["cogs/example/mandelbrot.pyx"],
            libraries=["gd", "png", "z", "jpeg", "freetype", "m"]
        )],
        compiler_directives = {"language_level": "3"}
    )
)
