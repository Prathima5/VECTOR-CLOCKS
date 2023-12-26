# VECTOR-CLOCKS

**Project Description:**

In this programming project, I developED an n-node distributed system that implements a vector clock. The distributed system uses a logical clock to timestamp messages sent/received among the nodes. To simplify the design and testing, the distributed system will be emulated using multiple processes on a single machine. Each process represents a machine and has a unique port number for communication.
Implement the vector clock for your distributed system. You can create two threads for each process, one for sending messages to other nodes and one for listening to its communication port. Communication among nodes can be done using RPC or using sockets. Once a process sends a message, it should print its vector clock before and after sending a message. Similarly, once a process receives a message, it should print its vector clock before and after receiving the message. You can assume that the number of processes (machines) is fixed (equal to or larger than 3) and processes will not fail, join, or leave the distributed system.

**Requirements**

● Python 3

● Visual Studio

**Getting Started**

Vector Clock is an algorithm that generates partial ordering of events and detects causality violations in a distributed system. These clocks expand on Scalar time to facilitate a causally consistent view of the distributed system, they detect whether a contributed event has caused another event in the distributed system. It essentially captures all the causal relationships. This algorithm helps us label every process with a vector(a list of integers) with an integer for each local clock of every process within the system. So for N given processes, there will be vector/ array of size N.

**Implementation Steps:**

● I have created two modules – unicast and broadcast.

● The unicast contains 3 Python files named as Process1, process2, process3.

● Each process contains send, receive and input parameter functions implemented using threads.

● For the Unicast process, the send function is used to unicast message to the user given process, and receive function is used to receive the message.

● The broadcast process sends messages to all the other processes.

● For Implementing we first have to execute the three files simultaneously.

● The process1 is the main process which has a main function which is used to decide the flow of the messages between the source and destination.

● In the unicact, a input parameter had to be provided which is source id and destination id also with what messages has to be sent.

● For the broadcast, only a process id is sufficient enough to send the messages to the other process.

● Example: If a message is unicasted from the process1 to process2. The process1 window ouputs about the vector clocks before and after sending the message. The process2 window outputs the vector clocks before and after receiving the message.

**Detailed Instructions to Execute Code**

● Reload the Whole Project in the Virtual Studio.

● Compile using commands in the command prompt.

● Change to the Process1 in the command prompt using the command

                                >cd directory\foldername\filename.

● Change to the Process2 in the command prompt using the command

                                >cd directory\foldername\filename.

● Change to the Process3 in the command prompt using the command

                                >cd directory\foldername\filename.

● To execute the process1, process2 and process3 run “Python filename.py” command in the command prompt.

**SNAPSHOTS OF THE PROJECT**

![image](https://github.com/Prathima5/VECTOR-CLOCKS/assets/154850398/4ea15d14-3b0c-4670-bf19-26b64c79b10b)

                        Img1:process 1 unicast msg to process 2

![image](https://github.com/Prathima5/VECTOR-CLOCKS/assets/154850398/677c8f86-b9da-437d-8201-c9417dc7d229)

                        Img2: process 2 unicast message to process 3
