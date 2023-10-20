import os
from tensorflow import keras
import tensorflow as tf
import time
import imageio
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image


# 데이터를 떠먹여 줄 클래스를 제작합니다.
class DataReader():
    def __init__(self):
        (self.train_X, _), (_, _) = keras.datasets.fashion_mnist.load_data()
        self.train_X = self.preprocess(self.train_X)
        self.train_dataset = tf.data.Dataset.from_tensor_slices(self.train_X).shuffle(50000).batch(256)
        
    def preprocess(self, images):
        images = images.reshape(images.shape[0], 28, 28, 1).astype('float32')
        images = images / 127.5 - 1
        return images

    def show_processed_images(self):
        plt.figure(figsize=(10, 10))
        for i in range(25):
            plt.subplot(5, 5, i + 1)
            plt.xticks([])
            plt.yticks([])
            plt.grid(False)
            plt.imshow(self.train_X[i])
        plt.show()
