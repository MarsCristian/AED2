#pragma once
//atacar diferente o problema
//atacar por vetor, pq pode acessar qualquer posicao dele em tempo constante
//funcoes de espalhamento(hash)
//vetor de tamanho M com M proporcional a S
//nao mantem dados ordenados
struct HashTable
{
    int *vetor;

};

int funcaoHash(int chave, int M)
{
    int i, h = 0;
    int primo = 127;

    for(i = 0; chave !='\00';i++)
        h = ((h*primo)+chave[i])%M;

        return h;

}

bool insere()
{

}

bool remove()
{

}

bool busca()
{

}