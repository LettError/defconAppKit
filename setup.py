#!/usr/bin/env python

import sys
from setuptools import setup

try:
    import fontTools
except:
    print("*** Warning: defcon requires FontTools, see:")
    print("    https://github.com/fonttools/fonttools")

setup(name="defconAppKit",
    version="0.1",
    description="A set of interface objects for working with font data.",
    author="Tal Leming",
    author_email="tal@typesupply.com",
    url="https://github.com/typesupply/defconAppKit",
    license="MIT",
    packages=[
        "defconAppKit",
        "defconAppKit.controls",
        "defconAppKit.representationFactories",
        "defconAppKit.tools",
        "defconAppKit.windows"
    ],
    package_dir={"":"Lib"}
)
