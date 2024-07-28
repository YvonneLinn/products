products = [] #大火車
while True:
	name = input('請輸入商品名稱:')
	if name == 'q': #quit
		break
	price = input('請輸入商品價格:')
	p = [] #小火車
	p.append(name) #p = [name, price]
	p.append(price)
	products.append(p) #products.append([name, price])
print(products) #二維清單

products[0][0] #第0格中的第0格
