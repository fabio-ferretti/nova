'''
V&A
@author: Fabio Ferretti
'''
import subprocess
import socket
import re
import os, sys

#Questo servizio deve essere in esecuzione in tutti i compute node

def listen_sleep_on_lan():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('',4312))
        buffersize = 256
        fpid = os.fork()
        if fpid!=0:
            while 1:
                pattern = re.compile("sleep_on_lan")
                data_received = sock.recvfrom(buffersize)
                result = pattern.search(data_received[0])
                if result is not None:
                    process = subprocess.Popen("sudo pm-suspend", shell=True, stdout=subprocess.PIPE)
    except:
        pass

if __name__ == '__main__':
    listen_sleep_on_lan()
