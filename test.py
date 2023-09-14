import cv2
import pandas as pd

# filepath = ".mp4"
cap = cv2.VideoCapture(0)
# webカメラを使うときはこちら

avg = None
frameNo = 0
list_df = pd.DataFrame(columns = ['FrameNo','x','y','w','h','cx','cy','area'])
contour_count = 0
list = [0,0,0,0,0]

