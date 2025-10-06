# Name: Ivy Loi
# Class Section: 3
# File Purpose: initialize __all__ to whoami and series file

from . import whoami as numbers_whoami # These two lines are needed otherwise whoami name in main appears as mathematics.geometry.whoami
from . import series

__all__ = ['numbers_whoami', 'series']