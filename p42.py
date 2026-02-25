#Find the Runner-Up Score
# Taking input just like the sample provided
n = int(input("N = "))
scores_input = input("Scores = ").split()


scores = [int(x) for x in scores_input]


unique_scores = list(set(scores))
unique_scores.sort(reverse=True)


if len(unique_scores) >= 1:
    print(unique_scores[1])
else:
    print("No runner-up exists (all scores might be identical).")