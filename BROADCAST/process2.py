from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client


Process2_Connection_ = xmlrpc.client.ServerProxy("http://localhost:8812/") #client
vector_of_process2 = [0,0,0]

def input_parameter():
    start_node_process_id = int(input("enter the process from where the message needs to be delieved "))
    if start_node_process_id == 2:
        send()
    elif start_node_process_id == 1:
        Process1_Connection_ = xmlrpc.client.ServerProxy("http://localhost:8810/")
        Process1_Connection_.send()
    elif start_node_process_id == 3:
        Process3_Connection_ = xmlrpc.client.ServerProxy("http://localhost:8816/")
        Process3_Connection_.send()
    return "Done"

def send():
    msg = input("enter the msg needed to be send")
    Process3_Connection_ = xmlrpc.client.ServerProxy("http://localhost:8816/")
    Process1_Connection_ = xmlrpc.client.ServerProxy("http://localhost:8810/")
    print("Broadcasting the message from the proccess 1")
    print("Vector Clock before sending the message : ",vector_of_process2)
    vector_of_process2[0] = vector_of_process2[0] + 1
    print("Vector Clock after sending the message :  ",[vector_of_process2[0],vector_of_process2[1],vector_of_process2[2]])
    Process3_Connection_.receive(vector_of_process2,msg)
    #Process1_Connection_.receive(vector_of_process2,msg)
    return "Done"

def receive(vector,msg):

    print("In Process 2: Broadcasted Message received is ", msg)
    vector_of_process2[1] = vector_of_process2[1]+1 ##changed
    print("Vector Clock before receiving the message : ",vector_of_process2)
    vector_of_process2[0] = max(vector_of_process2[0],vector[0])
    vector_of_process2[1] = max(vector_of_process2[1],vector[1])
    vector_of_process2[2] = max(vector_of_process2[2],vector[2])
    print("Vector Clock after receiving the message : ", vector_of_process2)
    return "Done"

Server_Connection_ = SimpleXMLRPCServer(("localhost",8812)) #server listening
Server_Connection_.register_function(send,"send")
Server_Connection_.register_function(receive,"receive")
Server_Connection_.register_function(input_parameter,"input_parameter")

print("listening")
print("Initially ", vector_of_process2)
Server_Connection_.serve_forever()


