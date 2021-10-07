<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: Demo floret vectors for English NER in StackOverflow

Train floret vectors and compare default vs. floret vectors for in-domain (StackOverflow) and out-of-domain (GitHub) test sets. The data comes from [Code and Named Entity Recognition in StackOverflow](https://aclanthology.org/2020.acl-main.443/).

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
| `init-floret-vectors` | Create an floret vectors model |
| `create-config` | Create a new config with an NER pipeline component |
| `convert` | Convert the data to spaCy's format |
| `train-novectors` | Train the model with no vectors |
| `train-standard` | Train the model with standard vectors |
| `train-floret` | Train the model with floret vectors |
| `evaluate` | Evaluate the models and export metrics |
| `evaluate-ood` | Evaluate the models and export metrics |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | `compile-fasttext` &rarr; `tokenize-oscar` &rarr; `train-fasttext-standard-vectors` &rarr; `train-floret-vectors` &rarr; `init-standard-vectors` &rarr; `init-floret-vectors` &rarr; `create-config` &rarr; `convert` &rarr; `train-novectors` &rarr; `train-standard` &rarr; `train-floret` &rarr; `evaluate` &rarr; `evaluate-ood` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| `software/floret` | Git |  |
| `assets/StackOverflowNER` | Git |  |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->
