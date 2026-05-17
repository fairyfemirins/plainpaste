#!/usr/bin/env python3
"""
PlainPaste: A cross-platform CLI tool to paste clipboard content as plain text.

**Minimal Version**: No external dependencies. Uses `xclip` (Linux) or `pbpaste` (macOS) as a fallback.
"""

import subprocess
import sys
import platform

def paste_plain():
    """Paste clipboard content as plain text using system tools."""
    try:
        system = platform.system()
        if system == "Linux":
            result = subprocess.run(["xclip", "-selection", "clipboard", "-o"], capture_output=True, text=True)
            if result.returncode != 0:
                raise FileNotFoundError("xclip not found. Install with: sudo apt-get install xclip")
            print(result.stdout)
        elif system == "Darwin":
            result = subprocess.run(["pbpaste"], capture_output=True, text=True)
            print(result.stdout)
        elif system == "Windows":
            import pyperclip
            print(pyperclip.paste())
        else:
            print("Unsupported platform.", file=sys.stderr)
            sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    paste_plain()

if __name__ == "__main__":
    main()