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

## Arquitetura

Este projeto segue uma separação em três camadas principais (domínio, serviços e adapters).
Uma descrição detalhada de como elas se relacionam e como podem ser estendidas está em
[docs/architecture.md](docs/architecture.md).
