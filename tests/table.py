import unittest
from unittest.mock import mock_open, patch

from src.table import transactions_csv, transactions_excel_xlsx

class TestTransactions(unittest.TestCase):

    # Тест успешного считывания данных из CSV
    @patch("builtins.open", new_callable=mock_open, read_data='"id";"state"\n"441945886";"EXECUTED"\n')
    def test_successful_read(self, mock_file):
        expected_output = [{"id": "441945886", "state": "EXECUTED"}]
        result = transactions_csv('fake_path.csv')
        self.assertEqual(result, expected_output)

    # Тест на отсутствие файла
    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_file_not_found(self, mock_file):
        result = transactions_csv('file.csv')
        self.assertEqual(result, [])

    # Тест на общую ошибку чтения файла
    @patch("builtins.open", new_callable=mock_open)
    def test_general_error(self, mock_file):
        mock_file.side_effect = Exception("Some parsing error")
        result = transactions_csv('fake_path.csv')
        self.assertEqual(result, [])

    @patch("src.table.openpyxl.load_workbook", side_effect=FileNotFoundError)
    def test_transactions_excel_xlsx_file_not_found(self, mock_load_workbook):
        result = transactions_excel_xlsx('file.xlsx')
        self.assertEqual(result, [])

    @patch("src.table.openpyxl.load_workbook", side_effect=Exception("XLSX error"))
    def test_transactions_excel_xlsx_general_error(self, mock_load_workbook):
        result = transactions_excel_xlsx('fake_path.xlsx')
        self.assertEqual(result, [])
