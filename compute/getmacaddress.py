'''
@author: Fabio Ferretti
'''
import struct
import socket
import fcntl

def get_mac_address(interface):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', interface[:15]))
        return ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]
