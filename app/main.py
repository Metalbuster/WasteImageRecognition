from fastapi import FastAPI, File, UploadFile

from waste_image_recognition.predictor import ImagePredictor
from waste_image_recognition.predictor_vgg16 import ImagePredictor_vgg16
from waste_image_recognition.predictor_densenet169 import ImagePredictor_densenet169
from waste_image_recognition.predictor_resnet101 import ImagePredictor_resnet101
from waste_image_recognition.predictor_mobilenetv2 import ImagePredictor_mobilenetv2
from waste_image_recognition.predictor_inceptionv3 import ImagePredictor_inceptionv3


app = FastAPI()

predictor_config_path = "config.yaml"

predictor = ImagePredictor.init_from_config_url(predictor_config_path)
predictor_vgg16 = ImagePredictor_vgg16.init_from_config_url(predictor_config_path)
predictor_densenet169 = ImagePredictor_densenet169.init_from_config_url(predictor_config_path)
predictor_resnet101 = ImagePredictor_resnet101.init_from_config_url(predictor_config_path)
predictor_mobilenetv2 = ImagePredictor_mobilenetv2.init_from_config_url(predictor_config_path)
predictor_inceptionv3 = ImagePredictor_inceptionv3.init_from_config_url(predictor_config_path)

@app.post("/prototype/")
def create_upload_file(file: UploadFile = File(...)):
    return predictor.predict_from_file(file.file)

@app.post("/vgg16/")
def create_upload_file(file: UploadFile = File(...)):
    return predictor_vgg16.predict_from_file(file.file)

@app.post("/densenet169/")
def create_upload_file(file: UploadFile = File(...)):
    return predictor_densenet169.predict_from_file(file.file)

@app.post("/resnet101/")
def create_upload_file(file: UploadFile = File(...)):
    return predictor_resnet101.predict_from_file(file.file)

@app.post("/mobilenetv2/")
def create_upload_file(file: UploadFile = File(...)):
    return predictor_mobilenetv2.predict_from_file(file.file)

@app.post("/inceptionv3/")
def create_upload_file(file: UploadFile = File(...)):
    return predictor_inceptionv3.predict_from_file(file.file)

