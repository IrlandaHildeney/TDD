Universidade Federal do Maranhão – UFMA
Bacharelado Interdisciplinar em Ciência e Tecnologia
Disciplina: Engenharia de Software
Alunos: Irlanda Hildeney
  Hamilton Luis


Trabalho sobre TDD
Requisitos Funcionais: 
RF1 – Adicionar produto 
RF2 – Deletar produto
RF3 – Fazer update do produto 
RF4 – Listar todos os produtos 
RF5 – Consultar um produto


Caso de uso para RF1 – Adicionar produto:
Fluxo principal: 
•	Selecionar a opção adicionar” novo produto”; 
•	O sistema solicita o preenchimento de dados como código do produto, nome e descrição;
•	O usuário preenche os dados corretamente;
•	Sistema registra o produto o novo produto; 
•	Sistema exibe uma mensagem na tela de confirmação do registro; 
Fluxo alternativo: 
•	Se o usuário escolher uma opção inexistente, sistema irá exibir um alerta. 
•	Se usuário digitar letras no campo de inserir código, sistema apresentará uma mensagem de erro.


RF2 – Deletar produto: 
Fluxo principal:
•	O caso de uso começa quando o usuário seleciona a opção para exibir lista de produtos registrados no sistema. 
•	O sistema exibe os produtos cadastrados.
•	O usuário escolhe a opção “Deletar produto” e insere o código do produto.
•	O produto é excluído e uma mensagem de confirmação é exibida
 Fluxo alternativo:
•	Se o usuário informar um código inexistente uma mensagem de erro será apresentada.
 Caso de uso para RF3 – Fazer update do produto:
 Fluxo principal:
•	O caso de uso começa quando o usuário acessa o menu com as opções.
•	O usuário seleciona a opção “atualizar do produto”. 
•	O sistema pergunta qual o código do produto a ser atualizado. 
•	Sistema pede que o usuário insira os novos dados do produto.
•	Usuário informa e confirma os dados
•	O sistema atualiza o produto aplicando alterações. 
•	Sistema exibe mensagem de sucesso na atualização do produto. 
Fluxo alternativo: 
•	Se o usuário selecionar um produto inexistente, o sistema exibirá uma mensagem de erro na tela. 


Caso de uso para RF4 – Listar todos os produtos: 
Fluxo principal:
•	Com a tela inicial exibida na tela, o usuário seleciona a opção de visualização de produtos cadastrados no sistema. 
•	O sistema exibe a lista de produtos cadastrados, incluindo suas características. Fluxo alternativo: 


Caso de uso para RF5 – Consultar um produto: 
Fluxo principal:
•	Com a tela inicial exibida na tela, o usuário seleciona um produto específico para consulta. 
•	O sistema exibe informações detalhadas sobre esse produto e caso de uso é encerrado.
Fluxo alternativo:
•	Se o usuário digitar uma opção inválida, o sistema apresentará um erro.



