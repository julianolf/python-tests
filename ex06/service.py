import logging
import os
from http import HTTPStatus
from json import JSONDecodeError
from typing import Any, Dict, Optional

try:
    import requests
except ImportError:
    from ex06 import fake_requests as requests

URL = "https://www.4devs.com.br/ferramentas_online.php"

log = logging.getLogger(__name__)
log.setLevel(os.getenv("LOG_LEVEL", logging.ERROR))


def random_person() -> Optional[Dict[str, Any]]:
    headers = {"Accept": "application/json"}
    payload = {
        "acao": "gerar_pessoa",
        "sexo": "I",
        "pontuacao": "N",
        "txt_qtde": 1,
    }

    response = requests.post(URL, data=payload, headers=headers)

    log.debug(f"status: {response.status_code} - body: {response.text}")

    if response.status_code != HTTPStatus.OK:
        log.warning(f"request failed with status - {response.status_code}")
        return None

    try:
        data = response.json()
        return data.pop()
    except (JSONDecodeError, IndexError) as error:
        log.error(f"fail to decode response - {error}")
