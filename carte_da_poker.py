
fiori = "\u2662"
picche = "\u2664" 
quadri = "\u2663"
cuori = "\u2661"
print(cuori, quadri, fiori, picche) 

smei_bytes = (b'\xe2\x99\xa0' + b'\xe2\x99\xa5' + b'\xe2\x99\xa6' + b'\xe2\x99\xa3')
str = smei_bytes.decode()
print(str)
