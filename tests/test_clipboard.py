import unittest
from unittest.mock import patch, MagicMock
from plainpaste.clipboard import PlainPaste

class TestPlainPaste(unittest.TestCase):
    def setUp(self):
        self.app = PlainPaste()

    def test_strip_formatting(self):
        # Test HTML stripping
        html_text = "<b>Hello</b> <i>World</i>"
        self.assertEqual(self.app.strip_formatting(html_text), "Hello World")
        
        # Test RTF stripping
        rtf_text = r"{\rtf1\b Hello} {\i World}"
        self.assertEqual(self.app.strip_formatting(rtf_text), "Hello World")
        
        # Test whitespace normalization
        whitespace_text = "Hello\n\tWorld"
        self.assertEqual(self.app.strip_formatting(whitespace_text), "Hello World")

    @patch('pyperclip.paste')
    @patch('pyperclip.copy')
    def test_update_clipboard(self, mock_copy, mock_paste):
        # Test clipboard update
        mock_paste.return_value = "<b>Hello</b>"
        self.app.update_clipboard()
        mock_copy.assert_called_with("Hello")
        
        # Test no update if content is unchanged
        mock_paste.return_value = "<b>Hello</b>"
        self.app.update_clipboard()
        mock_copy.assert_called_once()  # Should not be called again

if __name__ == "__main__":
    unittest.main()