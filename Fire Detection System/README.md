# Fire Detection with YOLOv8
 
# Note: 
* I have uploaded the model I trained for 80 epochs under `runs/detect/train/weights/best.pt`
* I trained the model on Google Colab on T4 GPU
# To run on webcam
```
python ./predict_on_webcam.py
```
# Training on your own again
* Follow the notebook `yolov8_on_fire.ipynb`
# Dataset
* I have uploaded the dataset on which yolov8 was transfer learned under `continuous_fire-6`
# References
@misc{
                            continuous_fire_dataset,
                            title = { continuous_fire Dataset },
                            type = { Open Source Dataset },
                            author = { 최지환 },
                            howpublished = { \url{ https://universe.roboflow.com/-jwzpw/continuous_fire } },
                            url = { https://universe.roboflow.com/-jwzpw/continuous_fire },
                            journal = { Roboflow Universe },
                            publisher = { Roboflow },
                            year = { 2022 },
                            month = { jul },
                            note = { visited on 2024-03-12 },
                            }
