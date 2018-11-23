def main():
    n = input()
    meg = input().strip().split()
    ran = input().strip().split()

    ml = len(meg)
    rl = len(ran)

    # j = 0
    # match = "Yes"
    # for i in range(rl):
    #     try:
    #         meg.remove(ran[i])
    #     except ValueError:
    #         match = "No"
    #         break
            

    ## better solution using dictionary

    mg_hash = dict()
    rn_hash = dict()

    for i in range(ml):
        val = mg_hash.get(meg[i], 0)
        mg_hash[meg[i]] = val+1

    for i in range(rl):
        val = rn_hash.get(ran[i], 0)
        rn_hash[ran[i]] = val + 1

    match = "Yes"
    for k,v in rn_hash.items() :
        val = mg_hash.get(k, 0)
        if val < v:
            match = "No"
            break

    print(match)


main()