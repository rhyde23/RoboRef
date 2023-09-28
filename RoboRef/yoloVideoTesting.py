#Yolo Testing
import cv2
import numpy as np

net = cv2.dnn.readNet("/Users/RHyde23/Desktop/RoboRef/yolov3.weights", "/Users/RHyde23/Desktop/RoboRef/yolov3.cfg")
net.setPreferableBackend(cv2.dnn.)


"""
classes = []
with open("/Users/RHyde23/Desktop/RoboRef/coco.txt", "r") as f:
    classes = f.read().splitlines()
"""

classes = ["person"]

cap = cv2.VideoCapture("/Users/RHyde23/Desktop/RoboRef/videoTest.mp4")
#img = cv2.imread("/Users/RHyde23/Desktop/RoboRef/image.jpg")

font = cv2.FONT_HERSHEY_PLAIN
height, width = 832, 832
while True :
    _, img = cap.read()
    blob = cv2.dnn.blobFromImage(img, 1/255, (width, height), (0, 0, 0), swapRB=True, crop=False)
    net.setInput(blob)
    output_layers_names = net.getUnconnectedOutLayersNames()
    layerOutputs = net.forward(output_layers_names)

    boxes = []
    confidences = []

    for output in layerOutputs :
        for detection in output :
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5 :
                center_x = int(detection[0]*width)
                center_y = int(detection[1]*height)
                w = int(detection[2]*width)
                h = int(detection[3]*height)
                x = int(center_x - w/2)
                y = int(center_y - h/2)
                boxes.append([x, y, w, h])
                confidences.append((float(confidence)))

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    for i in indexes.flatten() :
        x, y, w, h = boxes[i]
        confidence = str(round(confidences[i], 2))
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == 27:
        break 

cap.release()
cv2.destroyAllWindows()
