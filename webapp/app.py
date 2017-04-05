import os,uuid
from flask import Flask,request,Response,send_file
from PIL import Image,ImageDraw,ImageFont
app = Flask(__name__)

def allowed_file(filename):
    return filename.split('.')[-1] in ['jpg','JPG','jpeg','JPEG','png','PNG','gif','GIF']

def AddWaterMark(filename):
    img = Image.open(filename)
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('./BASKVILL.TTF', size=20)
    fillcolor = '#ff0000'
    draw.text((2,2), 'HUAWEI', font=myfont, fill=fillcolor)
    watermarked_file = uuid.uuid1().hex + filename
    img.save(watermarked_file, 'jpeg')
    return watermarked_file
    
@app.route('/upload_file',methods = ['GET','POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            file.save(file.filename)
            filename = AddWaterMark(file.filename)
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

@app.route('/health')
def health_check():
    return 'ok'
  
@app.route('/')
def health_check():
    return 'Hello'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
