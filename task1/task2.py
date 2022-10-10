for x in [False,True]:
    for y in [False,True]:
        for z in [False,True]:
            print(x , y , z)
            print(not(x or y or z) == (not x and not y and not z))