---
layout: post
title: March 6 Post Update
date: 2023-03-06 00:00:00 +0300
description: 
---

### Project Update: Nearly finished with the csv file and headway on NN implementation

This past week, I first realized that my csv file that had the 3 million rows of pitch data did not have the umpire names. Therefore, I wrote up a quick scraping program to obtain the umpires based off of the game_ids that were in the corresponding row. At first, I did this row by row, but then realized that the umpire would clearly be the same for some grouping of consecutive pitches, so I just used some memoization to speed up the process. It was still pretty slow, though, so then I used multiprocessing pools to send different html requests at the same time, which gave me the necessary decrease in runtime. Once I finished that, I realized that I also needed a column in my csv for whether or not the x and y coords of each pitch along with the umpire's call resulted in an incorrect call (just a boolean column). In the future, I will probably adjust this column to be able to determine if an umpire is strike-happy or ball-happy (which would be more insightful than just incorrect or correct call). Once I finished those two csv file tasks, I began pseudocoding and roughly implementing a NN model for my project. I ran into a couple of tensor type errors, so I had to do some label encoding, but other than that, it seemed to run ok (although it took forever to run). Now I just need to further refine the model for the next steps in my project. The programs that updated the csv file and the initial NN model program are in my GitHub.   

