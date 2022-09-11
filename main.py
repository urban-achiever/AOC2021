import numpy as np
import numpy.ma as ma

# get input data into two numpy arrays (drawn numbers and all bingo boards)
draws = np.genfromtxt('input.csv', dtype=int, delimiter=",", max_rows=1)
boards = np.empty((100,5,5), dtype=int)
for i in range(100):
    boards[i] = np.loadtxt('input.txt', dtype=int, skiprows=(2+i*6), ndmin=2, max_rows=5)

# create a mask array where matches for a given drawn number will be stored
masks = np.zeros((100,5,5), dtype=int)
finished = False
count = 1
for draw in draws:
    matches = np.where(boards == draw)
    masks[matches] = 1
    # count how many matches each board has so far
    for board_idx in range(len(masks)):
        board_score = np.sum(masks[board_idx])
        # if a board has at least 5 matches, check if they are in a single 
        # row or column
        if  board_score >= 5:
            colsums = np.sum(masks[board_idx], axis=0)
            if (5 in colsums):
                print("Board ", board_idx, "has a full column")
                finished = True
            rowsums = np.sum(masks[board_idx], axis=1)
            if (5 in rowsums):
                print("Board ", board_idx, "has a full row")
                finished = True
            
            if finished:
                print(boards[board_idx])
                print("Matches: \n", masks[board_idx])
                print("Draws so far: \n", draws[:count])
                break
    if finished:
        break
    count += 1
winner = boards[board_idx]
winner[np.array(masks[board_idx], dtype=bool)] = 0
score = np.sum(winner) * draws[count-1]
print("Score: ",score)
