import unittest
import os
import sys
import pandas as pd

dir_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir_root)

from energetic_source_cnpj_ibama_etl import (
    is_json_link, convert_json_to_dataframe)

class TestIsJsonLink(unittest.TestCase):
    def test_is_json_link(self):

        # Test with a valid JSON link
        valid_link: str = 'https://dadosabertos.ibama.gov.br/dados/RAPP/fonteEnergetica/relatorio.json'
        self.assertTrue(is_json_link(valid_link))

        # Test with an invalid link
        invalid_link: str = "https://example.com/data.txt"
        self.assertFalse(is_json_link(invalid_link))

        # Test with a malformed link
        malformed_link: str = "htp://example.com/data.json"
        self.assertFalse(is_json_link(malformed_link))


class TestConvertJsonToDataFrame(unittest.TestCase):

    url_test: str = 'https://dadosabertos.ibama.gov.br/dados/RAPP/fonteEnergetica/relatorio.json'

    def test_convert_json_to_dataframe(self):
        self.assertIsInstance(convert_json_to_dataframe(
            self.url_test), pd.DataFrame)

if __name__ == '__main__':
    unittest.main(verbosity=2)