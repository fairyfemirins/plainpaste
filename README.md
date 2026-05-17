# PlainPaste

A cross-platform CLI tool to paste clipboard content as plain text. No more manual cleanup after copying from Office apps, websites, or emails!

## Features
- Paste as plain text via `plainpaste`.
- Watch clipboard and auto-unformat on copy (`plainpaste --watch`).
- Works on Linux, macOS, and Windows.

## Installation
```bash
pip install plainpaste
```

## Usage
```bash
# Paste as plain text
plainpaste

# Watch clipboard and auto-unformat
plainpaste --watch
```

## Technical Architecture
- **Language**: Python
- **Libraries**: `pyperclip`, `argparse`, `colorama`
- **Clipboard Access**: Cross-platform via `pyperclip`
- **Auto-Unformat**: Uses `pynput` to monitor clipboard changes

## Limitations
- Requires Python 3.6+
- Clipboard monitoring (`--watch`) may require additional permissions on some systems.

## License
MIT