from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import threading

Process1_Connection_ = xmlrpc.client.ServerProxy("http://localhost:8810/") #client
vector_of_process1 = [0,0,0]
next_process = None

def input_parameter():

    loop = True
    while loop:
        start_node_process_id = int(input("Sender Process Id"))
        end_node_process_id = int(input("Destination Process Id"))
        if start_node_process_id == 1:
            send(end_node_process_id)
        elif start_node_process_id == 2:
            Process2_Connection_ = xmlrpc.client.ServerProxy("http://localhost:8812/")           
            Process2_Connection_.send(end_node_process_id)
        elif start_node_process_id == 3:
            Process3_Connection_ = xmlrpc.client.ServerProxy("http://localhost:8816/")
            Process3_Connection_.send(end_node_process_id)
        loop = input("enter Y to continue or N to stop")
        if loop == 'N':
            Process1_Connection_.__close()
            break
        elif loop == 'Y':
            loop  = True
    return "Done"


def send(next_process):
    msg = input("enter the msg needed to be send")
    print("Sending the message from the proccess 1")
    print("Vector Clock before sending the message : ",vector_of_process1)
    vector_of_process1[0] = vector_of_process1[0] + 1
    if next_process == 1:
        print("Vector Clock after sending the message : ",vector_of_process1)
        receive(vector_of_process1,msg)
    elif next_process == 2:
        Process2_Connection_ = xmlrpc.client.ServerProxy("http://localhost:8812/") #client
        print("Vector Clock after sending the message : ",vector_of_process1)
        Process2_Connection_.receive(vector_of_process1,msg)
    elif next_process == 3:
        Process3_Connection_ = xmlrpc.client.ServerProxy("http://localhost:8816/") #client
        print("Vector Clock after sending the message : ",vector_of_process1)
        Process3_Connection_.receive(vector_of_process1,msg)
    return "Done"
    

def receive(vector,msg):
    vector_of_process1[0] = vector_of_process1[0]+1 
    print("Vector Clock before receiving the message : ",vector_of_process1)
    vector_of_process1[0] = max(vector_of_process1[0],vector[0])
    vector_of_process1[1] = max(vector_of_process1[1],vector[1])
    vector_of_process1[2] = max(vector_of_process1[2],vector[2])
    print("Vector Clock after receiving the message : ", vector_of_process1)
    print("Message received is ",msg)
    return "Done"

  
Process1_Server_Connection_= SimpleXMLRPCServer(("localhost",8810)) #server listening
print("Initially " ,vector_of_process1)
Process1_Server_Connection_.register_function(send,"send")
Process1_Server_Connection_.register_function(receive,"receive")
Process1_Server_Connection_.register_function(input_parameter,"input_parameter")

input_parameter()
Process1_Server_Connection_.serve_forever()




