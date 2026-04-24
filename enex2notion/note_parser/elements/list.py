import logging
from typing import List

from bs4 import NavigableString, PageElement, Tag

from enex2notion.note_parser.elements.media import parse_img, parse_media
from enex2notion.note_parser.string_extractor import extract_string
from enex2notion.notion_blocks.base import NotionBaseBlock
from enex2notion.notion_blocks.list import (
    NotionBulletedListBlock,
    NotionNumberedListBlock,
    NotionTodoBlock,
)
from enex2notion.notion_blocks.text import NotionTextBlock, TextProp

logger = logging.getLogger(__name__)


class ListNodes(object):
    def __init__(self, is_ul: bool):
        self.nodes: List[NotionBaseBlock] = []
        self.is_ul = is_ul

    def add_li(self, subelement: Tag) -> None:
        pass

    def add_ul_ol(self, subelement: Tag) -> None:
        pass

    def add_odd_one(self, subelement):
        pass


def parse_list(element: Tag) -> List[NotionBaseBlock]:
    pass


def _extract_media(element: Tag):
    pass


def _make_blank_node(is_ul):
    pass


def _parse_odd_item(element: PageElement):
    pass


def _parse_list_item(list_item, is_ul):
    pass
