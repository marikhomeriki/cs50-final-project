# Object Detection with ML

## Video Demo:  <https://youtu.be/8aVP2dt2QuY>

## Description

In this web application it is possible to upload a photo and using Machine Learning app will detect objects in this photo. 
It is also possible to see the history of uploaded photos along with the list of objects detected on these photos. 

Let's start with the `layout.html`. In this file I have created a header and footer for the web application. 

`index.html` displays the history of all the photos uploaded. 

`upload.html` displays the upload functionality of the application. Once the photo is uploaded it is displayed with the detected objects. 

In the `static` folder there is `styles.css` file where all the visual effects live and favicon. Also, there is second file `files` where all uploaded files are saved. 

`helpers.py` is the file where the Machine Learning model is. There is a function detect_obj, which takes image url and returns list of detected objects. 


## Getting Started

- [Transformers Installation](https://huggingface.co/docs/transformers/installation)
- [Tensorflow Installation on Mac](https://www.tensorflow.org/install/pip)

## Tech Stack

- Python
- Flask
- PostgreSQL
- HTML
- CSS
- [facebook/detr-resnet-50](https://huggingface.co/facebook/detr-resnet-50)
