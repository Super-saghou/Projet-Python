from vidstream import *
import tkinter as tk
import socket
import threading
import requests
local_ip_adress = socket.gethostbyname(socket.gethostname())
public_ip_adress = requests.get('https://api.ipify.org')
server = StreamingServer(local_ip_adress,6666)
receiver = AudioReceiver(local_ip_adress,7777)

def start_listening():
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=receiver.start_server)
    t1.start()
    t2.start()


def start_camera_stream():
    camera_client = CameraClient(text_target_ip.get(1.0,'end_1c'),8888)
    t3 = threading.Thread(target=camera_client.start_stream)
    t3.start()

def start_audio_stream():
    audio_sender = AudioSender(text_target_ip.get(1.0,'end-1c'),9999)
    t4 = threading.Thread(target=audio_sender.start_stream)
    t4.start()








window = tk.Tk()
window.title("Audio call 0.0.1")
window.geometry('300x200')
label_target_ip = tk.Label(window , text='Target IP')
label_target_ip.pack()
text_target_ip = tk.Text(window,height = 1)
text_target_ip.pack()


btn_listen = tk.Button(window , text='Start listening' , width = 50,command=start_listening)
btn_listen.pack(anchor=tk.CENTER,expand=True)

btn_camera = tk.Button(window , text='Start Video Call' , width = 50,command = start_camera_stream)
btn_camera.pack(anchor=tk.CENTER,expand=True)

btn_audio = tk.Button(window , text='Start audio call' , width = 50,command=start_audio_stream)
btn_audio.pack(anchor=tk.CENTER,expand=True)

window.mainloop ()