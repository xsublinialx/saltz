# About Saltz

Saltz is an Open Source password generator for Linux. It provides secure passwords for any service you use. As of now the software is in alpha. This software is not complete, any feautures that are in the program now may be removed or updated. New features are constant.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine. See prerequisites and installing for notes on how to setup the software. 

It is worth noting that in older versions of the program a script file was needed. Becuase of changes this is no longer required and you can now run the python file by itself.


### Prerequisites

First make sure that you have Python 2.7 installed. You can either head over to python.org to install it or get it through the terminal.


wget and install the file and go through the setup process.
```
wget https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz
```

### Download and Set Up 

First navigate to the releases tab of the home page. Choose the release of your choice. I highly reccomend that you choose the newest release if it is in relation to bug fixes, older versions may be unstable.

Open and extract the zip or tar file to the user home directory. Make sure that you are in the directory in which you downloaded the file from so you can extract it. 

For the zip file
``` 
unzip saltz-1.0.2-alpha.zip "/home/YOUR USERNAME/"
```
or

For the tar file
```
tar xvzf saltz-1.0.2-alpha.tar.gz "/home/YOUR USERNAME/"
```
Now go inside of the folder you extracted into your user directory. Highlight the saltz.py file and copy and paste it outside of the folder into your user directory. After doing so, rename the folder to ``saltz``.

You will need to set execute permissions for the program so it can run on your computer do this by running chmod in a terminal window.
```
chmod +x saltz.py
```
You can now run the program!

```
python saltz.py
```
