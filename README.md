# Run

## With Docker

```
docker build . -t rafrafek/playground:0.1.0
```

```
docker run --name=playground -p 127.0.0.1:8000:8000 rafrafek/playground:0.1.0
```

## Without Docker

Install `pyenv` and `Poetry`.

Then:

```
pyenv install 3.11.0
```

```
poetry install
```

```
uvicorn playground.app:app
```

# Develop

Install `pyenv` and `Poetry`.

Then:

```
pyenv install 3.11.0
```

```
poetry install --with dev
```

```
pre-commit install
```

Run all pre-commit hooks whenever you need:

```
pre-commit run -a
```

# Test

Install everything from Develop step.

Then:

```
pytest
```
