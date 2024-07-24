from ultralytics import YOLO
import cv2
import math
import streamlit

# start webcam
#cap = cv2.VideoCapture(0)
#cap.set(3, 640)
#cap.set(4, 480)

# model
model = YOLO("models/best.pt")

# object classes
classNames = ['Hardhat', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 
              'Person', 'Safety Cone', 'Safety Vest', 'machinery', 'vehicle']

#cam in streamlit
img_file_buffer = st.camera_input("Starting camera...!")

while True:
    if img_file_buffer is not None:
        # To read image file buffer with OpenCV:
        bytes_data = img_file_buffer.getvalue()
        cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    
        #success, img = cap.read()
        results = model(cv2_img, stream=True)
    
        # coordinates
        for r in results:
            boxes = r.boxes
    
            for box in boxes:
                # bounding box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values
    
                # put box in cam
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
    
                # confidence
                confidence = math.ceil((box.conf[0]*100))/100
                print("Confidence --->",confidence)
    
                # class name
                cls = int(box.cls[0])
                print("Class name -->", classNames[cls])
    
                # object details
                org = [x1, y1]
                font = cv2.FONT_HERSHEY_SIMPLEX
                fontScale = 1
                color = (255, 0, 0)
                thickness = 2
    
                cv2.putText(cv2_img, classNames[cls], org, font, fontScale, color, thickness)
    
        cv2.imshow('Webcam', cv2_img)
        st.image(cv2_img)
        if cv2.waitKey(1) == ord('q'):
            break
    
cap.release()
cv2.destroyAllWindows()
