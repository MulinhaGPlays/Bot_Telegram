import webbrowser
import gtts
from playsound import playsound
import pyttsx3
import speech_recognition as sr


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def get_audio():
    with open('ReconhecimentoPorVoz/texto.txt', 'r') as arquivo:
        for linha in arquivo:
            frase = linha.strip()
            gtts.gTTS(
                text=frase, lang='pt-br').save('ReconhecimentoPorVoz/audio.mp3')
            playsound('ReconhecimentoPorVoz/audio.mp3')


def get_audio_google():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Fale algo: ')
        audio = r.listen(source)
        frase = r.recognize_google(audio, language='pt-BR')
        print(frase)
        with open('ReconhecimentoPorVoz/texto.txt', 'w') as arquivo:
            arquivo.write(frase)


def falar_com_jorginho():
    rec = sr.Recognizer()

    try:
        with sr.Microphone(1) as mic:
            # print(sr.Microphone.list_microphone_names())
            rec.adjust_for_ambient_noise(mic)  # faz o reconhecimento de ruido
            print("Diga algo: ")
            audio = rec.listen(mic)
            comando = rec.recognize_google(audio, language='pt-BR')
            comando = comando.lower()
            if 'jorginho' in comando:
                if 'navegador' in comando:
                    print('Abrindo navegador')
                    webbrowser.open('https://www.google.com')

    except:
        print("Não consegui reconhecer")


# get_audio_google()
get_audio()
# falar_com_jorginho()
