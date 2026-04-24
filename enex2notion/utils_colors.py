import contextlib
import re
from functools import partial
from math import sqrt
from types import MappingProxyType
from tinycss2 import parse_declaration_list
from tinycss2.color3 import parse_color
HEX_BASE = 16
base16 = partial(int, base=HEX_BASE)
EVERNOTE_STANDARD_FG = MappingProxyType({(51, 51, 51): 'black', (90, 90, 90): 'gray', (140, 140, 140): 'gray', (191, 191, 191): 'gray', (255, 255, 255): 'white', (87, 36, 194): 'purple', (182, 41, 212): 'purple', (252, 18, 51): 'red', (251, 95, 44): 'orange', (229, 158, 37): 'yellow', (24, 168, 65): 'teal', (26, 169, 178): 'blue', (24, 133, 226): 'blue', (13, 58, 153): 'blue'})
EVERNOTE_STANDARD_BG = MappingProxyType({(255, 209, 176): 'orange_background', (255, 239, 158): 'yellow_background', (255, 250, 165): 'yellow_background', (183, 247, 209): 'teal_background', (173, 236, 244): 'blue_background', (203, 202, 255): 'purple_background', (254, 193, 208): 'red_background'})
COLORS_FG = MappingProxyType({'black': (0, 0, 0), 'white': (255, 255, 255), 'gray': (140, 140, 140), 'brown': (159, 107, 83), 'orange': (251, 95, 33), 'yellow': (229, 158, 37), 'teal': (24, 168, 65), 'blue': (24, 133, 226), 'purple': (182, 41, 212), 'pink': (193, 76, 138), 'red': (252, 18, 51)})
COLORS_BG = MappingProxyType({'black_background': (0, 0, 0), 'white_background': (255, 255, 255), 'gray_background': (241, 241, 239), 'brown_background': (244, 238, 238), 'orange_background': (255, 209, 176), 'yellow_background': (255, 239, 158), 'teal_background': (183, 247, 209), 'blue_background': (173, 236, 244), 'purple_background': (203, 202, 255), 'pink_background': (249, 238, 243), 'red_background': (254, 193, 208)})

def extract_color(style):
    pass

def _parse_style(style):
    pass

def _parse_css_color(color_token):
    pass

def _extract_background_text(color_token):
    pass

def _extract_background_rgb(color_token):
    pass

def _extract_foreground_rgb(color_token):
    pass

def _closest_color(colors, rgb):
    pass
