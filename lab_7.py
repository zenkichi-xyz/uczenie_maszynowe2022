import pytesseract
from PIL import Image

def read_text_from_image(image_path):
  # Otwórz obrazek
  image = Image.open(image_path)

  # Użyj pytesseract do odczytania tekstu z obrazka
  text = pytesseract.image_to_string(image)

  # Zwróć odczytany tekst
  return text


image_paths = ['image1.png', 'image2.png', 'image3.png', 'image4.png', 'image5.png']

for image_path in image_paths:
  text = read_text_from_image(image_path)
  print(f'Tekst z obrazka "{image_path}": {text}')