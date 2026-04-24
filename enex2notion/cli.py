import logging
import sys
from pathlib import Path
from typing import List
from enex2notion.cli_args import parse_args
from enex2notion.cli_logging import setup_logging
from enex2notion.cli_notion import get_root
from enex2notion.cli_upload import EnexUploader
from enex2notion.cli_wkhtmltopdf import ensure_wkhtmltopdf
from enex2notion.utils_static import Rules
logger = logging.getLogger(__name__)

def cli(argv):
    pass

def _process_input(enex_uploader: EnexUploader, enex_input: List[Path]):
    pass

def main():
    pass
