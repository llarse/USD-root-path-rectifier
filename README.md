
# USD path rectifier tool

CLI tool for rectifying incorrect paths inside a USD file.  It works by traversing through all the asset argument paths and replacing any matched string with its replacement string. It also corrects for the autoformatting on export with USD. Can handle any USD-type file.





## Installation

Clone the project and install pxr or usd-core. This can cause issues for people and doesnt work beyond 3.10 due to the pxr package. For me, running a conda environment in python 3.10 and `pip install usd-core` was enough.     
## Usage/Examples

To run the code:

```
python USDrectifier.py -c path/to/config/file
```


The config file should look like this:
```
{
    "USDs": ["paths/to/USDs", "orPaths/to/USDas"],
    "remap_instructions": {"string to replace": "string to replace it with"}
}
```

You can also see the example config file using:

```
python USDrectifier.py -ch
```

#
While this is designed to be run from the command line, you can place it in a folder with an empty `__init__.py` file and import the main function as follows:

```
from USDrectifier import rectify_USD_paths

replacement_dictionary = {"stringSegmentToReplace": "stringSegmentToReplaceWith"}
usds = ["path/to/USD"]

rectify_USD_paths(usds, replacement_dictionary)
```