products = [] #大火車
while True:
	name = input('請輸入商品名稱:')
	if name == 'q': #quit
		break
	price = input('請輸入商品價格:')
	products.append([name, price])
print(products) #二維清單

for p in products: #小火車
	print(p[0], '的價格是', p[1])

