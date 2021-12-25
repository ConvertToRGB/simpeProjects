 ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

# A couple of simple simple scripts. 
Some of them help with simple tasks, other are made just for fun.
All scripts are organized by language they were written and interpreter version.

Every folder which contains scripts has readme.md file that explains what every script is doing.

---

# List of all scripts in this repository.

## Python
#### Python version: 2.7

- #### rsm.py
Simple script that was made for fun. It removes some letter from string and return it. 
Try this string: RoskomnadzorBannedLetter

- #### sum.py
Get sum of integer digits. For example:
`123 => 1+2+3=6`

- #### nod.py
  find out NOD (greatest common factor)

- ### chess_notation.py

  This script was made to get chess notation from [logic-games](https://logic-games.spb.ru/chess/). 
  There is no capability to copy chess notation from this site. By using this script you can 
  import ` <body></body> ` part element and save it as *.txt

  `*.txt` content must look like this:

```html
<tbody>
    <tr>
        <td>1</td>
        <td data-nmove="1" class="chessHistoryActiveMove">e4</td>
        <td data-nmove="2" class="">e5</td>
    </tr>
    <tr>
        <td>2</td>
        <td data-nmove="3">Nf3</td>
        <td data-nmove="4">Nc6</td>
    </tr>
    <tr>
        <td>3</td>
        <td data-nmove="5">Nc3</td>
        <td data-nmove="6">Bc5</td>
    </tr>
    <tr>
        <td>4</td>
        <td data-nmove="7">Be2</td>
        <td data-nmove="8">Nd4</td>
    </tr>
</tbody>
```

  **(!) Warning! No Cyrillic symbols allowed!**


- ### my_VKbot.py

  Bot that was written for [VK](https://vk.com)
  It automatically sends answer on every PM message from selected user.
  
- ### renamer.py

  Rename files that are dropped on that script. For example you have some pictures and they have random names [`banana.png`, `apple.jpg`, `nebula.jpg`] and you need to create sequence like [`pic_001.png`,`pic_002.jpg`, `pic_003.jpg`] then this script can help with this task. You must set new name and you can set padding (by default padding=3).

#### Python version: 3.8

- upperDecor.py

  Was created for faster stylizing `*.md` file. It allow user to set his text decorator when asked, for example: 
  `!!!mydecorator!!!`
  and make all income text in caps. Then user type string what requires decoration, for example:
  `my_string`
  The result string will be this: 
  `!!!mydecorator!!!MY_STRING!!!mydecorator!!!`
  This string then is copied to clipboard and then program waits for the next string. Two command are allowed:

  - 'stop' - stop program
  - 'change' - change decoration string

---

## JavaScript

- #### effect_cleaner.jsx
Script for Adobe After Effects.
Was tested on Adobe After Effects CC 2014

Remove chosen Effect from selected layers.
