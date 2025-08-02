# pid_reader_project/backend/ocr_reader.py
import easyocr
import cv2

class OCRReader:
    def __init__(self, lang='en'):
        self.reader = easyocr.Reader([lang], gpu=False)

    def extract_text(self, image_path):
        results = self.reader.readtext(image_path)
        text_data = []
        for (bbox, text, conf) in results:
            text_data.append({
                'text': text,
                'confidence': conf,
                'bbox': bbox
            })
        return text_data