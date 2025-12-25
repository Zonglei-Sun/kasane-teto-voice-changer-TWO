from RealtimeSTT import AudioToTextRecorder
import pyttsx3
import asyncio




async def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)

    try:
        engine.endLoop()
    except:
        pass
    text = text.replace(",", "")
    engine.say(text)
    engine.runAndWait()
    del engine

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
    