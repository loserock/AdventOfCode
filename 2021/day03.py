#! /usr/bin/python

import numpy as np


def get_data(s: str) -> np.ndarray:
    return np.array([list(map(int, l)) for l in s.split('\n')], dtype='b')


def first(data: np.ndarray) -> int:
    N = len(data[:, 0])
    L = len(data[0])
    most_common_bits = ''.join(
        map(lambda i: str(int(i)), np.sum(data, axis=0) > N/2))
    gamma = int(most_common_bits, 2)  # gamma: most common
    epsilon = gamma ^ int('1'*L, 2)  # epsilon: least common
    return gamma * epsilon


def second(data: np.ndarray):
    N = len(data[:, 0])
    L = len(data[0])
    most_common_by_pos = lambda d, pos: int(np.sum(d[:, pos]) >= len(d[:, 0]) / 2)
    # select by most common bits
    d = data.copy()
    for p in range(L):
        mc = most_common_by_pos(d, p)
        d = np.array([n for n in d if n[p]==mc])
        if len(d) == 1:
            oxygen = int(''.join(map(str, d[0])), 2)
            break
    # select by least common bits
    d = data.copy()
    for p in range(L):
        mc = most_common_by_pos(d, p)
        d = np.array([n for n in d if n[p]!=mc])
        if len(d) == 1:
            co2 = int(''.join(map(str, d[0])), 2)
            break
    print(f"oxigen: {oxygen}, co2: {co2}")
    return oxygen * co2


def main():
    global s  # TODO get input data to `s`
    d = get_data(s)
    r1 = first(d)
    r2 = second(d)
    print(f"For the 5th: {r1}; and the 6th: {r2}")


if __name__ == "__main__":
    main()
