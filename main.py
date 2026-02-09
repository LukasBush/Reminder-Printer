import config
import startup

def main():

    if not startup.start_app():
        print("Error in start up")
        return

    print("The program will now begin")
    print(config.GLOBAL_OFFSET)


if __name__ == "__main__":
    main()