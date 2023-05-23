import cv2
import easyocr
from flask import Flask
from flask import request
import numpy as np
from imageio import imread
import base64
import io

app = Flask(__name__)



@app.route("/")
def say_hello():
    return f"Hello Mister!"


@app.route("/opencv", methods = ['POST'])
def hello():
    data = request.json.get('data')
    # print(data)

    image_path = './data/test4.png'
    text_list=[]

    # img = cv2.imread(image_path)
    
    nparr = np.fromstring(base64.b64decode(data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # instance text detector
    reader = easyocr.Reader(['en'], gpu=False)

    # detect text on image
    text_ = reader.readtext(img)
    
    for t_, t in enumerate(text_):

        bbox, text, score = t
        text_list.append(text)
    return text_list




if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
# read image




# image_path = './data/test4.png'
# text_list=[]

# img = cv2.imread(image_path)

# # instance text detector
# reader = easyocr.Reader(['en'], gpu=False)

# # detect text on image
# text_ = reader.readtext(img)


# threshold = 0.25
# # draw bbox and text
# for t_, t in enumerate(text_):

#     bbox, text, score = t
#     text_list.append(text)
    
# print(text_list)
