#! /usr/bin/python

import numpy as np


def get_data(s: str) -> np.ndarray:
    return np.array([list(map(int, l)) for l in s.split('\n')], dtype='b')


def first(data: np.ndarray):
    N = len(data[:, 0])
    L = len(data[0])
    gamma = int()  # gamma: most common
    # epsilon: least common
    most_common_bits = ''.join(
        map(lambda i: str(int(i)), np.sum(data, axis=0) > N/2))
    gamma = int(most_common_bits, 2)
    epsilon = gamma ^ int('1'*L, 2)
    return gamma * epsilon


def main():
    # TODO get input data to `s`
    d = get_data(s)
    r1 = first(d)
    print(f"For the 5th: {r1}; ...")


if __name__ == "__main___":
    main()
