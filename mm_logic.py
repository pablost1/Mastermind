import random as rd

class Mastermind:

    def __init__ (self, difficulty):
        self.__LEVELS = {'easy':15, 'medium':10, 'hard':5}
        
        # Absolute Variables /\ #

        self.__difficulty = difficulty

    def start (self):
        # # # Variáveis condição para manter o loop do jogo
        self.__guesses = self.__LEVELS[self.__difficulty] # --> Chances restantes
        self.__completed = False # --> Se o jogo está ativo ou não

        # # # Gerando a sequência de números a serem adivinhados
        self.goal = []
        i = 0
        while i < 5:
            n = rd.randint(0,9)
            if n not in self.goal:
                self.goal.append(n)
                i+=1

        self.hints = ["_","_","_","_","_"] #--> lista de dicas
        return

    def __guess (self, guess_string):
        guess_list = []
        if len(guess_string) != 5: # verifica se o palpite tem exatamente 5 digitos *// Enquanto estiver construindo o GUI, faça uma verificação para que o guess_string só receba números
            print('Palpite invalido, tente novamente') # # # Remover depois 
            return 'Error 1'
        else:
            # # # Definindo as variáveis dicas
            hit  = 0 # --> Quantos algarismos foram postos em posições corretas
            miss = 0 # --> Quantos algarismos goram postos em posições erradas

            for x in guess_string:  # --> Transformando a string palpite numa lista
                guess_list.append(int(x))

            index = 0
            for x in guess_list:
                if x == self.goal[index]:
                    hit += 1
                    self.hints[index] = x
                elif x in self.goal:
                    miss += 1
                index+=1
            print(self.hints)
            print("hits:%s\nmisses:%s" % (hit, miss))
            if hit == 5:
                self.__completed = True

            self.set_guesses(self.get_guesses()-1) # --> subtraindo a chance perdida

        return

    def mainloop (self):
        while self.__guesses > 0 and self.__completed is False:
            player_input = input('Give your guess: ')
            self.__guess(player_input)
        if self.__guesses == 0 and self.__completed is False:
            print('defeated')
        else:
            print('You win')
        return

    # # # Gets n' Sets

    def get_guesses (self):
        return self.__guesses
    def set_guesses (self, new_value):
        self.__guesses = new_value
        return
    def decrease_guesses (self, value):
        self.__guesses -= value

if __name__ == "__main__":
    teste = Mastermind('medium')    
    teste.start()
    teste.mainloop()

    teste.start()
    teste.mainloop()