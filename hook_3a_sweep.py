# [Imports]
from build123d import *

from ocp_vscode import *
from rich import print 
from pathlib import Path 
from math import sin, pi


# [Parameters]
P_length = 40.0
P_height = 20.0
from hook_2_parameters import * 

# [Functions]

from hook_1_import import import_stl_hook

def part():

    # height of the regular triangle 
    # 60 degrees in radians

    P_height = sin(60 * pi / 180) * P_a3


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

        with BuildSketch(Plane.YZ.offset(P_h3)) as b3:
            RegularPolygon(P_b2, 8, rotation=P_rotation)
        with BuildSketch(Plane.YZ.offset(P_h4)) as b4:
            RegularPolygon(P_b3, 8, rotation=P_rotation)
        loft()

        with BuildLine() as l1:
            line_1 = Line((0.0,-P_l3,0.0),(0.0,-1.0,0.0))
        with BuildSketch(Plane.XZ.offset(P_l3)) as a3:
            RegularPolygon(P_a3, 8, rotation=P_rotation)
        
        add(sweep(path=l1))

        with BuildLine() as l2:
            line_2 = JernArc((0.0,-1.0,0.0), (0.0,1.0,0.0), radius=1.0, arc_size=-90)
        plane = Plane.XZ.offset(P_l3)
        with BuildSketch(line_2 ^ 0) as a3:
            RegularPolygon(P_a3, 8, rotation=P_rotation)        
        
        a4 = sweep()
        add(a4)

        with BuildLine() as l3:
            line_3 = Line((1.0,0.0,0.0),(P_h3,0.0,0.0))
        with BuildSketch(line_3 ^ 0) as b3:
            RegularPolygon(P_b2, 8, rotation=P_rotation)        
        add(sweep(path=l3))

    return part_A

# [Main]
def main():
    input = import_stl_hook()
    part_A = part()

    show(input, part_A, names=["input", "part_A"],colors=["#FF0000AA", "#0000FFAA", "#00FF00AA", "#00FFFFAA", "#FF00FFAA", "#AA00FFAA"])
    part_A.part.export_stl(f"{P_models_dir}/hook_sweep_{int(P_length)}x{int(P_height)}mm.stl")
    part_A.part.export_step(f"{P_models_dir}/hook_sweep_{int(P_length)}x{int(P_height)}mm.step")


if __name__ == "__main__":
    main()