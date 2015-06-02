from fluent2xml import *
import sys
from os import path

if len(sys.argv) == 1:
    print "Usage: python convert_mesh.py filename"
    sys.exit(0)

filename_fluent = sys.argv[1]
filename_xml = filename_fluent.replace(".msh", ".xml")
filename_xml = path.join(path.dirname(path.abspath(__file__)), filename_xml)
fluent2xml(filename_fluent, filename_xml)
