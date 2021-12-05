import csv

file = open('input.txt', 'r')
bingoNumbers = file.readline().split(',')
temp_board = []
boards = []
with open('input.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=' ')
    next(csv_reader)
    next(csv_reader)
    for row in csv_reader:
        row = ' '.join(row).split()
        if row == []:
            alt_temp_board = [list(tup) for tup in zip(*temp_board)]
            boards.extend(temp_board)
            boards.append([])
            boards.extend(alt_temp_board)
            temp_board.clear()
            alt_temp_board.clear()
            boards.append([])
        else:
            temp_board.append(row)

boardCheck = [0] * len(boards)

def boardChecker(board):
    numbers_called = []
    for number in bingoNumbers:
        numbers_called.append(number)
        for i in boards:
            for j in i:
                if j == number:	
                    boardCheck[board.index(i)] += 1
                    if boardCheck[board.index(i)] == 5:
                      return board.index(i), number, numbers_called
a = boardChecker(boards) #index of winning board, winning number, all numbers 
called_numbers = a[2]
counter = a[0]
for lines in boards[counter:]:
    if lines == []:
        break;
    else:
        counter+=1
counter -=5

winning_board = []
for i in boards[counter:]:
    for j in i:
        winning_board.append(int(j))
    if i == []:
        break
    
called_numbers = [int(i) for i in called_numbers]

add_these = [x for x in winning_board if x not in called_numbers]
answer = sum(add_these)
print(answer*int(a[1]))