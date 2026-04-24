import hashlib
import logging
import mimetypes
import re
from bs4 import Tag
from w3lib.url import parse_data_uri
from enex2notion.enex_types import EvernoteResource
from enex2notion.notion_blocks.embeddable import NotionImageEmbedBlock
from enex2notion.notion_blocks.uploadable import NotionAudioBlock, NotionFileBlock, NotionImageBlock, NotionPDFBlock, NotionVideoBlock
from enex2notion.utils_notion_filetypes import NOTION_AUDIO_MIMES, NOTION_IMAGE_MIMES, NOTION_VIDEO_MIMES
logger = logging.getLogger(__name__)

def parse_media(element: Tag):
    pass

def parse_img(element: Tag):
    pass

def _parse_img_resource(bin_src: str):
    pass

def _parse_media(block_type, element):
    pass

def _parse_dimensions(element: Tag):
    pass
