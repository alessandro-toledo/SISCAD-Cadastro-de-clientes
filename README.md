<h1> SISCAD - Cadastro de clientes </h1>
<h2> Sistema simples e rápido para cadastro básico de clientes de uma loja de roupas</h2>

<h3>Descrição</h3>
Sistema desenvolvido em linguagem Python com funções básicas (CRUD) e banco de dados SQLite. A interface gráfica (frontend) utiliza Tkinter. O sistema será utilizado numa loja de roupas e acessórios. O objetivo é ser o mais simples possível, não pesando na infraestrutura local e ser bastante intuitivo ao usuário. O sistema conterá o cadastro básico de clientes com os dados principais.

<h3>Funções</h3>
No menu “Cadastro de Clientes” há as funções “Cadastrar”, “Consultar”, “Alterar” e “Excluir”.
É possível acessar as funções também por botões na área de trabalho com "Cadastrar cliente", "Consultar cliente", "Alterar cliente" e "Excluir cliente".

<h3>Estrutura</h3>
O sistema, por sua simplicidade, apresenta os artefatos principais:
1. Principal.py – Arquivo principal onde ocorre toda a movimentação tanto de backend quanto de frontend, desenvolvidos em Python; 
2. itemdb – Banco de dados para persistência dos registros, desenvolvido em SQLite.
3. Scripts para conexão com banco de dados e janelas do Tkinter.

<h3>Tecnologias utilizadas</h3>
A linguagem de programação utilizada foi Python versão 3.11.3, desenvolvido em Visual Studio Code versão 1.78.2. Todo o sistema foi criado dentro de ambiente Linux Debian. O banco de dados utilizado foi SQLite versão 3.42. Testes foram rodados em Windows nas versões 10 e 11 e em Linux Debian.

<h3>Como usar</h3>
O sistema tem funcionamento local e foi projetado para uma única máquina. Assim, basta a instalação do Python e, eventualmente, SQLite. O acesso ao sistema se dá pelo arquivo "Principal.py". Com clique duplo o sistema é executado automaticamente, não sendo necessários maiores requisitos.

<h3>Requisitos do sistema</h3>
Para a instalação do sistema são necessários mínimos 4Gb de memória RAM, 1GB de espaço em disco disponível e processador Intel i3 ou similar. Esta mesma configuração pode ser utilizada para o uso diário do sistema.

<h3>Como contribuir para o projeto</h3>
Contribuições sempre são bem vindas. Para contribuir, entre em contato através do email alessandrosilva@toledoprudente.edu.br.

<h3>Práticas de código limpo</h3>
1. Na medida do possível, foram utilizados nomes de variáveis e funções fáceis de identificar;
2. Blocos que dizem respeito ao mesmo objetivo foram agrupados;
3. Métodos e funções com nomes de verbos e no infinitivo;
4. Código simples de ser entendido;
5. Código simples de ser testado;
6. Reaproveitamento constante.

<h3>Testes</h3>
Após a compilação do código, foi utilizado Selenium para testes. Resultados não demonstraram erros.
