from servlets import *

__version__ = "0.1.0"


"""Broadworks NS Portal Overview
===================

The Network Server portal application programming interface (API)constitutes 
a set of commands based on Hypertext Transfer Protocol(HTTP) requests, which
allows a portal server to communicate with the Network Server.  The interface 
consists of commands that are used to query the Network Server based on 
user information. The command interface is built upon the HTTP protocol.  
A client application sends an HTTP-based portal API requestto the BroadWorks
web portal running on the Network Server.

The Network Server Provisioning Server (PS) processes the request and returns 
the response to the BroadWorks web portal, which then returns an HTTP response 
to the client.
To prevent unauthorized portal API requests, the Network Server maintains an 
access control list that contains the only addresses from which portal API
requests are accepted. Support of the portal API over Hypertext Transfer 
Protocol Secure Sockets (HTTPS) is currently not offered"""


