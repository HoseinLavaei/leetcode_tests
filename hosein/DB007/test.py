def run_test(r):
    keys = r.keys('counter:*')
    result = {}
    for key in keys:
        result[key] = int(r.get(key))
    return result