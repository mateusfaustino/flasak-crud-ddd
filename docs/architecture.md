# Arquitetura da Aplicação

Este projeto segue uma estrutura inspirada em Domain Driven Design (DDD). Abaixo explicamos cada camada e como você pode estender ou substituir suas partes.

## Domínio

A camada de domínio contém as **entidades** e as **interfaces de repositório**. As entidades definem os dados principais do sistema, enquanto as interfaces descrevem as operações de persistência necessárias. Elas ficam em `app/domain`.

Para adicionar novas funcionalidades:

- Crie novos dataclasses em `app/domain/entities.py` para representar novos tipos de dados.
- Defina novas interfaces ou expanda as existentes em `app/domain/repositories.py` se precisar de outras operações.

## Serviços

Os serviços implementam a lógica de negócio utilizando as interfaces definidas no domínio. Eles residem em `app/services`. Cada serviço recebe um repositório que segue a interface do domínio, permitindo trocar a implementação facilmente.

Para estender ou substituir:

- Adicione métodos aos serviços existentes ou crie novos serviços em `app/services`.
- Passe implementações diferentes de repositório ao instanciar o serviço. Isso acontece em `app/__init__.py`, onde os serviços são criados e adicionados ao app Flask.

## Adapters

Adapters são implementações concretas das interfaces de repositório. No projeto, usamos SQLAlchemy e os adapters ficam em `app/adapters/sqlalchemy`. Caso queira usar outro mecanismo de persistência (por exemplo, uma API externa ou outro banco de dados), implemente as mesmas interfaces em outro módulo e forneça essas classes ao criar o app.

Para trocar a camada de persistência:

1. Crie novas classes seguindo as interfaces de `app/domain/repositories.py`.
2. No `create_app` em `app/__init__.py`, instancie seus repositórios personalizados e passe-os aos serviços.

Dessa forma, cada camada permanece independente e você pode evoluir o sistema substituindo partes específicas sem alterar o restante da aplicação.
