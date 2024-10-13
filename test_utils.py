import unittest
import os
from unittest.mock import patch, MagicMock
from utils import read_file, find_page_name


class TestReadFile(unittest.TestCase):
    @patch('utils.open')
    @patch('utils.find_page_name')
    def test_read_file_success(self, mock_find_page_name, mock_open):
        page_name = 'test_page.html'
        current_dir = os.getcwd()
        mock_find_page_name.return_value = os.path.join(current_dir, 'frontend', page_name)

        mock_file = MagicMock()
        mock_file.read.return_value = '<html><body>Test Content</body></html>'
        mock_open.return_value.__enter__.return_value = mock_file

        result = read_file(page_name)

        self.assertEqual(result, '<html><body>Test Content</body></html>')
        mock_find_page_name.assert_called_once_with(page_name)
        mock_open.assert_called_once_with(os.path.join(current_dir, 'frontend', page_name), 'r')

    @patch('utils.open')
    @patch('utils.find_page_name')
    def test_read_file_file_not_found(self, mock_find_page_name, mock_open):
        page_name = 'nonexistent_page.html'
        current_dir = os.getcwd()
        mock_find_page_name.return_value = os.path.join(current_dir, 'frontend', page_name)
        mock_open.side_effect = FileNotFoundError

        with self.assertRaises(FileNotFoundError):
            read_file(page_name)

        mock_find_page_name.assert_called_once_with(page_name)


if __name__ == '__main__':
    unittest.main()