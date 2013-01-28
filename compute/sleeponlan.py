'''
V&A
@author: Fabio Ferretti
'''
import socket

def sleep_on_lan(ipaddress):
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    sock.sendto("sleep_on_lan", (ipaddress,4312))        
    
if __name__ == '__main__':
    sleep_on_lan('192.168.1.3')