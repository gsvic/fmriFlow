import nibabel as nbl
import pickle
import ast

import matplotlib.pyplot as plt


def visualizeNifti(path, t, slice):
    data = nbl.load(path).get_data()
    n = len(data[0,0,0,:])
    series = []

    for i in range(0, n):
        series.append(data[:,:,:,i])

    print type(series[10])

    plt.imshow(series[t][slice,:,:])
    plt.show()

def predict(model, vector):
    with open(model, 'rb') as inModel:
        m = pickle.load(inModel)
        cluster = m.predict(ast.literal_eval(vector))
        print cluster
        return cluster