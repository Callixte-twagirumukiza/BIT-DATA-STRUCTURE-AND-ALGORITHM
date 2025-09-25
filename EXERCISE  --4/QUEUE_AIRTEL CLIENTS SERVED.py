#CLients at AIRTEL Line to be served
from collections import deque
queue =deque(["Client1", "Client2", "Client3", "Client4", "Client5", "Client6"])
#Serve two
queue.popleft()
queue.popleft()
#the next client
print("Next client:", queue[0])
