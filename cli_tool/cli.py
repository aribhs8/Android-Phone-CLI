""" Console script for cli tool """

import logging
import sys
import traceback
from functools import partial

import rich_click as click

from lazy_group import LazyGroup

__version__ = "0.0.1"

logger = logging.getLogger(__name__)

click.rich_click.USE_RICH_MARKUP = True
click.rich_click.USE_MARKDOWN = True
click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.SHOW_METAVARS_COLUMN = False
click.rich_click.APPEND_METAVARS_HELP = True
click.rich_click.ERRORS_EPILOGUE = (
    "To find out more, visit "
    "<Not created yet>"
)


def exception_hook(exc_type, exc_value, tb, debug=False):
    if debug:
        echo_err = partial(click.secho, fg="red", err=True)
        echo_err("Traceback:")
        echo_err("".join(traceback.format_tb(tb)))

    # Exception type and value
    click.secho(f"{exc_type.__name__}: ", fg="red", nl=False)
    click.secho(f"{exc_value}")


@click.group()
@click.version_option(__version__)
@click.option("--debug", is_flag=True)
def main(debug):
    """ CLI tool commandline interface """
    click.echo(f"CLI tool Interface version <Version {__version__}>", err=True)
    click.echo(err=True)

    sys.excepthook = partial(exception_hook, debug=debug)


@main.group(cls=LazyGroup, import_name="cli_tool.phone:phone_subcommands")
def phone():
    """ Phone subcommands"""


if __name__ == "__main__":
    main()
