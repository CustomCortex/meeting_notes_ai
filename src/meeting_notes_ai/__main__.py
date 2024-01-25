"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Meeting Notes AI."""


if __name__ == "__main__":
    main(prog_name="meeting_notes_ai")  # pragma: no cover
