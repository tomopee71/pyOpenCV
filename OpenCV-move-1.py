import cv2
cap = cv2.VideoCapture(0)
# 使用するコーディックを指定
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# 動画ファイル名と設定
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
while cap.isOpened():
    # カメラからフレームをキャプチャー
    ret, frame = cap.read()
    if not ret:
        break
    # フレームを動画に書き込む
    out.write(frame)
    # フレームを表示する
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # リソースの解放
cap.release()
out.release()
cv2.destroyAllWindows()

