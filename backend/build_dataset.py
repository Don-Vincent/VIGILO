import os
import numpy as np
from feature_extractor import extract_features
from sklearn.model_selection import train_test_split

# Change this to match your dataset directory
DATA_DIR = 'audio_dataset/urban_classes'

X = []
y = []
label_map = {}
class_folders = sorted(os.listdir(DATA_DIR))  # Ensure consistent class ordering

print("📁 Starting dataset processing...")

for label_index, class_name in enumerate(class_folders):
    folder_path = os.path.join(DATA_DIR, class_name)
    if not os.path.isdir(folder_path):
        continue

    label_map[label_index] = class_name
    print(f"🔍 Processing '{class_name}' as class {label_index}...")

    for file in os.listdir(folder_path):
        if file.endswith(".wav"):
            file_path = os.path.join(folder_path, file)
            features = extract_features(file_path)

            if isinstance(features, dict) and "error" in features:
                print(f"⚠️ Skipping {file}: {features['error']}")
                continue

            X.append(features)
            y.append(label_index)

X = np.array(X)
y = np.array(y)

print(f"✅ Finished feature extraction: {X.shape[0]} samples.")
print(f"🔢 Classes: {label_map}")

# Save label map
os.makedirs("model", exist_ok=True)
np.save("model/label_map.npy", label_map)

# Split dataset
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, stratify=y_temp, random_state=42)

# Save .npy files
np.save("model/X_train.npy", X_train)
np.save("model/y_train.npy", y_train)
np.save("model/X_val.npy", X_val)
np.save("model/y_val.npy", y_val)
np.save("model/X_test.npy", X_test)
np.save("model/y_test.npy", y_test)

print("💾 Dataset saved to 'model/' folder.")
