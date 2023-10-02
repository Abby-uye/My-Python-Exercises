def the_average(*args):

    return sum(*args) / len(*args)


exam_scores = []
for number in range(1, 11):
    score = int(input("Enter your scores: "))
    exam_scores.append(score)
print("The average of the scores is ",the_average(exam_scores))

