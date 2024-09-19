
# product

# id: int
# name:str
# price:float
# section:int

# 1, tech
# 2, clothes
# 3, food

store=[]

id = int (input("por favor ingrese el id de su producto:\n"))
name = input("por favor ingrese el nombre de su producto:\n")
price = float(input("por favor ingrese el precio:\n"))
section = input ("por favor ingrese la section para su producto:\n")

product1 =  {
    "id": id,
    "name":name,
    "price":price,
    "section":section
}

store.append(product1)

#mostrar los productos del almacen
for product in store:
    print(product)
