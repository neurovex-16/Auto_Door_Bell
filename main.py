import cv2
import face_recognition
import pygame
import threading
 
pygame.mixer.init()
cap=cv2.VideoCapture(0)
sound_played=False

def ring_bell():
    pygame.mixer.music.load("Audio/doorbell.wav")
    pygame.mixer.music.play()
while True:
    ret,frame = cap.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = face_recognition.face_locations(rgb_frame)
    if faces and not sound_played:
        threading.Thread(target=ring_bell).start()
        sound_played=True
    elif not faces and sound_played:
        sound_played=False
    cv2.imshow('Smart Doorbell',frame)
    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
