import os 
import os.path as fileChecker
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client


Process2_Connection_ = xmlrpc.client.ServerProxy("http://localhost:8812/") #client
vector_of_process2 = [0,0,0]

def input_parameter():
    start_node_process_id = int(input("Sender Process Id"))
    end_node_process_id = int(input("Destination Process Id"))
    if start_node_process_id == 2:
        send(end_node_process_id)
    elif start_node_process_id == 1:
        Process1_Connection_ = xmlrpc.client.ServerProxy("http://localhost:8810/")
        Process1_Connection_.send(end_node_process_id)
    elif start_node_process_id == 3:
        Process3_Connection_ = xmlrpc.client.ServerProxy("http://localhost:8816/")
        Process3_Connection_.send(end_node_process_id)

def send(next_process):
    msg = input("enter the msg needed to be send")
    print("Sending the message from the proccess 2")
    print("Vector Clock before sending the message : ",vector_of_process2)
    vector_of_process2[1] = vector_of_process2[1]+1
    print("Vector Clock after sending the message :  ",vector_of_process2)

    if next_process == 1:
        Process1_Connection_ = xmlrpc.client.ServerProxy("http://localhost:8810/") #client
        Process1_Connection_.receive(vector_of_process2,msg)

    elif next_process == 2:
        Process2_Connection_ = xmlrpc.client.ServerProxy("http://localhost:8812/") #client
        receive(vector_of_process2,msg)

    elif next_process == 3:
        Process3_Connection_ = xmlrpc.client.ServerProxy("http://localhost:8816/") #client
        Process3_Connection_.receive(vector_of_process2,msg)
    return "Done"

def receive(vector,msg):
    vector_of_process2[1] = vector_of_process2[1] + 1
    print("Vector Clock before receiving the message : ",vector_of_process2)
    vector_of_process2[0] = max(vector_of_process2[0],vector[0])
    vector_of_process2[1] = max(vector_of_process2[1],vector[1])
    vector_of_process2[2] = max(vector_of_process2[2],vector[2])
    print("Vector Clock after receiving the message : ", vector_of_process2)
    print("Message received is ",msg)
    return "Done"


Server_Connection_ = SimpleXMLRPCServer(("localhost",8812)) #server listening
Server_Connection_.register_function(send,"send")
Server_Connection_.register_function(receive,"receive")
Server_Connection_.register_function(input_parameter,"input_parameter")
print("listening")
print("Initially " ,vector_of_process2)
Server_Connection_.serve_forever()


