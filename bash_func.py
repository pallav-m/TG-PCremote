import subprocess

def is_valid_linux_command(command):
    try:
        # Use subprocess to execute the command with the "--help" flag
        # This will not run the command but just check if it's valid
        subprocess.run([command[0], "--help"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    command = input("Enter a command to check: ").split()

    if is_valid_linux_command(command):
        print(f"{command} is a valid Linux command.")
    else:
        print(f"{command} is not a valid Linux command.")

if __name__ == "__main__":
    main()
