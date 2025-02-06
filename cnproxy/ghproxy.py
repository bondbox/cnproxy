# coding:utf-8

from typing import Optional
from typing import Sequence

from xkits import add_command
from xkits import argp
from xkits import commands
from xkits import run_command

from .attribute import __urlhome__
from .attribute import __version__

DEFAULT_HOST: str = "127.0.0.1"
DEFAULT_PORT: int = 8800


@add_command("wsgi", help="GitHub Proxy Web Server Gateway Interface")
def add_cmd_wsgi(_arg: argp):
    _arg.add_argument("--host", type=str, default=DEFAULT_HOST,
                      help=f"The host to bind (default: {DEFAULT_HOST}).")
    _arg.add_argument("--port", type=int, default=DEFAULT_PORT,
                      help=f"The port to listen on (default: {DEFAULT_PORT}).")


@run_command(add_cmd_wsgi)
def run_cmd_wsgi(cmds: commands) -> int:
    return 0


@add_command("ghproxy")
def add_cmd(_arg: argp):
    pass


@run_command(add_cmd, add_cmd_wsgi)
def run_cmd(cmds: commands) -> int:
    return 0


def main(argv: Optional[Sequence[str]] = None) -> int:
    cmds = commands()
    cmds.version = __version__
    return cmds.run(root=add_cmd, argv=argv, description="GitHub Proxy",
                    epilog=f"For more, please visit {__urlhome__}.")
