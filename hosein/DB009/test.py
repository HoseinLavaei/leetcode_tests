def run_test(r):
    user = "alice"
    limit = 5
    window = 60
    start_time = 1000
    total_requests = 7
    step = 10
    key = f"rate_limit:{user}"
    allowed = 0

    for i in range(total_requests):
        now = start_time + i * step
        r.zremrangebyscore(key, 0, now - window)
        count = r.zcard(key)
        if count < limit:
            r.zadd(key, {now: now})
            r.expire(key, window)
            allowed += 1
    return allowed