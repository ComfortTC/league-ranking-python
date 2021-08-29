from collections import defaultdict
from operator import itemgetter

# expected input
data = """Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
Lions 1, FC Awesome 1
Tarantulas 3, Snakes 1
Lions 4, Grouches 0"""

data_list = data.splitlines()


def splitter(row):
    left_team, right_team = row.split(',')
    return {
        'left': left_team[:-2].strip(),
        'left_score': int(left_team[-2:].strip()),
        'right': right_team[:-2].strip(),
        'right_score': int(right_team[-2:].strip())
    }


data_dicts = [splitter(row) for row in data_list]

team_scores = defaultdict(int)
for game in data_dicts:
    if game['left_score'] == game['right_score']:
        team_scores[game['left']] += 1
        team_scores[game['right']] += 1
    elif game['left_score'] > game['right_score']:
        team_scores[game['left']] += 3
        team_scores[game['right']] += 0
    else:
        team_scores[game['left']] += 0
        team_scores[game['right']] += 3

teams_sorted = sorted(team_scores.items(), key=itemgetter(1), reverse=True)

for idx, (team, score) in enumerate(teams_sorted, 1):
    print(f'{idx}. {team} {score} pts')
