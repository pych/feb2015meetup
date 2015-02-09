
import xmlrpclib

server = xmlrpclib.Server('http://localhost:9001/RPC2')

server.system.listMethods()
server.supervisor.getAllProcessInfo()
