# This example is meant to be used from within the CadQuery module of FreeCAD.
import cadquery
from Helpers import show

# The dimensions of the model. These can be modified rather than changing the
# object's code directly.
plate_radius = 2.0
hole_pattern_radius = 0.25
thickness = 0.125

# Make the plate with 4 holes in it at various points
# Make the base
r = cadquery.Workplane("front").circle(plate_radius)
# Now four points are on the stack
r = r.pushPoints([(1.5, 0), (0, 1.5), (-1.5, 0), (0, -1.5)])
# Circle will operate on all four points
r = r.circle(hole_pattern_radius)
result = r.extrude(thickness)

# Render the solid
show(result)
