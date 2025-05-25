
import speech_recognition as sr
tr = "çÇğĞıİöÖşŞüÜ"
en = "cCgGiIoOsSuU"
x_tr = str.maketrans(en,tr)

r = sr.Recognizer()

with sr.Microphone() as source:
    #r.adjust_for_ambient_noise(source)

    print("Konuşabilirsiniz (Çıkmak için Ctrl+C)...")
    while True:
        try:
            audio = r.listen(source, phrase_time_limit=3)
            text = r.recognize_google(audio, language = "tr-TR")
            print("Text: ",text)

            if 'hey' in text.lower():
                print('Komut moduna geçildi')
                audio_command = r.listen(source)
                command = r.recognize_google(audio_command, language = "tr-TR")
                command_tr = command.lower().translate(x_tr)
                if 'ışığı aç' in command_tr:
                    print('ışık açıldı')

        except sr.WaitTimeoutError:
            print("Dinleme süresi aşıldı, tekrar dinleniyor...")
            continue
        except sr.UnknownValueError:
            print("Anlaşılamayan ses, tekrar deneyin...")
        except sr.RequestError as e:
            print(f"API hatası: {e}")
        except KeyboardInterrupt:
            print('Dinleme manuel sonlandirildi')
            break

                
