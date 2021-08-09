import srsly
import typer
from datasets import load_dataset
from itertools import islice
from pathlib import Path


def main(
    oscar_dataset: str,
    output_file: Path,
    max_texts: int=1,
):
    dataset = load_dataset("oscar", oscar_dataset, split="train", streaming=True)
    items = islice(iter(dataset), max_texts)
    srsly.write_jsonl(output_file, items)


if __name__ == "__main__":
    typer.run(main)
