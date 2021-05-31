import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' 

import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
print(tf.config.list_physical_devices('GPU'))

print(tf.test.is_built_with_cuda())

# import tensorflow.keras
# from tensorflow.keras import models, layers, optimizers
# import numpy as np

# # Create some fake data
# x = np.linspace(1, 2, 200)
# y = (x * 8) + (np.random.randn(x.shape[0]) * 0.5)

# # Examine data
# print('x:', x)
# print('y:', y)

# # Plot the data
# import matplotlib.pyplot as plt
# plt.plot(x, y, 'k.')
# plt.show()

# # Build model
# model = models.Sequential()
# model.add(layers.Dense(1, input_dim=1, activation='linear'))

# # Get initial, untrained weights
# print(model.layers[0].get_weights())

# # Configure training process
# model.compile(optimizer=optimizers.SGD(), loss='mse', metrics=['mse'])

# # Train model
# model.fit(x, y, batch_size=1, epochs=50, shuffle=False)

# # Try predicting 1 value
# model.predict([1.1])

# # Plot fitted line versus actual data
# y_pred = model.predict(x)
# plt.plot(x, y, 'k.', x, y_pred, 'b')
# plt.show()

# # Get trained weights
# print(model.layers[0].get_weights())

tf.__version__
import keras
keras.__version_