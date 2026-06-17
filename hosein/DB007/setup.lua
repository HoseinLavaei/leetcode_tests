redis.call('FLUSHDB')
redis.call('SET', 'counter:1', 10)
redis.call('SET', 'counter:2', 20)
redis.call('SET', 'counter:3', 30)