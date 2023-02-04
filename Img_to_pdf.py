import img2pdf

# Open the image
with open("image.jpg", "rb") as f:
    image = f.read()

# Convert the image to a PDF file
with open("image.pdf", "wb") as f:
    f.write(img2pdf.convert(image))
