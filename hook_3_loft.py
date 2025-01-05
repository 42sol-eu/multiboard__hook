# [Imports]
from build123d import *

from ocp_vscode import *
from rich import print 
from pathlib import Path 


# [Parameters]
from hook_2_parameters import * 


# [Functions]
from hook_1_import import import_stl_hook

def part_A():
    with BuildPart() as part_A:
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

        with BuildSketch(Plane.XZ.offset(P_l3)) as a3:
            RegularPolygon(P_a3, 8, rotation=P_rotation)
        with BuildSketch(Plane.XZ.offset(P_l4)) as a4:
            RegularPolygon(P_a3, 8, rotation=P_rotation)
        loft()
        with BuildSketch(Plane.YZ.offset(P_h1)) as b1:
            RegularPolygon(P_b1, 8, rotation=P_rotation)

        with BuildSketch(Plane.YZ.offset(P_h2)) as b2:
            RegularPolygon(P_b2, 8, rotation=P_rotation)
        loft()

        with BuildSketch(Plane.YZ.offset(P_h2)) as b2:
            RegularPolygon(P_b2, 8, rotation=P_rotation)
        with BuildSketch(Plane.YZ.offset(P_h3)) as b3:
            RegularPolygon(P_b2, 8, rotation=P_rotation)
        loft()

        with BuildSketch(Plane.YZ.offset(P_h3)) as b3:
            RegularPolygon(P_b2, 8, rotation=P_rotation)
        with BuildSketch(Plane.YZ.offset(P_h4)) as b4:
            RegularPolygon(P_b3, 8, rotation=P_rotation)
        loft()

    return part_A, a1, a2, a3, a4, b1, b2, b3, b4

# [Main]
input = import_stl_hook()
part_A, a1, a2, a3, a4, b1, b2, b3, b4 = part_A()

bounding_box = part_A.part.bounding_box()
length = bounding_box.max.X - bounding_box.min.X 

show(input, part_A, a1, b1, b3, b4, names=["input", "part_A", "a1", "b1", "b3", "b4" ],colors=["#FF0000AA", "blue", "green", "yellow", "purple", "orange"])

if __name__ == "__main__":
    part_A.part.export_stl(f"{P_models_dir}/hook_loft_{int(P_length)}mm.stl")
    part_A.part.export_step(f"{P_models_dir}/hook_loft_{int(P_length)}mm.step")