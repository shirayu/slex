#!/usr/bin/env python


from __future__ import print_function, absolute_import

import os

##//////////////////////////////////////////////////////
##  Metadata
##//////////////////////////////////////////////////////

# Version.  For each new release, the version number should be updated
# in the file VERSION.
try:
    # If a VERSION file exists, use it!
    version_file = os.path.join(os.path.dirname(__file__), 'VERSION')
    with open(version_file) as fh:
        __version__ = fh.read().strip()
except NameError:
    __version__ = 'unknown (running code interactively?)'
except IOError as ex:
    __version__ = "unknown (%s)" % ex

if __doc__ is not None: # fix for the ``python -OO``
    __doc__ += '\n@version: ' + __version__


###########################################################
# TOP-LEVEL MODULES
###########################################################

# Import top-level functionality into top-level namespace
from .stanford import *

###########################################################
# PACKAGES
###########################################################

