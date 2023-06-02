import subprocess

p = subprocess.Popen('./start_server.sh', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in iter(p.stdout.readline, b''): 
    print(line)
    # TODO: send log to database
retval = p.wait()
print("\n\nServer exited with return value: " + str(retval))
