def meme_version():
    print("1")
    print("4 6")
    print("9 11 13")
    print("17 19 21 23")

def QA_CSE_102(rows):
    lines = []
    increase = 2
    startnr = -1
    for row in range(rows):
        line = []
        increase += row
        startnr = startnr + increase
        for number in range(row+1):
            line.append(startnr+(number*2))
        lines.append(line)
    for l in lines:
        print(l)