# This example is meant to be used from within the CadQuery module of FreeCAD.
import cadquery
from Helpers import show

# The dimensions of the model. These can be modified rather than changing the
# object's code directly.
circle_radius = 3.0
thickness = 0.25

# Make the plate with two cutouts in it
# Current point is the center of the circle, at (0,0)
result = cadquery.Workplane("front").circle(circle_radius)
result = result.center(1.5, 0.0).rect(0.5, 0.5)  # New work center is (1.5,0.0)

result = result.center(-1.5, 1.5).circle(0.25)  # New work center is ( 0.0,1.5)
# The new center is specified relative to the previous center,
# not global coordinates!

result = result.extrude(thickness)

# Render the solid
show(result)
