import yaml

from yaml import load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


if __name__ == '__main__':
    stream = open('test.yaml', 'r')
    dictionary = yaml.load(stream, Loader=Loader)
    for key, value in dictionary.items():
        print(key, value)