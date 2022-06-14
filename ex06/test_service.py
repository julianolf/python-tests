import json
import unittest
from http import HTTPStatus
from unittest import mock

from ex06 import service


class TestService(unittest.TestCase):
    @mock.patch("ex06.service.requests")
    def test_random_person_returns_person(self, m_requests):
        expected = {
            "nome": "Theo Davi Cavalcanti",
            "idade": 53,
            "cpf": "88892423290",
            "rg": "368727324",
            "data_nasc": "14/04/1969",
            "sexo": "Masculino",
            "signo": "Áries",
            "mae": "Emily Luna Emily",
            "pai": "Enzo Bernardo Cavalcanti",
            "email": "theo.davi.cavalcanti@alanamaral.com.br",
            "senha": "Jx8BgK1UEz",
            "cep": "87340971",
            "endereco": "Praça Tiradentes, s/n",
            "numero": 128,
            "bairro": "Centro",
            "cidade": "Mamborê",
            "estado": "PR",
            "telefone_fixo": "4426417268",
            "celular": "44994862723",
            "altura": "1,62",
            "peso": 87,
            "tipo_sanguineo": "O+",
            "cor": "vermelho",
        }

        response = mock.MagicMock()
        response.status_code = HTTPStatus.OK
        response.text = json.dumps([expected])
        response.json.return_value = [expected]

        m_requests.post.return_value = response

        result = service.random_person()

        self.assertDictEqual(result, expected)

    @mock.patch("ex06.service.requests")
    def test_random_person_handles_failed_requests(self, m_requests):
        response = mock.MagicMock()
        response.status_code = HTTPStatus.UNAUTHORIZED
        response.text = ""

        m_requests.post.return_value = response

        with self.assertLogs(service.__name__, level="WARNING") as logs:
            result = service.random_person()

        self.assertIsNone(result)
        self.assertListEqual(
            logs.output,
            ["WARNING:ex06.service:request failed with status - 401"],
        )

    @mock.patch("ex06.service.requests")
    def test_random_person_handles_invalid_json_response(self, m_requests):
        response = mock.MagicMock()
        response.status_code = HTTPStatus.OK
        response.text = "foo"
        response.json.side_effect = json.JSONDecodeError("Expecting value", "foo", 0)

        m_requests.post.return_value = response

        with self.assertLogs(service.__name__, level="ERROR") as logs:
            result = service.random_person()

        self.assertIsNone(result)
        self.assertListEqual(
            logs.output,
            [
                (
                    "ERROR:ex06.service:fail to decode response - "
                    "Expecting value: line 1 column 1 (char 0)"
                )
            ],
        )

    @mock.patch("ex06.service.requests")
    def test_random_person_handles_empty_response(self, m_requests):
        response = mock.MagicMock()
        response.status_code = HTTPStatus.OK
        response.text = json.dumps([])
        response.json.return_value = []

        m_requests.post.return_value = response

        with self.assertLogs(service.__name__, level="ERROR") as logs:
            result = service.random_person()

        self.assertIsNone(result)
        self.assertListEqual(
            logs.output,
            ["ERROR:ex06.service:fail to decode response - pop from empty list"],
        )
