<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: Demo floret vectors

Show how to train floret vectors and load them into a spaCy vectors model.

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
| `train-floret` | Train floret vectors |
| `init-floret-vectors` | Create a floret vectors model |
| `floret-nn` | Demo floret vectors |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | `compile-floret` &rarr; `tokenize-oscar` &rarr; `train-floret` &rarr; `init-floret-vectors` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| `software/floret` | Git |  |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->
