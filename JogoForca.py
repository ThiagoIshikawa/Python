#Jogo da Forca
import random
palavras = ["banana", "abacaxi", "uva", "python", "gato"]
palavra = "banana"
def escolher_palavra():
    
    return random.choice(palavras)

def exibir_palavra(palavra, letras_corretas):
    return "".join([letra if letra in letras_corretas else "_" for letra in palavra])

def jogar():
    palavra = escolher_palavra()
letras_corretas = []
letras_erradas = []
tentativas = 6

while tentativas > 0:
        print(f"Tentativas restantes: {tentativas}")
        print(f"Letras erradas: {', '.join(letras_erradas)}")
        print("Palavra: " + exibir_palavra(palavra, letras_corretas))

        letra = input("Digite uma letra: ").lower()
        
        verificar_termino = "palavras"
        if letra in letras_corretas or letra in letras_erradas:
         print("Você já tentou essa letra. Tente outra.")
        
        if letra in palavra:
            letras_corretas.append(letra)
            print(f"Boa! A letra '{letra}' está na palavra.") 
        else:
            letras_erradas.append(letra)
            tentativas -= 1
            print(f"Que pena! A letra '{letra}' não está na palavra.")

            
        if  verificar_termino(palavra, letras_corretas, tentativas):
            break
            
            
if tentativas == 0:
            print(f"Você perdeu! A palavra era: {palavra}")
        
if __name__ == "__main__":
            jogar()
