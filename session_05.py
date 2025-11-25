#!/usr/bin/env python3

import argparse


parser = argparse.ArgumentParser(description="Test Script")

sub_parser = parser.add_subparsers(dest="subcommand")

# parser.add_argument(
#     "-N",
#     "--Names",
#     dest="names",
#     type=str,
#     # required=True,
#     help="The Name of User",
#     nargs="*",  # * +
# )
# parser.add_argument(
#     "-m",
#     "--message",
#     type=str,
#     required=True,
#     help="Message to Show User",
#     choices=(
#         "Hello",
#         "Bye",
#         "How",
#     ),
# )
sub_parser.add_argument(
    "-f",
    "--first",
    help="First Number to Divide",
    required=True,
    type=int,
)
sub_parser.add_argument(
    "-s",
    "--second",
    help="Second Number to Divide",
    required=False,
    type=int,
    default=3,
)
# argparse.Action
sub_parser.add_argument(
    "-r",
    "--round",
    help="Round Result Value",
    action="store_true",
    default=False,
)

if __name__ == "__main__":
    args = sub_parser.parse_args()

print(args)

result = args.first / args.second
if args.round:
    result = int(result)

print(result)

# print(args.names)

# for name in args.names:
#     print(args.message, name)

