# dochelper

Core library with the AI components used to build DocHelper.

## Install

From the repository root:

```shell
pip install -e "libs/dochelper[dev]"
```

## Development

- Create a conda environment (3.10 suggested)

  ```shell
  conda create -n dochelper python=3.10
  conda activate dochelper
  ```

- Install with dev dependencies

  ```shell
  pip install -e ".[dev]"
  ```

- Pre-commit

  ```shell
  pre-commit install
  ```

- Test

  ```shell
  pytest tests
  ```

## Credentials

Credentials are read from environment variables via `python-dotenv`. Keep a local
`.env` file for development and never commit it. `.env` usage is for development
only; it should not be relied on inside the main source code (`dochelper/` and
`tests/`).

## Code base structure

- documents: define document
- loaders
