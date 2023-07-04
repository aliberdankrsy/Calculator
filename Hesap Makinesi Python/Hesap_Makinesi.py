#Functions.
def Toplama():
	print(int(sayi_1) + int(sayi_2))
def Cikarma():
	print(int(sayi_1) - int(sayi_2))
def Carpma():
	print(int(sayi_1) * int(sayi_2))
def Bolme():
	print(int(sayi_1) / int(sayi_2))

sayi_1 = input("Birinci Sayıyı Girin : ")
sayi_2 = input("İkinci Sayıyı Girin : ")
try:
	sayi_1 = int(sayi_1)
	sayi_2 = int(sayi_2)
	
	islem = input("Yapmak istediğiniz işlemi seçin : \nToplama : +\nÇıkarma : -\nÇarpma : *\nBölme : /\n")

	if islem == "+":
		Toplama()
	elif islem == "-":
		Cikarma()
	elif islem == "*":
		Carpma()
	elif islem == "/":
		Bolme()
	else:
		print("Hatalı islem seçimi yaptınız")
except ValueError:
	print("Hatalı sayı girişi!")