from ECEntry import ECEntry


def main():
    while True:
        try:
            cmd = input("EC> ")
            cmd = cmd.split()
            if cmd[0] == 'load':
                load(cmd[1])
            elif cmd[0] == 'quit':
                print("exiting")
                break
            else:
                print("invalid command!")
                continue
        except Exception as e:
            # https://newbedev.com/print-an-error-message-python-in-red-code-example
            print(f"\033[38;2;{255};{255};{0}m{repr(e)} \033[38;2;255;255;255m")
            continue


# Load the file as input.
def load(file_path):
    ECEntry.load(file_path)


if __name__ == "__main__":
    main()
