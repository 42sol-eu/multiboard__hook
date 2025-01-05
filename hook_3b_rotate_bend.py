# [Imports]
from build123d import *

from ocp_vscode import *
from rich import print 
from pathlib import Path 
from math import sin, pi


# [Parameters]
from hook_2_parameters import * 

# [Functions]

from hook_1_import import import_stl_hook

def part_A():

    # height of the regular triangle 
    # 60 degrees in radians

    P_height = sin(60 * pi / 180) * P_a3


    with BuildPart() as part_A:

        Box(P_length, P_height, P_height)
    # part_B = part_A.part.copy().move(Location([0, 0, 20])).rotate(Axis.Y, P_rotation_fails)
        if No: 
            with BuildSketch(Plane.XZ.offset(P_l1)) as a1:
                RegularPolygon(P_a1, 8, rotation=P_rotation)

            with BuildSketch(Plane.XZ.offset(P_l2)) as a2:
                RegularPolygon(P_a2, 8, rotation=P_rotation)
            loft()

            with BuildSketch(Plane.XZ.offset(P_l2)) as a2:
                RegularPolygon(P_a2, 8, rotation=P_rotation)
            with BuildSketch(Plane.XZ.offset(P_l3)) as a3:
                RegularPolygon(P_a3, 8, rotation=P_rotation)
            loft()

            with BuildSketch(Plane.YZ.offset(P_h3)) as b3:
                RegularPolygon(P_b2, 8, rotation=P_rotation)
            with BuildSketch(Plane.YZ.offset(P_h4)) as b4:
                RegularPolygon(P_b3, 8, rotation=P_rotation)
            loft()

        
        a1 = None
        a2 = None
        a3 = None
    return part_A, a1, a2, a3

# [Main]
input = import_stl_hook()
part_A, a1, a2, a3 = part_A()

show(input, part_A, a1, a2, a3, names=["input", "part_A", "line_1", "line_2", "line_3" ],colors=["#FF0000AA", "#0000FFAA", "#00FF00AA", "#00FFFFAA", "#FF00FFAA", "#AA00FFAA"])

if True and  __name__ == "__main__":
    part_A.part.export_stl(f"{P_models_dir}/hook_sweep_{int(P_length)}x{int(P_height)}mm.stl")
    part_A.part.export_step(f"{P_models_dir}/hook_sweep_{int(P_length)}x{int(P_height)}mm.step")