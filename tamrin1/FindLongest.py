def findLongest(words):
    if not words:
        return []
    worditer = iter(words)
    ret = [next(worditer)]
    cur_len = len(ret[0])
    for wd in worditer:
        len_wd = len(wd)
        if len_wd > cur_len:
            ret = [wd]
            cur_len = len_wd
        else:
            if len_wd == cur_len:
                ret.append(wd)
    return ret

tests = [
    [],
    "this is for find longest".split(),
    ]

for test in tests:
    print findLongest(test)