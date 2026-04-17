# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:51:06 2026

@author: nix
"""

import socket

HOST = "192.168.0.30"
PORT = 5000


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Q:*RST")
    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Q:*IDN?")
    data = s.recv(4096)
    print(data.decode())    

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))    
    # Deshabilitar modulación
    s.sendall(b'Q:MOD:STATE OFF')
    
    # Configurar frecuencia
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Q:FREQ:CW 436.51 MHz')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))    
    # Configurar amplitud
    s.sendall(b'Q:AMPLITUDE:CW -60 dBm')

    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Q:SYST:REF:FREQ EXT10MHZ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))    
    # Habilitar RF
    s.sendall(b'Q:RFOutput:STATE ON')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))    
    s.sendall(b"Q:SYST:REF:FREQ?")
    data = s.recv(4096)
    print(data.decode())    
