import logging

import rich_click as click
from cli_tool.phone import (
    contacts
)

logger = logging.getLogger(__name__)

# Todo: make it so that phone argument is passed here and then sent to contacts


@click.group(name="phone", chain=True)
def phone_subcommands():
    """Phone subcommands"""


phone_subcommands.add_command(contacts.main)
