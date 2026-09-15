"""Validate values before rendering a project."""

from __future__ import annotations

import re


_SLUG_PATTERN = re.compile(r"[a-z0-9][a-z0-9_-]*\Z")
_MODULE_PATTERN = re.compile(r"[a-z_][a-z0-9_]*\Z")
_GITHUB_OWNER_PATTERN = re.compile(r"[A-Za-z0-9-]+\Z")


def _validate(pattern: re.Pattern[str], value: str, name: str) -> None:
    if not pattern.fullmatch(value):
        raise ValueError(f"{name} has an invalid value: {value!r}")


_validate(_SLUG_PATTERN, "{{ cookiecutter.project_slug }}", "project_slug")
_validate(_MODULE_PATTERN, "{{ cookiecutter.package_module }}", "package_module")
_validate(_GITHUB_OWNER_PATTERN, "{{ cookiecutter.github_owner }}", "github_owner")
