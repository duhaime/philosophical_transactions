with open("C:\\Users\\Douglas\\Desktop\\phil_trans\\philosophical_transactions_metadata_1.txt") as one:
    with open("C:\\Users\\Douglas\\Desktop\\phil_trans\\philosophical_transactions_metadata_2.txt") as two:
        with open("C:\\Users\\Douglas\\Desktop\\phil_trans\\philosophical_transactions_metadata_3.txt") as three:
            with open("aggregate_philosophical_transactions_metadata.txt","w") as out:
                o = one.readlines()
                for i in o:
                    out.write(i)
                #we've written headers so can skip them 
                tw = two.readlines()[1:]
                for j in tw:
                    out.write(j)
                #skip headers again    
                th = three.readlines()
                for k in th:
                    out.write(k)
