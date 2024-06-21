import pytesseract
from PIL import Image
import base64
from io import BytesIO
from django.core.files.base import ContentFile

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    
    # Placeholder for bold word extraction logic
    bold_words = []  # Implement your logic to find bold words
    
    # Convert image to base64
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    
    return text, bold_words, img_str
