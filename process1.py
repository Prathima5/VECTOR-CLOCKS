from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

Process1_Connection_ = xmlrpc.client.ServerProxy("http://localhost:8810/") #client
vector_of_process1 = [0,0,0]
next_process = None

def input_parameter():

    loop = True
    while loop:
        start_node_process_id = int(input("enter the process from where the message needs to be delieved "))
        if start_node_process_id == 1:
            send()
        elif start_node_process_id == 2:
            Process2_Connection_ = xmlrpc.client.ServerProxy("http://localhost:8812/")
            Process2_Connection_.send()
        elif start_node_process_id == 3:
            Process3_Connection_ = xmlrpc.client.ServerProxy("http://localhost:8816/",)
            Process3_Connection_.send()
        loop = input("enter Y to continue or N to stop")
        if loop == 'N':
            print("hi")
            break
        elif loop == 'Y':
            loop = True
    return "Done"


def send():
    msg = input("enter the msg needed to be send")
    Process2_Connection_ = xmlrpc.client.ServerProxy("http://localhost:8812/")
    Process3_Connection_ = xmlrpc.client.ServerProxy("http://localhost:8816/")
    print("Broadcasting the message from the proccess 1")
    print("Vector Clock before sending the message : ",vector_of_process1)
    vector_of_process1[0] = vector_of_process1[0] + 1
    print("Vector Clock after sending the message :  ",[vector_of_process1[0],vector_of_process1[1],vector_of_process1[2]])
    Process2_Connection_.receive(vector_of_process1,msg)
    Process3_Connection_.receive(vector_of_process1,msg)
    return "Done"
    
def receive(vector,msg):
    print("In Process 1: Broadcasted Message received is ", msg)
    vector_of_process1[0] = vector_of_process1[0]+1 ##changed
    print("Vector Clock before receiving the message : ",vector_of_process1)
    vector_of_process1[0] = max(vector_of_process1[0],vector[0])
    vector_of_process1[1] = max(vector_of_process1[1],vector[1])
    vector_of_process1[2] = max(vector_of_process1[2],vector[2])
    print("Vector Clock after receiving the message : ", vector_of_process1)
    return "Done"

  
Process1_Server_Connection_= SimpleXMLRPCServer(("localhost",8810)) #server listening
print("Initially ", vector_of_process1)
Process1_Server_Connection_.register_function(send,"send")
Process1_Server_Connection_.register_function(receive,"receive")
Process1_Server_Connection_.register_function(input_parameter,"input_parameter")

input_parameter()
Process1_Server_Connection_.serve_forever()




