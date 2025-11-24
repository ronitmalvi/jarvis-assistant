import sounddevice as sd
import soundfile as sf

print("Recording 3 seconds...")
rec = sd.rec(3 * 16000, samplerate=16000, channels=1)
sd.wait()

sf.write("test.wav", rec, 16000)
print("Saved test.wav")
