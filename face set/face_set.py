import cv2
cam = cv2.VideoCapture(0)
print("press 5 to save your fcae")
print("press q to quit")
while True:
    ret,frame = cam.read()
    if not ret:
        continue
    cv2.imshow("Register face",frame)
    key =cv2.waitKey(1)
    if key == ord('s'):
        cv2.imwrite("my_face.jpg",frame)
        print("face saved succesfully")
        break
    if key  == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()