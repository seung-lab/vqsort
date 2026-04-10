import os
import setuptools
import sys

from pybind11.setup_helpers import Pybind11Extension, build_ext

def read(fname):
  with open(os.path.join(os.path.dirname(__file__), fname), 'rt') as f:
    return f.read()

extra_compile_args = []
if sys.platform == 'win32':
  extra_compile_args += [
    '/std:c++20', '/O2'
  ]
else:
  extra_compile_args += [
    '-std=c++20', '-O3'
  ]

setuptools.setup(
  name="vqsort",
  version="0.0.1",
  setup_requires=["numpy","pybind11"],
  install_requires=[ 'numpy', ],
  extras_require={},
  python_requires=">=3.9.0",
  author="William Silversmith",
  author_email="ws9@princeton.edu",
  packages=setuptools.find_packages(),
  package_data={
    'vqsort': [
      'LICENSE',
    ],
  },
  ext_modules=[
    Pybind11Extension(
        "vqsort_bind",
        ["vqsort/vqsort_bind.cpp"],
        extra_compile_args=extra_compile_args,
        language="c++",
    ),
  ],
  description="Morphological image processing for 3D multi-label images.",
  long_description=read('README.md'),
  long_description_content_type="text/markdown",
  license = "BSD-3",
  keywords = "sorting sort vqsort",
  url = "https://github.com/seung-lab/fastmorph/",
  classifiers=[
    "Intended Audience :: Developers",
    "Development Status :: 4 - Beta",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: 3.14",
    "Intended Audience :: Science/Research",
    "Operating System :: POSIX",
    "Operating System :: MacOS",
    "Operating System :: Microsoft :: Windows :: Windows 10",
  ],  
)


