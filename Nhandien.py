
# train_model.py
from keras import Input, layers
from keras.models import Model
from keras.datasets import mnist
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# Tải và chuẩn bị dữ liệu
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_val, y_val = x_train[50000:60000, :, :], y_train[50000:60000]
x_train, y_train = x_train[:50000], y_train[:50000]

# Định dạng lại và chuẩn hóa dữ liệu đầu vào
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1).astype('float32') / 255
x_val = x_val.reshape(x_val.shape[0], 28, 28, 1).astype('float32') / 255
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1).astype('float32') / 255

# Chuyển nhãn thành dạng one-hot encoding
y_train = keras.utils.to_categorical(y_train)
y_val = keras.utils.to_categorical(y_val)
y_test = keras.utils.to_categorical(y_test)

# Xây dựng mô hình
input_tensor = Input(shape=(28, 28, 1))
x = layers.Conv2D(32, (3, 3), activation='relu')(input_tensor)
x = layers.Conv2D(64, (3, 3), activation='relu')(x)
x = layers.MaxPooling2D(2)(x)
x = layers.Flatten()(x)
x = layers.Dense(128, activation='relu')(x)
x = layers.Dense(10, activation='softmax')(x)

model = Model(inputs=input_tensor, outputs=x)

model.summary()

# Biên dịch mô hình
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Huấn luyện mô hình
h = model.fit(x_train, y_train, batch_size=32, epochs=20, validation_data=(x_val, y_val), verbose=1)

# Lưu mô hình đã huấn luyện
model.save('mnist_model.h5')

plt.plot(h.history['accuracy'])
plt.plot(h.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.show()

plt.imshow(x_test[0].reshape(28, 28), cmap='gray')
plt.show()
y_predict = model.predict(x_test[50].reshape(1, 28, 28, 1))

# In ra xác suất dự đoán của mô hình
print(y_predict)

# In ra nhãn được dự đoán (là chỉ số của xác suất lớn nhất)
print(np.argmax(y_predict))
