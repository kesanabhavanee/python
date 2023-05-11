import subprocess
new=open("log.txt","w")
subprocess.check_call(["python","files.py"],stdout=new)

