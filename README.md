
# OpenGesture for African Sign Language 
Platform | Build Status |
-------- | ------------ |
OpenCV AI Kit | [![Build status](https://ci.appveyor.com/api/projects/status/swutsp1bjcc56q64/branch/master?svg=true)](https://ci.appveyor.com/project/ddiakopoulos/hand-tracking-samples/branch/master)

<p align="center">
  <img width="460" height="300" src="https://github.com/TebogoNakampe/XRDrive-Sim/blob/master/Code/hand.gif">
</p>

## Audience

The code in this repository is authored for computer-vision and machine-learning students and researchers interested in developing hand gesture applications using OpenCV AI Kit: OAK—D depth cameras.

This project provides Python code to recognize African Sign Language gestures for numbers using OpenCV AI Kit: OAK—D depth cameras. Additionally, this project showcases the utility of convolutional neural networks as a key component of real-time gesture classification pipelines using Intel OpenVINO.

The software provided here works with the currently available OpenCV AI Kit: OAK—D and Intel® RealSense™ D400 depth cameras supported by librealsense2.

## Environment Setup
* Install [DepthAI](https://github.com/luxonis/depthai)<br>
* Install [OpenVINO™ Toolkit](https://software.intel.com/en-us/openvino-toolkit) <br>
* Purchase a DepthAI Camera (see [shop.luxonis.com](https://shop.luxonis.com/))
* Ubuntu 18.04 LTS
* Install requirements

# Data Collection

To train the OpenGesture Model data was collected using Intel RealSense D435.

## OpenGesture ML Model Training and Optimization Notebooks

* [OpenGesture African Sign Language Detection](OpenGesture_OAK_D.ipynb) - This notebook includes all the necessary scripts required to retrain the gesture.blob using TensorFlow Hub for transfer learning. Furthermore the notebook includes Intel OpenVINO Toolkit's model optimzer and inference engine plugins to create a blob compatible with OpenCV AI Kit: OAK-D.


## Running the OpenGesture for South African Sign Language 
* Preparation
	* Install Requirements
		```bash
		python3 -m pip install -r requirements.txt
		```
		
		
#### How to run 

## Usage

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




		


