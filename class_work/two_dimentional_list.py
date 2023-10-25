score = [[25, 50, 75],
         [40, 50, 60],
         [75, 65, 80]]

average_for_each = 0
total_average =0

for row in range(len(score)):
    total = 0
    for column in range(len(score)):
        total+= score[row][column]
    average_for_each += total / len(score)
    total_average = average_for_each/len(score)
    print(f"""The average for score of value in {row} index is{total/len(score):.1f} """)
    print(f"The average of all is{total_average}")
