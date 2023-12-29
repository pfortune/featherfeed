import cv2
import subprocess
from PIL import Image
import numpy as np
from pycoral.adapters import classify
from pycoral.adapters import common
from pycoral.utils.dataset import read_label_file
from pycoral.utils.edgetpu import make_interpreter

# Constants
MODEL_PATH = 'models/mobilenet_v2_1.0_224_inat_bird_quant_edgetpu.tflite'
LABELS_PATH = 'models/inat_bird_labels.txt'

def extract_frames(video_path, interval=30):
    print("Starting frame extraction...")
    frames = []
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0

    while success:
        if count % interval == 0:
            frames.append(image)
            print(f"Frame {count} extracted.")
        success, image = vidcap.read()
        count += 1

    vidcap.release()
    print("Frame extraction completed.")
    return frames

def preprocess_frame(frame, size):
    print("Preprocessing frame...")
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame)
    img = img.resize(size, Image.ANTIALIAS)
    print("Frame preprocessed.")
    return img

def classify_frame(frame, interpreter, labels):
    print("Classifying frame...")
    common.set_input(interpreter, frame)
    interpreter.invoke()
    classes = classify.get_classes(interpreter, top_k=1)
    results = [(labels[c.id], c.score) for c in classes]
    print("Classification completed.")
    return results

def run_bird_detection(video_path):
    print(f"Running bird detection on {video_path}")

    # Load the model and labels
    interpreter = make_interpreter(MODEL_PATH)
    interpreter.allocate_tensors()
    labels = read_label_file(LABELS_PATH)
    print("Model and labels loaded.")

    # Extract frames from the video
    frames = extract_frames(video_path, interval=5)

    # Process and classify each frame
    detections = []
    for frame in frames:
        preprocessed_frame = preprocess_frame(frame, common.input_size(interpreter))
        results = classify_frame(preprocessed_frame, interpreter, labels)
        detections.extend([(bird, score) for bird, score in results if bird != 'background'])

    print("Bird detection completed.")
    return detections

if __name__ == '__main__':
    detections = run_bird_detection(video_path)
    print("Detections:", detections)
