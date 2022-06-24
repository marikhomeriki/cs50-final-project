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

Based on the Hugging Face facebook/detr-resnet-50 documentation this is a model description:

>The DETR model is an encoder-decoder transformer with a convolutional backbone. Two heads are added on top of the decoder outputs in order to perform object detection: a linear layer for the class labels and a MLP (multi-layer perceptron) for the bounding boxes. The model uses so-called object queries to detect objects in an image. Each object query looks for a particular object in the image. For COCO, the number of object queries is set to 100.

>The model is trained using a "bipartite matching loss": one compares the predicted classes + bounding boxes of each of the N = 100 object queries to the ground truth annotations, padded up to the same length N (so if an image only contains 4 objects, 96 annotations will just have a "no object" as class and "no bounding box" as bounding box). The Hungarian matching algorithm is used to create an optimal one-to-one mapping between each of the N queries and each of the N annotations. Next, standard cross-entropy (for the classes) and a linear combination of the L1 and generalized IoU loss (for the bounding boxes) are used to optimize the parameters of the model.




`app.py` file we are connecting with PostgreSQL and the data inserted by the user is also managed in PGAdmin. Then we call a function that saves the uploaded files and creating a url for detect_obj function. 



## Getting Started

- [Transformers Installation](https://huggingface.co/docs/transformers/installation)
- [Tensorflow Installation on Mac](https://www.tensorflow.org/install/pip)

## Tech Stack

- Python
- Flask
- PostgreSQL
- HTML
- CSS
- JavaScript
- [facebook/detr-resnet-50](https://huggingface.co/facebook/detr-resnet-50)
