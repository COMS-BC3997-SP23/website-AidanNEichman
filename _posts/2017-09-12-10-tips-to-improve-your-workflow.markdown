---
layout: post
title: Feb 13 Post Update
date: 2023-02-13 00:00:00 +0300
description: 
img: workflow.jpg # Add image post (optional)
fig-caption: # Add figcaption (optional)
---

## Background Research
This week, the focus of the project was on conducting extensive background research on current implementations of machine learning (ML) and predictions in the realm of sports. The goal was to identify any weaknesses or gaps in existing models and determine whether they should be maintained or filled. The research conducted during this week did not necessary led to the conclusion about which algorithms and infrastructure I should be using (though I still have a feeling that I will end up using neural networks and backpropagation for this project). 

## Web Scraping Update
To gather data for the project, the primary focus was on writing code for web scraping. I utilized Chrome driver and selenium, tools that were new to me, and conducted some initial research to become familiar with these tools. The code written this week was designed to visit the ESPN website and gather information on game IDs. The program moves through the schedule of games from a given start day, compiling the gameIDs for each game, and then moves on to the next day of games until the end date is reached. This code allowed me to gather all of the gameIDs needed for the main web scraping implementation.

Once the gameIDs were gathered, I started writing the program to scrape all of the data needed from each game. For Major League Baseball (MLB), the data gathered includes pitch location, speed, umpires, base situations, and weather conditions. For the National Basketball Association (NBA), the data includes shots, game minutes, efficiency, and injury reports.

Moving forward, I plan to refine the web scraping code to account for all necessary variables so that the data can be cleaned up. The goal is to ensure that the data is as accurate and complete as possible, as this will be critical for the success of the project. In addition, I may also need to consider any ethical considerations related to web scraping, such as respecting the privacy of individuals and ensuring that data is collected in a responsible and legal manner.

In conclusion, this week was an important step in the development of this project, as I conducted valuable background research and made significant progress in gathering data through web scraping. The use of neural networks and backpropagation, as well as the collection of data through web scraping, will be critical in ensuring that the project is successful. 
