---
layout: default
title: Digital Transmission
parent: Waves
nav_order: 6
mathjax: true
---

# Digital Transmission
{: .no_toc }

EQ - _Why do we use digital signals for transmission and storage of data?_
{: .fs-6 .fw-300 .text-blue-000} 

Know - _What digital signals are._
{: .fs-6 .fw-300 .text-blue-000} 

Do - _Analog vs Digital, Storage Comparison, Attenuation_
{: .fs-6 .fw-300 .text-blue-000}

## Introduction
{: .no_toc}
You have heard the word 'digital' your entire life, but do you have any idea what it means?
It turns out that the word is very simply in its definition, **BUT** the consequences are vast.

_For those of you that say math has no use, mathematicians laid the foundations for our current digital age clear back in 1870s!_

<!-- table of contents for the page -->
## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

# Activity - Digital vs Analog
The whole topic is digital, but you must know what problems digital solves.
To outline this, let's play a game.

## Analog Telephone
For this activity, **you need**:
  * At least one other person, the more the merrier.
  * **X** pieces of paper (where **X** is the number of people in a group), post-it notes, or scrap paper work well.
  

Here is the **procedure**
  * Sit in a circle or some sort of obviously ordered arrangement.  _You'll be passing to your neighbor, so everyone must have a neighbor._
  * Now, everyone in the group draw a picture.  The more elaborate you make the picture the better.  _(An example of a great picture would be a squirrel holding a screwdriver.)_
  * Now, pass your pictures to the right.
  * Look at the picture, and then make a copy of the picture.
  * Place your copy on top of the original.
  * Pass the stack to the right.
  * Looking at ***ONLY*** the top picture, make a copy, and add it to the stack.
  * Once done, pass & repeat.
  * Keep repeating till the stack is with the original person.
  * Flip through the stack and LOL, or even ROFLOL if it is necessary.

Here are some reflection questions for you lab notebook.
<label class="tasks-list-item">
  <input type="checkbox" class="tasks-list-cb">
  <span class="tasks-list-mark"></span>
  <span class="tasks-list-desc">
    Did the final picture look identical to your starting picture?
  </span>
</label>
<label class="tasks-list-item">
  <input type="checkbox" class="tasks-list-cb">
  <span class="tasks-list-mark"></span>
  <span class="tasks-list-desc">
    Where does it appear that something went wrong?
  </span>
</label>
<label class="tasks-list-item">
  <input type="checkbox" class="tasks-list-cb">
  <span class="tasks-list-mark"></span>
  <span class="tasks-list-desc">
    What was the main factor in determining how closely the two pictures matched?
  </span>
</label>

## Digital Telephone
For this activity, **you need**:
  * At least one other person, the more the merrier.
  * **X** pieces of paper (where **X** is the number of people in a group), post-it notes, or scrap paper work well.
  

Here is the **procedure**
  * Sit in a circle or some sort of obviously ordered arrangement.  _You'll be passing to your neighbor, so everyone must have a neighbor._
  * Now, everyone in the group draw a grid.  2x2, 3x3, 4x4, 31x41, anything.
  * Now, shade in some of the squares in your grid.  Make a picture out of it if you are feeling creative, or random ones are fine.
  * Now, pass your 'pictures' to the right.
  * Look at the 'picture', and then make the grid and the 'picture'.
  * Place your copy on top of the original.
  * Pass the stack to the right.
  * Looking at ***ONLY*** the top picture, make a copy, and add it to the stack.
  * Once done, pass & repeat.
  * Keep repeating till the stack is with the original person.
  * Flip through the stack and yawn.

Here are some reflection questions for you lab notebook.
<label class="tasks-list-item">
  <input type="checkbox" class="tasks-list-cb">
  <span class="tasks-list-mark"></span>
  <span class="tasks-list-desc">
    How did the 'picture' change?
  </span>
</label>
<label class="tasks-list-item">
  <input type="checkbox" class="tasks-list-cb">
  <span class="tasks-list-mark"></span>
  <span class="tasks-list-desc">
    If it did change, where and why did that change occur?
  </span>
</label>
<label class="tasks-list-item">
  <input type="checkbox" class="tasks-list-cb">
  <span class="tasks-list-mark"></span>
  <span class="tasks-list-desc">
    Now, if you had a really big grid, say 1920x1080, do you think you could make a pretty good picture?
  </span>
</label>
<label class="tasks-list-item">
  <input type="checkbox" class="tasks-list-cb">
  <span class="tasks-list-mark"></span>
  <span class="tasks-list-desc">
    Compare the drawn picture with the grid 'picture'.
  </span>
</label>

Congratulations, you now know why digital is 'better' than analog.
It is super easy to copy accurately.

For those of you that have a lot of free time, or curiosity, here is a video of a comedy act, done by a mathematician, about spreadsheets, that ends with him making a spreadsheet of him making spreadsheets of him making spreadsheets, etc.

[Optional, amazing, video of spreadsheets](https://www.youtube.com/watch?v=UBX2QQHlQ_I){: .btn .btn-outline}


# What is Digital?
Digital is anything that only has 2 possibilities, 2 states.
Think of a light switch, not a new fancy one but the old ones, they are either off or on.
Here is a more extensive list:

| 0 | 1 |
|:-----:|:------:|
| Black | White |
| No | Yes |
| Off | On |
| Up | Down |
| Left | Right |

The important thing is that there is ***NO*** gray with digital, something either is or is not.
No source of confusion.

So, let us connect back to the activity.
  * Your first round where you were drawing pictures, there were an infinite number of possibilities.
    How the line was curved, how long it was, how they were connected, where you picked up the pencil, etc.
  * Your second round though you had a grid.  Either the square was filled in or it wasn't.  There was no confusion as to the state of each square.

To describe digital there are two things to consider.

## Threshold
Threshold is the point at which a signal is considered to be a yes, or a no.
Anything above the threshold is a yes, anything below is a no.

The threshold of a signal will later explain why a digital signal stops working as it gets smaller.

<figure>
<img src="/units/3 waves/resources/digital-threshold.png" alt="drawing" width="90%"/>
<figcaption>Picture showing the yes/no threshold for a digital signal.</figcaption>
</figure>

## Frequency
You are already familiar with frequency, so this will be quick.
Frequency is just how fast the on off signals are being sent.
Think of a light switch, you can only blink the lights about 10 times a second.
However computers can switch at billions of times a second.
More on that later too.

<figure>
<img src="/units/3 waves/resources/digital-frequency.png" alt="drawing" width="90%"/>
<figcaption>The frequency of a digital signal.  There are 10 states in 1 second, so the frequency is 10 Hz.</figcaption>
</figure>



# Activity - Storage Comparison

# How does attenuation effect digital transmission?

# Conclusion
Answer the following in your lab notebook in complete sentences.
  * <font color='blue'>How have I behaved in class today?</font>
  * <font color='blue'>How could I better contributed to a positive classroom environment.</font>
  * <font color='blue'>Summarize what you learned today in 1 sentence.</font>
  * <font color='blue'>Answer the days essential question (EQ).</font>