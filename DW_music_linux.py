from pytube import YouTube
import random
import string, random



def music(enlace):
    num = str(random.randint(0, 100))
    num1 = str(random.randint(1, 15))
    lett = random.choice(string.ascii_letters)
    id = lett + num + "_" + num1
    name = "Song_"+ id +".mp3" 
    video = YouTube(enlace)
    descarga = video.streams.get_audio_only()
    descarga.download(output_path='/home/dasl/Descargas', filename=name)

def video(enlace):
    num = str(random.randint(0, 100))
    num1 = str(random.randint(1, 15))
    lett = random.choice(string.ascii_letters)
    id = lett + num + "_" + num1
    name = "Video"+ id +".mp4" 
    video = YouTube(enlace)
    descarga = video.streams.get_highest_resolution()
    descarga.download(output_path='/home/dasl/Descargas', filename=name)



print("******************************\n")
print("Youtube Downloader\n")
print("******************************\n")
enlace = input("Ingrese un enlace: ")

print("Opciones:\n")
print("1) Descargar Video\n")
print("2) Descargar Audio\n")

op = int(input("Ingrese opcion: "))

if op == 1:
    video(enlace)
elif op == 2:
    music(enlace)    
