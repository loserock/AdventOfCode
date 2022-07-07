#! /usr/bin/python

def solve(s: str) -> (int, int):
    l = map(int, s.split())
    first = sum(1 for i,v in enumerate(l) if i>0 and v>l[i-1])
    second = sum(1 for i,v in enumerate(l) if i>1 and i<len(l)-1 and sum(l[i-1:i+2]) > sum(l[i-2:i+1]))
    return first, seconds


def main():
    # TODO get input data to `s`
    r1, r2 = solve(s)
    print(f"For the first star of 2021: {r1}; second star: {r2}")


if __name__=="__main___":
    main()
