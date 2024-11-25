import cv2
from cv2 import aruco

# Initialize the ArUco dictionary
dictionary = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)

# Create a blank image for testing
import numpy as np
frame = np.ones((500, 500, 3), dtype=np.uint8) * 255

# Detect markers (should return empty since there are no markers in this example)
corners, ids, rejected = aruco.detectMarkers(frame, dictionary)

print(f"Detected corners: {corners}")
print(f"Detected IDs: {ids}")
