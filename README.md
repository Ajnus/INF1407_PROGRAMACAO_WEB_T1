# INF1407_T1


Participantes: 

Miguel Garcia - 2120240
Jam Ajna Soares - 2211689


# THE FORUM

# O que é o THE FORUM?

THE FORUM é o nosso projeto, o qual se baseia em um forum online.

# Como funciona o THE FORUM?

Nele, o usuario terá acesso a uma lista de publicações, em que ele pode criar novas e alterar/deletar as suas.

Além disso, o usuario pode adicionar comentarios a uma publicação, independente se é sua ou de um terceiro.

Importante lembrar que, como a maioria dos foruns, o THE FORUM é publico, mas para ver os textos das publicacoes e poder criar seus proprios é necessario autenticação.

# Guia de instalação

1) Clone o repositorio com:

git clone https://github.com/miguelpgarcia/INF1407_T1.git

2) Dentro do repositorio, ativa o ambiente virtual:

source venv/bin/activate

3) Instale os requirements

pip install -r requirements.txt

4) Execute o app

python3 manage.py runserver



# O que foi implementado

Foi implementado autenticação completa, o CRUD completo de Publicações e CRD completo de Comentarios (na nossa concepção, não faz sentido editar comentarios) 


# O que não foi implementado

Durante o projeto tivemos mudanças de requisitos e optamos por fazer um Usuario com username, email e senha, sem considerar a data de nascimento que concluimos que não é tão relevante. Além disso, não conseguimos fazer a funcionalidade de "esqueci minha senha" mandar o email de fato.



