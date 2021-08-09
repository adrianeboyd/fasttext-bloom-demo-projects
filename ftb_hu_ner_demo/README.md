<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: Demo fasttext-bloom vectors for Hungarian NER

Train fasttext-bloom vectors on OSCAR and compare default pruned vectors vs. fasttext-bloom vectors on NER for vector tables of the same size.

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
| `fasttext-nn` | Demo fasttext-bloom vectors |
| `init-default-vectors` | Create a default vectors model |
| `init-ngram-vectors` | Create an ngram vectors model |
| `create-config` | Create a new config with an NER pipeline component |
| `convert` | Convert the data to spaCy's format |
| `train-no-vectors` | Train the model without vectors |
| `train-default` | Train the model with default vectors |
| `train-ngram` | Train the model with ngram vectors |
| `evaluate` | Evaluate the models and export metrics |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | `compile-fasttext` &rarr; `download-data` &rarr; `preprocess` &rarr; `train-fasttext` &rarr; `init-default-vectors` &rarr; `init-ngram-vectors` &rarr; `create-config` &rarr; `convert` &rarr; `train-no-vectors` &rarr; `train-default` &rarr; `train-ngram` &rarr; `evaluate` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| `software/fasttext-bloom` | Git |  |
| [`assets/business_NER`](assets/business_NER) | Local | Corpus of Business Newswire Texts from the Szeged Treebank |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->
