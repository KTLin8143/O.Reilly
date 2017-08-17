scores = {}
highest_score = 0
grade = open("grade.txt")
for line in grade:
    (name, score) = line.split()
    "key:score value:name"
    scores[score] = name
grade.close()

for score in sorted(scores.keys(), reverse=True):
    print (scores[score] + " score " + score)
