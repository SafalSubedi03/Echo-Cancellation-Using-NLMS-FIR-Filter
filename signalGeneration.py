import numpy as np 
import soundfile as sf 


un,Fs = sf.read("un.wav")

#Echo Simulation Parameters
alpha =  0.9                      #echo attenuation
delay_in_s = 1
D = int(delay_in_s*Fs)              #how far the sample is delayed


dn = np.zeros(len(un) + D)
dn[:len(un)] = un
dn[D:] += alpha * un + 0.00 * np.random.randn(len(un)) #No bg noise for now 
filename = "dn"


if __name__ == "__main__":
    #dn will store the desired signal which will store the audio + echo + bg noise
    sf.write(f"{filename}.wav",dn,Fs)
    print(f"Output {filename}.wav file created successfully")