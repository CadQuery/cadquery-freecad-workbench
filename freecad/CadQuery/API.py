# SPDX-License-Identifier: Apache-2.0
# SPDX-FileNotice: Part of the CadQuery addon.

from .display import show_object

from sys import modules


def setupAPI ():

    try:

        import cadquery as api

        setattr(api,'show',show_object)

        modules[ 'CadQuery' ] = api

    except:
        pass

