# PDF Translator


This project provides a Python script to **translate the text content of a PDF document** while preserving its layout, images, and text formatting as closely as possible. The translated PDF is saved as a new file. The script utilizes libraries such as:

- **PyMuPDF (fitz)**: For reading and extracting content from PDF files.
- **Googletrans**: For text translation.
- **ReportLab**: For generating and saving the translated PDF.



## Requirements

Make sure you have Python 3.x installed. Install the following dependencies:

```bash
pip install pymupdf googletrans==4.0.0-rc1 reportlab
```

## Usage

1. **Place the PDF file** you want to translate in the same directory as the script.  
2. **Open a terminal** and run:  

```bash
python main.py
```

### Example Script Execution

You can use the `translate_pdf` function directly in your Python script to translate a specific PDF file:

```python
translate_pdf("input.pdf", "output_translated.pdf")
```

## Language Configuration

By default, the script translates the text into **English (`en`)**. You can change the target language by modifying the following line in the script:

```python
translation_result = translator.translate(text, dest='en')
```

### Change the Language

To change the translation language, replace **en** with your desired language code:

- **en**: English (default)
- **tr**: Turkish
- **ar**: Arabic
- **fr**: French
- **es**: Spanish

It supports many more languages ​​like this.

### Example:
If you want to translate the PDF content into Turkish, update the code as follows:

```python
translation_result = translator.translate(text, dest='tr')
```

You can find a **full list of supported languages and their codes** in the Google Translate Supported Languages documentation.

## Contact

If you have any questions, suggestions, or feedback about this project, feel free to reach out:

- **Email:** [berfinzelihacicek@gmail.com](mailto:berfinzelihacicek@gmail.com)  
- **GitHub Issues:** [Open an Issue](https://github.com/berfinncicek/Pdf-Translator/issues) 

