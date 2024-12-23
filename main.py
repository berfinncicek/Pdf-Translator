import fitz
from googletrans import Translator
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import simpleSplit
import os

def translate_pdf(input_pdf, output_pdf):

    doc = fitz.open(input_pdf)
    translator = Translator()

    c = canvas.Canvas(output_pdf, pagesize=letter)
    print("ceviri yapiliyor..")
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text_blocks = page.get_text("blocks")
        images = page.get_images(full=True)
        #print(f"Images on page {page_num}: {images}")  
        
        
        page_width = page.rect.width
        page_height = page.rect.height
        c.setPageSize((page_width, page_height))
        
        
        for img_index, img in enumerate(images):
            if len(img) > 3:
                xref = img[0]
                img_info = doc.extract_image(xref)
                image_bytes = img_info.get("image")
                if image_bytes:
                    image_filename = f"temp_img_{page_num}_{img_index}.png"
                    with open(image_filename, "wb") as f:
                        f.write(image_bytes)
                    
                   
                    rects = page.get_image_rects(xref)
                    if rects:
                        rect = rects[0]
                        x, y, w, h = rect.x0, rect.y0, rect.width, rect.height
                       # print(f"Image rect: x={x}, y={y}, w={w}, h={h}")
                    else:
                        x, y, w, h = 0, 0, 100, 100  
                        #print("Using default image coordinates")
                    
                    c.drawImage(image_filename, x, page_height - y - h, w, h, preserveAspectRatio=True, anchor='nw')
                    os.remove(image_filename)
        
        
        for block in text_blocks:
            x, y, w, h, text, *_ = block
            try:
                translation_result = translator.translate(text, dest='en')
                #print(f"Original: {text} | Translated: {translation_result}")
                translated_text = translation_result.text if translation_result else text
            except Exception as e:
                #print(f"Translation error: {e}")
                translated_text = text
            
            
            font_size = 7.50
            while c.stringWidth(translated_text, "Helvetica", font_size) > w and font_size > 7:
                font_size -= 1
            
            c.setFont("Helvetica", font_size)
            
            
            text_lines = simpleSplit(translated_text, "Helvetica", font_size, w)
            for i, line in enumerate(text_lines):
                c.drawString(x, page_height - y - (i * font_size * 1.2), line)

       
        c.showPage()
       
    c.save()
    print(f"Translated PDF saved as {output_pdf}")

translate_pdf("Ramanujan.pdf", "Ramanujan_translated.pdf")
