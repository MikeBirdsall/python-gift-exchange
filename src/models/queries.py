#!/usr/bin/python3
import argparse
import sys
from clanlist import clanlist
from clans import clans

usagestrings = {}      # pylint: disable=invalid-name
cmdlist = {}           # pylint: disable=invalid-name

BAREHELP = """XMAS Models Driver

list of commands:
"""


class Driver():

    def naked_help(self):
        print(BAREHELP)
        print('\n'.join(
                [' {:<15} {}'.format(a, b) for a, b in sorted(cmdlist.items())]
            ))

    def help(self, args):
        if not args.command:
            self.naked_help()
        elif args.command in usagestrings:
            print(usagestrings[args.command])
        else:
            print("No command %s" % args.command)
            self.naked_help()

    def clanlist(self, dummy_args):
        print(clans().namelist())

    def members(self, args):
        if args.table == 'clan':
            clanmembers = clanlist(clanname=args.name, clanid=args.id).members
            print(*clanmembers, sep=",\n")
        else:
            print("Not yet implemented members %s" %args.table)

def main():
    d = Driver()                       # pylint: disable=invalid-name

    parser = argparse.ArgumentParser(
        description='Calls models which operate on xmas database')

    subparsers = parser.add_subparsers()

    cmd = 'help'
    query = subparsers.add_parser(cmd)
    query.set_defaults(func=getattr(d, cmd))
    query.add_argument('command', nargs='?')
    usagestrings[cmd] = query.format_help()
    cmdlist[cmd] = "show help for a given command or topic"

    cmd = 'clanlist'
    query = subparsers.add_parser(cmd)
    query.set_defaults(func=getattr(d, cmd))

    usagestrings[cmd] = query.format_help()
    cmdlist[cmd] = "list all clans"

    cmd = 'members'
    query = subparsers.add_parser(
        cmd,
        description=("List the members of a clan or sslist, based on it's name "
                     "or id."),
        help="help description")
    query.set_defaults(func=getattr(d, cmd))

    query.add_argument(
        'table',
        choices=['clan', 'sslist'],
        help='table to query')
    group = query.add_mutually_exclusive_group()
    group.add_argument('--name', '-n', help="clan or sslist name")
    group.add_argument('--id', '-i', type=int, help="clan or sslist id")

    usagestrings[cmd] = query.format_help()
    cmdlist[cmd] = "list the members of clan or sslist given the name or id"

    options = parser.parse_args()
    if len(sys.argv) < 2:
        d.naked_help()
    else:
        options.func(options)


if __name__ == "__main__":
    main()
