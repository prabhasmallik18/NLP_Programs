from nltk.util import ngrams
from collections import defaultdict

text = "Sachin and Virat were both well-known cricket players in India and people admired them for their hard work and steady performances."

words = text.split()

def print_ngrams(words):
    for n, title in [(1, "UNIGRAMS"), (2, "BIGRAMS"), (3, "TRIGRAMS"), (4, "4-GRAMS")]:
        print(f"\n{title}")
        for gram in ngrams(words, n):
            print(gram)

print_ngrams(words)

def highest_probability(text):
    words = text.split()
    bigram_counts = defaultdict(lambda: defaultdict(int))
    first_word_counts = defaultdict(int)

    for w1, w2 in zip(words, words[1:]):
        bigram_counts[w1][w2] += 1
        first_word_counts[w1] += 1

    result = {}
    for w1, followers in bigram_counts.items():
        best_w2, best_count = max(followers.items(), key=lambda x: x[1])
        result[w1] = (best_w2, best_count / first_word_counts[w1])

    return result

text2 = "Sachin and Virat played for India and both showed calm mindset and steady commitment during their careers."
output = highest_probability(text2)

print("\nHighest probabilities:")
for w1, (w2, prob) in output.items():
    print(f"After '{w1}' -> '{w2}' with probability {prob:.2f}")
