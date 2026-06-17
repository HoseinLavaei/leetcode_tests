def run_setup(r):
    r.flushdb()
    r.set('counter:1', 10)
    r.set('counter:2', 20)
    r.set('counter:3', 30)