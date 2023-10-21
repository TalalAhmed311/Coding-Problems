# Select Team which has max points


competitions =  [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
  ]
results =  [0, 0, 1]


def tournamentWinner(competitions, results):
    # Write your code here.
    winner = ""
    lookup = {}
    for i in range(len(results)):
        win_idx = 1 if results[i]==0 else 0
        winner = competitions[i][win_idx]

        if winner not in lookup.keys():
            lookup[winner] = 3

        else:
            lookup[winner] += 3
            
    
    return max(lookup,key=lambda key: lookup[key])