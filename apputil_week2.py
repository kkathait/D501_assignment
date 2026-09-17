def ways(n):
        count = (n // 5) +1

        return count

print (ways(12))
print(ways(20) )  
print(ways(3) )   
print (ways(0)  )     

def ways(cents, coin_types=[1, 5]):
    if cents == 0:
        return 1
    if cents < 0:
        return 0
    if not coin_types:
        return 0

    coin = coin_types[0]

    total = 0
    for num_coins in range(cents // coin + 1):
        total += ways(cents - num_coins * coin, coin_types[1:])

    return total

print(ways(100, [25,10,5,1]))


import numpy as np

def lowest_score(names, scores):
    index = np.argmin(scores)
    return names[index]


def sort_names(names, scores):
    indices = np.argsort(scores)[::-1]
    return names[indices]

names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
scores = np.array([99, 71, 85, 62, 91])

print(lowest_score(names, scores))
print(sort_names(names, scores))

names = np.array(['Alice', 'Bob', 'Charlie'])
scores = np.array([85,90,80])

print(lowest_score(names, scores))
print(sort_names(names, scores))

names = np.array(['David', 'Eve', 'Frank'])
scores = np.array([70,75,80
                   ])

print(lowest_score(names, scores))
print(sort_names(names, scores))