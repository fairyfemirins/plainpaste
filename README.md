# PlainPaste

A lightweight, cross-platform utility to paste unformatted text system-wide using `Ctrl+V`.

## Features
- **Cross-Platform**: Works on Windows, macOS, and Linux.
- **Lightweight**: Minimal dependencies, runs in the background.
- **System-Wide**: Overloads `Ctrl+V` to paste unformatted text in any application.
- **Tray Icon**: Optional system tray icon for easy access (coming soon).

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/femirins/plainpaste.git
   cd plainpaste
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate   # Windows
   pip install -r requirements.txt
   ```

## Usage
Run the tool:
```bash
python -m plainpaste
```

- Copy rich text (e.g., from a browser or Word document).
- Press `Ctrl+V` in any application to paste unformatted text.

## How It Works
1. Monitors the clipboard for rich text.
2. Strips formatting and stores plain text.
3. Overloads `Ctrl+V` to paste the plain text version.

## License
MIT