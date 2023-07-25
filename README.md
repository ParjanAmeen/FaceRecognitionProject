# Real-Time Face Recognition (RealTimeFaceRecognition.py)(I used 3.10.5)

## Description
This Python program utilizes computer vision techniques to perform real-time face recognition. When executed, it opens up a window that accesses your camera and scans for faces in the live feed. The program then compares the detected face with an image stored in the program directory. If a match is found, it will display the name of the recognized person next to their head. If there is no match, the output will be displayed as "Unknown."

## How to Use
1. Ensure you have Python installed on your system (Python 3.6 or higher).
2. Install the required libraries by running the following command:
pip install numpy,
pip install face_recognition,
pip install opencv-python

3. If you run into issues downloading face_recognition make sure you have cmake intalled (pip install cmake) and then dlib(pip install dlib) and then try pip install face_recognition. If you still experience any issues try visiting this webpage https://stackoverflow.com/questions/70001837/problem-in-installing-python-library-face-recognition-on-windows-10-11 

4. Place the image of the person you want to recognize in the program directory. Name the image appropriately to match the person's name or any unique identifier. You have to change line 14 to the correct image file name and line 20 to the name of what you want on the webcam.

5. Execute the program by running the following command in the terminal or command prompt:
python RealTimeFaceRecognition.py

6. A window will open, displaying the live feed from your camera. The program will start scanning for faces.

7. If a face is detected and recognized, the name of the person will be displayed next to their head. If the face does not match any stored image, the output will be "Unknown."

8. Press 'q' to quit the program and close the camera window.



# Real-Time Face Recognition (Basics.py)(I used 3.10.5)

## Description
This Python program utilizes computer vision techniques to perform face matching. When executed, it opens up two windows. One for each image that you are testing with. If there is a match between the two images it will output True and next to it will be the face distance number which is how similar the faces are.

## How to Use
1. Ensure you have Python installed on your system (Python 3.6 or higher).
2. Install the required libraries by running the following command:
pip install face_recognition,
pip install opencv-python

3. If you run into issues downloading face_recognition make sure you have cmake intalled (pip install cmake) and then dlib(pip install dlib) and then try pip install face_recognition. If you still experience any issues try visiting this webpage https://stackoverflow.com/questions/70001837/problem-in-installing-python-library-face-recognition-on-windows-10-11 

4. Place the images you want to match in the ImageBasic folder. Name the image appropriately to match the person's name or any unique identifier. You will have to change lines 6 and 8 to the correct file image names.

5. Execute the program by running the following command in the terminal or command prompt:
python Basics.py

7. Two winodws will open. One for each image and an output of either true or false along with the face distance number
