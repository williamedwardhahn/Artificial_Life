import base64
import json
import os

import cv2
import numpy as np
from flask import Flask, Response, request
import datetime

app = Flask(__name__)

image_dir = "./images"
if not os.path.isdir(image_dir):
    os.mkdir(image_dir)


@app.route('/save', methods=['POST'])
def save_image():
    data = request.data.decode('utf-8')
    data_json = json.loads(data)
    image = data_json['image']
    image_dec = base64.b64decode(image)
    data_np = np.frombuffer(image_dec, dtype='uint8')
    decimg = cv2.imdecode(data_np, 1)

    date_new = datetime.datetime.now().strftime('%y_%m_%d_%H:%M:%S')
    filename = f"./images/{date_new}.jpg"
    cv2.imwrite(filename, decimg)

    return Response(response=json.dumps({"message": "saved"}), status=200)



app.run(host="0.0.0.0",port=5000,debug = True)
