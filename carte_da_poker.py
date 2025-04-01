#unicode
fiori = "\u2662"
picche = "\u2664" 
quadri = "\u2663"
cuori = "\u2661"
print(cuori, quadri, fiori, picche, sep="") 

#utf
semi_bytes = (b'\xe2\x99\xa0' + b'\xe2\x99\xa5' + b'\xe2\x99\xa6' + b'\xe2\x99\xa3')
str = semi_bytes.decode()
print(str)
