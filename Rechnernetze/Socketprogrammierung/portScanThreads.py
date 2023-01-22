# -*- coding: utf-8 -*-
"""
Created on Tue May 17 12:42:38 2022

@author: simon
"""

import socket # for connecting
from colorama import init, Fore
from threading import Thread, Lock
from queue import Queue
import sys


N_THREADS = 200
q = Queue()
print_lock = Lock()

        
def scan_thread():
    global q
    while True:
        worker = q.get()
        udpScan(host, worker)
        try:
            s = socket.socket()
            s.connect((host, worker))
        except:
            with print_lock:
                print(f"{host}:{worker} is closed ")
        else:
            with print_lock: 
                print(f"{host}:{worker} is open")
        finally:
            s.close()
        q.task_done() 
        
def main(host, ports):
    global q
    for t in range(N_THREADS):
        t = Thread(target=scan_thread)
        t.start()
    for worker in ports:
        q.put(worker)
    q.join()
    
    
def udpScan(host,worker):
       try:
          consock = socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
          consock.connect((host,worker))
          print ("UDP Port Open: " + str(worker))
       except:
          print ("UDP port closed: " + str(worker))
    
if __name__ == "__main__":
    start_port = 1
    end_port = 50
    ports = [p for p in range(start_port, end_port)]
    host = '141.37.168.26'
    main(host, ports)
    
    