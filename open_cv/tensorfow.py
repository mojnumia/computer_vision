import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D,MaxPool2D, BatchNormalization
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import CategoricalCrossentropy,MeanAbsoluteError,MeanSquaredLogarithmicError
import numpy as np
x=np.array([1,2,4,5,6])

# complementary labels

def generate_compl_labels(labels):
    # args, labels: ordinary labels
    K = np.max(labels)+1
    candidates = np.arange(K)
    candidates = np.repeat(candidates.reshape(1, K), len(labels), 0)
    mask = np.ones((len(labels), K), dtype=bool)
    mask[range(len(labels)), labels] = False
    candidates_ = candidates[mask].reshape(len(labels), K-1)  # this is the candidates without true class
    idx = np.random.randint(0, K-1, len(labels))
    complementary_labels = candidates_[np.arange(len(labels)), np.array(idx)]
    return complementary_labels
