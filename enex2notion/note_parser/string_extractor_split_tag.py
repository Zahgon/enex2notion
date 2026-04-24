import copy
from typing import List, Union
from bs4 import NavigableString, PageElement, Tag
STANDALONES = ('h1', 'h2', 'h3', 'div')

def split_tag(tag: Tag) -> List[Tag]:
    """
    Element is either a single div itself or a collection of div or h1-3 "lines"
    it can also contain random inline strings, so we group them in separate lines
    """
    pass

def _split_line(element: Tag) -> List[Tag]:
    pass

def _is_whitespace(element: PageElement) -> bool:
    pass

def _is_inline(element: Union[Tag, PageElement]) -> bool:
    pass

def _make_block(elements: List[Union[Tag, PageElement]]) -> Tag:
    """Make a single block from a list of elements"""
    pass
