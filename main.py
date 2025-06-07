from detector import ObjectDetector
from tracker import ObjectTracker
from visualizer import Visualizer
import cv2
import os

def main(video_path):
    cap = cv2.VideoCapture(video_path)
    detector = ObjectDetector()
    tracker = ObjectTracker()
    visualizer = Visualizer()

    # Taking video properties
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps    = int(cap.get(cv2.CAP_PROP_FPS))

    # Setting up the video writer
    out_path = os.path.join("outputs", "output_video.mp4")
    out = cv2.VideoWriter(out_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        detections = detector.detect(frame)
        tracks = tracker.update(detections, frame)
        output_frame = visualizer.draw(frame, tracks)

        out.write(output_frame)  # Save to file
        cv2.imshow('Output', output_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    print(f"\n Output video saved to: {out_path}")

if __name__ == "__main__":
    main("data/input_video.mp4")
