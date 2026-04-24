from typing import List
from enex2notion.notion_blocks.base import NotionBaseBlock
from enex2notion.notion_blocks.text import NotionTextBlock, TextProp

class LineCondenser(object):

    def __init__(self, is_sparse: bool):
        self.result_blocks = []
        self.solid_block = None
        self.is_sparse = is_sparse

    @property
    def final_blocks(self):
        pass

    def add_block(self, b):
        pass

    def _start_new_solid_block(self):
        pass

    def _add_to_solid_block(self, b):
        pass

def condense_lines(blocks: List[NotionBaseBlock], is_sparse=False):
    pass

def _strip_paragraphs(blocks: List[NotionBaseBlock]):
    pass

def _join_empty_paragraphs(blocks: List[NotionBaseBlock]):
    pass

def _is_empty_paragraph(block: NotionBaseBlock):
    pass

def _concat_text_props(text_prop1: TextProp, text_prop2: TextProp) -> TextProp:
    pass
