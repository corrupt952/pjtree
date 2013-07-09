# -*- utf-8 -*-


def scan(data, path):
    u""" Scan directory and files.

    If scan file is direcotry, Add dict.
    Otherwise Add string.

    @param data dict data.
    @param path file path.

    @return dict data.
    """
    import os
    import base64
    
    files = os.listdir(path)
    for f in files:
        f_path = os.path.join(path, f)
        if os.path.isdir(f_path):
            data[f] = scan({}, f_path)
        else:
            fi = open(f_path, 'r')
            data[f] = 'b64:' + base64.b64encode(fi.read())
            fi.close()
    return data


def show(data):
    u""" Save json file in data.

    Dict data dump to json file.
    @param data dict data.
    """
    import json

    print(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))

