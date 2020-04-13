Uma biblioteca básica para trabalhar com arquivos .txt

Esta lib foi criada no intuíto de ajudar novos usuários de Python a manipular
arquivos do tipo .txt, visto que para quem está começando, trabalhar com o conceito de open(),
readlines e writelines pode ser um pouco díficil

Sinta-se livre para modificar a biblioteca para melhor se adaptar ao seu projeto

A biblioteca contém apenas 3 funções:
  - letTxt(nomeDoTxt)
  - gravarNoTxt(nomeDoTxt, novoConteudo)
  - atualizarTxt(nomeDoTxt, novoConteudo, antigoConteudo)
  
  
-> Abaixo segue um exemplo de utilização e resultado de cada função <-
    
   arquivo.txt:  # .txt ficticio
      123 João Neto
      Rua dos Vagalumes, 987
      Minha cor favorita é vermelho
      O Sol no inverno é extremamente confortável



import pyTXT  # Exemplo lerTxt()
conteudo = lerTxt('arquivo.txt')
print(conteudo)
['123 João Neto\n', 'Rua dos Vagalumes, 987\n', 
'Minha cor favorita é vermelho\n', 'O Sol no inverno é extremamente confortável']
 lerTxt() irá retornar uma lista com o conteúdo separado pelas linhas





import pyTXT  # Exemplo gravarNoTxt()
gravarNoTxt('arquivo.txt', 'Adoro manhãs de Sábado')
  Uma nova linha com o conteúdo 'Adoro manhãs de Sábado' será adicionada ao final do .txt

arquivo.txt:  # Ao abrir o .txt, o novo texto estará no final do arquivo
      123 João Neto
      Rua dos Vagalumes, 987
      Minha cor favorita é vermelho
      O Sol no inverno é extremamente confortável
      Adoro manhãs de Sábado
      
      


import pyTXT  # Exemplo atualizarTxt()
atualizarTxt('arquivo.txt', 'Minha cor favorita é azul', 'Minha cor favorita é vermelho')

  Está função irá procurar linha por linha pelo conteúdo antigo, ao encontrá-lo
 irá fazer a substituição dele pelo novo conteúdo fornecido nos parâmetros,
 note que ao buscar o conteúdo antigo, a função vai substituir todas as linhas em que
 o que foi passado for igual, então é convêniente passar exatamente todo o conteúdo
 da linha que se deseja fazer a atualização de conteúdo

 Após a chamada da função, o .txt deve ser o seguinte:
arquivo.txt:
      123 João Neto
      Rua dos Vagalumes, 987
      Minha cor favorita é azul
      O Sol no inverno é extremamente confortável
      
      
