"""
Uzrakstiet programmu Python, lai aprēķinātu cilindra tilpumu un virsmas laukumu.

Piezīme: Cilindrs ir viena no visvienkāršākajām izliektajām ģeometriskajām 
formām, virsma, ko veido punkti fiksētā attālumā no noteiktās taisnes, 
cilindra ass.

Piezīme:
Ievaddati: Pamata rādiuss un cilindra augstums
Izvaddati: Cilindra virsmas laukums un tilpums 
"""
Pamata_radiuss=int(input("ievadi radiussu"))
cilindra_augstums=int(input("ievadi augstumu"))
virsmas_laukums=print(3,14*(Pamata_radiuss*Pamata_radiuss))
cilindr_tilpums=print(3,14*(Pamata_radiuss*Pamata_radiuss)*cilindra_augstums)