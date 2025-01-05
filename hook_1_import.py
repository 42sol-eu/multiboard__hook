from build123d import *
from build123d.mesher import Mesher
from ocp_vscode import *

# [Parameters]
from hook_2_parameters import * 

# [Functions]
def import_stl_hook():
    print(f'importing {P_file_stl}')
    importer = Mesher()

    hook = importer.read(P_file_stl)
    print(
        f"{hook[0].bounding_box()}, {type(hook[0])}"
    )

    x, y, z = hook[0].center()
    x_diff = hook[0].bounding_box().max.X - hook[0].bounding_box().min.X
    y_diff = abs( hook[0].bounding_box().min.Y - hook[0].bounding_box().max.Y)
    z_diff = hook[0].bounding_box().max.Z - hook[0].bounding_box().min.Z
    print(f"{x_diff=}, {y_diff=}, {z_diff=}")

    hook[0].move(Location([-x+1.81, -y-8.6-0.31, -z]))
    
    return hook[0]


if __name__ == "__main__":
    model = import_stl_hook()
    show(model, names=["model"], colors=["red"])
