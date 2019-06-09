# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 15:57:13 2019

Chat application, server part.

Implementation of a server which serves several clients using threading.

@author: HTH
"""

import socket
import threading

"""
Server setup, define sockets and port numbers
"""

"""
Server functions

(1): Accept connections: Create thread for each client
(2): Receive message from a single client
(3): Broadcast messages to clients
 
"""

"""
This function listens for incoming connections from clients.
When a client connects, it creates a new thread for this client
"""
def acceptConnection():
    
    pass


"""
This function listens for messages from clients
Each connected client thread runs one instance of this function.
This function sends the clients' message to all other clients using 
the broadcastMessage() function.
When the client types Quit, the thread is terminated.
"""
def receiveMessage():
    
    pass


"""
This function broadcasts messages to all clients
It is called from the receiveMessage function.
"""
def broadcastMessage():
    
    pass