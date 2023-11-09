import pickle
import numpy as np

def predictPrice():
    pickled_model = pickle.load(open('model.pkl', 'rb'))
    data = np.array([1.0, 3.0, 2.0, 0.12, 14.0, 9.0, 601.0, 920.0, 0.0]).reshape(1, -1)

    prediction = pickled_model.predict(data)
    print("Predicted Price:", prediction)

predictPrice()
