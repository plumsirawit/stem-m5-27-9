import cv2
cap = cv2.VideoCapture(1)
f = open('counting.txt','r')
cnt = int(f.read().strip())
f.close()
while True:
  ret, frame = cap.read()
  rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
  cv2.imshow('Camera Screen', rgb)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    cv2.imwrite('plastic_bottle/' + str(cnt) + '.jpg',frame)
    cnt += 1
    f = open('counting.txt','w')
    f.write(str(cnt))
    f.write('\n')
    f.close()
cap.release()
cv2.destroyAllWindows()
