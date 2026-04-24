from collections import defaultdict
from pathlib import Path
from typing import Any, Callable, Dict, Iterator, List, Optional
from lxml import etree
from lxml.etree import XMLSyntaxError, _Entity

def iter_xml_elements_as_dict(xml_file: Path, tag_name: str) -> Iterator[Dict[str, Any]]:
    pass

def iter_process_xml_elements(xml_file: Path, tag_name: str, element_callback: Callable[[Any], Any], error_callback: Optional[Callable[[Path, List[str]], None]]=None) -> Iterator[Dict[str, Any]]:
    pass

def _etree_to_dict(t) -> Dict[str, Any]:
    pass

def _iter_entities_text(entities):
    pass

def _handle_bad_unicode_attr(obj, attr):
    pass

def _format_error_list(file_name, error_log) -> List[str]:
    pass
