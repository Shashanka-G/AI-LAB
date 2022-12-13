import time

def clean(floor,agent_pos):
    count = 0
    print()
    print("Ïnitial room status")
    print_floor(floor)
    agent_pos = (agent_pos-1) % len(floor)
    while count<len(floor):
        if all([x==0 for x in floor]):
            print()
            print("All rooms are cleaned")
            print()
            break
         # if room is dirty
        if floor[agent_pos] == 1:
            print() 
            print("Room {} is dirty. Agent is cleaning now".format(agent_pos+1))
            time.sleep(2.5)
            floor[agent_pos] = 0
            print_floor(floor)
            agent_pos = (agent_pos+1) % len(floor)
            count = count+1
        # If room is cleaned
        else:
            print("Room {} is already cleaned, going to next room".format(agent_pos+1))
            time.sleep(0.5)
            agent_pos = (agent_pos+1)%len(floor)
            count = count+1
    print("Destination state is reached")

def print_floor(floor):
    status_map = {0:"CLEAN",1:"DIRTY"}
    for i in range(len(floor)):
        print("Room {}".format(i+1),end='  ')
    print()
    for i in range(len(floor)):
        print(status_map[floor[i]],end='\t')
    print()

def main():
    #Entre initial condition
    floor = [None,None]
    print("Enter room status\nDirty-->1 Clean-->0")
    floor[0] = int(input("Enter status of room 1:"))
    floor[1] = int(input("Enter status of room 2:"))
    agent_pos = int(input("Enter agent position:"))
    clean(floor,agent_pos)

main()



------
OUTPUT
------


D:\Shashanka G\vaccume_cleaner>python vaccume_cleaner.py
Enter room status  
Dirty-->1 Clean-->0
Enter status of room 1:1
Enter status of room 2:1
Enter agent position:1

Ïnitial room status
Room 1  Room 2
DIRTY   DIRTY

Room 1 is dirty. Agent is cleaning now
Room 1  Room 2  
CLEAN   DIRTY

Room 2 is dirty. Agent is cleaning now
Room 1  Room 2  
CLEAN   CLEAN
Destination state is reached



D:\Shashanka G\vaccume_cleaner>python vaccume_cleaner.py
Enter room status  
Dirty-->1 Clean-->0
Enter status of room 1:1
Enter status of room 2:0
Enter agent position:2

Ïnitial room status
Room 1  Room 2
DIRTY   CLEAN
Room 2 is already cleaned, going to next room

Room 1 is dirty. Agent is cleaning now
Room 1  Room 2  
CLEAN   CLEAN
Destination state is reached
