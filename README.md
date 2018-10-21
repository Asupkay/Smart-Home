# Smart Home
## Introduction

Our team believes that there is an untapped market for smart home technology which utilizes machine learning. Therefore, over the course of this semester, our team will be designing and building a proof of concept for a smart home application that will offer users fundamental security and lifestyle features that will make their lives easier. Our initial target customer base are homeowners, but eventually could expand to businesses as well, since one of our basic features is understanding who has entered the building or room and identifying how the system should respond.

## Roles and Responsibilities
* Frontend Team
    * Kyle **Developer**
    * Kipsy **Developer**
    * Sanjeev **Team lead**
    * Pan **Developer**
    * Ziang **Developer**
* Backend Team
    * Pratik **Developer**
    * Alex **Team lead**
    * Sidd **Developer**
    * Suchita **Developer**

## Method
* Software
    * Python 3.6
    * Flask
    * React
    * Linux
    * OpenCV, Hog, CNN
    * Linter
* Infrastructure
    * App Engine (Standard Environment)
    * AutoML
    * Firestore
    
## Raspberry Pi Setup

How to connect via Windows and PuTTY:
   * Open PuTTY
   * Under "Host Name (or IP address)", enter 155.246.215.123
   * A Linux Command Prompt will appear. Next to "login as", enter pi
   * Next to "pi@155.246.215.123's password:", enter Stevens1870
   * You should be connected to the Pi. Enter linux commands as desired
   * To exit, enter sudo shutdown
   * Shutdown will be scheduled within the next minute. Do not exit until a PuTTY Fatal Error appears

How to connect via Mac:
   * Open terminal
   * Enter "ssh pi@155.246.215.123"
   * Enter "yes"
   * Enter password: Stevens1870
   * You should be connected to the Pi. Enter linux commands as desired
   * To exit, enter sudo shutdown
   * Shutdown will be scheduled within the next minute.
   * Will receive message, "Connection to 155.246.215.123 closed by remote host. Connection to 155.246.215.123   closed.

## Install OpenCV + 3 and Python on Raspberry Pi
    * The resource comes from https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/.
Install dependencies:
* Update and upgrade any existing packages.    
	* sudo apt-get update && sudo apt-get upgrade
	* Install the developer tools to help with configuring the OpenCV build process.    
	* sudo apt-get install build-essential cmake pkg-config
* Install image and video I/O packages that allow us to load various image file formats from disk as well as the video stream.
	* sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
	* sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
	* sudo apt-get install libxvidcore-dev libx264-dev
* Install highgui which is used to display images to our screen and build basic GUIs.
	* sudo apt-get install libgtk2.0-dev libgtk-3-dev
* Many operations inside of OpenCV (namely matrix operations) can be optimized further by installing a few extra dependencies
	* sudo apt-get install libatlas-base-dev gfortran
* Install Python3 Header files
	* sudo apt-get install python3-dev
* Download the OpenCV open source code(The version installed is 3.3.0, maybe we need to update the version in the future)
	* cd ~
	* wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.3.0.zip
	* unzip opencv.zip
* Install the opencv_contrib repository
	* wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.3.0.zip
	* opencv_contrib.zip
     
