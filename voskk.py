import sounddevice as sd
import queue
import json
import sys
from vosk import Model, KaldiRecognizer
q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

model = Model("C:\\vosk-model-en-us-0.22-lgraph")
samplerate = 16000
rec = KaldiRecognizer(model,samplerate) # 16khz

with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=None,
                       dtype='int16', channels=1, callback=callback):
    print('Konuşmaya başlayabilirsin')
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            print(result.get('text'))
        else:
            partial = json.loads(rec.PartialResult())
            print(partial)
            
