import pickle
# import numpy as np

def predictPrice(data):
    pickled_model = pickle.load(open('model/model.pkl', 'rb'))
    # data = np.array([1.0, 3.0, 2.0, 0.12, 14.0, 9.0, 601.0, 920.0, 0.0])
    data = data.reshape(1, -1)

    prediction = pickled_model.predict(data)
    return prediction[0]
