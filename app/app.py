#!/usr/bin/env python3
import asyncio
from argparse import Namespace, ArgumentParser
from foo import foo_print
from bar import bar_print
from core import stdout, ts


async def app_main(argv: Namespace):
    stdout(f"now: {ts()}")
    foo_print("called foo_print")
    bar_print("called bar_print")


if __name__ == "__main__":
    g_parser = ArgumentParser(
        prog='App',
        description='Runs the app')
    g_parser.add_argument("-c", "--config", type=str)

    g_args = g_parser.parse_args()

    asyncio.run(app_main(g_args))
