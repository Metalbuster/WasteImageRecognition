# WasteImageRecognition
This project is for providing people with interests in sorting waste using Image Recognition the starting point including the dataset from Thai's waste and the code for using trained CNN models from said dataset. CNN models used in this project are VGG16, DenseNet169, ResNet-101, MobileNetV2, and InceptionV3.

## Dataset
This repository contains the dataset that was inspired by [Trashnet](https://github.com/garythung/trashnet) which is the dataset made by [Gary Thung](https://github.com/garythung) and [Mindy Yang](http://github.com/yangmindy4). We have the original version made of Thai's waste and the combined version which is a combination of the new original dataset and the Trashnet dataset. The original dataset consists of 8,635 images:

- 1,667 glass
- 2,022 paper
- 1,778 plastic
- 1,313 metal
- 1,855 trash

The pictures were taken by placing the object on a white background with 4:3 ratio. They were taken by multiple smartphones from using data market service.

**The original dataset can be downloaded [here](https://drive.google.com/drive/folders/1WNzyYFiU_GqlSUpDFB6ubXoIAF-x8jd9).**
**The combined dataset can be downloaded [here](https://drive.google.com/drive/folders/1tzIJD0FnNYsQdx7zPOyeYS90bmydnN9n).**

## Building Docker

You can git clone this repository then run the following commands at the cloned folder to build the docker container. Make sure you install the docker first.

```docker build -t img_waste .```

```docker run -p 8080:8080 img_waste```

Then, you can access the local FastAPI version via http://localhost:8080/docs, and feel free to upload image and press execute on each model to use it yourself.
If you want to use the actual web based API version, you can run the docker container on the cloud and use call_api.py to use the VGG16 trained model to classify image name 'test.jpg' which you can put in the same folder as call_api.py. Replace test_docker in line 23 for any of the api_#num for the model that you want to use.

## Conclusion

If you want to contribute to the project, feel free to fork it or give citation to this repository. We wish that this project will help improving waste sorting using the Image Recognition.

