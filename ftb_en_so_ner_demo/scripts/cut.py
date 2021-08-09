import typer
from pathlib import Path


def main(f: int, infile: Path, outfile: Path, d: str="\t"):
    with open(infile) as infileh, open(outfile, "w") as outfileh:
        for line in infileh.readlines():
            line = line.strip()
            parts = line.split(d)
            outfileh.write(d.join(parts[:f]).strip() + "\n")


if __name__ == "__main__":
    typer.run(main)
