import bangunruang as br
import bangundatar as bd

print("---BANGUN RUANG---")
print(f"volume kubus dengan sisi 3 adalah {br.kubus(3)}")
print(f"volume balok adalah {br.balok(4,5,2)}")
print(f"volume prisma segitiga adalah {br.prisma(4,2,6)}")
print(f"volume tabung adalah {br.tabung(1,2)}")
print(f"volume kerucut adalah {br.kerucut(3,2)}")

print("---BANGUN DATAR---")
print(f"Luas persegi adalah {bd.persegi(4)}")
print(f"Luas persegiPanjang adalah {bd.persegiPanjang(2,3)}")
print(f"Luas segitiga adalah {bd.segitiga(5,2)}")
print(f"Luas lingkaran adalah {bd.lingkaran(3)}")
print(f"Luas jajarGenjang adalah {bd.jajarGenjang(4,7)}")