# Recibes una string conteniendo solo () y []
# Crea un algoritmos para validar que la sintaxis de los corchetes es correcta:
# Ejemplos validos:
# '()'
# '()()()()()()()()()'
# '([])[]()'
# Ejemplos no validos:
# ')'
# '()['
# '(([))]'
# '(((((((((((((((((((((((((((((((((('

# Cristian Aurelio Ramirez Anzaldo
# A01066337

def brackets(chain):
    stack = []
    i = 0
    correct = True

    while correct and i < len(chain):
        if chain[i] == '(' or chain[i] == '[':
            stack.append(chain[i])
        elif chain[i] == ')' and stack:
            br = stack.pop()
            if br != '(':
                correct = False
        elif chain[i] == ']' and stack:
            br = stack.pop()
            if br != '[':
                correct = False
        else:
            correct = False
        i = i + 1

    if not correct or stack:
        print("Sintaxis de corchetes es incorrecta")
    else:
        print("Sintaxis de corchetes es correcta")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    brackets(input("Enter your chain of brackets: "))

