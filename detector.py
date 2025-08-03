# pid_reader_project/backend/detector.py
from ultralytics import YOLO
import cv2

class InstrumentDetector:
    def __init__(self, model_path='yolov8n.pt'):
        self.model = YOLO(model_path)  

    def detect_components(self, image_path):
        results = self.model(image_path)
        boxes = []
        for result in results:
            for box in result.boxes.data.tolist():
                x1, y1, x2, y2, conf, cls = box
                boxes.append({
                    'bbox': (int(x1), int(y1), int(x2), int(y2)),
                    'class': int(cls),
                    'confidence': float(conf)
                })
        return boxes
