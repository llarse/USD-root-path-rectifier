import argparse
import os

# I'm going to start with a shell of how this will work from the console.


def main():
    # Parse the CLI arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-help', '-h', '--help', action='store_true')
    parser.add_argument('-c', '-config', '--config_path',
                        help='Path to the config file')
    args = parser.parse_args()

    # Handle invalid CLI calls
    if args.help:
        config_help()
    if args.config_path is None:
        config_help()


def config_help():
    print("Here is an example config file: \n")
    with open("example_config.json", 'r') as config_file:
        print(config_file.read())
    exit()


if __name__ == '__main__':
    main()
