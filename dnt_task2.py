# Unsure of code, got from a senior.

import cv2

cap = cv2.VideoCapture('input_video.mp4')

fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output_video.mp4', fourcc, fps, (int(cap.get(3)), int(cap.get(4))))


count = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        count += 1
        if count % 4 != 0:
            out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
