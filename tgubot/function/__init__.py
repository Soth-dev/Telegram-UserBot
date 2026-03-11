import pkgutil
import importlib

# import inspect
from pathlib import Path

# 1. Iterate through all modules in the current directory (hello, shell)
for _, module_name, _ in pkgutil.iter_modules([str(Path(__file__).parent)]):
    print(module_name)
    # 2. Import the module dynamically (e.g., lib.hello)
    importlib.import_module(f".{module_name}", package=__name__)

    # 3. Get all functions in that module
    """
    for name, obj in inspect.getmembers(module, inspect.isfunction):
        # 4. Check if the function name starts with an uppercase letter
        if len(name) >= 2 and name[0].isupper() and name[1].islower():
            # 5. Bind it to the __init__.py namespace
            globals()[name] = obj
            print(name)"""

# Optional: Clean up the namespace so these utility modules don't get imported
# del pkgutil, importlib, inspect, Path, module_name, module, name, obj
