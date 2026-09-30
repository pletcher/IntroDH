---
geometry: margin=1in
---

# Word Frequencies in Virginia Woolf's "On Not Knowing Greek"

**Before you code**: Skim the essay. Write down 3 words
that you _predict_ will be most frequent and 3 that you
think will be most _meaningful_. Save this; you'll come
back to it.

## Part 1: Getting the text

1. Find a plain-text version of Woolf's essay. It's in _The Common Reader_ (1925), available on Project Gutenberg. Copy only the ssay into a `.txt` file and upload the file to your
Colab notebook.
2. Open and read the file in Python.
3. **Checkpoint**: Print the first 200 characters. Does it start where the essay starts? Is there any header, footer, or title text? Any extra whitespace?

## Part 2: Data cleaning and preparation

1. Convert the text to lowercase.
2. Remove punctuation. (Hint: think through what counts as punctuation. How do you want to handle apostrophes?)
3. Split the text into a list of words.
4. **Checkpoint**: Print the total number of words (hint: use the `len()` function) and the first 30 words. Does anything look amiss?

## Part 3: Counting

1. Count how often each word appears using `collections.Counter`. (Hint: `Counter` is a class within the `collections` module.)
2. Print the 25 most frequent words and their counts.
3. **Reflect**: How doe these compare to your predictions? What kinds of words dominate the list? Does this tell you anything about Woolf's essay specifically?

## Part 4: Filtering stopwords

1. Create or import a stopword list (for example, you could use the NLTK's English list).
2. Remove stopwords from the list of words you created in Part 2.
3. **Reflect**:
    - Which words now rise to the top?
    - Are any words on the stopword list actually meaningful?
    - Are there words that you think you should add to the stopword list?

## Part 5: Plotting in Excel

1. Export your top 20 filtered words and counts to a `.csv` file. You'll need to consult the documentation: https://docs.python.org/3/library/csv.html
2. Open the CSV in Excel (or Google Sheets) and make a bar chart with a title and labeled axes.
3. **Checkpoint**: Is the chart sorted in a readable way? Would someone who hasn't read the essay understand it?

## Part 6: Troubleshooting

As you work, record each problem you hit in a table:

| Problem | Example from my output | What I tried | Did it work?|

Some problems to look out for: possessives, hyphens and dashes, curly quotes, Greek words, and stray text.

## Part 7: Final reflection (1 paragraph)

What can word frequencies tell us about Woolf's essay? What can't they tell us? Use at least two specific words from your results as evidence.

## Rubric

| Criterion | Excellent (4) | Proficient (3) | Developing (2) | Beginning (1) |
|---|---|---|---|---|
| **Working code** | Runs without errors; readable and commented | Runs with minor issues; mostly readable | Runs partially; hard to follow | Does not run |
| **Text cleaning** | Handles punctuation, case, and edge cases thoughtfully | Handles case and basic punctuation | Partial cleaning; obvious errors remain | Little or no cleaning |
| **Frequency and stopword analysis** | Clear before/after comparison; questions the stopword list itself | Accurate before/after lists with some comparison | Lists produced but not compared | Lists missing or incorrect |
| **Excel visualization** | Clear, labeled, sorted, and readable chart | Chart is correct with minor labeling gaps | Chart present but hard to read | No chart |
| **Troubleshooting log** | Several issues documented with attempted fixes | A few issues with some fixes | Issues listed without explanation | No log |
| **Interpretation** | Connects word patterns to the essay's argument and notes the limits of the method | Identifies patterns with some interpretation | Describes lists without interpreting | No reflection |
