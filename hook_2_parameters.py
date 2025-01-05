# [Imports]
import sys

# [Definitions]
Yes = True
No = False

main_globals = sys.modules["__main__"].__dict__

# [Parameters]
if "P_length" not in main_globals:   # you can define the parameter in the main script
    P_length = 20.0               # modify the hook length
    print(f'P_length is not defined in the main script, using default value {P_length}')
else: 
    P_length = main_globals["P_length"]
    print(f'P_length is defined in the main script as {P_length}')

if "P_height" not in main_globals:   # you can define the parameter in the main script
    P_height = 12.0               # modify the hook height
    print(f'P_height is not defined in the main script, using default value {P_height}')
else:
    P_height = main_globals["P_height"]
    print(f'P_height is defined in the main script as {P_height}')
# more parameters that might be modified to your needs
P_file_stl  = "Multiboard__Push-Fit-Hook__15x7.5mm.stl"
P_file_step = P_file_stl.replace(".stl", ".step")
P_models_dir = "./models"
P_a1 = 13.14 / 2.0 
P_a2 = 14.3 / 2.0
P_a3 = 14.7 / 2.0
P_b1 = 3.1 
P_b2 = P_a3 
P_b3 = 9.2 / 2.0
P_rotation = 157.5
P_l3 = P_length + 1.72
P_l2 = P_l3 + 5.5
P_l1 = P_l2 + 0.5
P_l4 = 0.0
P_h1 = -6.79
P_h2 = P_h1 + 4.0
P_h3 = P_height 
P_h4 = P_h3 + 2.5