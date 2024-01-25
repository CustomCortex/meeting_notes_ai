"""Sphinx configuration."""
project = "Meeting Notes AI"
author = "Guru Ilangovan"
copyright = "2024, Guru Ilangovan"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
