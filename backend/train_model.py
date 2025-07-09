import numpy as np
import tensorflow as tf
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt
import os

DATA_PATH = "model"

def load_data(split):
    return np.load(f"{DATA_PATH}/X_{split}.npy"), np.load(f"{DATA_PATH}/y_{split}.npy")

X_train, y_train = load_data("train")
X_val, y_val = load_data("val")
X_test, y_test = load_data("test")

X_train = X_train[..., np.newaxis]
X_val = X_val[..., np.newaxis]
X_test = X_test[..., np.newaxis]

model = tf.keras.Sequential([
    tf.keras.layers.Conv1D(32, 3, activation='relu', input_shape=(X_train.shape[1], 1)),
    tf.keras.layers.Conv1D(32, 3, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.MaxPooling1D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
history = model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=20, batch_size=8)

model.save(os.path.join(DATA_PATH, "model_02.h5"))

# Evaluate
y_pred = np.argmax(model.predict(X_test), axis=1)
print(f"Test Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")

# Binary class evaluation
interest_class = 1
y_true_bin = [1 if y == interest_class else 0 for y in y_test]
y_pred_bin = [1 if y == interest_class else 0 for y in y_pred]

print(classification_report(y_true_bin, y_pred_bin))
sns.heatmap(confusion_matrix(y_true_bin, y_pred_bin), annot=True, fmt='d')
plt.show()
