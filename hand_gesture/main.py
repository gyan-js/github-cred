import cv2
import numpy as np
import mediapipe as mp

vid_capture = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence=0.8,
                       min_tracking_confidence=0.5)

tipIds = [4, 8, 12, 16, 20]


def count_fingers(image, hand_landmarks, handNo=0):
    fingers = []
    if hand_landmarks:
        landmarks = hand_landmarks[handNo].landmark
        # TODO: print the landmarks for the counted fingers

# defined a function to draw hand landmakrs on the image...


def draw_hand_landmarks(image, hand_landmarks):
    if hand_landmarks:
        image_width, image_height, c = image.shape
        for landmarks in hand_landmarks:
            mp_drawing.draw_landmarks(
                image, landmarks, mp_hands.HAND_CONNECTIONS)

            # getting the X coordinate of the ring finger tip.
            #x_cord_ring_finger = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x * image_width
            # getting the Y coordinate of the ring finger tip.
            #y_cord_ring_finger = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y * image_height

            #print(f'Ring finger tip coordinates: (',

                  #f'{x_cord_ring_finger}, '

                  #f'{y_cord_ring_finger})'
                  #)


while True:
    success, img = vid_capture.read()

    img = cv2.flip(img, 1)

    results = hands.process(img)
    hand_landmarks = results.multi_hand_landmarks

    draw_hand_landmarks(img, hand_landmarks)
    count_fingers(img, hand_landmarks)

    cv2.imshow("Image", img)

    key_Code = cv2.waitKey(1)

    if key_Code == 32:
        break

cv2.destroyAllWindows()

# TODO: WRITE A FOR LOOP TO ACCESS ALL THE FINGER TIPS FROM THE FINGER TIP ARRAY

