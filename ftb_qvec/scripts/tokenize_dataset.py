import re
import spacy
import srsly
import typer
from functools import partial
from itertools import islice
from multiprocessing import Pool
from pathlib import Path
from datasets import load_dataset


def tokenize(nlp, batch):
    output = []
    texts = (re.sub("\s+", " ", line["text"].strip()) for line in batch)
    for doc in nlp.pipe(texts):
        for sent in doc.sents:
            output.append(" ".join([t.text for t in sent]) + "\n")
    return output


def read_chunks(dataset, n=1):
    i = 0
    batch = []
    for line in dataset:
        batch.append(line)
        i += 1
        if i == n:
            yield batch
            i = 0
            batch = []
    if batch:
        yield batch


def main(
    lang: str,
    oscar_dataset: str,
    max_texts: int,
    output_file: Path,
    n_process: int = 8,
):
    if lang == "ko":
        nlp = spacy.blank("ko", config={"nlp": {"tokenizer": {"@tokenizers": "spacy.Tokenizer.v1"}}})
    elif lang == "zh":
        nlp = spacy.blank("zh", config={"nlp": {"tokenizer": {"segmenter": "pkuseg"}}})
        nlp.tokenizer.initialize(pkuseg_model="spacy_ontonotes")
    else:
        nlp = spacy.blank(lang)

    nlp.add_pipe("sentencizer")
    nlp.max_length = 10 ** 8

    dataset = load_dataset("oscar", oscar_dataset, split="train", streaming=True)

    with open(output_file, "w") as output_fileh, Pool(processes=n_process) as pool:
        result = pool.imap(
            partial(tokenize, nlp),
            read_chunks(islice(iter(dataset), max_texts), n=100)
        )
        for lines in result:
            output_fileh.writelines(lines)


if __name__ == "__main__":
    typer.run(main)
