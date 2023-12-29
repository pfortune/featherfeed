import cv2
from PIL import Image
from pycoral.adapters import classify, common
from pycoral.utils.dataset import read_label_file
from pycoral.utils.edgetpu import make_interpreter

# Constants for model and label paths
MODEL_PATH = 'models/mobilenet_v2_1.0_224_inat_bird_quant_edgetpu.tflite'
LABELS_PATH = 'models/inat_bird_labels.txt'

# Function to extract frames from the video at a specified interval
def extract_frames(video_path, interval=30):
    print("Starting frame extraction...")
    frames = []
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0

    # Loop through video and extract frames at the defined interval
    while success:
        if count % interval == 0:
            frames.append(image)
            print(f"Frame {count} extracted.")
        success, image = vidcap.read()
        count += 1

    vidcap.release()
    print("Frame extraction completed.")
    return frames

# Function to preprocess each frame for model input
def preprocess_frame(frame, size):
    print("Preprocessing frame...")
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame)
    img = img.resize(size, Image.ANTIALIAS)
    print("Frame preprocessed.")
    return img

# Function to classify a preprocessed frame using the Coral TPU
def classify_frame(frame, interpreter, labels):
    print("Classifying frame...")
    common.set_input(interpreter, frame)
    interpreter.invoke()
    classes = classify.get_classes(interpreter, top_k=1)
    results = [(labels[c.id], c.score) for c in classes]
    print("Classification completed.")
    return results

# Main function to run bird detection on a video
def run_bird_detection(video_path):
    print(f"Running bird detection on {video_path}")

    # Load the Coral TPU model and labels
    interpreter = make_interpreter(MODEL_PATH)
    interpreter.allocate_tensors()
    labels = read_label_file(LABELS_PATH)
    print("Model and labels loaded.")

    # Extract frames from the video and classify each frame
    saved_frame_path = None  # Placeholder for the path of the saved frame
    frames = extract_frames(video_path, interval=5)

    bird_detections = []
    for frame in frames:
        # Preprocess and classify the frame
        preprocessed_frame = preprocess_frame(frame, common.input_size(interpreter))
        results = classify_frame(preprocessed_frame, interpreter, labels)
        
        # Record detections and save the first detected frame
        for bird, score in results:
            if bird != 'background':
                bird_detections.append((bird, score))
                if saved_frame_path is None:
                    frame_filename = video_path.rsplit('.', 1)[0] + '_detected.jpg'
                    cv2.imwrite(frame_filename, frame)
                    saved_frame_path = frame_filename

    return bird_detections, saved_frame_path

if __name__ == '__main__':
    # Example path for testing
    video_path = 'path/to/your/video.mp4'
    detections, saved_frame_path = run_bird_detection(video_path)
    print("Detections:", detections)
