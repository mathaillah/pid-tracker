# pid_reader_project/backend/main.py
from line_tracker import LineTracker
from detector import InstrumentDetector
from ocr_reader import OCRReader
from graph_builder import DiagramGraphBuilder
import cv2

def process_pid_image(image_path, model_path='yolov8-pid.pt'):
    # Line detection
    line_tracker = LineTracker(image_path)
    lines = line_tracker.detect_lines()

    # Instrument detection
    detector = InstrumentDetector(model_path)
    components = detector.detect_components(image_path)

    # OCR
    ocr = OCRReader()
    labels = ocr.extract_text(image_path)

    # Graph building
    graph_builder = DiagramGraphBuilder(lines, components, labels)
    graph = graph_builder.build_graph()
    graph_json = graph_builder.export_graph('json')

    # Visual result (optional)
    vis_image = line_tracker.visualize_lines()
    output_path = image_path.replace(".png", "_lines.png")
    cv2.imwrite(output_path, vis_image)

    return graph_json, output_path