import sys
import os
import importlib
from pathlib import Path
import inspect

# Add the src directory to the Python search path
src_dir = Path(__file__).resolve().parent.parent  # This should point to the src directory
sys.path.append(str(src_dir))

# Get the absolute path of the src/modules folder
modules_path = src_dir / 'modules'

def print_class_signatures(module):
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            print(f"Class: {obj.__name__}")
            print("Docstring:")
            if obj.__doc__:
                print(obj.__doc__)
            else:
                print("No docstring available")
            print("Methods:")
            for method_name, method_obj in inspect.getmembers(obj, predicate=inspect.isfunction):
                argspec = inspect.getfullargspec(method_obj)
                args = ', '.join(argspec.args)
                print(f"  {method_name}({args})")
            print()

# Iterate over all files in the src/modules folder
for filename in os.listdir(modules_path):
    # Check if the file is a Python source file
    if filename.endswith('.py') and not filename.startswith('__'):
        # Remove the ".py" extension and import the module
        module_name = 'modules.' + filename[:-3]
        module = importlib.import_module(module_name)

        # Call the print_class_signatures function for the imported module
        print_class_signatures(module)
