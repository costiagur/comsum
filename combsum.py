import itertools

def combsum(thelist,serchednum):
    res = 0
    for n in range(2,len(thelist),1):
        for eachcomb in itertools.combinations(thelist,n):
            if round(sum(eachcomb),2) == round(serchednum,2):
                res = eachcomb
                break
            #
        #
    
        if res != 0:
            break
        else:
            print(n)
        #
    #
    return res
#