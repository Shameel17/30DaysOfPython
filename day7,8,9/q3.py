def calculate_manhattan_distance(sequence):
    x, y = 0, 0
    for move in sequence:
        if move == 'UP':
            y += 1
        elif move == 'DOWN':
            y -= 1
        elif move == 'LEFT':
            x -= 1
        elif move == 'RIGHT':
            x += 1
    manhattan_distance = abs(x) + abs(y)
    return manhattan_distance


sequence = []
no_of_moves = int(input("how many moves do u want including start and stop: "))
for i in range(1, no_of_moves + 1):
    a = str(input("give your move: ")).upper()
    sequence.append(a)
distance = calculate_manhattan_distance(sequence)
print("Manhattan distance:", distance)
