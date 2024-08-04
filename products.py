#讀取檔案
products = [] #大火車
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue #和break一樣只能寫在迴圈內，continue是跳到下一迴的意思
		name, price = line.strip().split(',') #由左到右：先把換行去掉，再把","當切割的標準(切割的結果是清單)
		products.append([name, price])
print(products)

#讓使用者輸入
while True:
	name = input('請輸入商品名稱:')
	if name == 'q': #quit
		break
	price = input('請輸入商品價格:')
	price = int (price)
	products.append([name, price])
print(products) #二維清單

#印出所有購買紀錄
for p in products: #小火車
	print(p[0], '的價格是', p[1])

#字串可以加法'abc' + '123' = 'abc123'
#字串可以乘法'abc' * 3 = 'abcabcabc'

#寫入檔案
with open ('products.csv', 'w', encoding='utf-8') as f: #一般有OPEN就有CLOSE，但WITH會自動CLOSE，utf-8編碼
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') #寫入檔案：逗號會讓EXCEL為不同格
