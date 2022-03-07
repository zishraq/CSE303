# data_frame = [
#     [[250], [200]],
#     [[50], [1000]]
# ]

# data_frame = [
#     [[73]],
#     [[38]],
#     [[18]],
# ]

# data_frame = [
#     [[100], [300]],
#     [[300], [200]],
#     [[20], [80]]
# ]

data_frame = [
    [[100, 120], [300, 280]],
    [[300, 325], [200, 175]],
    [[20, 25], [80, 75]]
]

# row sum
for row in range(len(data_frame)):
    total = 0

    for col in range(len(data_frame[row])):
        total += data_frame[row][col][0]

    data_frame[row].append([total])

data_frame.append([])

# col sum
for col in range(len(data_frame[0])):
    total = 0

    for row in range(len(data_frame) - 1):
        total += data_frame[row][col][0]

    data_frame[-1].append([total])
    # print(total)

chi_square = 0

# for data in data_frame:













# x = [
#     [[250], [200], [450]],
#     [[50], [1000], [1050]],
#     [[300], [1200], [1500]]
# ]

# x = [
#     [[100], [300], [400]],
#     [[300], [200], [500]],
#     [[20], [80], [100]],
#     [[420], [580], [1000]]
# ]

# x = [
#     [[73], [73]],
#     [[38], [38]],
#     [[18], [18]],
#     [[129], [129]]
# ]
