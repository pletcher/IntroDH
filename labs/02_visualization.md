---
geometry: margin=1in
---

# Visualization Lab: Word Patterns in Plato

In the last lab, you counted the most frequent words in Woolf's
"On Not Knowing Greek." Now we're going to explore different ways
of visualizing frequencies — and related calculations — in the
Platonic corpus.

## Part 1: Get the texts (optional)

You can find a zip archive of the Perseus Digital Library's
English translations of Plato (including the spurious Letters)
on [Canvas](https://canvas.tufts.edu/courses/77052/files/folder/Week%2010%20-%20November%2023).

Download the archive to your computer. You don't need to unzip it.

## Part 2: "Upload" the texts to Voyant

Rather than upload multiple copies of the same corpus multiple
times to Voyant, we'll all use the corpus that I've already created:
[Plato on Voyant](https://voyant-tools.org/?corpus=18a6e6e04618763540e3cb64404ae2d9).

You can use this link if you'd like to return to it later. If you modify
the corpus — to exclude the Letters, for example — you might want to
create your own instance for experimentation.

## Part 3: Play

Test out the Voyant interface. What can you see at a glance? What is confusing?

> [!IMPORTANT]
> Write a short list of features that jump out to you, including notes
> about how you might use them or what you find confusing. Do you
> notice any problems that might be coming from the texts themselves?

## Part 4: Think

What kinds of questions do you want to ask of the corpus?
What visualizations would you use to guide your answers to these questions?

For example, can you find where a key word (e.g., "know", "justice", "soul")
appears in a dialogue? Or how vocabulary and keywords change from dialogue
to dialogue?

> [!IMPORTANT]
> Write a plan for two experiments that you'd like to conduct with this
> corpus. You can always revise the plan later, but be as detailed as
> possible here.

## Part 5: Build at least two visualizations

Choose from the menu below, or propose your own. At least one should go
beyond a bar chart.

| Level | Visualization | Answers questions like... |
|---|---|---|
| Starter | Side-by-side bar charts for two dialogues | How do their top words differ? |
| Intermediate | Word occurrences across a dialogue, split into 10 equal chunks (line chart) | Where does a theme appear or fade? |
| Intermediate | Dispersion plot showing each occurrence of a word by position | Are words clustered or spread out? |
| Advanced | Heatmap of key words across all dialogues in reading order | How do themes shift over the corpus? |
| Advanced | Comparison with Woolf's essay | What does "Greek" look like from each side? |

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
| **Text prep** | Texts cleanly prepared, including introductions and speaker labels | Most prep issues handled | Notable prep errors remain | Texts not prepared |
| **Legibility** | All checklist items met; takeaway is immediately clear | Most checklist items met | Several checklist items missing | Hard to read or interpret |
| **Creativity and fit** | Goes beyond bar charts; visualization choice clearly matches the question | At least one non-bar-chart visualization | Only bar charts, but well made | Visualization doesn't match the question |
| **Error detection** | Documents errors caught through visualization and explains fixes | Notes at least one error and fix | Mentions errors vaguely | No discussion of errors |
| **Interpretation and follow-up** | Insightful patterns, a concrete follow-up experiment, and attention to translation | Identifies patterns and proposes a follow-up | Describes charts without interpreting | No reflection |

## Extra credit

For an additional point (+10%) on this assignment, create additional visualizations using
Google Colab and Python. You can use `matplotlib`, which is built-in, or a library
like [Altair](https://altair-viz.github.io) or [Seaborn](https://seaborn.pydata.org).
