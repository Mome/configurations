#! /usr/bin/python3
from pathlib import Path
import sys
import os

destinations = {
    "zshrc" : "~/.zshrc",
    "shrc" : "~/.shrc",
    "bashrc" : "~/.bashrc",
    "vimrc" : "~/.vimrc",
    "tmux" : "~/.tmux.conf",
}

files_path = Path(__file__).parent / "files"
origins = {p.name: p for p in files_path.iterdir()}

for fname in sys.argv[1:]:
    if fname not in origins:
        print("No file named:", fname, file=sys.stderr)
        continue
    if fname not in destinations:
        print("No location for:", fname, file=sys.stderr)
        continue
    dest = Path(destinations[fname]).expanduser().absolute()
    if dest.exists():
        if dest.is_symlink():
            dest.unlink()
        else:
            dest.rename(dest.parent / (dest.name + '.backup'))
    origin = origins[fname].absolute()
    dest.symlink_to(origin)

