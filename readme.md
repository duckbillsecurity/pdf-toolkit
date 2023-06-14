# pdf2url

<a href="https://streamable.com/arr12g" title="pdf2url"><img src="https://github.com/ATTACKnDEFEND/pdf2url/blob/main/images/pdf2url.png" alt="pdf2url" /></a>

pdf2url is a Python script that generates a PDF file with a clickable link to open a url or download a file. It utilizes the ReportLab library to create the PDF and allows you to specify the text for the link, name of the PDF file and the URL to be opened when the link is clicked.

#### Disclaimer:
This script is intended for educational and informational purposes only. Use it responsibly. The user assumes all responsibility and risk associated with the use of this script.

#### Prerequisites:
- Python 3.x installed on your system
- reportlab library installed (pip install reportlab)

#### Arguments:
```
-t or --text: Text shown for the link (default: "Click me").
-u or --url: URL to be opened when the link is clicked (required).
-o or --output: Name of the PDF file to be saved (default: "output.pdf").
```
#### Example usage:
<br />
`python pdf2url.py -t "Click me" -u "https://www.example.com" -o "mydocument.pdf"`<br />
- NOTE: use double "" quotes

# pdf2js

The code is a Python script that allows you to create a PDF with JavaScript. It provides two main functionalities: inserting JavaScript code into in a new blank PDF with a single empty page or an existing PDF.

#### Disclaimer:
This script is intended for educational and informational purposes only. Use it responsibly. The user assumes all responsibility and risk associated with the use of this script.

#### Prerequisites:
- Python 3.x installed on your system
- PyPDF2: The code utilizes the PyPDF2 library for working with PDF files. You need to have PyPDF2 installed (pip install PyPDF2).

#### Arguments:
```
-i or --input: Specifies the input PDF file to which the JavaScript code will be added. If this is not specified a blank pdf file is created.
-j or --javascript: Specifies the JavaScript file containing the code to be embedded.
-o or --output: Specifies the output PDF file name where the modified PDF with embedded JavaScript will be saved. (required).
```
#### Example usage:

Inserting JavaScript into an existing PDF -
<br />
`python pdf2url.py -i input.pdf -j script.js -o output.pdf`<br />

Creating a blank PDF and inserting JavaScript -
<br />
`python pdf2url.py -j script.js -o output.pdf`<br />



