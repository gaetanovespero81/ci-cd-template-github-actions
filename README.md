# CI/CD Template – Python + Pytest + Pylint + Mypy

![CI](https://github.com/gaetanovespero81/ci-cd-template-github-actions/actions/workflows/ci.yml/badge.svg)
![Version](https://img.shields.io/github/v/tag/gaetanovespero81/ci-cd-template-github-actions?label=version)

This repository provides a minimal Python project designed to showcase a modern
CI/CD pipeline using GitHub Actions with the following quality checks:

- ✔ Unit testing with **pytest**
- ✔ Static code analysis with **pylint**
- ✔ Type checking with **mypy**
- ✔ A CI pipeline with **three separate jobs**:
  - `lint` → pylint
  - `type-check` → mypy
  - `tests` → pytest (depends on the other two)

The goal is to offer a clean and professional example of a Python workflow
with proper quality gates and continuous integration.

---

## 📦 Project Structure

├─ src/

| └─ app.py

├─ requirements.txt

├─ tests/
    
| └─ test_app.py

├─ mypy.ini

├─ pytest.ini

├─ .pylintrc.py

├─ .gitignore

└─ .github/

| └─ workflows/

| | └─ ci.yml

---

## 🧪 Running locally

### 1. Create the virtual environment

`python -m venv venv`

`source venv/bin/activate   # Windows: venv\Scripts\activate`

### 2. Install dependencies
`pip install -r requirements.txt`

### 3. Run pylint (static code analysis)

`pylint src/app.py`

### 4. Run mypy (type checking)

`mypy src/app.py`

### 5. Run unit tests

`pytest -v`

### 6. Deactivate the virtual environment

`deactivate`

---

## 👤 Author

*Gaetano Vespero*

*DevOps & Automation Engineer* | *Specialist in CI/CD + AI Workflow Integration*
