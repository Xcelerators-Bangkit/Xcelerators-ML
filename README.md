## Tools and resource

1. Python - Tested on Python 3.9+
2. Tensorflow - Tested on Tensorflow 2.13.0+
3. FastAPI
4. Docker

## Steps for model training
1. First download the datasets from the following link: https://drive.google.com/drive/folders/17_vJzfcs4KFM9Nkqv1Bjt4HIpGLQYtMo?usp=drive_link
   <h1 align="center">
       <br>
       <a href="https://ibb.co/cwjFq8B"><img src="https://i.ibb.co/Qk4N0Hg/Screenshot-from-2023-12-21-18-26-39.png" alt="Screenshot-from-2023-12-21-18-26-39" border="0"></a>
       <br>
   </h1>

2. Pre-processing the data and clean it up by separating the data into training, validation, and test.
   <h1 align="center">
       <br>
       <a href="https://ibb.co/HhTh3c6"><img src="https://i.ibb.co/qJYJVHK/Screenshot-from-2023-12-21-18-27-42.png" alt="Screenshot-from-2023-12-21-18-27-42" border="0"></a>
       <br>
   </h1>
3. Then, rescale the image and also determine the target image size that we will use. We use a target size of 224px.
   <h1 align="center">
       <br>
       <a href="https://ibb.co/HhTh3c6"><img src="https://i.ibb.co/qJYJVHK/Screenshot-from-2023-12-21-18-27-42.png" alt="Screenshot-from-2023-12-21-18-27-42" border="0"></a>
       <br>
   </h1>
4. After splitting into 3 parts, then each data is ready for model training.
5. For our training, we use the existing pre-trained model Xception as our base model.
   <h1 align="center">
       <br>
       <a href="https://ibb.co/RzQ7mhw"><img src="https://i.ibb.co/jg3H2VX/Screenshot-from-2023-12-21-18-28-31.png" alt="Screenshot-from-2023-12-21-18-28-31" border="0"></a>
       <br>
   </h1>
7. We also created our own model by adding a 2D Convolutional layer, MaxPooling, and also added 2 Neural Layers.
   <h1 align="center">
      <br>
      <a href="https://ibb.co/PWSxKt4"><img src="https://i.ibb.co/c8mJ0xt/Screenshot-from-2023-12-21-18-29-02.png" alt="Screenshot-from-2023-12-21-18-29-02" border="0"></a>
      <br>
   </h1>
8. With this model, we can predict a class from the equipment data that users will use later.
   <h1 align="center">
      <br>
      <a href="https://ibb.co/vJ7QVFn"><img src="https://i.ibb.co/y8wYd9j/Screenshot-from-2023-12-21-18-29-40.png" alt="Screenshot-from-2023-12-21-18-29-40" border="0"></a>
      <br>
   </h1>
9. We got an accuracy 99% and validation accuracy 87%
    <h1 align="center">
       <br>
       <a href="https://ibb.co/WkwS6Tc"><img src="https://i.ibb.co/LxW48GC/Screenshot-from-2023-12-21-18-29-59.png" alt="Screenshot-from-2023-12-21-18-29-59" border="0"></a>
       <br>
   </h1>
10. We do deployments using Docker, FastAPI, and also Cloud Run.
