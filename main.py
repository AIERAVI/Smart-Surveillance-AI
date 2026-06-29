import cv2
from ultralytics import YOLO
import numpy as np
import time
import pywhatkit as kit
import tkinter as tk
from tkinter import simpledialog
import threading
import os


ROOT = tk.Tk()
ROOT.withdraw() 
phone_number = simpledialog.askstring(title="Security Setup", 
                                      prompt="Please enter your WhatsApp number\n(With country code, e.g., +919876543210):") #Enter your phone number 

if not phone_number:
    print("No number entered. System will run without WhatsApp alerts.")
else:
    print(f"Alerts will be sent to this number: {phone_number}")


if not os.path.exists("alert_images"):
    os.makedirs("alert_images")


def send_whatsapp_alert(number, image_path):
    print("Sending WhatsApp alert... please wait.")
    try:
        # Wait 15 sec for web to open, send message, then close tab in 5 sec
        kit.sendwhats_image(number, image_path, "ALERT: Suspicious Movement Detected!", 15, True, 5)
        print("WhatsApp Alert Sent Successfully!")
    except Exception as e:
        print(f"Error: {e}")


model = YOLO('yolov8n.pt') 

camera_url = "enter_camera_ip/video" # Enter your IP APP ip address 
cap = cv2.VideoCapture(camera_url)

print("Connecting to Phone Camera... Press 'q' to exit.")

ret, frame1 = cap.read()
if not ret:
    print("Camera connection failed! Please check the IP address.")
    exit()

gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
last_alert_time = 0 

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    results = model(frame, stream=True)
    
    gray2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(gray1, gray2)
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
    motion_level = np.sum(thresh) 
    
    
    if motion_level > 3000000: 
        cv2.putText(frame, "ALERT: SUSPICIOUS MOVEMENT!", (50, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        
        current_time = time.time()
        
        if current_time - last_alert_time > 60:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            img_path = f"alert_images/intruder_{timestamp}.jpg"
            cv2.imwrite(img_path, frame) # Save photo
            
            if phone_number:
                
                threading.Thread(target=send_whatsapp_alert, args=(phone_number, os.path.abspath(img_path))).start()
            
            last_alert_time = current_time 

    
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls = int(box.cls[0])
            name = model.names[cls]
            color = (0, 255, 0) if name == 'person' else (255, 0, 0)
            
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    gray1 = gray2
    frame = cv2.resize(frame, (1000, 700))
    cv2.imshow("Smart IP Surveillance", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
