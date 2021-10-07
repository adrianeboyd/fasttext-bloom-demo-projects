<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: Demo floret vectors for Hungarian NER

Train floret vectors on OSCAR and compare default pruned vectors vs. floret vectors on NER for vector tables of the same size.

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
| `compile-fasttext` | Compile floret |
| `tokenize-oscar` | Download, tokenize, and sentencize data |
| `train-fasttext-standard-vectors` | Train fasttext standard vectors |
| `train-floret-vectors` | Train floret vectors |
| `init-standard-vectors` | Create a default vectors model |
| `init-floret-vectors` | Create a floret vectors model |
| `create-config` | Create a new config with an NER pipeline component |
| `convert` | Convert the data to spaCy's format |
| `train-no-vectors` | Train the model without vectors |
| `train-standard` | Train the model with default vectors |
| `train-floret` | Train the model with floret vectors |
| `evaluate` | Evaluate the models and export metrics |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | `compile-fasttext` &rarr; `tokenize-oscar` &rarr; `train-fasttext-standard-vectors` &rarr; `train-floret-vectors` &rarr; `init-standard-vectors` &rarr; `init-floret-vectors` &rarr; `create-config` &rarr; `convert` &rarr; `train-no-vectors` &rarr; `train-standard` &rarr; `train-floret` &rarr; `evaluate` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| `software/floret` | Git |  |
| [`assets/business_NER`](assets/business_NER) | Local | Corpus of Business Newswire Texts from the Szeged Treebank |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->
