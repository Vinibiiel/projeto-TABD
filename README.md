# PROJETO
CC6240 - TÓPICOS AVANÇADOS DE BANCOS DE DADOS

## MongoDB(Document Storage)

### COMO RODAR O PROJETO:
- Criar uma env: 
    - python -m venv env
- Entrar na env e instalar as dependencias: 
    - source env/bin/activate (linux distro) ou .\env\Scripts\activate (windows)
    - pip install -r requirements.txt
- Configurar o script:
    - Primeiro ir até o arquivo connect.py, e colocar o endereço do mongo onde o codigo irá rodar;
- Rodar os scripts:
    - Rodar o script de inserção de dados (Se caso for um banco novo)
    - Rodar o script de seleção dos dados (queries)



#### Observações
Eu deixei os códigos que usei pra parsear o SQL para json, para que eu pudesse utilizar no pymongoa
O nome do parser é parse_sql. Para fim de curiosidade, utiliza regex