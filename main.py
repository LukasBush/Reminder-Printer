import messages
import time
import startup

def main():
    successful_start_up = startup.start_app()

    if not successful_start_up:
        print("Error in start up")
        return

    print("The program will now begin")


if __name__ == "__main__":
    main()