# pid_reader_project/backend/line_tracker.py
import cv2
import numpy as np

class LineTracker:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = cv2.imread(image_path)
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def detect_lines(self):
        edges = cv2.Canny(self.gray, 50, 150, apertureSize=3)
        lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=50, maxLineGap=10)
        self.lines = lines if lines is not None else []
        return self.lines

    def visualize_lines(self):
        vis_image = self.image.copy()
        if self.lines is not None:
            for line in self.lines:
                x1, y1, x2, y2 = line[0]
                cv2.line(vis_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        return vis_image