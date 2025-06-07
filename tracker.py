class ObjectTracker:
    def __init__(self):
        self.next_id = 0

    def update(self, detections, frame):
        tracks = []
        for det in detections:
            track_id = self.next_id
            self.next_id += 1
            tracks.append({
                "bbox": det[:4],
                "conf": det[4],
                "class_id": det[5],
                "id": track_id
            })
        return tracks
