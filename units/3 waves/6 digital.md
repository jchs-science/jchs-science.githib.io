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

| ON | OFF |
|:-----:|:------:|
| Black | White |
| No | Yes |
| 0 | 1 |
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
Threshold is the point at which a signal is considered to be a ON or OFF.
Anything above the threshold is ON, anything below is a OFF.

The threshold of a signal will later explain why a digital signal stops working as it gets smaller.

<figure>
<img src="/units/3 waves/resources/digital-threshold.png" alt="drawing" width="90%"/>
<figcaption>Picture showing the ON/OFF threshold for a digital signal.</figcaption>
</figure>

Still confused?
Let's try a different approach.
Imagine you are drawing a picture and you make a mistake.
So you erase something.
You then keep going and make your picture perfectly.
Now, when you show someone else your picture they will know that you have erased something, but they can't really tell what was there before.
Since they can't really see it, they'll ignore it and only consider the darker lines that you've made.
That is what a threshold is, the cutoff for when you consider something.
In digital it is just very, very sharply defined.

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


# How does attenuation effect digital transmission?
This is actually fairly straight forward.
Think back to your activity where you were muffling your speaker.
<label class="tasks-list-item">
   <input type="checkbox" class="tasks-list-cb">
   <span class="tasks-list-mark"></span>
   <span class="tasks-list-desc">
     Which property of a wave changed when you built your muffler for your speaker? _Hint, it was only one of the 4 we have covered._
   </span>
</label> 

<label class="tasks-list-item">
  <input type="checkbox" class="tasks-list-cb">
  <span class="tasks-list-mark"></span>
  <span class="tasks-list-desc">
    Now, make a picture of two waves, showing what happens as it passes through a muffler, or anything that absorbs it, use the image below as a prompt.
  </span>
</label>

<figure>
<img src="/units/3 waves/resources/digital-absorbed-blank.png" alt="drawing" width="90%"/>
<figcaption>Sketch showing what you should have in your lab notebook for how your muffler changed the sound.</figcaption>
</figure>

Now, if you are stuck, [click here](#help-with-absorption)

So how does this relate to digital?
<label class="tasks-list-item">
  <input type="checkbox" class="tasks-list-cb">
  <span class="tasks-list-mark"></span>
  <span class="tasks-list-desc">
  Well, what do you think happens if you are trying to figure out if a signal is over the threshold if it keeps getting smaller?  
  </span>
</label>
<label class="tasks-list-item">
  <input type="checkbox" class="tasks-list-cb">
  <span class="tasks-list-mark"></span>
  <span class="tasks-list-desc">
    So if the signal gets 'absorbed' by too many things, would you still be able to interpret the signal?
  </span>
</label>


# Activity - Storage Comparison
Who likes music and movies?
Every wonder about those discs that they used to store them on?
What about NetFlix and why it is a bad idea to use mobile data with it?

The thing about digital is that the frequency has to be really, really fast for it to be any use to us.
Think back to the picture earlier.
If you could only fill in one square every second, it would take you forever to make a picture.
Instead, computers can fill in billions of squares a second.
Just how fast you ask, well, off to wikipedia.

## Instructions
For each of the items in the table below, you are going to find the format in 
[this wikipedia page](https://en.wikipedia.org/wiki/Bit_rate#Audio){: .btn .btn-outline}, with the exception of NetFlix, you are going to have to find that one else where.

<label class="tasks-list-item">
  <input type="checkbox" class="tasks-list-cb">
  <span class="tasks-list-mark"></span>
  <span class="tasks-list-desc">
    Copy and fill out the following table in your notes.
  </span>
</label>

| Format               | Bit rate |
|----------------------|----------|
| MP3 - medium quality |          |
| CD (look for CD-DA)  |          |
| YouTube 240p         |          |
| YouTube 720p         |          |
| YouTube 1080p        |          |
| DVD                  |          |
| Blu-Ray              |          |
| NetFlix**            |          |

And now, questions for your lab notebook
<label class="tasks-list-item">
  <input type="checkbox" class="tasks-list-cb">
  <span class="tasks-list-mark"></span>
  <span class="tasks-list-desc">
    Describe the difference between watching YouTube at 240p and watching YouTube at 1080p.
  </span>
</label>
<label class="tasks-list-item">
  <input type="checkbox" class="tasks-list-cb">
  <span class="tasks-list-mark"></span>
  <span class="tasks-list-desc">
    Compare the bit rate for 1080p with the bit rate for 240p, how much higher is it?
  </span>
</label>
<label class="tasks-list-item">
  <input type="checkbox" class="tasks-list-cb">
  <span class="tasks-list-mark"></span>
  <span class="tasks-list-desc">
    Describe the difference between watching a moving on DVD and Blu-ray?
  </span>
</label>
<label class="tasks-list-item">
  <input type="checkbox" class="tasks-list-cb">
  <span class="tasks-list-mark"></span>
  <span class="tasks-list-desc">
    The bit rate corresponds to the amount of information that the signal carries.  If the bit rate is higher, does it look/sound better?
  </span>
</label>
<label class="tasks-list-item">
  <input type="checkbox" class="tasks-list-cb">
  <span class="tasks-list-mark"></span>
  <span class="tasks-list-desc">
    Have you ever switched from WiFi to Cellular, or moved around, and had YouTube or NetFlix lower the video quality so it looked grainy?  What do you think was happening?  _Describe it using bit rate..._
  </span>
</label>


# Conclusion
Answer the following in your lab notebook in complete sentences.
<label class="tasks-list-item">
  <input type="checkbox" class="tasks-list-cb">
  <span class="tasks-list-mark"></span>
  <span class="tasks-list-desc">
    How have I behaved in class today?
  </span>
</label>
<label class="tasks-list-item">
  <input type="checkbox" class="tasks-list-cb">
  <span class="tasks-list-mark"></span>
  <span class="tasks-list-desc">
    How could I better contributed to a positive classroom environment.
  </span>
</label>
<label class="tasks-list-item">
  <input type="checkbox" class="tasks-list-cb">
  <span class="tasks-list-mark"></span>
  <span class="tasks-list-desc">
    Summarize what you learned today in 1 sentence.
  </span>
</label>
<label class="tasks-list-item">
  <input type="checkbox" class="tasks-list-cb">
  <span class="tasks-list-mark"></span>
  <span class="tasks-list-desc">
    Answer the days essential question (EQ).
  </span>
</label>


# Help with absorption
{: .no_toc}
So, the property is the amplitude.
When the sound comes out of the speaker it still sounds like music so the frequency and speed don't change, that leaves the amplitude.
The muffler makes it smaller.
So your picture should look something like...
<figure>
<img src="/units/3 waves/resources/digital-absorbed-filled.png" alt="drawing" width="90%"/>
<figcaption>Sketch showing what you should have in your lab notebook for how your muffler changed the sound.</figcaption>
</figure>

