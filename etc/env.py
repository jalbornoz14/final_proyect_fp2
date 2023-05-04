import os

class Env:
    TABULATE_STYLE = os.getenv("TABULATE_STYLE", "fancy_grid")
