# Object Detection & Tracking using YOLOv8

This project implements a real-time object detection and tracking pipeline using the **YOLOv8** model and a simple identity tracking mechanism. It detects multiple object classes (like people and cars) and assigns consistent IDs to each object across frames in a video.

---

## Objective

To demonstrate skills in object detection, tracking, and modular Python development by:
- Detecting at least two object classes using YOLOv8.
- Tracking object identities across video frames.
- Visualizing bounding boxes with class names and unique tracking IDs.

---

## Requirements

- Python 3.7+
- pip packages (see `requirements.txt`):
  ```bash
  pip install -r requirements.txt

---

## Project Structure
  
├── main.py              # Entry point to run the pipeline

├── detector.py          # YOLOv8 object detection logic

├── tracker.py           # Simple ID assignment tracker

├── visualizer.py        # Draws boxes, labels, IDs

├── data/

 │   └── input_video.mp4  # Input video file

├── outputs/

 │   └── output_video.mp4 # Output with tracking visualization

├── requirements.txt     # Python dependencies

└── README.md

---

## Instructions to produce the output video

- Make sure to install the requirements mentioned in requirements.txt.
- Run main.py file.
- The video will display with bounding boxes and IDs.
- Type 'q' on your keyboard to close the video.
- The output video will be saved in the outputs folder.

---

## Input video

The input video used is from Pexels and is free for personal/commercial use.

Input video URL: https://videos.pexels.com/video-files/5402042/5402042-hd_1920_1080_30fps.mp4 

---

## Output video properties

Detected object classes: person, car, and more.

Assigned consistent tracking IDs per object.

Real-time visualization with OpenCV.
