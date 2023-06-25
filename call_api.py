import requests
#from picamera import PiCamera
from time import sleep

check = 0
ans = ""
api_1 = 'https://wasteimg-tioov5bccq-as.a.run.app/vgg16/'
api_2 = 'https://wasteimg-tioov5bccq-as.a.run.app/densenet169/'
api_3 = 'https://wasteimg-tioov5bccq-as.a.run.app/resnet101/'
api_4 = 'https://wasteimg-tioov5bccq-as.a.run.app/mobilenetv2/'
api_5 = 'https://wasteimg-tioov5bccq-as.a.run.app/inceptionv3/'
test_docker = 'http://127.0.0.1:8080/vgg16'
image_file = 'test.jpg'
#camera = PiCamera()

#camera.start_preview()
#sleep(3)
#camera.capture(image_file)
#camera.stop_preview()

files = {'file': open(image_file, 'rb')}
    
response = requests.post(test_docker, files=files)

try:
    results = response.text
    results = results.strip("{}")
    results = results.split(",")

    for text in results:
        splt = text.split(":")
        num = float(splt[1])
        if (num > check):
            check = num
            ans = splt[0]
    print(ans)
    print(check)               
except requests.exceptions.RequestException:
    print(response.text)