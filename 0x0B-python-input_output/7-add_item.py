#!/usr/bin/python3
"""A script that stores arguments to a JSON file."""
import sys
import os
from importlib import import_module as using


save_to_json_file, load_from_json_file = (
    using('5-save_to_json_file').save_to_json_file,
    using('6-load_from_json_file').load_from_json_file
)
args_list = []
file_name = 'add_item.json'


def makeScript():
    if not os.path.exists(file_name):
        with open(file_name, mode='w', encoding='utf-8') as file:
            file.write('[]')
    json_list = load_from_json_file(file_name)
    if (type(json_list) is list) and all(type(s) is str for s in json_list):
        args_list.extend(json_list)
    args_list.extend(sys.argv[1:])
    save_to_json_file(args_list, file_name)


if __name__ == '__main__':
    makeScript()
