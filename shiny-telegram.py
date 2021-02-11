from argparse import ArgumentParser

arg_parser = ArgumentParser(
    "shiny-telegram", description="Monitor a twitter handle")
arg_parser.add_argument("handle", metavar="HANDLE",
                        help="the twitter handle to monitor", type=str)
arg_parser.add_argument("-p", "--port", metavar="PORT",
                        help="the port the API listens on", type=int, default=8080)


def main(argv: list):
    args = arg_parser.parse_args(argv)
    print(args)
    # TODO: start monitor subprocess

    # TODO: start web API

    # TODO: listen for SIGINT


if __name__ == "__main__":
    from sys import argv
    main(argv[1:])
