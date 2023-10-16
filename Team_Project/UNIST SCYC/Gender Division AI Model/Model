```python
import os
import tensorflow as tf
import keras
from tensorflow import keras
from keras.callbacks import EarlyStopping
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn-white")
import os
import shutil
from keras.preprocessing import image
import cv2
```

```python
img_train_male = "dataset/Training/male"
img_train_female = "dataset/Training/female"
img_valid_male = "dataset/Validation/male"
img_valid_female = "dataset/Validation/female"
size = 64
```

```python
def preprocess_image(img_path):
    img = keras.utils.load_img(img_path, target_size=(size,size))
    tensor = keras.utils.img_to_array(img)
    tensor /= 255.0 
    return tensor
```

```python
categories = ["male", "female"]
nb_class = len(categories)
x = []
y = []

# variables to test the face with a mask
test_on_male_x = []
test_on_male_y = []

# variables to test the face with a mask
test_female_x = []
test_female_y = []
```

```python
#a=0
# preprocess the images, each of which is a face with mask
for i in os.listdir(img_train_male):
    img_path = os.path.join(img_train_male, i)
    img_tensor = preprocess_image(img_path)
    x.append(img_tensor)
    y.append(0)
 #   if a < 10:
 #       print ("len\[x\]:  %d" % len(x) )
 #   a=a+1
```

```python
# preprocess the images, each of which is a face without mask
for i in os.listdir(img_train_female):
    img_path = os.path.join(img_train_female, i)
    img_tensor = preprocess_image(img_path)
    x.append(img_tensor)
    y.append(1)
```

```python
x = np.array(x)
y = np.array(y)
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.1)
Y_train = keras.utils.to_categorical(Y_train, 2)
Y_test = keras.utils.to_categorical(Y_test, 2)
```

```python
model = keras.models.Sequential()
model.add(keras.layers.Conv2D(32, kernel_size=(3, 3), padding="same", activation="relu", input_shape=(size, size, 3)))

model.add(keras.layers.BatchNormalization())

model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))

model.add(keras.layers.Flatten())

model.add(keras.layers.Dense(128, activation="relu"))
model.add(keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(64, activation="relu"))
model.add(keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(2, activation="softmax"))

print(model.summary())
```

```python
model.compile(optimizer="sgd", loss="hinge", metrics=["accuracy"])
```

```python
model.fit(X_train, Y_train, epochs=5, validation_split=0.1)
```

```python
# evaluate a deep learning model
prediction = model.predict(X_test)
loss, acc = model.evaluate(X_test, Y_test, verbose=2)
```

```python
# draw images with accuracies and labels
topCnt = 8 *10
if len(X_test) < topCnt:
    topCnt = len(X_test)
    
plt.figure(figsize=(15,15))
for idx in range(topCnt):
    plt.subplot(8, 10, idx+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(X_test[idx], cmap=plt.cm.binary)
    
    if prediction[idx][0] > prediction[idx][1]:
        label = "Male " + str(int(prediction[idx][0] * 100)) + " %"
    else:
        label = "Female " + str(int(prediction[idx][1] * 100)) + " %"
    plt.xlabel(label)
plt.show()
```
