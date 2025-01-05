# [Imports]
from build123d import *

from ocp_vscode import *
from rich import print 
from pathlib import Path 


# [Parameters]
P_length = 40.0
P_height = 20.0
from hook_2_parameters import * 


# [Functions]
from hook_1_import import import_stl_hook

def part():
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

    return part_A

# [Main]
def main():
    input = import_stl_hook().move(Location([30.0, 0, 0]))
    part_A = part()

    bounding_box = part_A.part.bounding_box()
    length = bounding_box.max.X - bounding_box.min.X 

    show(input, part_A, names=["input", "part_A", ],colors=["#FF0000AA", "blue", "green", "yellow", "purple", "orange"])
    
    part_A.part.export_stl(f"{P_models_dir}/hook_loft_{int(P_length)}x{int(P_height)}mm.stl")
    part_A.part.export_step(f"{P_models_dir}/hook_loft_{int(P_length)}x{int(P_height)}mm.step")

if __name__ == "__main__":
    main()