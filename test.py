#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
テスト用ダミーアプリです．

Usage:
  test.py [-c CONFIG]

Options:
  -c CONFIG     : CONFIG を設定ファイルとして読み込んで実行します．[default: config.yaml]
"""
import time
import pathlib
import os


def say(config):
    print(config["message"])


def abs_path(config_path):
    return pathlib.Path(os.getcwd(), config_path)


if __name__ == "__main__":
    from docopt import docopt
    import yaml

    args = docopt(__doc__)

    config_path = abs_path(args["-c"])
    with open(config_path, "r") as file:
        config = yaml.load(file, Loader=yaml.SafeLoader)
        while True:
            say(config)
            time.sleep(1)
