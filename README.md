# Haiku Reader
Inspired by kwojcik's Bash script, Haiku Reader generates random haikus that you can hear with the `say` command.

Status: It currently does not work.

## What's a haiku?
As you may recall from poetry class, a haiku is three lines. The first line has five syllables, the second has seven, and the last has five.

## How does Haiku Reader make a haiku?
- Reads the list of words in the dictionary
- Randomly chooses a word
- Checks the syllables of that word
  - If over 5, it chooses another word
  - If exactly 5, it moves on to the next line
  - If under 5, it keeps the word and chooses another until the first line needs 0 more syllables, then moves on to the next line
- Still need punctuation between lines (preferably period, question mark)

## How do I hear the haiku recited aloud?
- Do `./haiku.py | say`
