from lib import *
file_path = 'img.jpg'
project_id = 'news-201704'
model_id = 'ICN2537684054848942050'
THRESH = 64
THRESH_C = 20000
import cv2
cap = cv2.VideoCapture(1)
import numpy
mask = {'plastic_bottle' : 1, 'paper_cup' : 2, 'aluminum_can' : 3, 'plastic_cup' : 4, 'snack' : 5}
last = None
act = -1
while True:
  ret, frame = cap.read()
  grs = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
  smsk = numpy.multiply(grs > THRESH,grs)
  cv2.imshow('Camera Screen', rgb)
  c = 0
  if last is None:
    last = frame
  else:
    c = (grs <= THRESH).sum()
  print('[INFO]',c)
  if act == -1:
    if c > THRESH_C:
      act = 0
  else:
    act += 1
  if cv2.waitKey(1) & 0xFF == ord('q') or act > 50:
    out = cv2.imwrite(file_path, frame)
    with open(file_path, 'rb') as ff:
      content = ff.read()
    #print(get_prediction(content, project_id, model_id))
    raw = get_prediction(content, project_id, model_id).payload
    if len(raw) == 0:
      send_data(0)
    else:
      dat = raw[0].display_name
      send_data(mask[dat])
    act = -100
    print('Sent',dat)
cap.release()
cv2.destroyAllWindows()
