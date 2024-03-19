student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

highest_scores = 0
for scores in student_scores:
  if scores > highest_scores:
    highest_scores = scores
print(highest_scores)
