from typing import List
from bs4 import Tag
BLOCK_TAGS = ('div', 'h1', 'h2', 'h3', 'hr', 'ul', 'ol', 'hr', 'table', 'en-crypt', 'en-media', 'img')

def extract_nested_blocks(root: Tag):
    """Extract all block types to the document root
    new Evernote does something similar, while old one allowed to nest them
    """
    pass

def flatten_root(root: Tag):
    """Make sure that each <div> block represents single paragraph
    BAD                     | GOOD
    <en-note>               | <en-note>
     <div>                  |  <div>paragraph1</div>
      <div>paragraph1</div> |  <div>paragraph2</div>
      <div>paragraph2</div> |  <div><br /></div>
     </div>                 | </en-note>
     <div></div>            |
     <div><br /></div>      |
    </en-note>              |
    """
    pass

def _group_inline_tags(elements: List[Tag]):
    pass

def _make_block(elements: List[Tag]):
    """Make a single block from a list of elements"""
    pass

def _is_element_has_direct_blocks(element):
    pass

def _is_div_special_block(element: Tag):
    """Evernote has 3 special blocks that don't have their own tag:
    1. Code blocks
    2. Task
    3. Google drive links
    """
    pass
