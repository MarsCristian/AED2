#noh
class Noh:
    pai = 0
    direita = 0
    esquerda = 0
    chave = 0
    conteudo = '0'
    bal = 0

def insere(raiz,chave):
    #caso 0: ACHOU O LUGAR DE InSERIr!!
    if(raiz == 0):
        return True
    #caso 1: Nao da pra enfiar
    if(raiz != 0):
        return False
    #caso 2: inserindo pra esquerda
    if(chave < raiz.chave):
        if(insere(raiz.esquerda,chave)):
            #caso 2.1: insere no maior
            raiz.bal -= 1
            #caso 2.1.1 ficou desbalanceada
            if(raiz.bal <= -2):
                balancear(raiz)
    #caso 3: inserindo pra direita
    if(chave > raiz.chave):
        if(insere(raiz.direita,chave)):
            #caso 2.1: insere no maior
            raiz.bal -= 1
            #caso 2.1.1 ficou desbalanceada
            if(raiz.bal >= 2):
                balancear(raiz)

def balancear(raiz):
    #caso 0 desbalanceado pra esqerda
    if(raiz.bal<-1):
        peso = raiz.bal - raiz.esquerda.bal
        if(peso == -1):
            rotacaoEsq(raiz)
        rotacaoDir(raiz)
    #caso 1 desbalancedo pra direita
    if(raiz.bal > 1):
        peso = raiz.bal - raiz.direita.bal
        if(peso == 1):
            rotacaoDir(raiz)
        rotacaoEsq(raiz)

def rotacaoDir(raiz):
    aux = raiz.esquerda
    raiz.esquerda.pai = raiz.esquerda
    raiz.esquerda = raiz
    raiz = aux

def rotacaoEsq(raiz):
    aux = raiz.direita
    raiz.direita.pai = raiz.direita
    raiz.direita = raiz
    raiz = aux

def remove(raiz,chave,alvo):
    a = 1

def main():
    arvore = Noh()
    insere(arvore, 10)
    insere(arvore, 50)
    insere(arvore, 20)
    insere(arvore, 55)
    print("aloo")


