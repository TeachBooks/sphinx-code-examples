"""
sphinx_code_examples._compat
"""

from docutils.nodes import Element
from typing import Iterator


def findall(node: Element, *args, **kwargs) -> Iterator[Element]:
    # findall replaces traverse in docutils v0.18
    # note a difference is that findall is an iterator
    impl = getattr(node, "findall", node.traverse)
    return iter(impl(*args, **kwargs))
