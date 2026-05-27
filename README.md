# Performance em Sistemas Ciberfísicos

Repositório de atividades da disciplina **Performance em Sistemas Ciberfísicos**, do curso de **Bacharelado em Ciência da Computação** da PUCPR.

O material acompanha os temas com foco em técnicas de desempenho para sistemas ciberfísicos, considerando hierarquias de memória, processamento paralelo, comunicação e coordenação entre processos e threads.

## Sobre a disciplina

A disciplina tem natureza teórico-prática e trabalha a análise de concorrência e paralelismo em nível de hardware e sistema operacional. Ao longo do semestre, os exercícios e trabalhos exploram como empregar mecanismos de performance de acordo com a situação-problema e com os recursos computacionais disponíveis.

Temas de estudo:

- **TE1 - Sistemas de Memória**
- **TE2 - Sistemas de Processamento Paralelo**
- **TE3 - Comunicação entre Processos e Threads**
- **TE4 - Coordenação de Processos e Threads**

Resultados de aprendizagem:

- **RA1:** implementar técnicas para reduzir latência em nível de hardware, considerando hierarquias de memória e processamento paralelo.
- **RA2:** implementar programas concorrentes que otimizem o uso do hardware disponível.

## Estrutura do repositório

```text
.
├── formativas/
│   ├── aprox_pi.py
│   ├── arquitetura_basica.py
│   ├── condicao_corrida.py
│   ├── contador.py
│   ├── contador_sem.py
│   ├── contpid-proc.py
│   ├── coverter_decimal.py
│   ├── criacao_processos.py
│   ├── localidade.py
│   ├── memoria_compartilhada.py
│   ├── mutex.py
│   ├── pratica_imprimir_x.py
│   ├── rendezvous.py
│   ├── sinalizacao_basica.py
│   └── vn-basic-singlefile.py
└── trabalhos/
    ├── cache.py
    ├── coerencia_cache.txt
    └── precedencia.py
```

## Atividades formativas

A pasta `formativas/` reúne práticas de aula usadas para fixar os conceitos da disciplina.

Principais tópicos abordados:

- medição simples de desempenho com `time`;
- aproximação de π por série numérica;
- conversão de bases numéricas;
- arquitetura básica de Von Neumann, RAM, CPU e entrada/saída;
- hierarquia e localidade de memória;
- criação de processos com `multiprocessing`;
- identificação de PID e PPID;
- memória compartilhada com `Value`;
- condição de corrida;
- exclusão mútua com semáforos;
- sincronização por sinalização;
- rendezvous entre processos;
- controle de precedência e coordenação de execução.

Esses exercícios se relacionam principalmente aos assuntos de memória, processamento paralelo, programação concorrente e técnicas de exclusão mútua.

## Trabalhos

A pasta `trabalhos/` contém implementações e anotações mais próximas das avaliações práticas.

- `cache.py`: simulação de RAM, cache de mapeamento direto, leitura, escrita, tratamento de miss e linha suja.
- `coerencia_cache.txt`: registro conceitual de transições de estado em coerência de cache entre dois processadores.
- `precedencia.py`: implementação de um grafo de precedência usando processos e semáforos, coordenando a ordem de execução entre tarefas.

## Como executar

Os exemplos foram escritos em Python e podem ser executados individualmente.

Requisitos:

- Python 3 instalado;
- terminal ou PowerShell;
- bibliotecas padrão do Python, especialmente `time`, `os`, `threading` e `multiprocessing`.

Exemplos:

```powershell
python formativas\aprox_pi.py
python formativas\mutex.py
python trabalhos\cache.py
python trabalhos\precedencia.py
```

Alguns programas executam laços longos, imprimem muitas linhas ou criam processos. Em especial, `aprox_pi.py`, `localidade.py` e `pratica_imprimir_x.py` podem consumir mais tempo ou recursos dependendo da máquina.

## Cronograma relacionado

Pelo plano de ensino, os conteúdos do repositório acompanham especialmente as aulas sobre:

- Arquitetura Von Neumann/Harvard;
- hierarquia de memória;
- memória cache;
- gerência de memória, paginação e memória virtual;
- pipeline, paralelismo e arquiteturas paralelas;
- processos e threads;
- programação concorrente e compartilhamento de memória;
- condição de corrida;
- exclusão mútua;
- problemas clássicos de sincronização de processos;
- escalonamento de processos.
