#!/usr/bin/python3.7
# -*- coding: UTF-8 -*-

import os


def discover(initial_path):
    extensions = [
        # file system
        'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw',  # images
        'mp3', 'mp4', 'm4a', 'aac', 'ogg', 'flac', 'wav', 'wma', 'aiff', 'ape',  # audios
        'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpg', 'mpeg', 'wvm', 'swf', '3gp',  # videos
        'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx',  # microsoft office
        'yml', 'yaml', 'json', 'xml', 'csv',  # files config
        'db', 'sql', 'bdf', 'mdb', 'iso',  # data base
        'go', 'py', 'pyc', 'bf', 'coffee',  # other data in font code
        'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css', 'ts', 'tsx'  # web technologies
                                                                                'c', 'cpp', 'cxx', 'hpp', 'hxx',
        # font code C and C++
        'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak'  # zip files
    ]

    for dir_path, dirs, files in os.walk(initial_path):
        for _file in files:
            absolute_path = os.path.abspath(os.path.join(dir_path, _file))
            ext = absolute_path.split('.')[-1]
            if ext in extensions:
                yield absolute_path


if __name__ == '__main__':
    x = discover(os.getcwd())

    for i in x:
        print(i)
