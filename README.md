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
    

# Exemplo lerTxt()
 - conteudo = lerTxt('arquivo.txt')
 - Irá retornar uma lista com o conteúdo separado pelas linhas




# Exemplo gravarNoTxt()
 - gravarNoTxt('arquivo.txt', 'Adoro manhãs de Sábado')
 - Uma nova linha com o conteúdo 'Adoro manhãs de Sábado' será adicionada ao final do .txt
      
      


# Exemplo atualizarTxt()
 - atualizarTxt('arquivo.txt', 'Minha cor favorita é azul', 'Minha cor favorita é vermelho')

Está função irá procurar linha por linha pelo conteúdo antigo, ao encontrá-lo
irá fazer a substituição dele pelo novo conteúdo fornecido nos parâmetros,
note que ao buscar o conteúdo antigo, a função vai substituir todas as linhas em que
o que foi passado for igual, então é convêniente passar exatamente todo o conteúdo
da linha que se deseja fazer a atualização de conteúdo
