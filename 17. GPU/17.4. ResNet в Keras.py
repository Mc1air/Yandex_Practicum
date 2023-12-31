
from tensorflow import keras
from tensorflow.keras.layers import Conv2D, Flatten, Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet import ResNet50
optimizer = Adam(lr=0.0001)
import numpy as np

def load_train(path):
    datagen = ImageDataGenerator(rescale=1./255,
                               horizontal_flip=True,
                               vertical_flip=True,
                               rotation_range=90,
                               width_shift_range=0.2, 
                             )
    train_datagen_flow = datagen.flow_from_directory(path, 
                                                   target_size=(150, 150), 
                                                   batch_size=16, 
                                                   class_mode='sparse',
                                                   seed=12345)
    
 
  return train_datagen_flow

def create_model(input_shape):
    '''model = ResNet50(input_shape=None,
                   classes=1000,
                   include_top=True,
                   weights='imagenet')'''
    backbone = ResNet50(input_shape=(150, 150, 3),
                    weights='imagenet', 
                    include_top=False)

    model = Sequential()
    model.add(backbone)
    model.add(GlobalAveragePooling2D())
    model.add(Dense(12, activation='softmax')) 


    '''model.add(Conv2D(filters=6, kernel_size=(5, 5), padding='same', activation='relu', input_shape=input_shape))
    model.add(AvgPool2D(pool_size=(2, 2)))

    model.add(Conv2D(filters=16, kernel_size=(5, 5), padding='valid', activation='relu'))
    model.add(AvgPool2D(pool_size=(2, 2)))

    model.add(Conv2D(filters=16, kernel_size=(5, 5), padding='same', activation='relu'))
    model.add(AvgPool2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(keras.layers.Dense(units=120, activation='relu'))
    model.add(keras.layers.Dense(units=84, activation='relu'))
    model.add(keras.layers.Dense(units=12, activation='softmax'))'''
    
  
  model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['acc'])

    return model

def train_model(model, train_data, test_data, batch_size=None, epochs=2,
                steps_per_epoch=None, validation_steps=None):
    if steps_per_epoch is None:
    steps_per_epoch = len(train_data)
    if validation_steps is None:
    validation_steps = len(test_data) 
  
  model.fit(train_data,
            validation_data=test_data,
            batch_size=batch_size, epochs=epochs,
            steps_per_epoch=steps_per_epoch,
            validation_steps=validation_steps,
            verbose=2, shuffle=True)
  
  return model