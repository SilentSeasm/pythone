class Studente:
    def __init__(self, nome, cognome, score, quiz):
        self.nome = nome
        self.cognome = cognome
        self.score = score
        self.quiz = quiz

    def getName(self):
        return self.nome + " " + self.cognome
              
    def addQuiz(self, punteggio):
        self.quiz += 1
        self.score += punteggio
          
    def getTotalScore(self):    
        return self.score
        
    def getAverageScore(self):  
        if self.quiz == 0:
            return 0 
        return self.score / self.quiz


risultati = Studente("Mario", "Rossi", 10, 5)
print(risultati.getName())  
print("Punteggio totale:", risultati.getTotalScore())
print("Punteggio medio:", risultati.getAverageScore())