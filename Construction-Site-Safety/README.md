# Construction-Site-Safety
## Image Processing Mini Project
### Group Members
* Akshay Dongare BC218
* Yash Dagadkhair BC212
* Jaydatta Patwe BC223

## Overview
4,764 workers died on the job in 2020 (3.4 per 100,000 full-time equivalent workers). Workers in transportation and material moving occupations and construction and extraction occupations accounted for nearly half of all fatal occupational injuries (47.4 percent), representing 1,282 and 976 workplace deaths, respectively.
Occupational Safety and Health Administration (US Department of Labour)
There have been many accidents in construction sites due to lack of safety measures. A major reason for this has been workers not wearing Personal Protective Equipments (PPE) for their safety. Detecting PPEs become very crucial for the continuous monitoring of worker safety.
Dataset collection
This dataset is provided as a collection in Roboflow, please check this link: Construction Site Safety Image Dataset under the CC BY 4.0 License

This dataset is a great collection of images, since the labels are in the following format: 'Hardhat', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person', 'Safety Cone', 'Safety Vest', 'machinery', 'vehicle'. It is very important in tracking and monitoring applications whether a person is wearing Hardhat or NO-Hardhat. Most of the datasets are not annotated in this particular way, making this dataset very useful.

## Quick Summary
Number of classes: 10
Label Annotation: YOLO format (.txt)
Metadata: metadata.csv and count.csv provides information about the dataset and train-val-test count information.
PPE Class Map: {0: 'Hardhat', 1: 'Mask', 2: 'NO-Hardhat', 3: 'NO-Mask', 4: 'NO-Safety Vest', 5: 'Person', 6: 'Safety Cone', 7: 'Safety Vest', 8: 'machinery', 9: 'vehicle'}
## Quick Run
* Clone the repo:
```
git clone https://github.com/Akshay-Dongare/Construction-Site-Safety.git
```
* Go to the directory
```
cd Construction-Site-Safety
```
* Install the dependencies
```
pip install -r requirements.txt
```
* Install PyTorch according to your system configuration from: https://pytorch.org/get-started/locally/
* Example (if you have Windows, pip, Nvidia GPU and want to use Cuda 12.1):
```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```
* Run inference on webcam in real-time
```
python predict_using_webcam.py
```
* Run inference on video
```
yolo predict model="./models/best.pt" source="./source_files/example_video.mp4"
```
* Open notebook in colab
<a target="_blank" href="https://colab.research.google.com/github/Akshay-Dongare/YOLOv8-Projects/blob/main/Construction-Site-Safety/main.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open Notebook In Colab"/>
</a>

# Sources
* https://blog.roboflow.com/how-to-train-yolov8-on-a-custom-dataset/
* https://github.com/snehilsanyal/Construction-Site-Safety-PPE-Detection
* @misc{ construction-site-safety_dataset,
    title = { Construction Site Safety Dataset },
    type = { Open Source Dataset },
    author = { Roboflow Universe Projects },
    howpublished = { \url{ https://universe.roboflow.com/roboflow-universe-projects/construction-site-safety } },
    url = { https://universe.roboflow.com/roboflow-universe-projects/construction-site-safety },
    journal = { Roboflow Universe },
    publisher = { Roboflow },
    year = { 2023 },
    month = { feb },
    note = { visited on 2023-02-23 },
}
