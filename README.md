# Dota2_Predictor

[Modified on: 18/11/21]

This work is inspired by "cat" or "NOT cat" classification problem from Coursera (Andrew Ng). So what if instead of "cat" or "NOT cat" but "win" or "NOT win" in MOBA game match. Dota2 Predictor is a logistic regression model that's able to classify binary classes.

Dota2 is a MOBA game. There are 2 teams fighting against each other. Each team has 5 players. Individuals will pick hero for selves. Chosen heros will be unique (There is no same hero walking in the game). There is only 1 team winning which could be "Team Radiant" or "Team Dire". We will build model that's able to predict the victory of Team Radiant. Whether it's WIN or NOT. 

The records of player achievements for each hero will be used as training feature. Let's look at it step by step. 

## 1. Collect data
We need match record in csv format looks something like this:

<table>
  <theader>
    <tr>
      <th>Team Radiant</th>
      <th>Player:Hero</th>
      <th>Player:Hero</th>
      <th>Player:Hero</th>
      <th>Player:Hero</th>
      <th>Player:Hero</th>
      <th>Team Dire</th>
      <th>Player:Hero</th>
      <th>Player:Hero</th>
      <th>Player:Hero</th>
      <th>Player:Hero</th>
      <th>Player:Hero</th>
      <th>Results</th>
    <tr>
  </theader>
</table>

Here is what raw data looks like:
<img width="900px" src="https://github.com/Elstargo00/Dota2_Predictor/blob/master/images/history.png">

## 2. Manipulate data
Based on labels ("win" or "not win") in the last column, we manage to record team and player:hero acheivements as numerical features as shown in the following:

<img width="900px" src="https://github.com/Elstargo00/Dota2_Predictor/blob/master/images/num_history.png">

## 3. Predict 
Fill form by giving inputs as string of the current match that you want to predict

### Review some pages:

<img width="900px" src="https://github.com/Elstargo00/Dota2_Predictor/blob/master/images/1.png">
<img width="900px" src="https://github.com/Elstargo00/Dota2_Predictor/blob/master/images/2.png">
<img width="900px" src="https://github.com/Elstargo00/Dota2_Predictor/blob/master/images/3.png">
<img width="900px" src="https://github.com/Elstargo00/Dota2_Predictor/blob/master/images/4.png">


### Conclusion:
The model works pretty well based on the gambling game that I won (16 out of 18). Not bad at all. However, the web application is the worst in terms of User Experience (UX). You need to entry the exact string in the form (that's why we need the "Name Encyclopedia" page as references). So that model are able to retrieve  the correct numerical features, recorded in database.
