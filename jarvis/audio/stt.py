from faster_whisper import WhisperModel
import numpy as np
import os

# Windows MKL fix
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# Use a better model for accuracy
model = WhisperModel("base", device="cpu")

def transcribe(audio, sr):
    # Ensure float32
    audio = audio.astype(np.float32)

    # Only use supported arguments
    segments, _ = model.transcribe(
        audio,
        language="en",
        beam_size=1
    )

    text = "".join([seg.text for seg in segments])
    return text.strip()
