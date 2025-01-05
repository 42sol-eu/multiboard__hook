"""
file-name:      hook_3b_revolve_bend.py
file-uuid:      153c8f82-3ef1-4e07-8e09-f68ad862b11a
file-version:   2025.0.1
project-name:   multiboard__hooks
project-uuid:   c56a8125-5103-46bb-b250-3ebe7c28b11a
description:    create a MultiBoard push fit hook using a revolve on the bend.
"""
# [Imports]
from build123d import *

from ocp_vscode import *
from rich import print 
from pathlib import Path 
from math import cos, sin, pi, sqrt


# [Parameters]
P_length = 40.0
P_height = 20.0
from hook_2_parameters import * 

# [Functions]

from hook_1_import import import_stl_hook

def part():

    # calculate the values:
    # - a = side of the octogon, 
    # - b = height of outer triangle, 
    # - c = half of the base / radius to the center of a side
    a = 2 * P_a3 * sin(pi / 8.0)
    b = a / sqrt(2)
    c = b + a / 2 

    with BuildPart() as part_0:
        with BuildSketch(Plane.XZ) as sketch_2:
            with BuildLine() as c1:
                line_1 = PolarLine((c, 0), a, 90.0)
                line_2 = PolarLine(line_1 @ 1, a, 135.0)
                line_3 = PolarLine(line_2 @ 1, a, 180.0)
                line_4 = PolarLine(line_3 @ 1, a, 225.0)
                line_5 = PolarLine(line_4 @ 1, a, 270.0)
                line_6 = Line(line_5 @ 1, line_1 @ 0)
            make_face()
        c2 =revolve(axis=Axis.X, revolution_arc=90.0).move(Location([0, 0, -a/2]))

    with BuildPart() as part_A:
        adjust = Location([0, -a/2, -a/2])
        with BuildSketch(Plane.XY.offset(-P_l1).move(adjust)) as a3:
            RegularPolygon(P_a1, 8, rotation=P_rotation)
        with BuildSketch(Plane.XY.offset(-P_l2).move(adjust)) as a2:
            RegularPolygon(P_a2, 8, rotation=P_rotation)
        loft()
        with BuildSketch(Plane.XY.offset(-P_l2).move(adjust)) as a2:
            RegularPolygon(P_a2, 8, rotation=P_rotation)
        with BuildSketch(Plane.XY.offset(-P_l3).move(adjust)) as a1:
            RegularPolygon(P_a3, 8, rotation=P_rotation)
        loft()

        with BuildSketch(Plane.XY.move(adjust)) as a1:
            RegularPolygon(P_a3, 8, rotation=P_rotation)
        extrude(amount=-P_l3)

    with BuildPart() as part_B:
        add(part_A.part)
        add(c2)

        with BuildSketch(Plane.XZ) as b1:
            RegularPolygon(P_b2, 8, rotation=P_rotation)
        extrude(amount=-P_h3)

        with BuildSketch(Plane.XZ.offset(-P_h3)) as b2:
            RegularPolygon(P_b2, 8, rotation=P_rotation)
        with BuildSketch(Plane.XZ.offset(-P_h4)) as b3:
            RegularPolygon(P_b3, 8, rotation=P_rotation)
        loft()

    return part_B

# [Main]
def main():
    input = import_stl_hook().rotate(Axis.X, 90.0).rotate(Axis.Z, 90.0).move(Location([0, -2.85, -2.79]))
    part_A = part()

    show(input, part_A, names=["input", "part_A"],colors=["#FF0000AA", "#0000FFAA", "#00FF00AA", "#00FFFFAA", "#FF00FFAA", "#AA00FFAA"])
    part_A.part.export_stl(f"{P_models_dir}/hook_revolve_bend_{int(P_length)}x{int(P_height)}mm.stl")
    part_A.part.export_step(f"{P_models_dir}/hook_revolve_bend_{int(P_length)}x{int(P_height)}mm.step")

if __name__ == "__main__":
    main()
