basket = ['Apple','Bun','Cola']
crate=['Egg','Fig','Grape']

print('Basket List:',basket)
print('Basket Elements:',len(basket))

basket.append('Damson')
print('New Basket List:',basket)
print('New Basket Elements:',len(basket))

print('Last Item added or removed',basket.pop())


basket.extend(crate)
print('\nNew Basket List:',basket)
print('New Basket Elements:',len(basket))

print('Last Item added or removed',basket.pop())

del basket[1]
print('\nDel Bun:',basket)
print('New Basket Elements:',len(basket))

del basket[0:2]
print('\nNew Basket List:',basket)
print('New Basket Elements:',len(basket))
