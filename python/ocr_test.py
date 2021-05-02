from PIL import Image
import pytesseract


# Simple image to string
print(pytesseract.image_to_string(Image.open('data/rg_test.jpeg')))

# List of available languages
print(pytesseract.get_languages(config=''))

# French text image to string
# print(pytesseract.image_to_string(Image.open('data/rg_test.jpeg'), lang='por'))

# In order to bypass the image conversions of pytesseract, just use relative or absolute image path
# NOTE: In this case you should provide tesseract supported images or tesseract will return error
print(pytesseract.image_to_string('data/rg_test.jpeg'))

# Batch processing with a single file containing the list of multiple image file paths
# print(pytesseract.image_to_string('images.txt'))

# Timeout/terminate the tesseract job after a period of time

# Timeout after 2 seconds
print(pytesseract.image_to_string(Image.open('data/rg_test.jpeg'), timeout=5))
# Timeout after half a second
# print(pytesseract.image_to_string('data/rg_test.jpg', timeout=0.5))


# Get bounding box estimates
# print(pytesseract.image_to_boxes(Image.open('data/rg_test.jpeg')))

# # Get verbose data including boxes, confidences, line and page numbers
# print(pytesseract.image_to_data(Image.open('data/rg_test.jpeg')))

# # Get information about orientation and script detection
# print(pytesseract.image_to_osd(Image.open('data/rg_test.jpeg')))

# Get a searchable PDF
# pdf = pytesseract.image_to_pdf_or_hocr('data/rg_test.jpeg', extension='pdf')
# with open('data/test.pdf', 'w+b') as f:
#     f.write(pdf)  # pdf type is bytes by default

# Get HOCR output
# hocr = pytesseract.image_to_pdf_or_hocr('data/rg_test.jpeg', extension='hocr')

# # Get ALTO XML output
# xml = pytesseract.image_to_alto_xml('data/rg_test.jpeg')
