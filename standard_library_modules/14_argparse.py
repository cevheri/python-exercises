# argparse module
import argparse

custom_parser = argparse.ArgumentParser(
    description="Argparse Module")

custom_parser.add_argument('-i',
                           '--first argument',
                           nargs='+',
                           required=False,
                           help="First Argument")

custom_parser.add_argument('-a',
                           '--second argument',
                           nargs='+',
                           required=False,
                           help="Second Argument")

custom_parser.print_help()

print(custom_parser.parse_args(['-a', '7']))


# Namespace(**{'first argument': None, 'second argument': ['7']})
# class argparse.ArgumentParser(
#         prog=None,
#         usage=None,
#         description=None,
#         epilog=None,
#         parents=[],
#         formatter_class=argparse.HelpFormatter,
#         prefix_chars='-',
#         fromfile_prefix_chars=None,
#         argument_default=None,
#         conflict_handler='error',
#         add_help=True,
#         allow_abbrev=True)



# add_argument()
# ArgumentParser.add_argument(
# name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])




