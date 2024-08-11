import re
import pytesseract
from pdf2image import convert_from_path
from pytesseract import Output

def preprocess_text(text):
    # 文字と文字の間の半角スペースを削除
    text = re.sub(r'(?<=\S) (?=\S)', '', text)

    # 行ごとに処理して、行頭および行末の空白を削除
    lines = text.split('\n')
    lines = [line.strip() for line in lines]
#
    ## 改行で結合して前処理後のテキストを返す
    #return '\n'.join(lines)
    return lines

# OCR設定
pytesseract.pytesseract.tesseract_cmd = "/usr/local/bin/tesseract"

# PDFを画像に変換
images = convert_from_path("png2pdf.pdf")

# 画像からテキストを抽出
text = pytesseract.image_to_string(images[0], lang="jpn")

# テキストの前処理
lines = preprocess_text(text)
#print(text)

# 取引先を抽出する正規表現パターン
torihikisaki_pattern = "^(株式会社|有限会社).+|.+[（\(]?(株式会社|有限会社)[）\)]?$"

for line in lines:
    print(line)

    # 取引先を抽出
    torihikisaki = re.search(torihikisaki_pattern, text)
    if torihikisaki:
        print("取引先:", torihikisaki.group())

    # 合計金額を抽出する正規表現パターン
    total_amount_pattern = r'(合計|総額|合計金額)\s?([0-9,]+)'

    # 合計金額を抽出
    total_amount = re.search(total_amount_pattern, text)
    if total_amount:
        print("合計金額:", total_amount.group(2))
