from __future__ import print_funtion
from pathlib import Path
import sys
import os

destinations = {
    "zshrc" : "~/.zshrc",
    "shrc" : "~/.shrc",
    "bashrc" : "~/.bashrc",
    "vimrc" : "~/.vimrc",
    "tumx" : "~/.tmux.conf",
}

module_path = Path(__file__).parent
origins = {p.name for p in module_path.iterdir()}

for fname in sys.argv[1:]:
    if fname not in origins:
        print("No file named:", fname, file=sys.stderr)
    if fname not in destinations:
        print("No location for:", fname, file=sys.stderr)
    dest = Path(destinations[fname])
    if dest.exists():
        dest.rename(dest.parent / (dest.name + '.backup'))
    origin = origins[fname]
    dest.symlink_to(origin)
