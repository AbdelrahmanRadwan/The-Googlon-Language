# The Googlon Language

## How to run
### Run the Interactive testing
Run interactive terminal to be able to test new cases which are not mentioned in the ```The-Googlon-Language/test/test_cases.json``` file.

```bash
python3 test/interactive_testing.py
```

### Run the validator
Run the validator to test the given test cases in the ```The-Googlon-Language/test/test_cases.json``` file, and writes the results to
```The-Googlon-Language/test/test_results/results.json```

```bash
python3 test/validator.py
```
## Language Characteristics

### Letter Classification
Googlon letters are classified in *two groups*
 
- The letters (u, d, x, s, m, p, f) are called *foo letters*.
- The other letters are called *bar letters*.

### Prepositions
In the Googlon language, the prepositions are the words of exactly 6 letters
which end in a foo letter and do not contain the letter u.

### Verbs
In the Googlon language, verbs are words of 6 letters or more, that end in a bar letter.
 
Furthermore, if a verb starts in a bar letter, then the verb is inflected in its
subjunctive form.

### Lexicographical Order
In Googlon, like in our system, words are always ordered lexicographically, but the challenge is that the order of
the letters in the Googlon alphabet is different from ours. Their alphabet, in order, is: sxocqnmwpfyheljrdgui.

### Numbers
In Googlon, words also represent numbers given in base 20, where each letter is a digit. The digits are ordered from the least
significant to the most significant, which is the opposite of our system. 
That is, the leftmost digit is the unit, the second digit is worth 20, the third one is worth 400, and so on and so forth. 

The values of the letters are given by the order they appear in the Googlon alphabet (which, as we saw, is ordered differently from our alphabet).
That is, the first letter of the Googlon alphabet represents the digit 0, the second letter represents the digit 1,
and the last one represents the digit 19.

As an example, the Googlon word gxjrc represents the number 605637.

Googlons consider a number to be pretty if it satisfies all of the following properties:
- it is greater than or equal to 81827
- it is divisible by 3


