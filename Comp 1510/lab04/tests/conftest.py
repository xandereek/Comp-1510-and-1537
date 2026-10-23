"""Connect the supplied tests to the project files. Leave this file unchanged.

The test files start with imports like ``from q2 import ...``, but on
their own the tests cannot see ``q2.py`` one folder up. Pytest loads
this file automatically before running any tests, and it points pytest
to the project folder so the imports work.
"""

import sys
from pathlib import Path

_root = Path(__file__).resolve().parent.parent
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))
