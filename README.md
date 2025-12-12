# cli-docx2pdf
A fast and frustration-free CLI tool to convert **DOCX → PDF** — created for anyone who's ever accidentally submitted the wrong PDF thanks to Microsoft Word’s confusing UI.

Say goodbye to hunting through menus. Convert documents instantly from your terminal.


## Features

* Convert `.docx` files to `.pdf` with a single command
* Simple CLI — no GUI clutter
* Perfect for automation, CI/CD, or batch operations

## Getting Started

### Install dependencies

This project uses **uv** for dependency management:

```bash
uv sync
```

### Build the CLI executable

Generate a standalone binary using **PyInstaller**:

```bash
pyinstaller --onefile src/main.py
```

The compiled executable will appear in the `dist/` folder.

## Usage

After building the tool, run:

```bash
cli-docx2pdf input.docx
```

This tool will output the file to ~/Desktop/DOCX2PDF on Windows and macOS, ~/DOCX2PDF on Linux

## Contributing

Contributions are welcome!
Feel free to submit issues, open pull requests, or suggest improvements.

To set up a development environment:

```bash
uv sync
```
