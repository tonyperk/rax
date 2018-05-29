# rax
Parse a bulleted outline

Assumptions:
- It assumes that there is a max of 50 subsections, of the format:
	- 1.1.1....1 (up to 50 subsections)
	- The intermediate subsections don't have an upperband, since they are stored as integers within a list.
- It preprocesses sections to mitigate too much information in RAM.

cat input.txt | python script.py > output.txt

Problem Statement: https://pastebin.com/qrnX9Y4G
Write a python script that takes input.txt as input, parses it, and produces output.txt as output.
 
The script should be a general script that works on any file supplied with the format of input.txt.
 
The script should be run like this:
 
cat input.txt | python script.py > output.txt
 
[-- input.txt is below --]
 
* This is an outline
 
. It's not a very good outline
 
.. I've seen better
 
.. I've seen worse
 
... I saw a really bad one back in 2008
 
* This is the second numbered item in the outline
 
. This is sub text that spans multiple lines
 
This should be included with the previous line
 
And this line too
 
.. That is more sub text
 
* Numbers
 
. Some text
 
** Lots
 
. Some more text
 
. And some more
 
*** And lots
 
. One
 
.. Two
 
... Three
 
**** Of numbers
 
. Another line
 
** Less Numbers
 
. Text
 
*** More Numbers
 
. Blah
 
* One number again
 
. The last line
 
[-- output.txt is below this line --]
 
1 This is an outline
  + It's not a very good outline
   - I've seen better
   + I've seen worse
    - I saw a really bad one back in 2008
2 This is the second numbered item in the outline
  + This is sub text that spans multiple lines
    This should be included with the previous line
    And this line too
   - That is more sub text
3 Numbers
  - Some text
3.1 Lots
  - Some more text
  - And some more
3.1.1 And lots
  + One
   + Two
    - Three
3.1.1.1 Of numbers
  - Another line
3.2 Less Numbers
  - Text
3.2.1 More Numbers
  - Blah
4 One number again
  - The last line

