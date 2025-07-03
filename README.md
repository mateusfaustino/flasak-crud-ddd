# Flask CRUD DDD Example

This project demonstrates a simple Domain Driven Design (DDD) structure for a Flask 2.3 application with JWT based authentication and product CRUD endpoints.

## Setup

Install dependencies (which include Flask-SQLAlchemy) and run the application:

```bash
pip install -r requirements.txt
python -m flask db upgrade  # run migrations
python -m app.main
```

After running the application you can access the interactive API documentation
provided by Swagger at `http://localhost:5000/apidocs/`.

### Configuração com MySQL

A aplicação foi preparada para usar o MySQL como banco de dados padrão. Os
detalhes de conexão podem ser ajustados por meio das seguintes variáveis de
ambiente:

- `DB_HOST` (padrão `localhost`)
- `DB_PORT` (padrão `3306`)
- `DB_USER` (padrão `user`)
- `DB_PASSWORD` (padrão `password`)
- `DB_NAME` (padrão `appdb`)

Você também pode definir `DATABASE_URI` com a URI completa de conexão. O arquivo
`docker-compose.yml` já fornece essas variáveis e sobe um contêiner MySQL pronto
para uso.

## Arquitetura

Este projeto segue uma separação em três camadas principais (domínio, serviços e adapters).
Uma descrição detalhada de como elas se relacionam e como podem ser estendidas está em
[docs/architecture.md](docs/architecture.md).
