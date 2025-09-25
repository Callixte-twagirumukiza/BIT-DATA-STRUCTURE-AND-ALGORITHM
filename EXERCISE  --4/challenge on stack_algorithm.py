#start with empty stack
#push x,y,z→stack becomes [x,y,z]
stack=["x","y","z"]
#pop once → removes z,stack becomes [x,y]
stack.pop()
#push w → stack becomes [x,y,w]
stack.append("w")
#top item is w
print("top itm is:",stack[-1])
