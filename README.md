# Alerta+ | Verificador de Enchentes

## Visão Geral
O **Alerta+** é uma ferramenta de linha de comando em Python destinada a apoiar a população em situações de risco de enchentes. A aplicação coleta dados de temperatura e umidade, calcula o nível de risco de enchente e indica a rota de fuga adequada para a cidade informada. Os registros de alerta são armazenados em arquivos de texto e em planilhas Excel para consulta futura.

## Funcionalidades Principais
- Coleta interativa de informações: cidade, bairro, temperatura (ºC) e umidade (%).  
- Cálculo de risco: classificação como "Sim" ou "Não" com base em parâmetros definidos (temperatura > 30°C e umidade > 90%).  
- Consulta de rotas de fuga pré-definidas para diversas cidades brasileiras.  
- Registro de logs em arquivo TXT (`alerta.txt`) e arquivo Excel (`alerta.xlsx`).

## Pré-requisitos
- Python 3.7 ou superior  
- Biblioteca `pandas` (para manipulação e armazenamento dos dados em Excel)  

## Instalação
1. Clone este repositório:
   ```bash
   git clone https://seu-repositorio.git
   cd alerta-plus
   ```
2. Instale as dependências:
   ```bash
   pip install pandas openpyxl
   ```

## Como Executar
No terminal, dentro da pasta do projeto, execute:
```bash
python alerta.py
```  
Siga as instruções na tela para informar cidade, bairro, temperatura e umidade. Ao final, serão exibidos:
- Localização informada (bairro e cidade).  
- Temperatura e umidade fornecidas.  
- Indicação de risco de enchente.  
- Rota de fuga correspondente.

## Estrutura do Código
```text
├── alerta.py         # Script principal de execução
├── alerta.txt        # Arquivo de log em formato TXT (gerado automaticamente)
└── alerta.xlsx       # Planilha Excel com registros de alertas (gerado automaticamente)
```

### Principais Funções
- `obter_rota(cidade)`: retorna a rota de fuga cadastrada para a cidade ou uma mensagem genérica caso não exista cadastro.  
- `salvar_dados(dados, arq_txt, arq_xlsx)`: registra o alerta em `alerta.txt` e adiciona a entrada à planilha `alerta.xlsx`.  
- `main()`: orquestra a coleta de dados do usuário, cálculo de risco e exibição de resultados.

## Contribuidores
- Alexandre Colvet Delfino (RM 560059)  
- Enzo Luciano Barros de Oliveira (RM 559557)  
- Lívia Pereira Dias Correa (RM 559414)

---
*Projeto desenvolvido como parte da disciplina de WebDev do curso Global Solution.*
