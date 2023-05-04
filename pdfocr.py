from PIL import Image
import pytesseract
from pdf2image import convert_from_path

# Tesseractのパスを指定
pytesseract.pytesseract.tesseract_cmd = "/usr/local/bin/tesseract"

# PDFを画像に変換
images = convert_from_path('png2pdf.pdf')

# すべてのページに対してOCRを実行
for i, image in enumerate(images):
    text = pytesseract.image_to_string(image, lang='jpn')
    print(f'--- ページ{i+1} ---')
    print(text)