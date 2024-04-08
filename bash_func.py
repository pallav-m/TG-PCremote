import subprocess
from decouple import config

import logging

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)



# def is_valid_linux_command(command):
#     try:
#         # Use subprocess to execute the command with the "--help" flag
#         # This will not run the command but just check if it's valid
#         # with open('file.txt', "w") as outfile:
#         #     subprocess.run([*command], stdout=outfile)
#         result = subprocess.run([*command, "--help"], shell=True, check=True, capture_output=True, text=True)
#
#         return True
#     except subprocess.CalledProcessError:
#         return False


def run_command(command):
    input_command = command

    try:
        subprocess.run('cd ~', shell=True)
        #passing the command as a string, hence shell=True
        result = subprocess.run(input_command, check=False, capture_output=True, text=True, shell=True)
        logging.info(result.stdout)
        logging.info(result.stderr)
        if(result.stderr == ''):
            return result.stdout
        else:
            return result.stderr
    except:
        return "Unexpected Error"



