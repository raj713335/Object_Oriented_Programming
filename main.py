from phone import Phone
from item import Item

phone1 = Phone("jscPhonev10", 500, 5,1)
print(phone1.calculate_total_price())
phone2 = Phone("jscPhonev20", 500, 5,1)


print(Phone.all)

item1 = Item("MyItem", 750)
item2 = Item("MyItem2", 750)
item1.name = "OtherItem"

print(item1.name)