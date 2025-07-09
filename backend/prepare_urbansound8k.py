import os
import shutil
import pandas as pd

# Paths
base_dir = 'audio_dataset/UrbanSound8K'
audio_dir = os.path.join(base_dir, 'audio')
csv_path = os.path.join(base_dir, 'metadata', 'UrbanSound8K.csv')
output_dir = 'audio_dataset/urban_classes'

# Create target folders
os.makedirs(output_dir, exist_ok=True)

# Load metadata
df = pd.read_csv(csv_path)

for index, row in df.iterrows():
    fold = f"fold{row['fold']}"
    file_name = row['slice_file_name']
    class_label = row['class'].replace(' ', '_').lower()  # e.g. "gun shot" → "gun_shot"
    
    src = os.path.join(audio_dir, fold, file_name)
    dst_folder = os.path.join(output_dir, class_label)
    os.makedirs(dst_folder, exist_ok=True)
    dst = os.path.join(dst_folder, file_name)
    
    try:
        shutil.copy(src, dst)
    except Exception as e:
        print(f"Failed to copy {src}: {e}")

print("✅ Dataset organized by class.")
