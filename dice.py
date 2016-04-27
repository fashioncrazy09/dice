#!/usr/bin/env python3

import argparse

from random import randint


class Player:
    def __init__(self, name, loop):
        self.name = name
        self.score = sum(randint(1, 6) for _ in range(loop))


class Game:
    def __init__(self, names, loop):
        if len(names) == 1:
            names.append('Machine')
        self.players = [Player(name, loop) for name in names]


def count_scores(players):
    win = max(i.score for i in players)
    block = max(len(i.name) for i in players) + 2
    for i in players:
        print("{}:{:>{}}".format(i.name, i.score, block-len(i.name)))
    return [i.name for i in players if i.score == win]


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
    game = Game(args.play, args.loop)
    winners = count_scores(game.players)
    while True:
        if len(winners) == 1:
            print('\nCongrats {}!'.format(winners[0]))
            break
        else:
            print('\nNo winner, one more throw:')
            game = Game(winners, args.loop)
            winners = count_scores(game.players)


if __name__ == '__main__':
    main()
