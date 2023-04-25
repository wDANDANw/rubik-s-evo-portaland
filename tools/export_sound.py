import pyxel
import numpy as np
from pydub import AudioSegment

pyxel.init(160, 120)
pyxel.load("test.pyxres")

def generate_sine_wave(frequency, duration, sample_rate=44100):
    samples = (np.sin(2 * np.pi * np.arange(sample_rate * duration) * frequency / sample_rate)).astype(np.float32)
    return samples

def save_sound_to_wav(sound, file_name):
    num_notes = len(sound.notes)

    samples = []
    for i in range(num_notes):
        note = sound.notes[i]
        tone = sound.tones[i % len(sound.tones)]
        volume = sound.volumes[i % len(sound.volumes)]
        effect = sound.effects[i % len(sound.effects)]

        if note >= 0:
            frequency = 440.0 * 2**((note - 33) / 12)  # Convert note to frequency
            duration = 10 / 60  # duration in seconds
            sine_wave = generate_sine_wave(frequency, duration)
            sample = AudioSegment(sine_wave.tobytes(), frame_rate=44100, sample_width=4, channels=1)
            gain = 20 * np.log10(volume / 7)  # Convert linear volume to dB
            sample = sample.apply_gain(gain)  # Apply volume
            samples.append(sample)

    if samples:
        audio = sum(samples)
        audio.export(file_name, format="wav")
    else:
        print("No samples to export")

for i in range(30):
    save_sound_to_wav(pyxel.sound(i+1), f"clip_{i+1}.wav")