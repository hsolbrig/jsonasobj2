#!/usr/bin/env python
import sys
from setuptools import setup
from warnings import warn

if sys.version_info < (3, 6, 0):
    warn(f"jsonasobj2 requires python 3.6.0 or later.  Current version: {sys.version_info}")

setup(
    setup_requires=['pbr'],
    pbr=True,
)
