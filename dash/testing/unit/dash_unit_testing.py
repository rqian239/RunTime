# --------------------------------------------------------
import sys
from pathlib import Path


# This is needed so that imports work in this project
# Not best practice but it makes files within the dash/ directory visible by Python interpreter

src_dir = Path(__file__).resolve().parent.parent.parent # This loads the "dash" directory...
# print(src_dir)
sys.path.append(str(src_dir))
# --------------------------------------------------------

