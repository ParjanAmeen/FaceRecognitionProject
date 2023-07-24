# Real-Time Face Recognition (RealTimeFaceRecognition.py)

## Description
This Python program utilizes computer vision techniques to perform real-time face recognition. When executed, it opens up a window that accesses your camera and scans for faces in the live feed. The program then compares the detected face with an image stored in the program directory. If a match is found, it will display the name of the recognized person next to their head. If there is no match, the output will be displayed as "Unknown."

## How to Use
1. Ensure you have Python installed on your system (Python 3.6 or higher).
2. Install the required libraries by running the following command:
pip install opencv-python
pip install opencv-python-headless
pip install opencv-contrib-python

Note: These libraries provide the necessary tools for face detection and recognition.

3. Place the image of the person you want to recognize in the program directory. Name the image appropriately to match the person's name or any unique identifier.

4. Execute the program by running the following command in the terminal or command prompt:
python RealTimeFaceRecognition.py

5. A window will open, displaying the live feed from your camera. The program will start scanning for faces.

6. If a face is detected and recognized, the name of the person will be displayed next to their head. If the face does not match any stored image, the output will be "Unknown."

7. Press 'q' to quit the program and close the camera window.
