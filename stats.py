from contextlib import contextmanager
from typing import Counter


def count_words(contents):
    words_count = contents.split()
    return len(words_count)


def count_charecters(contents):
    num_char=contents.lower()
    return Counter(num_char)

def sort_on(items):
    return items["num"]


def sorted_list(contents):
    lis_con=[
        {"char":"e","num": 0},
        {"char":"t","num": 0},
        {"char":"a","num": 0},
        {"char":"o","num": 0},
        {"char":"i","num": 0},
        {"char":"n","num": 0},
        {"char":"s","num": 0},
        {"char":"r","num": 0},
        {"char":"h","num": 0},
        {"char":"d","num": 0},
        {"char":"l","num": 0},
        {"char":"m","num": 0},
        {"char":"u","num": 0},
        {"char":"c","num": 0},
        {"char":"f","num": 0},
        {"char":"y","num": 0},
        {"char":"w","num": 0},
        {"char":"p","num": 0},
        {"char":"g","num": 0},
        {"char":"b","num": 0},
        {"char":"v","num": 0},
        {"char":"k","num": 0},
        {"char":"x","num": 0},
        {"char":"j","num": 0},
        {"char":"q","num": 0},
        {"char":"z","num": 0},
        {"char":"æ","num": 0},
        {"char":"â","num": 0},
        {"char":"ê","num": 0},
        {"char":"ë","num": 0},
        {"char":"ô","num": 0},
        {"char":"a","num": 0},
    ]
    for index in range(0, len(lis_con)):
        char = lis_con[index]["char"]
        if char in contents:
            lis_con[index]["num"] = contents[char]
    lis_con.sort(reverse=True, key=sort_on)


    return lis_con

