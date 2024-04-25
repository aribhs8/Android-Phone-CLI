import functools
import rich_click as click
from phone_lib.android_phonestatus import AndroidPhoneStatus
from click_option_group import optgroup

CONTACT_ARGS = [
    "add",
    "add_multiple",
    "remove",
    "wipe",
    "exists"
]


def contact_params(func):
    @optgroup.group(
        "CONTACTS configuration",
        help="The configuration for manipulating contacts"
    )
    @optgroup.option(
        "-a",
        "--add",
        help="Specify contact to add",
        type=click.STRING
    )
    @optgroup.option(
        "-m",
        "--add-multiple",
        help="Add multiple predefined contacts (removes all existing)",
        type=click.INT
    )
    @optgroup.option(
        "-r",
        "--remove",
        help="Specify contact to remove",
        type=click.STRING
    )
    @optgroup.option(
        "-w",
        "--wipe",
        is_flag=True,
        help="Delete all contacts from phone"
    )
    @optgroup.option(
        "-e",
        "--exists",
        help="Check if a contact exists",
        type=click.STRING
    )
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def pop_contacts_args(kwargs):
    contacts_args = {arg: kwargs.pop(arg) for arg in CONTACT_ARGS}
    return contacts_args


@click.command(name="contacts")
@contact_params
@click.argument("serial", type=click.STRING)
def main(serial, **kwargs):
    """
    Sent command to phone to manipulate contacts on device.
    """
    # get arguments
    if kwargs == "":
        print("Please pass an option!")
        return

    contacts_args = pop_contacts_args(kwargs)

    # complete action using android phone status
    aps = AndroidPhoneStatus(serial)

    # add
    if contacts_args['add'] is not None:
        aps.add_contact(contacts_args['add'])

    elif contacts_args['add_multiple'] is not None:
        aps.add_multiple_contact(contacts_args['add_multiple'])

    # remove
    if contacts_args['remove'] is not None:
        aps.remove_contact(contacts_args['remove'])

    elif contacts_args['wipe'] is not False:
        aps.remove_all_contacts()

    # contact exists
    if contacts_args['exists'] is not None:
        result = aps.is_contact_exist(contacts_args['exists'])
        print("Contact", "exists" if result else "does not exist")


if __name__ == "__main__":
    main()
