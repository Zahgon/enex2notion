import hashlib
import logging
import re
from base64 import b64encode
import fitz
import pdfkit
from bs4 import Tag
from enex2notion.enex_types import EvernoteNote, EvernoteResource
from enex2notion.notion_blocks.uploadable import NotionImageBlock, NotionPDFBlock
logger = logging.getLogger(__name__)

def parse_webclip_to_pdf(note: EvernoteNote, note_dom: Tag, is_add_pdf_preview: bool):
    pass

def _get_pdf_preview(pdf_bin: bytes):
    pass

def _get_pdf_first_page_png(pdf_bin: bytes):
    pass

def _convert_local_images(note_dom: Tag, note: EvernoteNote):
    pass

def _remove_remote_images(note_dom: Tag):
    pass
