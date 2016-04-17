def answer(minions):
    answers = [0] * len(minions)
    for i, list in enumerate(minions):
        answers[i] = (i,float(list[0]) * (float(list[2])/float(list[1])))

    answers = sorted(answers, key= lambda x:x[1])
    return [x[0] for x in answers]
