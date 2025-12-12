import platform
from pathlib import Path

def get_output_path() -> Path:
    system = platform.system()

    if system == 'Windows':
        output_path = Path("~/Desktop/DOCX2PDF").expanduser()
    elif system == 'Darwin':
        output_path = Path("~/Desktop/DOCX2PDF").expanduser()
    elif system == 'Linux':
        output_path = Path("~/DOCX2PDF").expanduser()
    else:
        output_path = Path("~").expanduser() / "DOCX2PDF"

    output_path.mkdir(parents=True, exist_ok=True)

    return output_path.resolve()
