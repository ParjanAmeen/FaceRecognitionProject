import cv2
import face_recognition

# Loading in the images from the ImageBasic directory and assigning them to variables
imgElon = face_recognition.load_image_file('ImageBasic/ElonMusk.jpg')
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('ImageBasic/ElonMuskTest.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

# Encodes the images from the ImageBasic directory and prints out rectangular box
faceLoc = face_recognition.face_locations(imgElon)[0]
encodeElon = face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon, (faceLoc[3], faceLoc[0]),
              (faceLoc[1], faceLoc[2]), (225, 0, 255), 2)

# Encodes the images from the ImageBasic directory and prints out rectangular box
faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]),
              (faceLocTest[1], faceLocTest[2]), (225, 0, 255), 2)

# Set the threshold for face matching (adjust this value as needed)
threshold = 0.6

# Compares two images and determines if they are a match. Prints out a true/false statement
results = face_recognition.compare_faces([encodeElon], encodeTest, tolerance=threshold)
faceDis = face_recognition.face_distance([encodeElon], encodeTest)
print(results, faceDis)
cv2.putText(imgTest, f'{results} {round(faceDis[0], 2)}',
            (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

# After running prints shows both images
cv2.imshow('ElonMusk', imgElon)
cv2.imshow('ElonMuskTest', imgTest)
cv2.waitKey(0)
