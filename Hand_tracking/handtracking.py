import cv2
import mediapipe as mp

import numpy as np

import time

cap = cv2.VideoCapture(0)
mphands= mp.solutions.hands

hands = mphands.Hands()

draw = mp.solutions.drawing_utils

prev_time = 0
current_time=0


while True:
    ret, frame = cap.read()

    results = hands.process(frame)

    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handlm in results.multi_hand_landmarks:
            for id, landmark in enumerate(handlm.landmark):
                height, width, channel = frame.shape

                cx, cy = int(landmark.x * width), int(landmark.y * height)

                print(id, cx, cy)
                if id ==0:
                    cv2.circle(frame, (cx, cy), 14, (172, 172, 200), cv2.FILLED)

                if id ==4:
                    cv2.circle(frame, (cx, cy), 14, (172, 172, 200), cv2.FILLED)

                if id ==8:
                    cv2.circle(frame, (cx, cy), 14, (172, 172, 200), cv2.FILLED)

                if id ==12:
                    cv2.circle(frame, (cx, cy), 14, (172, 172, 200), cv2.FILLED)

                if id ==16:
                    cv2.circle(frame, (cx, cy), 14, (172, 172, 200), cv2.FILLED)

                if id ==20:
                    cv2.circle(frame, (cx, cy), 14, (172, 172, 200), cv2.FILLED)

                    
            draw.draw_landmarks(frame, handlm, mphands.HAND_CONNECTIONS)



    current_time = time.time()
    fps = 1/(current_time - prev_time)
    prev_time = current_time


    cv2.putText(frame, "FPS: {}".format(int(fps)), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (120, 220, 255), 2)
    cv2.imshow("image", frame)
    if  cv2.waitKey(1) & 0xFF == 27:
        break


