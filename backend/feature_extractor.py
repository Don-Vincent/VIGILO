import librosa
import numpy as np

def extract_features(file_path):
    try:
        y, sr = librosa.load(file_path, sr=None)
        if len(y) < 512:
            raise ValueError("Audio too short for feature extraction.")

        padded_length = 2 ** int(np.ceil(np.log2(len(y))))
        y = np.pad(y, (0, max(0, padded_length - len(y))), mode='constant')

        n_fft = max(512, min(2048, 2 ** int(np.floor(np.log2(len(y) // 70)))))
        hop_length = n_fft // 4

        y_harmonic = librosa.effects.harmonic(y) if len(y) > 2048 else y

        mel = librosa.feature.melspectrogram(y=y_harmonic, sr=sr, n_fft=n_fft, hop_length=hop_length)
        mfcc = librosa.feature.mfcc(y=y_harmonic, sr=sr, n_fft=n_fft, hop_length=hop_length, n_mfcc=13)
        contrast = librosa.feature.spectral_contrast(y=y_harmonic, sr=sr, n_fft=n_fft, hop_length=hop_length)
        chroma = librosa.feature.chroma_stft(y=y_harmonic, sr=sr, n_fft=n_fft, hop_length=hop_length)
        tonnetz = librosa.feature.tonnetz(y=y_harmonic, sr=sr)

        feature_vector = np.hstack([
            np.mean(contrast, axis=1),
            np.mean(tonnetz, axis=1),
            np.mean(chroma, axis=1),
            np.mean(mel, axis=1),
            np.mean(mfcc, axis=1)
        ])
        return feature_vector
    except Exception as e:
        return {"error": str(e)}
