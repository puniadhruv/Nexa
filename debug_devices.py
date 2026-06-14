import sounddevice as sd
from scipy.io.wavfile import write

fs = 16000
seconds = 5
device_index = 1  # Change to your working mic index

print("🎤 Speak now...")
recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, device=device_index)
sd.wait()
write("audio.wav", fs, recording)
print("✅ Recorded and saved as audio.wav")
