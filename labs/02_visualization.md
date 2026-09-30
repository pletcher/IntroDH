---
geometry: margin=1in
---

# Visualization Lab: Word Patterns in Plato

In the last lab, you counted the most frequent words in Woolf's
"On Not Knowing Greek." Now you'll reuse that code on the Plato dialogues
we've read and explore how visualization can reveal patterns (and errors)
that lists of numbers hide.

## Part 1: Reuse your code
1. Turn your cleaning and counting code from the Woolf lab into functions,
   such as `clean_text(text)` and `count_words(words, stopwords)`.
2. Test them on the Woolf essay. **Checkpoint:** Do you get the same
   results as last time?

## Part 2: Prepare the Plato texts
1. Download the dialogues we've read from Project Gutenberg
   (Jowett translations). Save each dialogue as its own `.txt` file.
2. **Watch out:** Jowett's translations begin with a long introduction
   written by Jowett, not Plato. Remove it, along with the Gutenberg
   header and footer.
3. **Checkpoint:** Print the first and last 200 characters of each file.
   Does each one begin and end with Plato's text?
4. Add any new issues to your troubleshooting log from the Woolf lab.

## Part 3: A first look
1. Make a simple bar chart of the top 20 words (after stopwords) for
   one dialogue.
2. **Reflect:** Is anything in your top 20 an artifact of the text's
   format rather than its content? (Hint: how are dialogues written on
   the page?) Decide how to handle it, and explain your choice.

## Part 4: Sketch before you code
Choose one question you want your visualization to answer. For example:
- Where in a dialogue does a key word (e.g., "soul," "justice," "love")
  appear?
- How does vocabulary differ between two dialogues?
- How does Plato's vocabulary compare with Woolf's?

Sketch your visualization on paper. Label the axes and note what a
reader should notice.

## Part 5: Build at least two visualizations
Choose from the menu below, or propose your own. At least one should go
beyond a bar chart.

| Level | Visualization | Answers questions like... |
|---|---|---|
| Starter | Side-by-side bar charts for two dialogues | How do their top words differ? |
| Intermediate | Word occurrences across a dialogue, split into 10 equal chunks (line chart) | Where does a theme appear or fade? |
| Intermediate | Dispersion plot showing each occurrence of a word by position | Are words clustered or spread out? |
| Advanced | Heatmap of key words across all dialogues in reading order | How do themes shift over the course? |
| Advanced | Comparison with Woolf's essay | What does "Greek" look like from each side? |

You may want use Python (matplotlib), Excel, or
[Voyant Tools](https://beta.voyant-tools.org). If you use Voyant, compare
its results with your own code's output and explain any differences.

## Part 6: Legibility checklist
Before submitting, check each visualization:

- [ ] Descriptive title
- [ ] Labeled axes with units (e.g., "occurrences per 1,000 words")
- [ ] Readable font size and no overlapping labels
- [ ] Legend, if there is more than one data series
- [ ] One-sentence caption stating the main takeaway

## Part 7: Reflection (1–2 paragraphs)
- What patterns did your visualizations reveal?
- Did visualization help you catch any errors? Describe one.
- What follow-up experiment would you run next, and why?
- What does reading Plato in translation mean for word-frequency analysis?

## Rubric

| Criterion | Excellent (4) | Proficient (3) | Developing (2) | Beginning (1) |
|---|---|---|---|---|
| **Code reuse and text prep** | Reusable functions; texts cleanly prepared, including introductions and speaker labels | Functions reused; most prep issues handled | Some reuse; notable prep errors remain | No reuse; texts not prepared |
| **Legibility** | All checklist items met; takeaway is immediately clear | Most checklist items met | Several checklist items missing | Hard to read or interpret |
| **Creativity and fit** | Goes beyond bar charts; visualization choice clearly matches the question | At least one non-bar-chart visualization | Only bar charts, but well made | Visualization doesn't match the question |
| **Error detection** | Documents errors caught through visualization and explains fixes | Notes at least one error and fix | Mentions errors vaguely | No discussion of errors |
| **Interpretation and follow-up** | Insightful patterns, a concrete follow-up experiment, and attention to translation | Identifies patterns and proposes a follow-up | Describes charts without interpreting | No reflection |
