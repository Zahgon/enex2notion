import logging
import re
from bs4 import Tag
from enex2notion.note_parser.string_extractor import extract_string
from enex2notion.notion_blocks.container import NotionCodeBlock
from enex2notion.notion_blocks.list import NotionTodoBlock
from enex2notion.notion_blocks.minor import NotionBookmarkBlock
from enex2notion.notion_blocks.text import NotionTextBlock
logger = logging.getLogger(__name__)

def parse_div(element: Tag):
    pass

def parse_codeblock(element: Tag):
    pass

def parse_text(element: Tag):
    pass

def parse_richlink(element: Tag):
    pass
