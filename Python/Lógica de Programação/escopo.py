#escopo global e local

var_global = "Curso completo de python"

def escreve_texto():
    var_local = "Leonardo Capristo"
    print(f"Variável global : {var_global}")
    print(f"Variável local : {var_local}")

if __name__ == "__main__":
    print(f"Executar a função escreve texto: ")
    escreve_texto()

    print("Tentando acessar as variaveis diretamente: ")
    print(var_global)
#    print(var_local) #erro



