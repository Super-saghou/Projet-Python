from vidstream import *
import tkinter as tk
import socket
import threading
import time

local_ip_adress = socket.gethostbyname(socket.gethostname())




def start_camera_stream():
    receiving = StreamingServer('192.168.1.4',7777)
    sending = CameraClient('192.168.1.4',7777)

    t1 = threading.Thread(target=receiving.start_server)
    t1.start()

    time.sleep(2)

    t2 = threading.Thread(target=sending.start_stream)
    t2.start()

    while input("") != "STOP":
        continue

    receiving.stop_server()
    sending.stop_stream()




def start_audio_stream():
    receiver = AudioReceiver('192.168.1.4',5555)
    receive_thread = threading.Thread(target=receiver.start_server)

    sender = AudioSender('192.168.1.4',6666)
    sender_thread = threading.Thread(target=sender.start_stream)

    receive_thread.start()
    sender_thread.start()








window = tk.Tk()
window.title("Audio call 0.0.1")
window.geometry('300x200')
label_target_ip = tk.Label(window , text="Target IP:")
label_target_ip.pack()
text_target_ip = tk.Text(window,height = 1)
text_target_ip.pack()




btn_camera = tk.Button(window , text="Start Video Call" , width = 50,command = start_camera_stream)
btn_camera.pack(anchor=tk.CENTER,expand=True)


btn_audio = tk.Button(window , text="Start audio call" , width = 50,command=start_audio_stream)
btn_audio.pack(anchor=tk.CENTER,expand=True)

window.mainloop ()