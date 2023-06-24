#!/usr/bin/python3

import sys
import zipfile
import getopt

opt, par = getopt.getopt(sys.argv[1:], "-s:")
input_file = par[0]
output_file = par[1]

try:
    # Read compressed file
    zfile = zipfile.ZipFile(input_file)
    files = zfile.namelist()

    # Check whether we have a FreeCAD document
    if "Document.xml" not in files:
        print(input_file, " doesn't look like a FreeCAD file")
        sys.exit(1)

    # Read thumbnail from file or use default icon
    image = "thumbnails/Thumbnail.png"
    if image in files:
        image = zfile.read(image)
    else:
        # apps should have at least 48x48 icons
        freecad = open("/usr/share/icons/hicolor/48x48/apps/freecad.png", "rb")
        image = freecad.read()

    # Write icon to output_file
    thumb = open(output_file, "wb")
    thumb.write(image)
    thumb.close()

except Exception:
    print("Error creating FreeCAD thumbnail for file ", input_file)
    sys.exit(1)
