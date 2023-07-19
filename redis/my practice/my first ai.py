
import tensorflow as tf
from tensorflow.keras import layers

# Создание модели
model = tf.keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(784,)),
    layers.Dense(10, activation='softmax')
])

# Компиляция модели
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Загрузка и подготовка данных (пример MNIST)
mnist = tf.keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
train_images, test_images = train_images / 255.0, test_images / 255.0

# Обучение модели
model.fit(train_images, train_labels, epochs=5)

# Оценка точности модели
test_loss, test_acc = model.evaluate(test_images, test_labels)
print("Точность на тестовых данных:", test_acc)





