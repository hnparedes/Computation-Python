#1
# string = 'Polytechnic'
# print("%s...%s" % (string[0 : 3], string[len(string) - 3 : len(string)]))

#2
# price = float(input("enter price: "))
#
# dollars = int(price)
# cents = int((price - dollars) * 100 + 0.5)
#
# print(dollars, "dollars", cents, "cents")
# print(f"{dollars} dollars {cents} cents")

#3
# names = ['Fritz']
# names.insert(1, 'Ann')
# names.insert(0, 'Melina')
# names.pop(2)
# names.append('Jorge')
# print(names)

#4
contacts = {'Jenny': 8675309,'James': 5551212}
print(*contacts)
print('Jennys number is', contacts['Jenny'])
brian = contacts.get('James')
print('Brian has new number',brian)
