# Exercícios de Python - EDN

**Autor:** Kayky Brito Silva  
**Email:** kaykybritosilva23@gmail.com  
**Data:** 29 de junho de 2025

## Descrição

Este repositório contém soluções para exercícios de programação em Python, organizados em 7 atividades principais. Cada atividade aborda conceitos fundamentais da linguagem Python, desde operações básicas até manipulação de arquivos e análise de dados.

## Estrutura do Projeto

```
pythonexamplesstudiesEDN/
├── README.md
├── requirements.txt
├── atividade1/
│   ├── 1_saudacao.py
│   ├── 2_calculadora_soma.py
│   ├── 3_calculadora_volume.py
│   ├── 4_calculadora_preco_total.py
│   └── 5_calculadora_numero_inteiro.py
├── atividade2/
│   ├── 1_conversor_moeda.py
│   ├── 2_calculadora_desconto.py
│   ├── 3_calculadora_media_escolar.py
│   ├── 4_calculadora_consumo_combustivel.py
│   ├── 5_calculadora_soma_entrada_usuario.py
│   └── 6_calculadora_salario_horas.py
├── atividade3/
│   ├── 1_area_circunferencia.py
│   ├── 2_classificador_idade.py
│   ├── 3_calculadora_imc.py
│   ├── 4_conversor_temperatura.py
│   ├── 5_verificador_ano_bissexto.py
│   ├── 6_calculadora_comissao.py
│   └── 7_calculadora_media.py
└── atividade4/
    ├── 1_calculadora_com_erros.py
    ├── 2_registro_notas.py
    ├── 3_verificador_senha.py
    └── 4_contador_par_impar.py
└── atividade5/
    ├── 1_calculadora_gorjeta.py
    ├── 2_verificador_palindromo.py
    ├── 3_calculadora_desconto.py
    └── 4_calculadora_idade_dias.py
└── atividade6/
    ├── 1_gerador_senha.py
    ├── 2_perfil_usuario_aleatorio.py
    ├── 3_consulta_cep.py
    └── 4_consulta_cotacao.py
└── atividade7/
    ├── 1_log_ml_estatisticas.py
    ├── 2_escrever_csv.py
    ├── 3_ler_csv.py
    └── 4_json_pessoa.py
```

## Atividades

### 📁 Atividade 1 - Conceitos Básicos
Exercícios introdutórios focados em operações básicas e manipulação de variáveis:

1. **Programa de Saudação** - Imprime "Hello, world!"
2. **Calculadora de Soma** - Soma dois números predefinidos
3. **Calculadora de Volume** - Calcula volume de caixa retangular
4. **Calculadora de Preço Total** - Calcula preço total de uma compra
5. **Calculadora de Número Inteiro** - Calcula diferença entre produtos

### 📁 Atividade 2 - Operações e Entrada de Dados
Exercícios com cálculos mais elaborados e entrada do usuário:

1. **Conversor de Moeda** - Converte reais para dólar e euro
2. **Calculadora de Desconto** - Calcula desconto em produtos
3. **Calculadora de Média Escolar** - Calcula média de notas
4. **Calculadora de Consumo** - Calcula consumo de combustível
5. **Soma com Entrada** - Soma números inseridos pelo usuário
6. **Salário por Horas** - Calcula salário baseado em horas trabalhadas

### 📁 Atividade 3 - Estruturas Condicionais e Cálculos Avançados
Exercícios com estruturas condicionais e algoritmos mais complexos:

1. **Área da Circunferência** - Calcula área usando π
2. **Classificador de Idade** - Classifica idade em categorias
3. **Calculadora de IMC** - Calcula IMC e classifica resultado
4. **Conversor de Temperatura** - Converte entre C°, F° e K
5. **Verificador de Ano Bissexto** - Verifica se ano é bissexto
6. **Calculadora de Comissão** - Calcula comissão de vendedor
7. **Calculadora da Média** - Sistema completo de média escolar

### 📁 Atividade 4 - Tratamento de Erros e Validação
Exercícios focados em tratamento de exceções e validação de dados:

1. **Calculadora com Tratamento de Erros** - Calculadora com try/except
2. **Registro de Notas** - Sistema de notas com validação
3. **Verificador de Senha** - Valida força de senhas
4. **Contador Par/Ímpar** - Conta números pares e ímpares

### 📁 Atividade 5 - Funções e Aplicações Práticas
Exercícios com funções e aplicações do mundo real:

1. **Calculadora de Gorjeta** - Calcula gorjeta em restaurantes
2. **Verificador de Palíndromo** - Verifica se texto é palíndromo
3. **Calculadora de Desconto** - Calcula preço com desconto
4. **Calculadora de Idade em Dias** - Converte idade para dias

### 📁 Atividade 6 - APIs e Módulos Externos
Exercícios com APIs externas e módulos avançados do Python:

1. **Gerador de Senha** - Gera senhas aleatórias personalizáveis
2. **Perfil de Usuário Aleatório** - Usa API Random User Generator
3. **Consulta de CEP** - Consulta endereços via API ViaCEP
4. **Consulta de Cotação** - Cotações de moedas via AwesomeAPI

### 📁 Atividade 7 - Manipulação de Arquivos e Análise de Dados
Exercícios focados em leitura/escrita de arquivos e análise estatística:

1. **Análise de Log ML** - Calcula estatísticas de tempos de execução
2. **Escrever CSV** - Cria arquivo CSV com dados pessoais
3. **Ler CSV** - Lê e exibe dados de arquivo CSV
4. **Manipular JSON** - Lê e escreve dados em formato JSON

## Como Executar

### Instalação de Dependências

Para executar os programas da **Atividade 6**, você precisa instalar a biblioteca `requests`:

```bash
pip install -r requirements.txt
```

Ou instalar manualmente:
```bash
pip install requests
```

### Executando os Programas

Para executar qualquer programa, navegue até a pasta correspondente e execute:

```bash
python nome_do_arquivo.py
```

Exemplo:
```bash
cd atividade1
python 1_saudacao.py
```

## Tecnologias Utilizadas

- **Python 3.x** - Linguagem de programação principal
- **Conceitos abordados:**
  - Variáveis e tipos de dados
  - Operações matemáticas
  - Entrada e saída de dados
  - Estruturas condicionais (if/elif/else)
  - Formatação de strings
  - Operadores lógicos e relacionais
  - Tratamento de exceções (try/except)
  - Validação de dados
  - Funções personalizadas
  - Loops e estruturas de repetição
  - Módulos e bibliotecas externas
  - Requisições HTTP (requests)
  - Manipulação de APIs REST
  - Geração de dados aleatórios
  - Manipulação de arquivos (leitura/escrita)
  - Processamento de dados CSV e JSON
  - Análise estatística básica
  - Módulo statistics do Python

## Observações

- Todos os programas foram desenvolvidos seguindo as especificações exatas dos exercícios
- Formatação de saída conforme solicitado em cada exercício
- Tratamento adequado de casas decimais quando necessário

---

**Desenvolvido como parte dos estudos em Python - EDN**