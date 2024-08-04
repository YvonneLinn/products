products = [] #大火車
while True:
	name = input('請輸入商品名稱:')
	if name == 'q': #quit
		break
	price = input('請輸入商品價格:')
	price = int (price)
	products.append([name, price])
print(products) #二維清單

for p in products: #小火車
	print(p[0], '的價格是', p[1])

#字串可以加法'abc' + '123' = 'abc123'
#字串可以乘法'abc' * 3 = 'abcabcabc'

with open ('products.csv', 'w', encoding='utf-8') as f: #一般有OPEN就有CLOSE，但WITH會自動CLOSE，utf-8編碼
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') #寫入檔案：逗號會讓EXCEL為不同格
