import os
from flask import Flask,request,Response,send_file
from PIL import Image,ImageDraw,ImageFont
import requests
import time
app = Flask(__name__)
#UPLOAD_DIR = '/tmp/upload'
UPLOAD_DIR = 'C:/Users/w00412055/Desktop/'
def allowed_file(file_name):
    return file_name.split('.')[-1] in ['jpg','JPG','jpeg','JPEG','png','PNG','gif','GIF']

def AddWaterMark(ImagePath):
    img = Image.open(ImagePath)
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    fillcolor = '#ff0000'
    draw.text((2,2), 'HUAWEI', font=myfont, fill=fillcolor)
    img.save('C:/Users/w00412055/Desktop/result.jpg', 'jpeg')
    return 'C:/Users/w00412055/Desktop/result.jpg'
    
@app.route('/upload_file',methods = ['GET','POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            ImagePath = os.path.join(UPLOAD_DIR,file.filename)
            file.save(ImagePath)
            filename = AddWaterMark(ImagePath)
            return send_file(filename,mimetype='image/jpeg')
        return "<p>file type not allowed!</p>"
    return '''
    <!DOCTYPE html>
    <title>Change new icon</title>
    <h1>Upload new </h1>
    <form action = "" method = "post" enctype=multipart/form-data>
        <input type = "file" name = file>
        <input type = "submit" value = Upload>
    </form>
    '''

  

if __name__ == '__main__':
    app.run(port=5001,debug=True)
