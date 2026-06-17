def run_test(r):
    all_players = r.zrevrange('leaderboard', 0, -1, withscores=True)
    by_score = {}
    for name, score in all_players:
        score = int(score)
        by_score.setdefault(score, []).append(name)
    distinct = sorted(by_score.keys(), reverse=True)
    result = []
    for score in distinct[:3]:
        for name in sorted(by_score[score]):
            result.append([name, score])
    return result