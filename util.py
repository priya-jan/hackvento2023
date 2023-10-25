import cvlib as cv
from cvlib.object_detection import draw_bbox
from numpy.lib.polynomial import poly
import cv2
import streamlit as st
#for prediction
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import time


def load(path):
    # img= cv2.imread(path)
    # img = path
    img = cv2.imread(path)
    img1= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    '''plt.figure(figsize=(10,10)) #setting figure size
    plt.imshow(img1)
    plt.show()'''
    fig = plt.figure(figsize=(5,5)) 
    plt.axis('off')
    plt.imshow(img1)
    st.pyplot(fig)

def show_box(path):
    # img = path
    img = cv2.imread(path)
    box, label, count= cv.detect_common_objects(img)
    output= draw_bbox(img, box, label, count)
    output= cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
    fig = plt.figure(figsize=(5,5)) #setting figure size
    plt.axis('off')
    plt.imshow(output)
    st.pyplot(fig)

def pred(path):
    
    img = cv2.imread(path)
    # img = path
    boxes, labels, _ = cv.detect_common_objects(img)
    label_counts = {}
    for label in labels:
        if label not in label_counts:
            label_counts[label] = 1
        else:
            label_counts[label] += 1
    for label, count in label_counts.items():
        st.success(f'{label}: {count}')
    st.success('total no of vehicles:',sum(label_counts.values()))
    return sum(label_counts.values())

def pred(path):
    weight = {'bus':3, 'truck':3 , 'motorcycle':1 , 'car':2}
    weight_label = ['bus','truck','motorcycle','car']
    
    img = cv2.imread(path)
    boxes, labels, _ = cv.detect_common_objects(img)
    label_counts = {}
    label_weights = {}
    for label in labels:
        if label not in weight_label:
            continue
        elif label not in label_counts:
            label_counts[label] = 1
            label_weights[label] = 1*weight[label]
        else:
            label_counts[label] += 1
            label_weights[label] += 1*weight[label]
    
    for label, count in label_counts.items():
        st.success(f'{label}: {count}')
    st.success(f'Total no of vehicles: {sum(label_counts.values())}')
    st.success(f'Total Labeled weights: {sum(label_weights.values())}')
    return sum(label_weights.values())

def time_pred(weight):
    if weight <= 10:
        st.success('Green Signal Time:  15')
        time1 = 15
    elif  weight  <= 30:
        st.success('Green Signal Time: 35')
        time1 = 35
    elif weight  <= 60:
        st.success('Green Signal Time: 50')
        time1 = 50
    elif weight  <= 85:
        st.success('Green Signal Time: 70')
        time1 = 70
    else:
        st.success('Green Signal Time: 90')
        time1 = 90
    
    timer_text = st.empty()  # Create an empty element to display the timer
    for i in range(time1, 0, -1):
        timer_text.text('Green Signal Time: {}'.format(i - 1))
        time.sleep(1)
    st.error('STOP')