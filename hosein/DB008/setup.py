def run_setup(r):
    r.delete('leaderboard')
    r.zadd('leaderboard', {'Alice': 1000, 'Bob': 1500, 'Carol': 1200, 'Dave': 1500, 'Eve': 800})