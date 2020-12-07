from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix

from pre_processing import PreProcess


SRC_DIR = ''

data_process = PreProcess(SRC_DIR)
input_data_1 = data_process.process_image(low,high,max_length)

SRC_DIR = ''
data_process = PreProcess(SRC_DIR)
input_data_2 = data_process.process_image(low,high,max_length)

input_data_1.append(input_data_2)
imgdata = input_data_1
x = imgdata.drop('Class',axis = 1)
y = imgdata['Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)

svm_classifier = SVC(kernel='linear')
svm_classifier.fit(X_train, y_train)
y_pred = svclassifier.predict(X_test)
print(confusion_matrix(y_test,y_pred))