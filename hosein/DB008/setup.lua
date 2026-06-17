redis.call('DEL', 'leaderboard')
redis.call('ZADD', 'leaderboard', 1000, 'Alice')
redis.call('ZADD', 'leaderboard', 1500, 'Bob')
redis.call('ZADD', 'leaderboard', 1200, 'Carol')
redis.call('ZADD', 'leaderboard', 1500, 'Dave')   -- tie with Bob
redis.call('ZADD', 'leaderboard', 800, 'Eve')