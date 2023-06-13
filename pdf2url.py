import argparse
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black
from reportlab.pdfbase.pdfmetrics import stringWidth


def create_pdf(file_name, text, url):
    # Create a PDF canvas
    c = canvas.Canvas(file_name)

    # Define the link coordinates and size
    x, y = 50, 650
    font = "Helvetica"
    font_size = 12

    # Calculate the width of the text
    text_width = stringWidth(text, font, font_size)

    # Adjust the size of the rectangle based on the text width
    width = text_width + 10  # Add some padding
    height = 30

    # Draw a rectangle to simulate a button
    c.rect(x, y, width, height, fill=0)

    # Add text as a link
    c.setFillColor(black)  # Set font color to black
    c.setFont(font, font_size)  # Set font type and size
    c.drawCentredString(x + width / 2, y + height / 2, text)

    # Add the link destination
    c.linkURL(url, (x, y, x + width, y + height), relative=0)

    # Save the PDF
    c.save()

    print("PDF created successfully.")


def main():
    parser = argparse.ArgumentParser(description="Create a PDF with a clickable link.")
    parser.add_argument("-t", "--text", default="Click me", help="Text shown for the link")
    parser.add_argument("-u", "--url", required=True, help="URL to be opened when the link is clicked")
    parser.add_argument("-f", "--file_name", default="output.pdf", help="Name of the PDF file to be saved (default: output.pdf)")
    args = parser.parse_args()

    create_pdf(args.file_name, args.text, args.url)


if __name__ == "__main__":
    main()
