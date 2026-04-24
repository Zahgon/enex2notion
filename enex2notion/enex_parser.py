import base64
import hashlib
import logging
import mimetypes
import re
import uuid
from datetime import datetime
from pathlib import Path
from typing import Iterator
from dateutil.parser import isoparse
from enex2notion.enex_parser_xml import iter_process_xml_elements, iter_xml_elements_as_dict
from enex2notion.enex_types import EvernoteNote, EvernoteResource
logger = logging.getLogger(__name__)

def count_notes(enex_file: Path) -> int:
    pass

def _log_xml_errors(xml_file: Path, errors):
    pass

def iter_notes(enex_file: Path) -> Iterator[EvernoteNote]:
    pass

def _process_note(note_raw: dict) -> EvernoteNote:
    pass

def _parse_resources(note_raw):
    pass

def _is_webclip(note_raw: dict):
    pass

def _convert_resource(resource_raw):
    pass

def _is_banned_extension(filename):
    pass
