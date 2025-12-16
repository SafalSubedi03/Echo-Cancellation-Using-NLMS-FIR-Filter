import numpy as np
import sounddevice as sd
import soundfile as sf

sampling_rate = 44100

duration_u = 10
duration_v = 10

print("Recording u[n] ...")
un = sd.rec(int(duration_u * sampling_rate),
            samplerate=sampling_rate,
            channels=1,
            dtype='float32')
sd.wait()

max_val = np.max(np.abs(un))
if max_val > 0:
    un = un / max_val

sf.write("un.wav", un, sampling_rate, subtype="PCM_16")

# print("Recording v[n] ...")
# vn = sd.rec(int(duration_v * sampling_rate),
#             samplerate=sampling_rate,
#             channels=1,
#             dtype='float32')
# sd.wait()

# max_val = np.max(np.abs(vn))
# if max_val > 0:
#     vn = vn / max_val

# sf.write("vn.wav", vn, sampling_rate, subtype="PCM_16")

print("Recording completed.")
