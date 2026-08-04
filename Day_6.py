# Excercise 6 : Level 1

tpl=tuple()

tpll=("Shripad","Bipin","Vinay","Lucky","Shashank","Om")
tplll=("Sony","Adi","Anj","Vai","Sne","Sou")

tpbs=tpll+tplll
print(tpbs)

print(len(tpbs))

tpbs=list(tpbs)
tpbs.append("Mom")
tpbs.append("Dad")
family_members=tpbs
print(family_members)

tpbs.remove("Mom")
tpbs.remove("Dad")
print(family_members)

fruits=("Mango","Banana","Apple","Grapes","Pineapple")
vegetables=("Tomato","Potato","Onion","Cabbage","Carrot")
animals_products=("Milk","Eggs","Meat","Honey","Cheese")
food_stuff_tp=fruits+vegetables+animals_products
print(food_stuff_tp)

food_stuff_lt=list(food_stuff_tp)

n=len(food_stuff_lt)
print(food_stuff_lt[n//2])
nn=n-3

print(food_stuff_lt[0:4])
print(food_stuff_lt[nn:])

del food_stuff_tp

print("------------------------------------------------------------")

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

if 'Iceland' in nordic_countries:
    print("Yes, 'Iceland' is a nordic country.")

if 'Estonia' in nordic_countries:
    print("Yes, 'Estonia' is a nordic country.")
























