![Logo Desenvolve Academia](imgs/logo.png)

## Desenvolve Academia
### Introdução

A Desenvolve é uma rede de academias com equipamentos de qualidade, que trabalha com o modelo de assinatura mensal para que os clientes usufruam de seus benefícios. Possui 3 planos: Básico, Intermediário e Premium, que se referem à quantidade de dias na semana que o cliente frequenta a academia e a alguns benefícios extras, como nutricionista e avaliações de bioimpedância mensais.

### Implementação

- **Organização da academia**: Um CSV com todos os clientes, planos, preços e data de matrícula.
- **Organização de usuários do software**: Um YAML para o gerenciamento de usuários, senhas e permissões de acesso.
- **Planos de Treino**: Um CSV com cada tipo de treino que o cliente tem acesso. O CRUD para as planilhas de treino personalizado seria algo a se pensar no futuro, mas a título de exemplo, deixei modelos padrões para cada cliente.

A ideia é a gestão de acessos com 3 níveis: Admin, Visualizador e Cliente. Essa gestão foi feita através da autenticação do role que cada usuário do software tem em seu cadastro.

- **Admin**: Tem acesso ao CRUD de Clientes e Usuários.
- **Visualizador**: Tem acesso ao Read somente de Clientes.
- **Clientes**: Tem acesso somente aos planos de treino personalizados.

A aplicação foi feita usando Streamlit e Streamlit Authenticator.

### Usuários já cadastrados para teste

- **admin**
- **viewer**
- **customer**

**Senha Padrão para login**: `abcd1234`

### Funcionalidades

- **Painel do Admin**: CRUD de Clientes e Usuários. Basta selecionar a ação desejada e ativar o toggle para os dataframes aparecerem.
- **Painel do Visualizador**: Pesquisa por Cliente e tipo de plano, ambos ou separados.
- **Painel do Cliente**: Seleção de treinos para cada grupo muscular.

### Conclusão

Para mim, o projeto ficou bem completo, faltando apenas um gerenciamento mais personalizado para os clientes, mas para o escopo do trabalho já atenderia ao pedido. Um acerto muito grande foi o uso de funções que facilitaram muito a implementação final e a solução de erros, que foram muitos, principalmente para a manipulação do YAML, que foi um arquivo novo com uma estrutura de dados mais completa e um pouco complexa.

Gostei bastante do resultado e vejo que ainda tenho muito a aprender, mas a criação de uma estrutura de permissões de usuário personalizadas parece não ser um bicho de sete cabeças tão grande como era antes da realização do projeto (isso se eu fiz de uma maneira razoavelmente correta).

Espero que gostem!
