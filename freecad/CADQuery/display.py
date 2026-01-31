# SPDX-License-Identifier: Apache-2.0
# SPDX-FileNotice: Part of the CADQuery addon.

from .Qt.Widgets import QMdiArea
from cadquery import Workplane , Shape
from FreeCAD import activeDocument , getDocument , newDocument , Gui
from Part import Shape as PartShape
from io import BytesIO



# Define the show_object function which CadQuery execution environments need to provide
def show_object(cq_object, options=None):

    from .Qt.Widgets import QMdiArea
    from cadquery import Workplane , Shape
    from FreeCAD import activeDocument , getDocument , newDocument , Gui
    from Part import Shape as PartShape
    from io import BytesIO


    # Create the object that the BRep data will be read into
    brep_stream = BytesIO()

    # Keep track of the feature name
    feature_name = None
    # Check to see what type of object we are dealing with
    if isinstance(cq_object, Workplane):

        value = cq_object.val()

        if isinstance(value,Shape):

            # Handle the label if the user set it
            if value.label:
                feature_name = value.label

            # If we have a workplane, we need to convert it to a solid
            value.exportBrep(brep_stream)

    elif isinstance(cq_object, Shape):
        # If we have a solid, we can export it directly
        cq_object.exportBrep(brep_stream)
    elif hasattr(cq_object, "wrapped"):
        # Handle the label if the user has it set
        if hasattr(cq_object, "label"):
            feature_name = cq_object.label

        from build123d import export_brep
        export_brep(cq_object, brep_stream)
    elif hasattr(cq_object, "_obj"):
        # Handle the label if the user has it set
        if hasattr(cq_object, "label"):
            feature_name = cq_object.label

        from build123d import export_brep
        export_brep(cq_object._obj, brep_stream)
    else:
        print("Object type not suuport for display: ", type(cq_object).__name__)
        return

    # Get the title of the current document so that we can create/find the FreeCAD part window
    doc_name = "untitled"
    mw = Gui.getMainWindow()
    mdi_area = mw.findChild(QMdiArea)

    if not mdi_area:
        return

    active_subwindow = mdi_area.activeSubWindow()
    if active_subwindow:
        doc_name = active_subwindow.windowTitle().split(" :")[0]
        doc_name = doc_name.split(".py")[0]

    # Create or find the document that corresponds to this code pane
    # If the matching 3D view has been closed, we need to open a new one
    try:
        getDocument(doc_name)
    except NameError:
        newDocument(doc_name)
    ad = activeDocument()

    # Convert the CadQuery object to a BRep string and then into a FreeCAD part shape
    brep_string = brep_stream.getvalue().decode('utf-8')
    part_shape = PartShape()
    part_shape.importBrepFromString(brep_string)

    # options={"alpha":0.5, "color": (64, 164, 223)}

    # If the user wanted to use a specific name in the tree, use it
    if not feature_name:
        feature_name = doc_name

    # Find the feature in the document, if it exists
    cur_feature = None
    for feat in ad.Objects:
        if feat.Name == feature_name or feat.Label == feature_name:
            cur_feature = feat
            break

    # Decide whether to create a new object or update an existing one
    if cur_feature:
        # Update the existing object
        cur_feature = ad.getObject(feature_name)
        cur_feature.Shape = part_shape
    else:
        cur_feature = ad.addObject("Part::Feature", feature_name)
        cur_feature.Label = feature_name
        cur_feature.Shape = part_shape

    # Apply any options to the imported shape
    if options:
        # Handle a transparency change, if requested
        if "alpha" in options:
            # Make sure that the alpha is scaled between 0 and 255
            alpha = int(options["alpha"] * 100)
            cur_feature.ViewObject.Transparency = alpha

        # Handle a color change, if requested
        if "color" in options:
            cur_feature.ViewObject.ShapeColor = options["color"]

    # Make sure the document updates
    ad.recompute()
