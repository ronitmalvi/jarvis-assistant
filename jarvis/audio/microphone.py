import sounddevice as sd
import numpy as np
import librosa

def record(seconds=4):
    sr_original = 44100  # better recording quality
    print("🎤 Recording...")
    audio = sd.rec(int(seconds * sr_original),
                   samplerate=sr_original,
                   channels=1,
                   dtype="float32")
    sd.wait()
    print("✔ Recording complete.")

    # Resample to 16000 Hz for Whisper
    audio_16k = librosa.resample(audio.flatten(), orig_sr=sr_original, target_sr=16000)

    return audio_16k.astype("float32"), 16000
