import cv2
import os
# カレントディレクトリー取得
path = os.getcwd()
print(path)
from datetime import datetime
# 動画ファイルの読み込み
cap = cv2.VideoCapture(0)

while True:
    # 画像を読み込めた場合bool値　trueを返す
    ret, frame = cap.read()
    # 画像ファイルの表示
    cv2.imshow("camera",frame)
    
    k = cv2.waitKey(1)&0xff
    if k == ord('s'):
        date = datetime.now().strftime("%y%m%d_%H%M%S")
        path = "./img/"+date+".png"
        # 画像ファイルの保存
        cv2.imwrite(path,frame)
        # 画像ファイルの表示
        cv2.imshow(path, frame)
    elif k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
