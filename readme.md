# pdf2url

<a href="https://streamable.com/arr12g" title="pdf2url"><img src="https://github.com/ATTACKnDEFEND/pdf2url/blob/main/images/pdf2url.png" alt="pdf2url" /></a>

pdf2url is a Python script that generates a PDF file with a clickable link. It utilizes the ReportLab library to create the PDF and allows you to specify the text for the link, name of the PDF file and the URL to be opened when the link is clicked.

Disclaimer:
This script is intended for educational and informational purposes only. Use it responsibly. The user assumes all responsibility and risk associated with the use of this script.

Prerequisites:
- Python 3.x installed on your system
- `reportlab` library installed (`pip install reportlab`)

Options:
- `-t`, `--text`: Text shown for the link (default: "Click me")
- `-u`, `--url`: URL to be opened when the link is clicked (required)
- `-f`, `--file_name`: Name of the PDF file to be saved (default: "output.pdf")

Example usage:
python pdf2url.py -t "Click me" -u "https://www.example.com" -f "mydocument.pdf"
* use double "" quotes

