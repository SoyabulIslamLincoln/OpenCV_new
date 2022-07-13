import os
from time import time
import cv2
import time
import os
from hand_detector_module import hand_detection


widthCam =720
heightCam = 640
cap = cv2.VideoCapture(0)

cap.set(3, widthCam)
cap.set(4, heightCam)

path = "D:/opencv_projects/Hand_tracking/Hand_image"

image_list = os.listdir(path)
print(image_list)
overlay_image=[]
reshaped_image=[]

for im_path in image_list:
    image = cv2.imread(f'{path}/{im_path}')
    image= cv2.resize(image, (100, 100))
    overlay_image.append(image)


print(len(reshaped_image))


prev_time = 0
current_time=0


detection = hand_detection()

tip_ids = [4, 8, 12, 16, 20]
while True:
    set, frame = cap.read()
    frame = detection.hand_find(frame)
    position = detection.findPosition(frame, draw=False)
    #print(position)

    if len(position) !=0:

        finger =[]

        #thumb

        if position[tip_ids[0]][1] > position[tip_ids[0]-1][1]:
            finger.append(1)
        else:
            finger.append(0)
        for i in range(1,5):
            if position[tip_ids[i]][2] < position[tip_ids[i]-2][2]:
                finger.append(1)
            else:
                finger.append(0)


        #print(finger)

        total_fingers = finger.count(1)
        print(total_fingers)
        
        
        
        frame[0:100, 0:100] = overlay_image[total_fingers]

        cv2.putText(frame, str(total_fingers), (20, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    current_time = time.time()
    fps = 1/(current_time - prev_time)
    prev_time = current_time



    cv2.putText(frame, "FPS: {}".format(int(fps)), (100,35), cv2.FONT_HERSHEY_SIMPLEX, 1, (120, 220, 255), 2)
    cv2.imshow('frame', frame)



    if  cv2.waitKey(1) & 0xFF == 27:
        break