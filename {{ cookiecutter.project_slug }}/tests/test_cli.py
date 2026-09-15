from __future__ import annotations

from {{ cookiecutter.package_module }}.cli import main


def test_main(capsys) -> None:
    main([])

    assert capsys.readouterr().out == "Hello from {{ cookiecutter.project_slug }}!\n"
