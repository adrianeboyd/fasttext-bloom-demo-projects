import re
import spacy
import srsly
import typer
from functools import partial
from itertools import islice
from multiprocessing import Pool
from pathlib import Path


def tokenize(nlp, batch):
    output = []
    texts = (re.sub("\s+", " ", line["text"].strip()) for line in batch)
    for doc in nlp.pipe(texts):
        for sent in doc.sents:
            output.append(" ".join([t.text for t in sent]) + "\n")
    return output


def read_chunks(fileh, n=1):
    i = 0
    batch = []
    for line in fileh:
        batch.append(srsly.json_loads(line.strip()))
        i += 1
        if i == n:
            yield batch
            i = 0
            batch = []
    if batch:
        yield batch


def main(
    lang: str,
    input_file: Path,
    output_file: Path,
    n_process: int = 8,
):
    nlp = spacy.blank(lang)
    if lang == "zh":
        nlp = spacy.blank("zh", config={"nlp": {"tokenizer": {"segmenter": "pkuseg"}}})
        nlp.tokenizer.initialize(pkuseg_model="spacy_ontonotes")

    nlp.add_pipe("sentencizer")
    nlp.max_length = 10 ** 8

    with open(input_file) as input_fileh, open(output_file, "w") as output_fileh, Pool(processes=n_process) as pool:
        result = pool.imap(
            partial(tokenize, nlp),
            read_chunks(input_fileh, n=100)
        )
        for lines in result:
            output_fileh.writelines(lines)


if __name__ == "__main__":
    typer.run(main)
