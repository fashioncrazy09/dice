#!/usr/bin/env python3

import argparse

from random import randint


class Player:
    def __init__(self, name, loop):
        self.name = name
        self.score = sum(randint(1, 6) for _ in range(loop))


def entry():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-n', help='the loop length (default 3)', dest='loop',
        action='store', default=3, type=int, choices=(1, 2, 3))
    parser.add_argument(
        '-p',
        nargs='+',
        help='participants, e.g. Name1 Name2 ... NameN',
        dest='play',
        action='store', required=True)

    return parser.parse_args()


def main():
    args = entry()
    print('Количество бросков кубика: {}'.format(args.loop))
    print('Игроки:')
    for i in args.play:
        print('\t', i)


if __name__ == '__main__':
    main()
