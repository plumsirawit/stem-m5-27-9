import sys
import serial
from google.cloud import automl_v1beta1
from google.cloud.automl_v1beta1.proto import service_pb2

prediction_client = automl_v1beta1.PredictionServiceClient.from_service_account_json('news.json')
params = {}
def get_prediction(content, project_id, model_id):
  name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
  payload = {'image': {'image_bytes': content }}
  request = prediction_client.predict(name, payload, params)
  return request  # waits till request is returned

def send_data(num):
  assert(isinstance(num,int))
  ser = serial.Serial('/dev/ttyUSB0',9600)
  ser.write(chr(num+48).encode())
  ser.close()
