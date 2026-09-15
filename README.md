# Python package template

Cookiecutter template for a small Python package using `uv`, `ruff`, `ty`,
`pytest`, `prek`, and Zensical.

## Usage

Install Cookiecutter and render a new project:

```sh
uv tool install cookiecutter
cookiecutter gh:keksiqc/template-pypackage

# or

uvx cookiecutter gh:keksiqc/template-pypackage
```

The generated project is created in a directory named after `project_slug`.
The template asks for the project name, project slug, Python module name,
package metadata, and GitHub owner. The slug and module name are derived from
the project name by default and can be adjusted during the prompts.

The generated project does not include a lockfile. Create it after rendering
with:

```sh
cd my_python_package
uv sync
```

The files used to render a project live under
`{{ cookiecutter.project_slug }}/`.
