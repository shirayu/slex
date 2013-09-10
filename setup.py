#!/usr/bin/env python

__author__ = 'Yuta Hayashibe' 
__version__ = ""
__copyright__ = ""
__license__ = "GPL v3"

import os
version_file = os.path.join(os.path.dirname(__file__), 'VERSION')
with open(version_file) as fh:
    slex_version = fh.read().strip()


from setuptools import setup, find_packages, Extension
setup(
    name = "slex",
    version = slex_version,
    maintainer = "Yuta Hayashibe",
    maintainer_email = "yuta@hayashibe.jp",
    author = "Yuta Hayashibe",
    author_email = "yuta@hayashibe.jp",
    description = "Stanford Parser buindings for Python.",
    license = "GNU GENERAL PUBLIC LICENSE Version 3",
    url = "https://github.com/shirayu/slex-python",
#    package_dir={},
    package_data = {"slex" : ["tool/ClassPathModifier.*"]},
    scripts = ["slex/scripts/slex"],
#    packages=['slex'],
    install_requires=[
        "JPype >= 0.5.4.2"
    ],
    packages = find_packages(),
)

