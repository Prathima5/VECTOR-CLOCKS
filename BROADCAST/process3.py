import os 
import os.path as fileChecker
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client


Process3_Connection_ = xmlrpc.client.ServerProxy("http://localhost:8816/") #client
vector_of_process3 = [0,0,0]

def input_parameter():
    start_node_process_id = int(input("enter the process from where the message needs to be delieved "))
    if start_node_process_id == 3:
        send()
    elif start_node_process_id == 2:
        Process2_Connection_ = xmlrpc.client.ServerProxy("http://localhost:8812/")
        Process2_Connection_.send()
    elif start_node_process_id == 1:
        Process1_Connection_ = xmlrpc.client.ServerProxy("http://localhost:8810/")
        Process1_Connection_.send()

    return "Done"
def send():
    msg = input("enter the msg needed to be send")
    Process2_Connection_ = xmlrpc.client.ServerProxy("http://localhost:8812/")
    Process1_Connection_ = xmlrpc.client.ServerProxy("http://localhost:8810/",allow_none=True)
    print("Broadcasting the message from the proccess 3")
    print("Vector Clock before sending the message : ",vector_of_process3)
    vector_of_process3[0] = vector_of_process3[2] + 1
    print("Vector Clock after sending the message :  ",[vector_of_process3[0],vector_of_process3[1],vector_of_process3[2]])
    Process1_Connection_.receive(vector_of_process3,msg)
    Process3_Connection_.receive(vector_of_process3,msg)
    return "Done"

def receive(vector,msg):
    vector_of_process3[2] = vector_of_process3[2] + 1
    print("Vector Clock before receiving the message : ",vector_of_process3)
    print(vector_of_process3)
    vector_of_process3[0] = max(vector_of_process3[0],vector[0])
    vector_of_process3[1] = max(vector_of_process3[1],vector[1])
    vector_of_process3[2] = max(vector_of_process3[2],vector[2])
    print("Vector Clock after receiving the message : ", vector_of_process3)
    return "done"

Server_Connection_ = SimpleXMLRPCServer(("localhost",8816)) #server listening
Server_Connection_.register_function(send,"send")
Server_Connection_.register_function(receive,"receive")
Server_Connection_.register_function(input_parameter,"input_parameter")
print("listening")
print(vector_of_process3)
Server_Connection_.serve_forever()
