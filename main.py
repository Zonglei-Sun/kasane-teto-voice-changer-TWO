import pyautogui
import os
import librosa
import numpy as np
import sounddevice as sd
import asyncio

from RealtimeSTT import AudioToTextRecorder
from random import choices
from string import (ascii_letters, digits)
from time import sleep

SAMPLE_RATE = 16000  # must match sd.rec and librosa

def hz_to_midi(f0_hz, default=80):
    # if f0_hz is None or f0_hz <= 0:
    #     return default
    return int(round(69 + 12 * np.log2(f0_hz / 440.0)))  # A4 = 440 Hz

def detect_pitch(recorder, duration=0.25):
    try:
        # record a short chunk from mic
        audio = sd.rec(
            int(duration * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="float32"
        )
        sd.wait()
        audio = audio.flatten()

        # optional pre-emphasis / normalization
        if np.max(np.abs(audio)) > 0:
            audio = audio / np.max(np.abs(audio))

        # librosa pitch estimation (pyin)
        f0, voiced_flag, _ = librosa.pyin(
            audio,
            fmin=librosa.note_to_hz("C2"),   # ~65 Hz
            fmax=librosa.note_to_hz("C6")    # ~1046 Hz
        )

        # use median voiced f0
        if f0 is None:
            return "62"  # default
        voiced_f0 = f0[voiced_flag]
        if len(voiced_f0) == 0:
            return "62"

        median_f0 = np.median(voiced_f0)
        midi_note = hz_to_midi(median_f0, default=62)

        # clamp to a sensible range (Teto-ish mid register)
        midi_note = max(60, min(72, midi_note))

        return str(midi_note)
    except Exception:
        # on any error, use a neutral tone
        return "62"

def generate_random_string(length=8):
    return ''.join(choices(ascii_letters + digits, k=length))

def replace_in_file(output_file, replacement_string, recorder):
    try:
        words = replacement_string.split()

        with open("templates\\template.txt", 'r', encoding='utf-8') as file:
            file_template = file.read()

        with open("templates\\word.txt", 'r', encoding='utf-8') as file:
            speech_template = file.read()

        updated_content = file_template
        with open(f"temp\{output_file}", 'w', encoding='utf-8') as output_file:
            total_dur = 0
            for i in range(len(words)):
                segment = speech_template

                segment = segment.replace("POS__", str(total_dur))

                segment = segment.replace("WORD__", words[i])

                words[i] = words[i].replace(".","") \
                    .replace(",","") \
                    .replace("?","") \
                    .replace("!","") \
                    .replace("'","")
                
                duration = len(words[i])*100
                segment = segment.replace("DUR__", str(duration))
                
                total_dur = total_dur + duration

                segment = segment.replace("TONE__", detect_pitch(recorder)) #<------  line that changes tone, very important
                
                updated_content = updated_content + "\n" + segment
            
            updated_content = updated_content + "\nwave_parts: []"
            output_file.write(updated_content)

    except Exception as e:
        print(f"An error occurred: {e}")

def play(file):
    path = os.path.abspath(f"temp\{file}")

    pyautogui.hotkey('ctrl', 'o')
    sleep(1)
    pyautogui.typewrite(path)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('space')
    os.remove(path)

if __name__ == '__main__':
    print("Wait until it says 'speak now'")

    recorder = AudioToTextRecorder(language="en")
    
    
    while True:
        text = recorder.text()
        print(text)
        output_file = f'{generate_random_string()}.ustx'
        replace_in_file(output_file, text, recorder)
        play(output_file)