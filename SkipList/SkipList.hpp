#pragma once
struct Noh
{
    int numNiveis
    int chave
    levelNoh *proximo
}Noh;

struct levelNoh
{
    int n;
    levelNoh *dir;
};

void cria(Noh t, levelNoh l)
{
    l.n = 0;
    l.dir = 0;
    t.numNiveis = 0
    t.chave = 0
    t.proximo = l;
}

bool insere(Noh t,int chave);

bool busca(Noh t,int chave);

bool remove(Noh t,int chave);