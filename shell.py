from shop.models import Item, Purchase

a = Item.objects.create(name="Notebook", price = 1000)
a.purchased_item.create(name="Harry Potter", age=25,)
a.purchased_item.create(name="Ron Weasley", age=18,)
a.purchased_item.all()

b = Item.objects.create(name="Refrigerator", price = 2000)
b.purchased_item.create(name="Hermione Granger", age=19,)
b.purchased_item.create(name="Fleur Delacour", age=45,)
b.purchased_item.all()

c = Item.objects.create(name="Microwave", price = 500)
c.purchased_item.create(name="Dudley Dursley", age=25,)
c.purchased_item.create(name="Albus Dumblrdore", age=99,)
c.purchased_item.all()

d = Item.objects.create(name="Vacuum Cleaner", price = 1500)
d.purchased_item.create(name="Bellatrix Lestrange", age=44,)
d.purchased_item.create(name="Neville Longbottom", age=17,)
d.purchased_item.all()

e = Item.objects.create(name="Washing Machine", price = 3200)
e.purchased_item.create(name="Lucius Malfoy", age=51,)
e.purchased_item.create(name="Minerva McGonagall", age=73,)
e.purchased_item.all()

f = Item.objects.create(name="Notebook", price = 1000)
f.purchased_item.create(name="Harry", age=25,)
f.purchased_item.create(name="Ron", age=18,)
f.purchased_item.all()

g = Item.objects.create(name="Blander", price = 1000)
g.purchased_item.create(name="Peter Pettigrew", age=33,)
g.purchased_item.create(name="Severus Snape", age=48,)
g.purchased_item.all()

h = Item.objects.create(name="Mixer", price = 800)
h.purchased_item.create(name="Nymphadora Tonks", age=16,)
h.purchased_item.create(name="Cedric Diggory", age=21,)
h.purchased_item.all()

i = Item.objects.create(name="Toaster", price = 400)
i.purchased_item.create(name="Argus Filch", age=36,)
i.purchased_item.create(name="Gregory Goile", age=23,)
i.purchased_item.all()

j = Item.objects.create(name="Dish washer", price = 2500)
j.purchased_item.create(name="Gellert Grindewald", age=37,)
j.purchased_item.create(name="Rubeus Hagrid", age=65,)
j.purchased_item.all()