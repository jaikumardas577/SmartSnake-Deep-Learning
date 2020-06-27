from tensorflow import keras
import pandas as pd

# loading the model
model = keras.models.load_model('training/models/my_model-version1.1')

# print(model)
print(model)
# testing the model

d = {"L1": [0.1],"L2":[0.2],"L3":[0.3],"L4":[0.8],"Gradient":[-0.0]
        ,"Orientation": [0.000000]}
d_ =  pd.DataFrame(data = d)

predict_ = model.predict(test1)

print(predict_)