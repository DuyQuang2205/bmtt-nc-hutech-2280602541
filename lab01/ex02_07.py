print ("Nhap cac dong van ban (Nhap 'done' de ket thuc): ")
lines = []
while True:
    lines = input()
    if lines.lower() == 'done':
        break
    lines.append(line)
    print("Cac dong da nhap sau khi chuyen thanh chu in hoa: ")
    for line in lines:
        print (line.upper())