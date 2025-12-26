from RealtimeSTT import AudioToTextRecorder
import pyttsx3
import asyncio
from pygame import mixer
import os
import random
import string
import time



mixer.init(devicename="CABLE Input (VB-Audio Virtual Cable)")


def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def speak_sync(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)

    try:
        engine.endLoop()
    except:
        pass
    text = text.replace(",", "")
    name = f"{generate_random_string()}.wav"

    engine.save_to_file(text,name)
    #engine.say(text)
    engine.runAndWait()
    engine.stop()

    time.sleep(0.1)

    mixer.music.load(name)
    mixer.music.play()

    while mixer.music.get_busy():
        time.sleep(0.1)

    mixer.music.unload()
    os.remove(name)

async def speak(text: str):
    await asyncio.to_thread(speak_sync, text)

async def main():
    while True:
        print("Wait until it says 'speak now'")
        recorder = AudioToTextRecorder(language="en")
        text = recorder.text()
        print(text)


        if text.strip():  # Only speak if text detected
            await speak(text)


       
if __name__ == '__main__':
    asyncio.run(main())