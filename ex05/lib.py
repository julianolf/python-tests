__version__ = (2, 0)


def do_something() -> str:
    if __version__ < (2, 0):
        return "done"
    else:
        return "Done!"


def does_something_wrong():
    return 2 // 0
