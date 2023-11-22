import argparse
import os
import json
from pxr import Sdf, Usd


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
    rectify_USD_paths(config["USD_paths"], config["replacement_dict"])


def load_config(config_path):
    with open(config_path, 'r') as config_file:
        return json.load(config_file)


def config_help():
    print("Config files are in JSON format and store the path the the USDs and a hash table of the strings to replace.")
    print("Here is an example config file: \n")
    with open("example_config.json", 'r') as config_file:
        print(json.load(config_file))
    exit()


def rectify_USD_paths(USD_paths: list, replacement_dict: dict):
    ''' Replaces the paths in the USD paths with the new paths in the replacement dictionary. 
    Args: USD_paths (list): List of USD paths to be rectified.
        replacement_dict (dict): Dictionary of old paths strings (keys) to new paths strings (values).'''
    for USD_path in USD_paths:
        # Stage the USD or USDa
        try:
            stage = Usd.Stage.Open(USD_path)
        except Exception as e:
            print(f"Failed to stage USD @ {USD_path}: {e}")
            continue

        # Traverse all prims in the stage
        for prim in stage.TraverseAll():
            # Iterate through all attributes of the prim
            for attr in prim.GetAttributes():
                # Check if the attribute type is an Asset (used for file paths)
                if attr.GetTypeName() == Sdf.ValueTypeNames.Asset:
                    # Get the current value of the attribute as a string
                    current_value_str = str(attr.Get())
                    # Iterate through the replacement dictionary
                    for old_path, new_path in replacement_dict.items():
                        # Check and replace the old paths with the new paths in the attribute value
                        if old_path in current_value_str:
                            # Replace the old path with the new path
                            # USD will automatically "double" correct the @ so we need to remove them or we will get 4 @s instead of 1
                            new_value_str = current_value_str.replace(
                                old_path, new_path).replace("@", "")
                            # Convert the string back to an AssetPath and set it
                            new_value = Sdf.AssetPath(new_value_str)
                            attr.Set(new_value)
        # Resave the USD file
        stage.Save()


if __name__ == '__main__':
    main()
