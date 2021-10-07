import typer
from pathlib import Path


def main(input_file: Path, output_stem: str):
    with open(input_file, encoding="iso-8859-1") as input_fileh:
        orig_lines = list(input_fileh.readlines())
    # replace 0 with O
    orig_lines = [l.replace("\t0", "\tO") for l in orig_lines]
    splits = {"train": .8, "dev": .1, "test": .1}
    lines = []
    for line in orig_lines:
        parts = line.split("\t")
        word = parts[0].strip()
        # handle tokens that contain " "
        # (note: doesn't work correctly for B-, which doesn't occur in this data
        if " " in word:
            for subword in word.split(" "):
                lines.append(subword + "\t" + parts[1])
        else:
            lines.append(line)
    i = 0
    target_line_no = 0
    for split_name, split_size in splits.items():
        target_line_no += int(split_size * len(lines))
        with open(f"{output_stem}{split_name}.conll", "w") as output_fileh:
            while i < target_line_no and i < len(lines):
                output_fileh.write(lines[i])
                i += 1
            # split on the next sentence boundary
            while i < len(lines) and lines[i].strip() != "":
                output_fileh.write(lines[i])
                i += 1

if __name__ == "__main__":
    typer.run(main)
