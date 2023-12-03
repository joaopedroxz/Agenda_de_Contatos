1. Título:
  Agenda de Contatos:
  Uma agenda de contatos com funções adicionais, como adição de categoria aos contatos, filtragem por categoria escolhida e direcionamento para conversa no WhatsApp. codigo feito em phyton

2. Autores:
  Xotape - 231021478
  Roberth Nascimento de Jesus - 231021487
  Jon 231021342
  
3. Contexto de Aplicação:
  Com o objetivo de armazenar dados de um contato em uma lista, de forma que tenhamos livre acesso para fazer a travessia, foi escolhida a estrutura de lista duplamente encadeada. Essa lista possui o comportamento de fila, com a intenção de que os primeiros dados a serem inseridos na lista devem ser também os primeiros a serem processados. Os dados são inseridos no fim da lista e são removidos e processados no início da lista.
Ordenação após inserção:

4. Estruturas de Dados Utilizadas:
  Lista duplamente encadeada com comportamento de fila:
  Armazenamento dos dados com livre travessia entre eles, armazenamento e processamento de dados com a regra de que o primeiro contato inserido é sempre o primeiro a ser processado. Estruturas relevantes para dar ordem nos processamentos e armazenamento de dados de forma que facilite a implementação de operações que envolvem manipulação de nós adjacentes.

5. Ordenação após inserção:
   Foi implementado o insertion sort:
   1 - Ao adicionar um novo contato na lista encadeada, o algoritmo verifica a posição correta com base no nome para manter a ordem alfabética.
Ordenação em Tempo Real:
  2 - Durante a inserção de um novo contato, este é posicionado na lista encadeada de forma a manter a ordem alfabética existente.
Comparação de Nomes:
  3 - O algoritmo compara o nome do novo contato com os nomes dos contatos existentes na lista para encontrar a posição adequada de inserção.
Manutenção da Ordem:
  4 - A inserção ocorre respeitando a ordem alfabética, garantindo que a lista permaneça ordenada após cada adição.
Estrutura da Lista Preservada:
A ordenação ocorre sem a necessidade de reorganizar toda a lista, apenas ajustando os ponteiros entre os contatos para manter a estrutura encadeada.
  Essa abordagem permite que a lista encadeada seja organizada alfabeticamente pelos nomes completos dos contatos, garantindo que a inserção de novos contatos mantenha a ordem correta na lista.

7. Instruções de Execução:
Para usar o código, é necessário ter instalada em seu idle a biblioteca Streamlit.
Para instalar a biblioteca, vá até o terminal e digite "pip install streamlit" e aguarde a instalação. Com a biblioteca instalada, vá até o terminal e execute o Streamlit com o comando "streamlit run projeto.py", onde "projeto.py" deve ser substituído pelo nome do arquivo onde está o código. O Streamlit fornecerá um link para acessar a aplicação.

8. Instruções de Uso:
Para utilizar o programa, é necessário inserir dados de nome, categoria e número, e confirmar cada funcionalidade.
As funcionalidades do programa incluem: adicionar contato com nome, categoria e número (o número obrigatoriamente com 11 dígitos, pressione Enter após a adição dos 11 dígitos), remover contato digitando um nome, buscar por nome com campo de pesquisa e resultado exibindo o nome pesquisado com botão de direcionamento para o WhatsApp, buscar por categoria com campo de pesquisa e resultado exibindo todos os contatos com determinada categoria. Botão para atualizar a página.

8.Referências:
  - Slides fornecidos pela professora
  - Codigos github professora Geovana
  - Descobrimos o streamlit em um post do instragam: https://www.instagram.com/p/Czw1zH6tydC/?igshid=MzRlODBiNWFlZA==
  - Video do canal "hashtag Programação" para saber mais sobre a biblioteca: https://youtu.be/0sxWFeFlsHs?si=PnccEu3YLrPOcYe7
  - Site com documentação do streamlit: https://docs.streamlit.io
