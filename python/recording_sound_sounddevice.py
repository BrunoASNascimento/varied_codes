import sounddevice as sd
from scipy.io.wavfile import write

print(sd.query_devices())
fs = 44100  # Sample rate
seconds = 5  # Duration of recording
sd.default.device = 1

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('data\output.wav', fs, myrecording)  # Save as WAV file
