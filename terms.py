import sys,subprocess
from subprocess import call

if len(sys.argv) > 1:
  command = []
  for value in range(1,len(sys.argv)):
    command.append(sys.argv[value])
  full_command = []
  for value in range(1,25):
    full_command = ['sudo','ttyecho','-n','/dev/tty'+str(value)]
    for string in command:
      full_command.append(string)
    p = subprocess.Popen(full_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output,error = p.communicate()
else:
  print "no command given"
