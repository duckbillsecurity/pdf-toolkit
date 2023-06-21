import argparse
import os
from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import blue
from reportlab.pdfgen import canvas

def insert_autolaunch_url(input_path, output_path, url, text):
    # Read the input PDF file
    with open(input_path, 'rb') as file:
        reader = PdfReader(file)
        writer = PdfWriter()

        # Iterate through each page of the input PDF
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]

            # Calculate the font size based on the available space
            width, height = letter
            font_size = 24  # Double the font size
            while True:
                c = canvas.Canvas("temp.pdf", pagesize=letter)
                c.setFont("Helvetica", font_size)
                text_width = c.stringWidth(text)
                if text_width < width - 200:
                    break
                font_size -= 1

            # Create a new PDF using reportlab
            c = canvas.Canvas("temp.pdf", pagesize=letter)
            c.setFont("Helvetica", font_size)

            # Calculate the coordinates for positioning near the top
            rect_width = text_width + 4
            rect_height = font_size + 4
            x = (width - rect_width) / 2
            y_rect = height - rect_height - 50  # Adjust the offset from the top
            y_text = y_rect + 6  # Add some space between text and rectangle

            # Draw a rectangle around the text
            c.rect(x, y_rect, rect_width, rect_height)

            # Add the text and hyperlink within the rectangle
            c.drawString(x + 2, y_text, text)
            c.linkURL(url, (x, y_rect, x + rect_width, y_rect + rect_height), relative=0, thickness=1, color=blue)
            c.save()

            # Merge the new PDF with the input PDF page
            temp_pdf = PdfReader("temp.pdf")
            page.mergePage(temp_pdf.pages[0])
            writer.add_page(page)

        # Write the modified PDF to the output file
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

    # Remove the temporary PDF file
    os.remove("temp.pdf")

def main():
    parser = argparse.ArgumentParser(description='Insert URL link into a PDF.')
    parser.add_argument('input', help='input PDF file path')
    parser.add_argument('output', help='output PDF file path')
    parser.add_argument('url', help='URL link to be inserted')
    parser.add_argument('text', help='text to be displayed')
    args = parser.parse_args()

    input_path = args.input
    output_path = args.output
    url = args.url
    text = args.text

    # Validate input path
    if not os.path.isfile(input_path):
        print(f"Error: Input file '{input_path}' does not exist.")
        return

    # Remove the output file if it already exists
    if os.path.isfile(output_path):
        os.remove(output_path)

    # Insert URL link into the PDF
    insert_autolaunch_url(input_path, output_path, url, text)
    print(f"URL link inserted successfully into '{output_path}'.")

if __name__ == '__main__':
    main()
