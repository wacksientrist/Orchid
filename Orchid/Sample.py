from Public.Orchid import Instance

C1 = Instance("1")
C2 = Instance("2")

for i in range(1000):
	C1.Process(i, 3, "M")
	C2.Process(C1.Read(), 9, "A")

	#print(i)
	C1.Read()
	C2.Read()