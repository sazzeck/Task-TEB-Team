#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from multiprocessing import Process

from django.core.management.commands.runserver import Command as runserver
from django.conf import settings


def run_app():
    import django
    django.setup()
    from bot import MyBot
    from server import MyServer

    bot = Process(target=MyBot.run)
    server = Process(target=MyServer.run)

    bot.start()
    server.start()


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings.local")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # if "runserver" in sys.argv:
    #     runserver.default_port = settings.RUN_SERVER_PORT
    #     return run_app()

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
