# Keylogger App
Keylogging application that sends log to email!
The purpose of this program is to learn the basics of cybersecurity and the libraries from Python

![image](https://user-images.githubusercontent.com/66978846/150712645-425da74a-8820-4cbf-b2d4-f253334d1397.png)

## Introduction
- To begin, check if your device has Python installed by typing `python --version` 

### Installation
- Usually, pip is automatically installed if you are: working in a virtual environment using Python downloaded from python.org using Python that has not been modified by a redistributor to remove ensurepip. 
- Keep in mind the script does not work on Python 2.7 The minimum supported Python version is 3.6. so please use https://bootstrap.pypa.io/get-pip.py 

on your terminal write:

```
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

$ python3 get-pip.py
```

- pip is the standard package manager for Python. It allows you to install and manage additional packages that are not part of the Python standard library.

##### Install Pip on macOS via easy_install

```
$sudo easy_install pip
```

##### Install Pip on macOS via brew

```
$brew install python
```

### Installing libraries 
Install `pynput`
```
$pip install pynput 
```` 
pynput allows you to control and monitor input devices. Currently, mouse and keyboard input and monitoring are supported.

## Other

- I used a [ASCII text generator](https://patorjk.com/software/taag/#p=display&f=Slant&t=KeyLogger) to make the Keylogger text that pops up on the terminal in the picture above. 
- I used the smtplib library to produce the sending email feature, most keyloggers save the words in a text file, but I felt like sending it in an email is more of how a hacker would do it. https://realpython.com/python-send-email/
- used this as reference for the code https://pypi.org/project/pynput/



