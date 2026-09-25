def linearsearch(li,search_ele):
    for ind in range(0,len(li)):
        if(li[ind] == search_ele):
            return ind
    else:
            return -1
li= [ 40,50,30,60,20,10]        
ele   = 3
res = linearsearch(li,ele)
if(res != -1):
    print(f'{ele} is present at index {res}')
else:
    print(f'{ele} is not present at index{res}') 
