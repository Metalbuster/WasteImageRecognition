from setuptools import setup
from setuptools import find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

try:
    with open(os.path.join(here, "requirements.txt"), encoding="utf-8") as f:
        REQUIRED = f.read().split("\n")
except:
    REQUIRED = []

setup(name='waste_image_recognition',
      version='1.0',
      description='Models for Waste image classification',
      url='https://github.com/Metalbuster/WasteImageRecognition',
      install_requires=REQUIRED,
      classifiers=[
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'Programming Language :: Python :: 3.10',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      packages=find_packages(exclude=("example", "app", "data", "docker", "tests")))