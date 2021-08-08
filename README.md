
# OpenGesture for African Sign Language 
Platform | Build Status |
-------- | ------------ |
OpenCV AI Kit | [![Build status](https://ci.appveyor.com/api/projects/status/swutsp1bjcc56q64/branch/master?svg=true)](https://github.com/AfricaMachineIntelligence/opengesture)
Google Colab | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AfricaMachineIntelligence/opengesture/blob/main/OpenGesture_OAK_D.ipynb)

<p align="center">
  <img width="460" height="300" src="https://github.com/TebogoNakampe/XRDrive-Sim/blob/master/Code/hand.gif">
</p>

## Audience

The code in this repository is authored for computer-vision and machine-learning students and researchers interested in developing hand gesture applications using OpenCV AI Kit: OAK—D depth cameras.

This project provides Python code to recognize African Sign Language gestures for numbers using OpenCV AI Kit: OAK—D depth cameras. Additionally, this project showcases the utility of convolutional neural networks as a key component of real-time gesture classification pipelines using Intel OpenVINO.

The software provided here works with the currently available OpenCV AI Kit: OAK—D and Intel® RealSense™ D400 depth cameras.

## Environment Setup
* Install [DepthAI](https://github.com/luxonis/depthai)<br>
* Install [OpenVINO™ Toolkit](https://software.intel.com/en-us/openvino-toolkit) <br>
* Install [Ubuntu 18.04 LTS ](https://ubuntu.com/download/desktop)<br>
* Purchase a DepthAI Camera (see [shop.luxonis.com](https://shop.luxonis.com/))

# Data Collection

To train the OpenGesture Model data was collected using Intel RealSense D435.
## 2. Defining hand gestures.
Depth                 |  Color
:-------------------------:|:-------------------------:
![](https://github.com/AfricaMachineIntelligence/OpenGesture/blob/main/Assets/11_Depth_adobespark%20(1).png)  |  ![](https://github.com/AfricaMachineIntelligence/OpenGesture/blob/main/Assets/11a_Color_adobespark_adobespark.png)


Download [OpenGesture Depth and Color Dataset](https://github.com/AfricaMachineIntelligence/opengesture3d-data)<br>


## OpenGesture ML Model Training and Optimization Notebooks

* [TF Hub Transfer Learning: OpenGesture ASL](OpenGesture_OAK_D.ipynb) - This notebook includes all the necessary scripts required to retrain the gesture.blob using TensorFlow Hub for transfer learning. Furthermore the notebook includes Intel OpenVINO Toolkit's model optimzer and inference engine plugins implementation code to create a blob compatible with OpenCV AI Kit: OAK-D.

* [Image Classification Custom Model: OpenGesture ASL](OpenVINO_+_OpenCV_OAK_Tensorflow_Gesture_Classification.ipynb) - This notebook includes all the necessary scripts required to train a custom classifier the gesture.blob using TensorFlow and Keras for and also includes Intel OpenVINO Toolkit's model optimzer and inference engine plugins implementation code to create a blob compatible with OpenCV AI Kit: OAK-D.

## Running the OpenGesture for South African Sign Language 
* Preparation
	* Install Requirements
		```bash
		git clone https://github.com/AfricaMachineIntelligence/opengesture.git
		cd opengesture
		python3 -m pip install -r requirements.txt
		```
		
		
#### How to run 

```
usage: main.py [-h] [-nd] [-cam] [-vid VIDEO]

optional arguments:
  -h, --help            show this help message and exit
  -nd, --no-debug       Prevent debug output
  -cam, --camera        Use DepthAI 4K RGB camera for inference (conflicts with -vid)
  -vid VIDEO, --video VIDEO
                        Path to video file to be used for inference (conflicts with -cam)

* For English: Run the python3 main.py -cam
* For Setswana: Run the python3 main_setwana.py -cam
* For Zulu: Run the python3 main_zulu.py -cam
* For Xhosa: Run the python3 main_xhosa.py -cam




		


