import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

engine.setProperty("rate", 180)
engine.setProperty("volume", 1.0)


def falar(texto):
    engine.say(texto)
    engine.runAndWait()


def ouvir():
    reconhecedor = sr.Recognizer()

    with sr.Microphone() as source:

        print("🎤 Ouvindo...")

        reconhecedor.adjust_for_ambient_noise(
            source,
            duration=1
        )

        audio = reconhecedor.listen(source)

    try:
        texto = reconhecedor.recognize_google(
            audio,
            language="pt-BR"
        )

        return texto

    except:
        return None
    
    ctk.CTkButton(
    frame,
    text="🎤",
    command=usar_microfone
).pack(side="left", padx=5)