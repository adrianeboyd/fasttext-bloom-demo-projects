## Demos for fasttext-bloom vectors

> Note: As specified in `requirements.txt`, all demos currently require 
> a custom version of spaCy, usually
> [`feature/fasttext-bloom-vectors`](https://github.com/adrianeboyd/spaCy/tree/feature/fasttext-bloom-vectors).

A demo for training and loading `fasttext-bloom` vectors:

* [`ftb_vectors_demo`](ftb_vectors_demo)

Demos for training vectors and and spaCy pipelines with a focus on cases 
where `fasttext-bloom` vectors are expected to improve the performance:

* [`ftb_en_noisy_ner_demo`](ftb_en_noisy_ner_demo): noisy 
  data with English NER for Twitter on emerging events

* [`ftb_en_noisy_ner_demo`](ftb_en_so_ner_demo): 
  out-of-domain data with English NER for StackOverflow vs. GitHub

  With 1M (5G) tokenized training texts and 20K 300-dim vectors:

  | Vectors                | F (in-domain) | F (out-of-domain) |
  | ---------------------- | ------------: | ----------------: |
  | default (pruned)       | 55.5          | 29.8              |
  | ngram (minn 5, maxn 6) | 55.4          | 35.7              |

* [`ftb_hu_noisy_ner_demo`](ftb_hu_ner_demo): agglutinative
  languages with Hungarian NER

  With 500K (1.5G) tokenized training texts and 20K 300-dim vectors:

  | Vectors                | P    | R    | F    |
  | ---------------------- | ---: | ---: | ---: |
  | none                   | 93.7 | 93.5 | 93.6 |
  | default (pruned)       | 95.9 | 94.1 | 95.0 |
  | ngram (minn 5, maxn 6) | 96.9 | 96.1 | 96.5 |

* [`ftb_ko_ud_demo`](ftb_ko_ud_demo): agglutinative languages with Korean UD

   With 1M (3.3G) tokenized training texts and 50K 300-dim vectors:

  | Vectors                | TAG  | POS  | DEP UAS | DEP LAS |
  | ---------------------- | ---: | ---: | ------: | ------: |
  | none                   | 72.4 | 85.2 | 73.7    | 64.9    |
  | default (pruned)       | 78.0 | 89.5 | 78.7    | 72.9    |
  | ngram (minn 1, maxn 3) | 83.6 | 94.4 | 83.2    | 80.3    |

  The ngram model is ~3x slower than the default model.

### Notes

To test a workflow quickly, set `max_texts` to very small value like 
`100`. A much larger amount of training data for the vectors is 
obviously needed for more meaningful comparisons in the test cases. The 
provided defaults are still quite small for typical vector training 
data, but should show some results and train in a not-too-unreasonable 
amount of time on a small number of threads.

For reference, 1M texts from the OSCAR datasets are about 5G for English 
and 4G for Hungarian. In a real project, the vector training text 
download and tokenization steps could be combined, but to demonstrate 
streaming from huggingface's `datasets` more explicitly, the texts are 
downloaded and tokenized in two separate steps, which doubles the amount 
of disk space required.

`fasttext` does not support streamed input, so it is necessary to have 
the tokenized training data saved in a file. Outside of a demo, I'd 
usually use tmpfs.
