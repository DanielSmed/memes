

def Assignment_5(n):

    result = []
    for row in range(1,n+1):
        sup_result = [row]
        for col in range(1,n):
            if col%2==0:
                sup_result.append(row+(n*col))
            else:
                sup_result.append(((n*(col+1))+1)-row)
        result.append(sup_result)

    for sr in result:
        print(*sr,sep=" ")