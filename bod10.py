a=[7,2,9,4,1,6]
b=a.index(max(a))
c=a.index(min(a))
a[b],a[c]=a[c],a[b]
print(a)