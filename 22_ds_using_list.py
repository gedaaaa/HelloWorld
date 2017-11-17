# this is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print('i have', len(shoplist), 'items to purchase')

print('these items are:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice.')
shoplist.append('rice')
print('my shoppinglist is now:', shoplist)

print('I will sort my list now.')
shoplist.sort()
print('sorted shopping list is', shoplist)
print('the first thing i wiil buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('i bought the', olditem)
print('my shoppinglist is now:', shoplist)
