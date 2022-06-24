from numpy import argmax
import numpy
from transformers import DetrFeatureExtractor, DetrForObjectDetection
from flask import Flask

from PIL import Image
import requests

app = Flask(__name__)


def detect_obj(url):

  image = Image.open(url)

  feature_extractor = DetrFeatureExtractor.from_pretrained('facebook/detr-resnet-50')
  model = DetrForObjectDetection.from_pretrained('facebook/detr-resnet-50')
  
  inputs = feature_extractor(images=image, return_tensors="pt")
  outputs = model(**inputs)
  
  logits = outputs.logits
  bboxes = outputs.pred_boxes

  # model predicts bounding boxes and corresponding COCO classes
  threshod = 0.7
  labels =['background', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
       'train', 'truck', 'boat', 'traffic light', 'fire hydrant',
       'street sign', 'stop sign', 'parking meter', 'bench', 'bird',
       'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra',
       'giraffe', 'hat', 'backpack', 'umbrella', 'shoe', 'eye glasses',
       'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard',
       'sports ball', 'kite', 'baseball bat', 'baseball glove',
       'skateboard', 'surfboard', 'tennis racket', 'bottle', 'plate',
       'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana',
       'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog',
       'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed',
       'mirror', 'dining table', 'window', 'desk', 'toilet', 'door', 'tv',
       'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave',
       'oven', 'toaster', 'sink', 'refrigerator', 'blender', 'book',
       'clock', 'vase', 'scissors', 'teddy bear', 'hair drier',
       'toothbrush']

  np_softmax = (logits.softmax(-1)[0, :, :-1]).detach().numpy()
  classes = []
  probability = []
  idx = []
  
  for i, j in enumerate(np_softmax):
    if numpy.max(j) > 0.7:
      classes.append(labels[numpy.argmax(j)])
      probability.append(numpy.max(j))
      idx.append(i)
  
  return classes

  
if __name__ == '__app__':
    app.run(debug=True)