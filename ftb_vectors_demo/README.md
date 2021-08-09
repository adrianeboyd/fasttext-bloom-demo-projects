<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: Demo fasttext-bloom vectors

Show how to train fasttext-bloom vectors and load them into a spaCy vectors model.

## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `compile-fasttext` | Compile fasttext-bloom |
| `download-data` | Download data from OSCAR dataset |
| `preprocess` | Tokenize and sentencize data |
| `train-fasttext` | Train fasttext-bloom vectors |
| `init-ngram-vectors` | Create an ngram vectors model |
| `fasttext-nn` | Demo fasttext-bloom vectors |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | `compile-fasttext` &rarr; `download-data` &rarr; `preprocess` &rarr; `train-fasttext` &rarr; `init-ngram-vectors` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| `software/fasttext-bloom` | Git |  |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->
