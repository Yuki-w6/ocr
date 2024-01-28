# ocr
ChatGPTより

PythonでOCRを行う場合、pytesseractというライブラリを使用することが一般的です。これはGoogleが開発した無料のOCRエンジンであるTesseractをPythonから使うためのライブラリです。

pytesseractとPIL（Python Imaging Library）をインストールします。これらは、Pythonで画像を操作するために必要なライブラリです。Python環境で以下のコマンドを実行してインストールします。

```bash
pip install pytesseract pillow

```

次に、Tesseract OCRエンジンをインストールする必要があります。これはシステムレベルのソフトウェアで、pytesseractがこれをバックエンドとして使用します。



PDF形式からテキストを抽出するには、PDFを画像に変換し、その画像に対してOCRを行う方法が一般的です。Pythonでは、pdf2imageというライブラリを用いてPDFを画像に変換できます。

```bash
pip install pytesseract pillow pdf2image

```