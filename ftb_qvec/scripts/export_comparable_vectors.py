import spacy
import typer
from pathlib import Path


def main(
    input_vectors: Path, input_model: Path, input_oracle: Path, output_vectors: Path
):
    nlp = spacy.load(input_model)
    vectors = {}
    with open(input_vectors) as fileh:
        for line in fileh.readlines():
            parts = line.strip().split()
            vectors[parts[0]] = " ".join(parts[1:])
    with open(input_oracle) as fileh:
        lines = fileh.readlines()
        words = [line.split()[0] for line in lines]
    for word in words:
        if word not in vectors:
            vectors[word] = " ".join(str(v) for v in nlp.vocab[word].vector)
    with open(output_vectors, "w") as fileh:
        for word in sorted(vectors.keys()):
            fileh.write(word + " " + vectors[word] + "\n")


if __name__ == "__main__":
    typer.run(main)
