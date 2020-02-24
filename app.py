import numpy as np
from flask import Flask, request, jsonify, render_template,redirect
import cv2
import os
app = Flask(__name__)

from os import listdir
from os.path import isfile, join



@app.route('/')
def home():
    return render_template('index.html')
app.config["UPLOADS"]="D:/chest train val deployment/uploads"
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    side=150
    if request.method=='POST':
        if request.files:
            x=request.files['image']
    #y=cv2.imread(x)
    
    x.save(os.path.join(app.config["UPLOADS"],x.filename))
    #print(y)
    #cv2.imshow('image',y)
    #cv2.waitKey(0)
    
    mypath="D:/chest train val deployment/uploads"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    
    def preprocess_image(img, side=150):    
        img = cv2.resize(img, (side,side))
        return img / 255.0
    def load_image(file_path):
        return cv2.imread(file_path)
    
    load_images = [load_image(file) for file in onlyfiles]
    eval_images = preprocess_image(load_images[0])
    print(eval_images)
    
    

    
    
    
    
    
    
    
    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format("hell"))


if __name__ == "__main__":
    app.run(debug=True)