import webbrowser
import gtts
import pyttsx3
from playsound import playsound
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit as kit

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
    engine = pyttsx.init()

    try:
        with sr.Microphone(1) as mic:
            # print(sr.Microphone.list_microphone_names())
            rec.adjust_for_ambient_noise(mic)  # faz o reconhecimento de ruido
            print("Diga algo: ")
            audio = rec.listen(mic)
            comando = rec.recognize_google(audio, language='pt-BR')
            comando = comando.lower()
            if 'jorginho' or 'jorges' or 'jorge' or 'filho' in comando:
                comando = executa_comando()
                if 'hora' or 'horas' in comando:
                    hora = datetime.datetime.now().strftime('%H:%M')
                    engine.say("Agora são" + hora)
                    engine.runAndWait()
                elif 'procure por' in comando:
                    procurar = comando.replace('procure por', '')
                    wikipedia.set_lang('pt')
                    resultado = wikipedia.summary(procurar, sentences=2)
                    engine.say(resultado)
                    engine.runAndWait()
                elif 'toque' in comando:
                    musica = comando.replace('toque', '')
                    resultado = kit.playonyt(musica)
                    engine.say('Tocando musica')
                    engine.runAndWait()
                    
    except:
        print("Não consegui reconhecer")

# get_audio_google()
# get_audio()
falar_com_jorginho()
# speak('Olá, tudo bem?')


