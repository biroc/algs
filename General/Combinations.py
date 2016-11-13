def combinations(start,string,out,current):
    for i in range(start,len(string)):
        current.append(string[i])
        out.append(''.join(current))
        if i < len(string)-1:
            combinations(i+1,string,out,current)
        current.pop()


