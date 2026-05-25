import pyperclip
import keyboard
import time
import re

class PlainPaste:
    def __init__(self):
        self.last_clipboard_content = ""
        self.plain_text = ""

    def strip_formatting(self, text):
        """Strip rich text formatting and return plain text."""
        # Remove HTML tags
        text = re.sub(r'<[^>]*>', '', text)
        # Remove RTF control words and braces
        text = re.sub(r'\\\w+|\{|\}', '', text)
        # Remove extra whitespace
        text = ' '.join(text.split())
        return text

    def update_clipboard(self):
        """Update the clipboard with plain text."""
        try:
            current_content = pyperclip.paste()
            if current_content != self.last_clipboard_content:
                self.last_clipboard_content = current_content
                self.plain_text = self.strip_formatting(current_content)
                pyperclip.copy(self.plain_text)
        except Exception as e:
            print(f"Error updating clipboard: {e}")

    def paste_plain_text(self):
        """Paste plain text using Ctrl+V."""
        try:
            keyboard.send('ctrl+v')
        except Exception as e:
            print(f"Error pasting: {e}")

    def run(self):
        """Run the PlainPaste utility."""
        print("PlainPaste is running. Press Ctrl+V to paste unformatted text.")
        keyboard.add_hotkey('ctrl+v', self.paste_plain_text)
        while True:
            self.update_clipboard()
            time.sleep(0.1)

if __name__ == "__main__":
    app = PlainPaste()
    app.run()