# SPDX-License-Identifier: Apache-2.0
# SPDX-FileNotice: Part of the CADQuery addon.


from .display import show_object

# Register the show_object function as a global function
globals()['show_object'] = show_object
