"""@TODO: colors module docstring"""

from collections import namedtuple


class Color(namedtuple('Color', ['r', 'g', 'b'])):
    """@TODO: Color class docstring"""

    # @TODO: override arithmetic operators


BLACK = Color(0x00, 0x00, 0x00)
# WHITE = ~BLACK
RED = Color(0xff, 0x00, 0x00)
GREEN = Color(0x00, 0xff, 0x00)
BLUE = Color(0x00, 0x00, 0xff)
# CYAN = GREEN + BLUE
# MAGENTA = BLUE + RED
# YELLOW = RED + GREEN
