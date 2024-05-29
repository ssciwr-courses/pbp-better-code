# not using context manager
# change the below code to use context manager
f = open("data/efield.t","r")
numbers = f.read()
f.close()

# for example for threads, databases, etc - for improved resource handling