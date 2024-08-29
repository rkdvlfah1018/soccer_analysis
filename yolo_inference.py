from ultralytics import YOLO

#choose a model yolo + version number + size of the parameter (x for the largest model)
model = YOLO('yolov8x')

#run the model
results = model.predict('./input_videos/08fd33_4.mp4', save = True)
