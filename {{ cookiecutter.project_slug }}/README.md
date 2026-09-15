# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Getting started

Install the project and its development dependencies:

```sh
uv sync
```

Run the command-line interface:

```sh
uv run {{ cookiecutter.project_slug }}
```

Run the checks:

```sh
uv run ruff format --check .
uv run ruff check .
uv run ty check .
uv run pytest
```
