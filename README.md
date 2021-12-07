# Saviour_Eye_Project

## Steps to configure

* First boot up the raspberry pi.
* Install git.
```
sudo apt-get install git
```
* Clone this git directory:
```
git clone https://github.com/supr3sh/Saviour_Eye_Project.git
cd Saviour_Eye_Project
```
* Set up the enviornment:
```
source tflite-env/bin/activate
bash get_pi_requirements.sh
pip install -r requirements.txt
```

* Make sure you have a camera attached to your raspberry pi.
* Start the script by python 