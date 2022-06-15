"""
Dummy module to mimic `requests` package just for the sake of
the tests without the need to install any external dependency.
"""
from __future__ import annotations

from dataclasses import dataclass
from http import HTTPStatus
from typing import Any, Dict, Optional


@dataclass
class Response:
    status_code: int = HTTPStatus.OK
    text: str = ""

    def json(self) -> Dict[str, Any]:
        return {}


def post(
    url: str, data: str = "", headers: Optional[Dict[str, str]] = None
) -> Response:
    return Response()
