import numpy as np
import sounddevice as sd
import soundfile as sf

# Parameters
duration = 5
filename = 'my_recording.wav'
sampling_rate = 44100

# Record audio (mono)
print("Recording started...")
audio_data = sd.rec(int(duration * sampling_rate), samplerate=sampling_rate, channels=1, dtype='float32')
sd.wait()
print("Recording finished.")

# Normalize
max_val = np.max(np.abs(audio_data))
if max_val > 0:
    audio_data = audio_data / max_val

# Save as 16-bit WAV
sf.write(filename, audio_data, sampling_rate, subtype='PCM_16')
print(f"Audio saved to {filename}")
