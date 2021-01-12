import os

pid = os.fork()

if pid == 0:
    print("this is child")
else:
    print("this is parent")