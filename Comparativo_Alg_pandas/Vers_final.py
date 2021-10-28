import pandas as pd 
import time
## Declaração de funcoes.....
def Selectionsort():
 print("Sua Seleção foi o SelectionSort\n")
 select = int(input(" 1-Acession do Menor para Maior\n 2-Acession do Maior para o Menor\n 3-Data do maior para o menor\n insira a opcao:"))
 valor = select
 if valor == 1:
 	df = pd.read_csv("dados2.csv", encoding = "UTF-8", sep = ";")
 	inicio = time.time()
 	print(df.sort_values("Acession",ascending = True ,kind = "selectionsort"))
 	fim = time.time()
 	tmp = fim - inicio
 	return tmp
 elif valor == 2:
 	df = pd.read_csv("dados2.csv", encoding = "UTF-8", sep = ";")
 	inicio = time.time()
 	print(df.sort_values("Acession",ascending = False ,kind = "selectionsort"))
 	fim = time.time()
 	tmp = fim - inicio
 	return tmp
 elif valor == 3:
 	df = pd.read_csv("dados2.csv", encoding = "UTF-8", sep = ";")
 	inicio = time.time()
 	print(df.sort_values("Date",ascending = True ,kind = "selectionsort"))
 	fim = time.time()
 	tmp = fim - inicio
 	return tmp
 else:
		print("OPÇÃO INVADIDA!!!!")


def Quicksort():
	print("Sua Seleção foi o QuickSort\n")
	select = int(input(" 1-Acession do Menor para Maior\n 2-Acession do Maior para o Menor\n 3-Data do maior para o menor\n insira a opcao:"))
	valor = select
	if valor == 1:
	 	df = pd.read_csv("dados2.csv", encoding = "UTF-8", sep = ";")
	 	inicio = time.time()
	 	print(df.sort_values("Acession",ascending = True ,kind = "quicksort"))
	 	fim = time.time()
	 	tmp = fim - inicio
	 	return tmp
	elif valor == 2:
	 	df = pd.read_csv("dados2.csv", encoding = "UTF-8", sep = ";")
	 	inicio = time.time()
	 	print(df.sort_values("Acession",ascending = False ,kind = "quicksort"))
	 	fim = time.time()
	 	tmp = fim - inicio
	 	return tmp
	elif valor == 3:
	 	df = pd.read_csv("dados2.csv", encoding = "UTF-8", sep = ";")
	 	inicio = time.time()
	 	print(df.sort_values("Date",ascending = True ,kind = "quicksort"))
	 	fim = time.time()
	 	tmp = fim - inicio
	 	return tmp
	else:
		print("OPÇÃO INVADIDA!!!!")


def Mergesort():
	print("Sua Seleção foi o MergeSort\n")
	select = int(input(" 1-Acession do Menor para Maior\n 2-Acession do Maior para o Menor\n 3-Data do maior para o menor\n insira a opcao:"))
	valor = select
	if valor == 1:
	 	df = pd.read_csv("dados2.csv", encoding = "UTF-8", sep = ";")
	 	inicio = time.time()
	 	print(df.sort_values("Acession",ascending = True ,kind = "mergesort"))
	 	fim = time.time()
	 	tmp = fim - inicio
	 	return tmp
	elif valor == 2:
	 	df = pd.read_csv("dados2.csv", encoding = "UTF-8", sep = ";")
	 	inicio = time.time()
	 	print(df.sort_values("Acession",ascending = False ,kind = "mergesort"))
	 	fim = time.time()
	 	tmp = fim - inicio
	 	return tmp
	elif valor == 3:
	 	df = pd.read_csv("dados2.csv", encoding = "UTF-8", sep = ";")
	 	inicio = time.time()
	 	print(df.sort_values("Date",ascending = True ,kind = "mergesort"))
	 	fim = time.time()
	 	tmp = fim - inicio
	 	return tmp
	else:
		print("OPÇÃO INVADIDA!!!!")
 
def Heapsort():
	print("Sua Seleção foi o HeapSort\n")
	select = int(input(" 1-Acession do Menor para Maior\n 2-Acession do Maior para o Menor\n 3-Data do maior para o menor\n insira a opcao:"))
	valor = select
	if valor == 1:
	 	df = pd.read_csv("dados2.csv", encoding = "UTF-8", sep = ";")
	 	inicio = time.time()
	 	print(df.sort_values("Acession",ascending = True ,kind = "heapsort"))
	 	fim = time.time()
	 	tmp = fim - inicio
	 	return tmp
	elif valor == 2:
	 	df = pd.read_csv("dados2.csv", encoding = "UTF-8", sep = ";")
	 	inicio = time.time()
	 	print(df.sort_values("Acession",ascending = False ,kind = "heapsort"))
	 	fim = time.time()
	 	tmp = fim - inicio
	 	return tmp
	elif valor == 3:
	 	df = pd.read_csv("dados2.csv", encoding = "UTF-8", sep = ";")
	 	inicio = time.time()
	 	print(df.sort_values("Date",ascending = True ,kind = "heapsort"))
	 	fim = time.time()
	 	tmp = fim - inicio
	 	return tmp
	else:
		print("OPÇÃO INVADIDA!!!!")
def Comparation():
	print("Escolha o modo de Comparação\n")
	select = int(input(" 1-Acession do Menor para Maior\n 2-Acession do Maior para o Menor\n 3-Data do maior para o menor\n insira a opcao:"))
	valor = select
	if valor == 1:
		#SELECTIONSORT
		df = pd.read_csv("dados2.csv", encoding = "UTF-8", sep = ";")
		inicSel = time.time()
		df.sort_values("Acession",ascending = True,kind = "selectionsort")
		fimSel = time.time()
		tmpSel= fimSel - inicSel
		#QUICKSORT
		inicQui = time.time()
		df.sort_values("Acession",ascending = True,kind = "quicksort")
		fimQui = time.time()
		tmpQui= fimQui - inicQui
		#MERGESORT
		inicMer = time.time()
		df.sort_values("Acession",ascending = True,kind = "mergesort")
		fimMer = time.time()
		tmpMer= fimMer - inicMer
		#HEAPSORT
		inicheap = time.time()
		df.sort_values("Acession",ascending = True,kind = "heapsort")
		fimheap = time.time()
		tmpheap= fimheap - inicheap

		print("Selection:",tmpSel)
		print("Quick:",tmpQui)
		print("Merge:",tmpMer)
		print("Heap:",tmpheap)
	elif valor == 2:
		#SELECTIONSORT
		df = pd.read_csv("dados2.csv", encoding = "UTF-8", sep = ";")
		inicSel = time.time()
		df.sort_values("Acession",ascending = False,kind = "selectionsort")
		fimSel = time.time()
		tmpSel= fimSel - inicSel
		#QUICKSORT
		inicQui = time.time()
		df.sort_values("Acession",ascending = False,kind = "quicksort")
		fimQui = time.time()
		tmpQui= fimQui - inicQui
		#MERGESORT
		inicMer = time.time()
		df.sort_values("Acession",ascending = False,kind = "mergesort")
		fimMer = time.time()
		tmpMer= fimMer - inicMer
		#HEAPSORT
		inicheap = time.time()
		df.sort_values("Acession",ascending = False,kind = "heapsort")
		fimheap = time.time()
		tmpheap= fimheap - inicheap

		print("Selection:",tmpSel)
		print("Quick:",tmpQui)
		print("Merge:",tmpMer)
		print("Heap:",tmpheap)
	elif valor == 3:
		#SELECTIONSORT
		df = pd.read_csv("dados2.csv", encoding = "UTF-8", sep = ";")
		inicSel = time.time()
		df.sort_values("Date",ascending = True,kind = "selectionsort")
		fimSel = time.time()
		tmpSel= fimSel - inicSel
		#QUICKSORT
		inicQui = time.time()
		df.sort_values("Date",ascending = True,kind = "quicksort")
		fimQui = time.time()
		tmpQui= fimQui - inicQui
		#MERGESORT
		inicMer = time.time()
		df.sort_values("Date",ascending = True,kind = "mergesort")
		fimMer = time.time()
		tmpMer= fimMer - inicMer
		#HEAPSORT
		inicheap = time.time()
		df.sort_values("Date",ascending = True,kind = "heapsort")
		fimheap = time.time()
		tmpheap= fimheap - inicheap

		print("Selection:",tmpSel)
		print("Quick:",tmpQui)
		print("Merge:",tmpMer)
		print("Heap:",tmpheap)
	else:
		print("OPÇÃO INVADIDA!!!!")


## Execução do programa.....
a = 1
b = 2
c = 3
d = 4
e = 5

print ("Trabalho 1: Estrutura de Dados2")
print ("Selecione uma opção de ordenacao\n 1- SelectionSort\n 2- QuickSort\n 3- MergeSort\n 4- Heapsort\n 5-Comparação Geral")
opcao = int(input("selecione uma opcao: "))
valor = opcao
if valor == a:
	tmp = Selectionsort()
	print("Tempo de ordenação SelectionSort:",tmp)
elif valor == b:
	tmp2 = Quicksort()
	print("Tempo de ordenação QuickSort:",tmp2)
elif valor == c:
	 tmp3 = Mergesort()
	 print("Tempo de ordenação MergeSort:",tmp3)
    #print("Tempo de ordenação MergeSort:",tmp3)
elif valor == d:
	tmp4 = Heapsort()
	print("Tempo de ordenação HeapSort:",tmp4)
elif valor == e:
	Comparation()
else:
	print("Opção invalida")