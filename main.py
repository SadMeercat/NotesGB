
import console

if __name__ == '__main__':
    console.printManual()
    while True:
        command = input("Type command: ")
        if command == "exit":
            break
        console.userTalk(command)
