import numpy as np
import face_recognition as fr
import cv2

# Video capture through webcam
video_capture = cv2.VideoCapture(0)

# Loads the image in the directory and encodes it
parjan_image = fr.load_image_file('Parjan.jpg')
parjan_face_encoding = fr.face_encodings(parjan_image)[0]

# array that holds the face encodings
known_faces_encodings = [parjan_face_encoding]

# If I had more names we would just pass more in this array
known_face_names = ['Parjan']

# Set the threshold for face matching (adjust this value as needed)
threshold = 0.6

while True:
    ret, frame = video_capture.read()

    rgb_frame = frame[:, :, ::-1]

    face_location = fr.face_locations(rgb_frame)
    face_encodings = fr.face_encodings(rgb_frame, face_location)

    for (top, right, bottom, left), face_encodings in zip(face_location, face_encodings):

        matches = fr.compare_faces(known_faces_encodings, face_encodings, tolerance=threshold)

        name = 'Unknown'

        face_distance = fr.face_distance(known_faces_encodings, face_encodings)

        best_match_index = np.argmin(face_distance)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom - 35),
                      (right, bottom), (0, 0, 255), cv2.FILLED)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Webcam_face_recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
