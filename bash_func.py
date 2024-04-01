import subprocess
from decouple import config

base_dir = config('base_dir', default='~/')

def is_valid_linux_command(command):
    try:
        # Use subprocess to execute the command with the "--help" flag
        # This will not run the command but just check if it's valid
        # with open('file.txt', "w") as outfile:
        #     subprocess.run([*command], stdout=outfile)
        result = subprocess.run([*command, "--help"], shell=True, check=True, capture_output=True, text=True)

        return True
    except subprocess.CalledProcessError:
        return False

def run_command(command):
    input_command = command

    try:
        #subprocess.run(f"cd {base_dir}")
        result = subprocess.run([*input_command], check=False, capture_output=True, text=True)
        return result.stdout
    except:
        return "Unexpected Error"

def main():
    command = input("Enter a command to check: ").split()

    if is_valid_linux_command(command):
        print(f"{' '.join(command)} is a valid Linux command.")
        a = run_command(command)
        print(a)
    else:
        print(f"{command} is not a valid Linux command.")

if __name__ == "__main__":
    main()
