import pkgutil
import importlib

from pathlib import Path

# 1. Iterate through all modules in the current directory (hello, shell)
for _, module_name, _ in pkgutil.iter_modules([str(Path(__file__).parent)]):
    print(f"\nModules: {module_name}")
    # 2. Import the module dynamically (e.g., lib.hello)
    importlib.import_module(f".{module_name}", package=__name__)
