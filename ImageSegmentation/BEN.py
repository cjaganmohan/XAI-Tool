import os
import subprocess
from subprocess import Popen, PIPE, STDOUT


# reference - pass value for interactive jar file in shell script
#    -- https://unix.stackexchange.com/questions/440897/how-to-pass-value-for-interactive-jar-file-in-shell-script



#subprocess.call(['java', '-jar', './BEN.jar'])

# reference -- https://stackoverflow.com/questions/17257694/running-jar-files-from-python
def run_command(command):
    p = subprocess.Popen(command,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')

for output_line in run_command(['java', '-jar', './BEN.jar']):
    print(output_line)
