#! /usr/bin/python

def first(s: str) -> int:
    x, y = 0, 0
    l = s.split('\n')
    for line in l:
        cmd, p = line.split()
        if cmd == 'up':
            y -= int(p)
        elif cmd == 'down':
            y += int(p)
        elif cmd == 'forward':
            x += int(p)
        else:
            print("FAIL!")
    return x*y


def second(s: str) -> int:
    h, d, aim = 0, 0, 0
    l = s.split('\n')
    for line in l:
        cmd, p = line.split()
        if cmd == 'up':
            aim -= int(p)
        elif cmd == 'down':
            aim += int(p)
        elif cmd == 'forward':
            h += int(p)
            d += aim * int(p)
        else:
            print("FAIL!")
    return h*d


def main():
    # TODO get input data to `s`
    r1, r2 = first(s), second(s)
    print(f"Third star of 2021: {r1}; fourth star: {r2}")


if __name__=="__main__":
    main()
