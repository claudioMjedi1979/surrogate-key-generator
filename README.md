Biblioteca(LIB) de Geração de Chaves Surrogate

Biblioteca em Python para gerar chaves surrogate mascarando IDs usando algoritmos de hashing. Esta biblioteca foi 
desenvolvida para facilitar a criação de chaves surrogate para IDs de banco de dados ou outros identificadores, 
com suporte para adicionar um salt, proporcionando maior segurança e singularidade.

Contexto de Uso
Inicialmente, a ideia era utilizar esta biblioteca diretamente no Databricks, porém, 
ao testar no Databricks Community Edition, observou-se que o processo de instalação de bibliotecas pode ser bastante demorado, 
devido à capacidade limitada dessa versão gratuita. Em alguns casos, a instalação pode levar mais de 40 minutos para ser concluída.

<img width="1186" alt="image" src="https://github.com/user-attachments/assets/9da1b4a8-e041-43b1-85b1-247326b162cb">

Por isso, para fins de teste e validação do código, a biblioteca foi executada diretamente em um notebook como uma solução temporária 
para garantir que a funcionalidade básica estava operando corretamente.

Se você estiver utilizando o Databricks Community Edition, recomendamos seguir o mesmo caminho de teste 
diretamente no notebook para verificar se o código funciona antes de tentar empacotar e instalar a biblioteca.

<img width="1395" alt="image" src="https://github.com/user-attachments/assets/1b8badb2-fb46-407e-889d-5ab0a93fb42b">



