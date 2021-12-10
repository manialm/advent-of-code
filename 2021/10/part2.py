with open('input.txt') as f:
    s = f.read().splitlines()

open = '([{<'
close = ')]}>'


def closes(c):
    return close[open.index(c)]


def close_stack(stack):
    ret = []
    while stack:
        top = stack.pop()
        ret.append(closes(top))
    return ret


def incomplete(s):
    stack = []

    for c in s:
        if c in open:
            stack.append(c)
        else:
            if c != closes(stack.pop()):
                return []

    return close_stack(stack)


points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def score(string):
    if not (stack := incomplete(string)):
        return 0
    score_string = ''.join(str(points[c]) for c in stack)
    ret = int(score_string, 5)
    return ret


scores = sorted(filter(lambda x: x > 0, map(score, s)))
res = scores[len(scores) // 2]
print(res)
