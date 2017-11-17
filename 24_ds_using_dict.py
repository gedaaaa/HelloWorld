# ab是adress book的简写
ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}
print("swaroop's adress is", ab['Swaroop'])
del ab['Spammer']
print('\nThere are {} contacts in the adress book\n'.format(len(ab)))

for name, adress in ab.items():
    print('Contact {} at {}'.format(name, adress))

# 添加一对
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
    print("Guido's address is", ab['Guido'])
