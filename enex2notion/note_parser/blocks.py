import logging
from typing import List
from bs4 import NavigableString, Tag
from enex2notion.note_parser.blocks_helpers import extract_nested_blocks, flatten_root
from enex2notion.note_parser.blocks_indented import group_blocks_by_indent, is_indentation_inconsistent, parse_indented, parse_indented_plain
from enex2notion.note_parser.elements import div, encrypt, header
from enex2notion.note_parser.elements import list as el_list
from enex2notion.note_parser.elements import media, table
from enex2notion.notion_blocks.base import NotionBaseBlock
from enex2notion.notion_blocks.minor import NotionDividerBlock
from enex2notion.notion_blocks.text import NotionTextBlock, TextProp
logger = logging.getLogger(__name__)

def parse_note_blocks(note: Tag) -> List[NotionBaseBlock]:
    pass

def _append_branch(blocks, branch):
    pass

def _parse_indented_group(child):
    pass

def _parse_block(element: Tag):
    pass
