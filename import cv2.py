import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('Cedula.jpg')

face_coordinates = face_cascade.detectMultiScale(img)

#cv2.rectangle(image,  start_point,  end_point,  color,  thickness)

(x, y, w, h ) = face_coordinates[0]

cv2.rectangle(img,  (x, y), (x+w, y+h), (255, 255, 255), 2)

cv2.imshow('Cedula Identificaión',  img)

cv2.waitKey()

print ('Code Done')