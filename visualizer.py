import cv2

class Visualizer:
    def draw(self, frame, tracks):
        for obj in tracks:
            x1, y1, x2, y2 = obj["bbox"]
            cls_id = obj["class_id"]
            track_id = obj["id"]
            label = f"ID {track_id} | Class {cls_id}"
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
        return frame
