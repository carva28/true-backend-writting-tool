# true-backend-writting-tool
## Backend do Projeto TRUE.


Para se proceder à instalação da API que retorna as palavras com erros ortográficos e das entidades numa frase, desenvolvida em Python, deve-se instalar no servidor o Python (https://www.python.org/downloads/). Para verifficar se o python foi instalado corretamente verifica-se a versão do python através do comando python –v (e certificar que a versão do python3 está instalada na máquina - no caso de Linux/Mac). 

De seguida, deve-se instalar as bibliotecas necessárias para correr o algoritmo, que se encontram no ficheiro requeriments.txt. Para isso, basta correr o comando pip install -r requirements.txt (verificar ficheiro requierements.txt na pasta). Caso contrário deverá instalar as seguintes bibliotecas: 

### Pienchant: 

``` pip install pyenchant (Comum aos SO’s) ```

``` pkg install enchant2 (LINUX) ```

``` brew install enchant (MAC) ```

Ainda nesta fase será necessário adicionar os ficheiros do dicionário Hunspell em PT-pt  (ver na raiz desta pasta), dentro da pasta ``` lib/hunspell ``` (https://localcoder.org/pyenchant-cant-find-dictionary-file-on-mac-os-x) - no Windows a pasta encontra-se no seguinte caminho: ``` C:\Users\user\local_pasta_projeto\env\Lib\site-packages\enchant\data\mingw64\share\enchant\hunspell ``` 

### Spacy: 

``` pip install -U pip setuptools wheel ``` 

``` pip install -U spacy ```

``` python -m spacy download en_core_web_sm ``` 

``` python -m spacy download pt_core_news_sm ``` 

### FLASK 

``` pip install Flask ``` 

``` pip install -U flask-cors ```

Para o caso do windows deve-se instalar um virtual environment, (python3 -m venv venv). Depois correr o ficheiro  ``` . venv/bin/activate ```.  


Após lhe aparecer: “(env) nome_do_seu_local_onde_se_encontra_a_aplicação” pode-se correr a API. 

Para adicionar palavras ao Dicionário, basta incluir novas palavras no ficheiro palavras.txt  

Para ativar o virtual envirnoment deve-se correr o seguinte comando: 

``` venv\Scripts\activate.bat ```



