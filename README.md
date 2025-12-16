# Adaptive Noise Cancellation (ANC) Project
## Overview
This project is all about **removing unwanted noise from audio signals** using Python. It can record your voice, simulate or add noise, and then apply an **adaptive filter** to clean it up.
Along the way, it shows you plots of the original, filtered, and error signals, and saves the processed audio so you can listen to it.

---

## Features
* Record audio directly from your microphone.
* Produces three main outputs:

  * **Filtered signal (`y[n]`)** – the cleaned-up audio
  * **Error signal (`e[n]`)** – what the filter couldn’t remove
  * **Original input (`u[n]`)** – your raw recording
  * * **Original input (`d[n]`)** – echo added to the raw recording u[n]
* Saves audio files (`yn.wav` and `error.wav`) for playback.
* Plots all signals so you can see how well the filter works.
* Easy to tweak filter settings like length, step size, and sampling rate.

---

## Getting Started
First, make sure you have all the necessary Python packages. You can install them using:
```bash
pip install -r requirements.txt
```
---

## File Structure
Here’s what the project looks like:
```
ANC_Project/
├── main.py              # The adaptive filter in action
├── signalGeneration.py  # Generates or simulates input signals
├── RecordYourVoice.py   # Records audio from your microphone
├── requirements.txt     # All dependencies
├── yn.wav               # Filtered output (generated)
├── error.wav            # Error signal (generated)
└── README.md            # This file
```

---

## How to Use It

### 1. Record your audio

```bash
python RecordYourVoice.py
```

This will record your voice as the input signal `u[n]` and save it as `un.wav`.

### 2. Run the adaptive filter

```bash
python signalGeneration.py
```

* The script adds synthetic echo to the input singal u[n]
* It generates `dn.wav` (the echoed audio).


---

### 3. Run the adaptive filter

```bash
python main.py
```

* The script applies the **NLMS filter** to your recording.
* It generates `yn.wav` (the cleaned audio) and `error.wav` (the remaining noise).
* It also shows plots of:

  * Your original recording
  * The filtered audio
  * The error signal

---

## How It Works

1. Record or generate an input signal `u[n]`.
2. Generate a desired signal `d[n]` 
3. The NLMS filter iteratively adjusts its weights to aproximate `y[n]` to the `u[n]` part of the signal `d[n]`
4. The result is a filtered signal that is the signal with removed echo.
 

---



## Tweakable Parameters

* **M** – The filter length (number of taps).
* **mu_max, mu_min** – Maximum and minimum step size for the adaptive filter.
* **Fs** – Sampling rate (samples per second).

---


Do you want me to do that?
