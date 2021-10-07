<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: Evaluate floret vectors with qvec

Evaluate floret vectors with qvec

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
| `compile-floret` | Compile floret |
| `tokenize-oscar` | Download, tokenize, and sentencize data |
| `train-fasttext-standard` | Train fasttext standard vectors (with ngrams) |
| `train-floret` | Train floret vectors |
| `init-default-vectors` | Create an default vectors model |
| `init-floret-vectors` | Create a floret vectors model |
| `export-comparable-vectors` | Export comparable vectors for all qvec eval items |
| `run-qvec` | Run qvec |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | `compile-floret` &rarr; `tokenize-oscar` &rarr; `train-fasttext-standard` &rarr; `train-floret` &rarr; `init-default-vectors` &rarr; `init-floret-vectors` &rarr; `export-comparable-vectors` &rarr; `run-qvec` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| `software/floret` | Git |  |
| `software/qvec` | Git |  |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->
