import os
from docx2pdf import convert
from pathlib import Path

from modules.psutil import check_process_running
from modules.argparser import parser
from modules.Path import get_output_path


def main():
    args = parser.parse_args()
    
    input_docx_file: Path = args.input_docx_file
    
    if check_process_running():
        raise RuntimeError('an instance of Microsoft Word is running, close all instances of Microsoft Word')
    
    convert(input_docx_file, get_output_path())


if __name__ == "__main__":
    main()
