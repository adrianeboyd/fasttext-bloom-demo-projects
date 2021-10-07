## Demos for floret vectors

> Note: As specified in `requirements.txt`, all demos currently require
> a custom version of spaCy, [`feature/fasttext-bloom-vectors`](https://github.com/adrianeboyd/spaCy/tree/feature/fasttext-bloom-vectors).

Demos currently use data from [OSCAR](https://oscar-corpus.com) for
training vectors, streaming the unshuffled deduplicated corpora using
[datasets](https://huggingface.co/docs/datasets/).

A demo for training and loading `floret` vectors:

- [`floret_vectors_demo`](floret_vectors_demo)

A demo for training and comparing standard `fasttext` and `floret`
vectors using [`QVEC`](https://github.com/ytsvetko/qvec):

- [`ftb_qvec`](ftb_qvec)

Demos for training vectors and and spaCy pipelines with a focus on cases where
`floret` vectors are expected to improve the performance as compared to
standard `fasttext` vectors on a fixed vocabulary:

- [`floret_ko_ud_demo`](floret_ko_ud_demo): agglutinative languages with Korean UD

  With 1M (3.3G) tokenized training texts and 50K 300-dim vectors, ~800K
  keys for the standard vectors:

  | Vectors                 |  TAG |  POS | DEP UAS | DEP LAS |
  | ----------------------- | ---: | ---: | ------: | ------: |
  | none                    | 72.6 | 85.0 |    73.3 |    64.6 |
  | standard (pruned)       | 78.2 | 89.7 |    78.9 |    73.1 |
  | floret (minn 2, maxn 3) | 83.2 | 94.2 |    83.4 |    80.7 |

  With 12G tokenized training texts and 50K 300-dim vectors (except for
  unpruned), ~1M keys for the standard vectors:

  | Vectors                 |  TAG |  POS | DEP UAS | DEP LAS | SPEED |
  | ----------------------- | ---: | ---: | ------: | ------: | ----: |
  | none                    | 72.6 | 85.0 |    73.3 |    64.6 | 15272 |
  | standard (pruned)       | 78.9 | 89.9 |    79.0 |    73.5 | 14754 |
  | standard (unpruned)     | 81.6 | 91.8 |    80.8 |    76.1 | 14200 |
  | floret (minn 2, maxn 3) | 83.6 | 94.3 |    83.5 |    80.7 | 13530 |

- [`floret_fi_ud_demo`](floret_fi_ud_demo): agglutinative languages with
  Finnish, UD_Finnish-TDT (syntax) and turku-ner-corpus (NER)

  With 13G tokenized training texts and 50K 300-dim vectors (except for
  unpruned), ~1M keys for the standard vectors:

  | Vectors                 |  TAG |  POS | MORPH | DEP UAS | DEP LAS | ENTS F | SPEED (syntax) |
  | ----------------------- | ---: | ---: | ----: | ------: | ------: | -----: | -------------: |
  | none                    | 93.5 | 92.5 |  86.2 |    79.4 |    72.7 |   62.0 |          12693 |
  | standard (pruned)       | 96.6 | 95.6 |  89.6 |    84.6 |    79.6 |   72.2 |          13407 |
  | standard (unpruned)     | 97.0 | 96.0 |  90.9 |    84.6 |    80.0 |   72.2 |          13269 |
  | floret (minn 4, maxn 5) | 97.1 | 96.0 |  91.6 |    84.6 |    80.2 |   73.6 |          12044 |

- [`ftb_hu_ner_demo`](ftb_hu_ner_demo): agglutinative
  languages with Hungarian NER

  With 500K (1.5G) tokenized training texts and 50K 300-dim vectors, with
  ~650K unique keys for the standard vectors:

  | Vectors                 |    P |    R |    F |
  | ----------------------- | ---: | ---: | ---: |
  | none                    | 93.7 | 93.5 | 93.6 |
  | standard (pruned)       | 94.9 | 95.0 | 95.0 |
  | floret (minn 5, maxn 6) | 97.1 | 95.9 | 96.5 |

- [`ftb_en_noisy_ner_demo`](ftb_en_noisy_ner_demo): noisy
  data with English NER for Twitter on emerging events

  With 500K (2.5G) tokenized training texts and 20K 300-dim vectors, with
  ~200K unique keys for the standard vectors:

  | Vectors                 |    P |    R |    F |
  | ----------------------- | ---: | ---: | ---: |
  | none                    | 30.7 | 18.7 | 23.3 |
  | standard (pruned)       | 34.5 | 25.6 | 29.4 |
  | floret (minn 5, maxn 6) | 39.9 | 23.3 | 29.4 |

- [`ftb_en_so_ner_demo`](ftb_en_so_ner_demo):
  out-of-domain data with English NER for StackOverflow vs. GitHub

  With 500K (2.5G) tokenized training texts and 20K 300-dim vectors:

  | Vectors                 | F (in-domain) | F (out-of-domain) |
  | ----------------------- | ------------: | ----------------: |
  | none                    |          55.6 |              37.6 |
  | standard (pruned)       |          55.3 |              35.1 |
  | floret (minn 5, maxn 6) |          55.5 |              35.9 |

  In this case, the OSCAR texts are not particularly suitable training
  data for the vectors. It would probably be better to train vectors on
  texts from StackOverflow or a similar source instead.

### Notes

To test a workflow quickly, set `max_texts` to very small value like
`100`. A much larger amount of training data for the vectors is
obviously needed for more meaningful comparisons in the test cases. The
provided defaults are still quite small for typical vector training
data, but should show some results and train in a not-too-unreasonable
amount of time on a small number of threads.

For reference, 1M texts from the OSCAR datasets are about 5G for
English, 4G for Hungarian, and 3G for Korean. In some of the projects,
to demonstrate streaming from huggingface's `datasets` more explicitly,
the texts are downloaded and tokenized in two separate steps, which
doubles the amount of disk space required.

`fasttext` does not support streamed input, so it is necessary to have
the tokenized training data saved in a file. Outside of a demo, I'd
often use tmpfs.
