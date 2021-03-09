# CityFace-Mask-Detection
For CityHack2021 by Hacking Genie

## Introduction
This is an innovative cloud-based entrance detection & control system using machine learning and computer vision at SR.

It integrates functions of SID, temperature, and mask wearing detection with complete automation. The data collected will be transmitted to and analyzed in the cloud, and further visualized before posting to a website. Any abnormal situation will be notified.

The project frees the labor of the securities, lowers the risk of infection through physical contact and upgrades the efficiency of the detecting & recording process to a great extent.

In addition to monitoring the SR, our project could potentially be applied to much wider scenarios such as miscellaneous entrance systems and be enhanced by integrating physical access control modules, for instance, automated gates, buzzers etc..

##Setup
1. Clone the repository
```
git clone https://github.com/Laylar-sleep/CityFace-Mask-Detection.git
```
2. Run the following command in your Terminal/Command Prompt to install the libraries required
```
pip install -r requirements.txt
```

##Execute
1. Go into the cloned project directory and run the following command:
```
python train_mask_detector.py --dataset dataset
```
2. Run the following command to detect face masks in real-time video streams:
```
python detect_mask_video.py 
```
##Results
We can detect 4 kinds of mask wearing situations with around 98% accuracy: 
1. with mask
2. incorrectly wear (mouth & nose not covered)
3. incorrectly wear (nose not covered)
4. without mask

