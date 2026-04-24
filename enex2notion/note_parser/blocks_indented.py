import re
from typing import List
from bs4 import Tag
from enex2notion.note_parser.elements.div import parse_text
EVERNOTE_INDENT_MARGIN = 40

def group_blocks_by_indent(root: Tag):
    pass

def is_indentation_inconsistent(paragraphs: List[Tag]):
    """Evernote has strict indentation margin of 40px"""
    pass

def parse_indent_level(element: Tag):
    pass

def parse_indented(paragraphs: List[Tag], indent_level: int=None):
    """Builds paragraphs tree using indentation levels"""
    pass

def parse_indented_plain(paragraphs: List[Tag]):
    pass
