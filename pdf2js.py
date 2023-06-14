import argparse
from PyPDF2 import PdfWriter, PdfReader


def create_blank_pdf(output_file):
    # Create a blank PDF with a single empty page
    output = PdfWriter()
    output.add_blank_page(612, 792)  # Letter size (8.5 x 11 inches)
    with open(output_file, 'wb') as f:
        output.write(f)

    print("Blank PDF created successfully.")


def insert_javascript(input_file, javascript_file, output_file):
    output = PdfWriter()
    ipdf = PdfReader(open(input_file, 'rb'))

    for i in range(len(ipdf.pages)):
        page = ipdf.pages[i]
        output.add_page(page)

    with open(javascript_file, 'r') as js_file:
        javascript = js_file.read()
        output.add_js(javascript)

    with open(output_file, 'wb') as f:
        output.write(f)

    print("JavaScript inserted successfully.")


def main():
    parser = argparse.ArgumentParser(description="Create a PDF with embedded JavaScript.")
    parser.add_argument("-i", "--input", help="Input PDF file")
    parser.add_argument("-j", "--javascript", help="JavaScript file to embed")
    parser.add_argument("-o", "--output", help="Output PDF file", required=True)
    args = parser.parse_args()

    if args.input:
        insert_javascript(args.input, args.javascript, args.output)
    else:
        create_blank_pdf(args.output)
        if args.javascript:
            insert_javascript(args.output, args.javascript, args.output)


if __name__ == "__main__":
    main()

