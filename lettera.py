class Letter:
    def __init__(self, letterFrom, letterTo): 
        self.letterFrom = letterFrom
        self.letterTo = letterTo
        self.corpo = ""  
    
    def addLine(self, line): 
        self.corpo += line + "\n"  

    def getText(self): 
        if not self.corpo:
            return "Inserire del testo"
        else:
            return f"Caro {self.letterTo},\n\n{self.corpo}\nSinceramente,\n\n{self.letterFrom}"

lettera = Letter("Mario", "Marco")

lettera.addLine("Mi dispiace simao partiti.")
lettera.addLine("Ti auguro il meglio.")

print(lettera.getText())

