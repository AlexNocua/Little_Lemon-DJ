import speech_recognition as sr

import os
from PLN import ouvir_microphone


def ouvir_microphone():
    microfone = sr.Recongnizer()

    with sr.Microphone() as source:
        microfone.sr.adjust_for_ambient_noise(source)
        print('Fale alguma coisa')
        audio = microfone.liste(source)

    try:
        frase = microfome.recongnize_google(audio, language='pt-BR')
        if 'navegador' in frase:
            os.system('start chorome.exe')
            return False
        elif 'Excel' in frase:
            os.system('start Excel.exe')
        else:
            print('Aconteceu alfguma coisa')

    except:
        print('Aconteceu algum erro na frase e a leitura da mesma')
        
    return False

while True:
    if ouvir_microphone():
        break
