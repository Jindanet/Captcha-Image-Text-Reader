import requests
from PIL import Image
import pytesseract
from io import BytesIO
import re

def get_valid_captcha_text(url):
    while True:
        response = requests.get(url, allow_redirects=True)

        # ตรวจสอบว่า request สำเร็จหรือไม่
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            text = pytesseract.image_to_string(image, config='--psm 6').strip()

            # ตรวจสอบว่า text เป็นเลข 4 หลักหรือไม่
            if re.match(r'^\d{4}$', text):
                return text

# URL ของภาพ
url = 'https://ag1.ufabet.com/Public/img.aspx'

while True:
    captcha_text = get_valid_captcha_text(url)

    print(f'Captcha text: {captcha_text}')
