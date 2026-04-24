import logging
from typing import Optional
from bs4 import BeautifulSoup, Tag
from enex2notion.enex_types import EvernoteNote
from enex2notion.note_parser.note_post_process_condense import condense_lines
from enex2notion.note_parser.note_post_process_resources import resolve_resources
from enex2notion.note_parser.note_type_based import parse_note_blocks_based_on_type
from enex2notion.notion_blocks.container import NotionCalloutBlock
from enex2notion.notion_blocks.text import TextProp
from enex2notion.utils_static import Rules
logger = logging.getLogger(__name__)

def parse_note(note: EvernoteNote, rules: Rules):
    pass

def _parse_note_dom(note: EvernoteNote) -> Optional[Tag]:
    pass

def _filter_yinxiang_markdown(note_dom: Tag) -> Tag:
    pass

def _add_meta(note_blocks, note: EvernoteNote):
    pass

def _get_note_meta(note: EvernoteNote):
    pass
