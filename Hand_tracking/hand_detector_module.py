import cv2
import mediapipe as mp

import numpy as np

import time


class hand_detection():
    def __init__(self, mode= False, max_number_hands = 2,detection_conf = 0.5, track_conf=0.5):
        
        #self.mode = mode
        #self.max_number_hands = max_number_hands
        #self.detection_conf = detection_conf
        #self.track_conf = track_conf

        self. mphands= mp.solutions.hands

        self.hands = self.mphands.Hands()

        self.draw = mp.solutions.drawing_utils


    def hand_find(self, frame, draw=True):
        self.results = self.hands.process(frame)

        if self.results.multi_hand_landmarks:
            for handlm in self.results.multi_hand_landmarks:
                if draw:
                    self.draw.draw_landmarks(frame, handlm, self.mphands.HAND_CONNECTIONS)



                
        return frame


    def findPosition(self, frame, hand_number= 0, draw= True):
        landmarks=[]

        if self.results.multi_hand_landmarks:
            myhand = self.results.multi_hand_landmarks[hand_number]
            for id, landmark in enumerate(myhand.landmark):
                height, width, channel = frame.shape
                cx, cy = int(landmark.x * width), int(landmark.y * height)


                landmarks.append([id, cx, cy])
                if draw:
                   cv2.circle(frame, (cx, cy), 8, (172, 172, 200), cv2.FILLED)
                   
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
        return landmarks

        



def main():
    prev_time = 0
    current_time=0

    cap = cv2.VideoCapture(0)
    detection = hand_detection()
    while True:
        ret, frame = cap.read()
        frame = detection.hand_find(frame)
        list = detection.findPosition(frame, draw=False)
        if len(list) != 0 :
            print(list[4])

        current_time = time.time()
        fps = 1/(current_time - prev_time)
        prev_time = current_time


        cv2.putText(frame, "FPS: {}".format(int(fps)), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (120, 220, 255), 2)



        cv2.imshow("image", frame)
        if  cv2.waitKey(1) & 0xFF == 27:
            break
    

if __name__ == "__main__":
    main()