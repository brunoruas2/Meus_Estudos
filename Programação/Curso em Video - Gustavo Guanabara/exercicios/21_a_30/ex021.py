# Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
from pygame import mixer

mixer.init()
mixer.music.load(r'E:\bruno\Podcast\_Aberturas\analise_musical.mp3')
mixer.music.play()

# found a solution where https://stackoverflow.com/questions/20021457/playing-mp3-song-on-python