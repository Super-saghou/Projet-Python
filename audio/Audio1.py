from vidstream import AudioReceiver
from vidstream import AudioSender
import threading


receiver = AudioReceiver = AudioReceiver('192.168.1.4',6666)
receive_thread = threading.Thread(target=receiver.start_server)

sender = AudioSender('192.168.1.4',5555)
sender_thread = threading.Thread(target=sender.start_stream)

receive_thread.start()
sender_thread.start()