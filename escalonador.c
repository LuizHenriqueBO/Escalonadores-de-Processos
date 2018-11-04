#include <stdio.h>

char *leitor_arquivo()
{

    char url[] = "processos.txt";
    char ch;
    FILE *arq;

    char **processos = (char *)calloc(10, sizeof(char *));
    for (int i = 0; i < 10; i++)
    {
        processos[i] = calloc
    }

    arq = fopen(url, "r");

    if (arq == NULL)
        printf("Erro, nao foi possivel abrir o arquivo\n");
    else
        while ((ch = fgetc(arq)) != EOF)
        {
            putchar(ch);
        }
    fclose(arq);

    return 0;
}

int Shortest_job_first()
{
}

int processoround_robin()
{
}

int Prioridade()
{
}
int main()
{
    int processo = 0;
    do
    {
        printf("    Escolha o processo! \n\n\n");
        printf("    [1] -> Shortest Job First (SJF)\n");
        printf("    [2] -> Prioridade (PRIO)\n");
        printf("    [3] -> Round­Robin  (RR)\n\n");
        scanf("%d", &processo);
    } while (processo < 1 || processo > 3);

    leitor_arquivo();

    switch (processo)
    {
    case (1):
    {
        Shortest_job_first();
        break;
    }
    case (2):
    {
        Prioridade();
        break;
    }
    case (3):
    {
        processoround_robin();
    }
    }

    return 0;
}