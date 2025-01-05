from build123d import *
from build123d import importers
from rich import print 
from pathlib import Path 
from build123d.mesher import Mesher

P_file_step = "15 x 7.5 mm, Push-Fit Hook.step"
P_file_stl  = "15 x 7.5 mm, Push-Fit Hook.stl"

from ocp_vscode import *
set_defaults(reset_camera=Camera.CENTER, helper_scale=5)

if Path(P_file_step).is_file():
    print(f"File {P_file_step} exists")

if Path(P_file_stl).is_file():  
    print(f"File {P_file_stl} exists")

P_radius_1 = 6.1 * MM
P_radius_2 = 13.227 * MM / 2
P_radius_main = 13.5 * MM / 2
P_radius_end  = 8.5 * MM / 2
P_length_inner = 15.5 * MM
P_length_outer = 16.5 * MM
P_length = 24.456 * MM
P_length_end = 2.5 * MM

with BuildPart() as part:
    # with BuildLine() as hook:

    with BuildSketch() as sketch:
        RegularPolygon(P_radius_2, 8)
    with BuildSketch(Plane.XY.offset(P_length_end)) as top:
        RegularPolygon(P_radius_end, 8)
    loft()


show_all()