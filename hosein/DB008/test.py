def run_test(r):
    # Get all players sorted by score descending
    all_players = r.zrevrange('leaderboard', 0, -1, withscores=True)
    # Build dict of score -> list of names
    by_score = {}
    for name, score in all_players:
        score = int(score)
        by_score.setdefault(score, []).append(name)
    # Sort distinct scores descending
    distinct = sorted(by_score.keys(), reverse=True)
    # Take first 3 distinct scores (including all ties)
    result = []
    for score in distinct[:3]:
        for name in sorted(by_score[score]):
            result.append([name, score])
    return result