import argparse
import os
import json

# I'm going to start with a shell of how this will work from the console.


def main():
    parser = argparse.ArgumentParser()
    # Parse the CLI arguments
    parser.add_argument('-c', '--config_path',
                        help='Path to the config file')
    parser.add_argument('-ch', '--config_help',
                        help='An Example config file', action='store_true')
    args = parser.parse_args()

    # Handle invalid CLI calls
    if args.config_help:
        config_help()
    if args.config_path is None:
        config_help()

    config = load_config(args.config_path)
    print(config)


def load_config(config_path):
    with open(config_path, 'r') as config_file:
        return json.load(config_file)


def config_help():
    print("Config files are in JSON format and store the path the the USDs and a hash table of the strings to replace.")
    print("Here is an example config file: \n")
    with open("example_config.json", 'r') as config_file:
        print(json.load(config_file))
    exit()


if __name__ == '__main__':
    main()
