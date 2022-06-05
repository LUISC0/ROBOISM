def order(list,n):
    op=['asc','desc','none']
    if n == 'asc':
        return sorted(list)
    if n=='desc':
        return sorted(list,reverse=True)
    if n == 'none':
        return list



numbers=[1,3,2]

print(order(numbers, "asc"))
print(order(numbers,"desc"))
print(order(numbers,"none"))