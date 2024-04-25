# Android-Phone-CLI

A command-line utility written in Python with the rich-click library. The purpose of this tool is to interface with an Android Phone to control specific data such as contacts, call logs and messages. This library utilizes a preexisting library that handles Android operations along with a custom Android app (AndroidPhoneStatus) that must be downloaded to the phone under test.

## 🤔 Motivation
When testing functionality on device that requires connection to a mobile device, it can become tedious to modify contacts and call data manually. The focus of this project is to help manual testers by providing a utility to perform common operations within seconds. This can greatly speedup testing as testers no longer have to manually enter data on the phone or remove/modify existing data one at a time.

### 🏁 Goal
The goal of this project was to reduce time taken by manual testing. Using this utility, a manual tester was able to reduce the time taken testing by 10 minutes. Thus, the main goal of this project was achieved by providing common functionalities that previously serverd as a bottleneck when testing.

## 🚀 Quick Start
Download the repository by either cloning the repo or downloading the ZIP. I recommend creating a new virtual environment in Python as the project has several dependencies that will need to be installed (found in requirements.txt).

First install the dependencies using the following:
```
pip install -r "requirements.txt"
```

## 🚴 Usage
The launcher code is found in cli.py. Run the code by using the following:
```
py cli.py phone <commands>
```

Example arguements include the following:
```
Add contact:
py cli.py phone contacts --add <string>

Add 100 predefined contacts:
py cli.py phone contacts --add-multiple

Remove contact:
py cli.py phone contacts --remove <string>
```

Additional arguments and their usecases can be found by viewing the help page of the tool.

```
py cli.py -h
```