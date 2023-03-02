from barcode import EAN13
import aspose.words as aw

# SVG file's path
number = input('Enter your barcode: ')
fileName = f"{number}.svg"

bcode = EAN13(number)
bcode.save(number)
# create a document
doc = aw.Document()

# create a document builder and initialize it with document object
builder = aw.DocumentBuilder(doc)

# insert SVG image to document
shape = builder.insert_image(fileName)

# OPTIONAL
# Calculate the maximum width and height and update page settings
# to crop the document to fit the size of the pictures.
pageSetup = builder.page_setup
pageSetup.page_width = shape.width
pageSetup.page_height = shape.height
pageSetup.top_margin = 0
pageSetup.left_margin = 0
pageSetup.bottom_margin = 0
pageSetup.right_margin = 0

# save as PNG
doc.save(f"{number}.png")
print('Barcode Generated')

