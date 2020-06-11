# importing all libraries
import io
import h5py
import pandas as pd
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
from sklearn.model_selection import train_test_split
from keras.models import model_from_json
import os


# Creating The model

model = Sequential()
model.add(Dense(64, activation='relu', input_dim=6))   #adding layer
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(4, activation='softmax'))

# reading the file
data = pd.read_csv('data.csv')

y = data["Move"]
data  = data.iloc[:,[0,1,2,3,4,5]]

X_train, X_test, y_train, y_test = train_test_split(data, y, test_size=0.2)
y_train =  keras.utils.to_categorical(y_train, num_classes=4)
y_test =  keras.utils.to_categorical(y_test, num_classes=4)

# sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

score = model.evaluate(X_test, y_test, batch_size=128)



# Predicting The Test
model.predict(X_test)

# Saving The Model
model.save('D:\TensorFlowEnv\SmartSnake-Deep-Learning')

# import tempfile
# new_file, filename = tempfile.mkstemp()
# model_json = model.to_json()
# os.write(new_file,bytes(model_json, 'utf-8') )
# os.close(new_file)
# file1 = drive.CreateFile({'title': 'Modelnew.json'})
# file1.SetContentFile(filename)
# file1.Upload()
