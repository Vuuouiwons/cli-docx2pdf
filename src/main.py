import os
from docx2pdf import convert
from pathlib import Path


from modules.argparser import parser
from modules.Path import get_output_path


def main():
    args = parser.parse_args()
    
    input_docx_file: Path = args.input_docx_file
    
    convert(input_docx_file, get_output_path())


if __name__ == "__main__":
    main()
