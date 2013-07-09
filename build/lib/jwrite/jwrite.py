# -*- utf-8 -*-


def load_json(path, encode):
    u""" Loading json.

    Loading json file.

    @param path   json file path.
    @param encode file encode.

    @return dict
    """
    import json
    import codecs

    fi = codecs.open(path, 'r', encode)
    data = json.load(fi)
    fi.close()

    return data


def trace(data, path):
    u""" Trace directory or files.

    If data type is Dict, create directory.
    Otherwise, create empty file.

    @param data dict or str
    @param path file path
    """
    import os

    if isinstance(data, dict):
        make_file(path,  None)
        for k, v in data.items():
            trace(v, os.path.join(path, k))
    else:
        make_file(path,  data)


def make_file(path, url):
    u""" Making directory or file.

    Making directory or file.
    path is making file path.
    data is download file url.

    @param path str
    @param url  str
    """
    import os
    import re

    if os.path.exists(path):
        print('Already exists %s.' % path)
    elif url == None:
        print('Make %s.' % path)
        os.mkdir(path)
        print('%s Done.' % path)
    elif re.match('url:', url):
        import urllib
        print('make %s.' % path)
        url = url.replace('url:', '')
        urllib.urlretrieve(url, path)
        print('%s done.')
    elif re.match('b64:', url):
        import base64
        print('Make %s.' % path)
        f = open(path, 'w')
        url = url.replace('b64:', '')
        f.write(base64.b64decode(url))
        f.close()
        print('%s Done.' % path)
    else:
        print('make %s.' % path)
        f = open(path, 'w')
        f.write(url)
        f.close()
        print('%s done.')

