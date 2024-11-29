



Plataforma de Crowdfunding para Startups

Este projeto é uma plataforma de crowdfunding criada em Django, que conecta empreendedores e investidores. Empreendedores podem cadastrar suas empresas ou ideias, enquanto investidores encontram oportunidades para investir em startups ou novos negócios.

Estrutura do Projeto

A estrutura do projeto está dividida em diversas pastas, com cada uma representando uma funcionalidade ou componente específico:

 1. GitHub Workflows
- Pasta: `github/workflows`
- Arquivo: `django.yml` 
    - Configuração para integração e deploy contínuo usando GitHub Actions.

2. Core
- Função: Gerenciamento central da aplicação Django, incluindo as configurações globais.
- Arquivos:
  - `__init__.py`: Inicializador do módulo.
  - `asgi.py`: Configuração para ASGI.
  - `settings.py`: Configuração geral do Django (banco de dados, apps instalados, etc.).
  - `urls.py`: Rotas principais do projeto.
  - `wsgi.py`: Configuração para WSGI.

 3. Empresários
- Função: Gerenciamento de empresas e startups cadastradas pelos empreendedores.
- Subcomponentes:
  - Migrations: Scripts para versionamento do banco de dados.
  - Templates: Arquivos HTML para exibição das páginas (cadastro de empresa, lista de empresas, etc.).
  - Models.py: Modelos representando os dados das empresas e suas métricas.
  - Views.py: Lógica das páginas e interações.
  - URLs.py: Rotas específicas para os recursos de empresários.

 4. Investidores
- Função: (A ser implementado) Gerenciamento do acesso dos investidores à plataforma.

---

## **Funcionalidades**

1. **Cadastro de Empresas**
   - Empreendedores podem cadastrar startups, incluindo documentos e métricas.
2. **Listagem de Startups**
   - Investidores podem visualizar as startups disponíveis para investimento.
3. **Detalhes da Startup**
   - Informações detalhadas sobre cada empresa, incluindo métricas e documentação.

---

## **Instalação**

Siga os passos abaixo para configurar o ambiente e executar o projeto:

### **Requisitos**
- Python 3.10 ou superior
- Pipenv (gerenciador de ambiente virtual)
- Banco de dados configurado (ex.: SQLite ou PostgreSQL)

### **Passos**
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Instale as dependências:
   ```bash
   pipenv install
   ```

3. Ative o ambiente virtual:
   ```bash
   pipenv shell
   ```

4. Configure o banco de dados em `core/settings.py`.

5. Aplique as migrações:
   ```bash
   python manage.py migrate
   ```

6. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

7. Acesse o sistema no navegador:
   ```
   http://127.0.0.1:8000/
   ```

---

## **Tecnologias Utilizadas**

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Banco de Dados**: SQLite (padrão do Django)
- **Integração Contínua**: GitHub Actions

---

## **Roadmap**

- [x] Cadastro de empresas
- [x] Listagem de startups
- [ ] Implementação do módulo de investidores
- [ ] Funcionalidade de busca avançada
- [ ] Integração com meios de pagamento

---

## **Como Contribuir**

1. Faça um fork deste repositório.
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b feature/nome-da-feature
   ```
3. Faça commit das suas alterações:
   ```bash
   git commit -m 'Adicionando nova feature'
   ```
4. Faça push para sua branch:
   ```bash
   git push origin feature/nome-da-feature
   ```
5. Abra um Pull Request.

---

## **Licença**

Este projeto está licenciado sob a [MIT License](LICENSE).

---

Com este README.md, o seu projeto terá uma documentação completa e organizada, facilitando a colaboração de outros desenvolvedores e o entendimento das funcionalidades pelos usuários.
