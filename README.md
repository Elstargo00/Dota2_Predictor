# Dota2_Predictor

One day I've learn (Andrew Ng) neural networks course from Coursera. There is one assigment that want me to program ML that's able to classify binary problem.
The picture is 'cat' or 'NOT (cat)'. After that I seek to apply it with excitement. But where the hell can I use 'cat' or 'NOT cat' application in my routine?
I need to come up with a side project that, likewise, able to classify a thing (binary problem) and a bit fun and useable. And that's a Dota2 Predictor


I'm a big fan of Dota2 game. If you have no idea what Dota2 is, here are very brief explanations. Dota2 is a moba game.
There are 2 teams with 5 player on each. Each player will pick their own hero (can't be the same).
Finally the game has only 1 winner team which could be 'Team Dire' or 'Team Radiant'.
What I want to build is ML that's able to classify <b>the picture of the victory</b> of the radiant team.
If the output = 1, it's mean "Radiant Victory". Else (the output = 0), mean "NOT Radiant Victory". It's pretty much the same concept with 'cat' or 'NOT cat'.

So how <b>the picture of the victory</b> team will look like?

I have to create some criterias that are able to represent the acchievement of team, player and hero and that's criteria shold be quantitative enough to tell
that who gonna win this match. Look at the picture might help you to under stand the idea.

![alt text](some URL)


In the example, I've changed from 'string record' to 'numerical record'. Why I choose "team, player, hero" as a pre-feature? 
Since they're reliable statistics that have been used throughout dota2 history program, you will oftenly see the record win/lose of Player:Hero shown up.


So the idea is to train the machine to know that this is the picture of wining match (high value of pixel above) or losing match (low value of pixel above).

Each time we predict, it requires information of:
1. (The radiant team)                                  7. (The radiant team)  
2. Position 1 of the radiant team (Player:Hero)        8. Position 1 of the dire team (Player:Hero)
3. Position 2 of the radiant team (Player:Hero)        9. Position 2 of the dire team (Player:Hero)
4. Position 3 of the radiant team (Player:Hero)       10. Position 3 of the dire team (Player:Hero)
5. Position 4 of the radiant team (Player:Hero)       11. Position 4 of the dire team (Player:Hero)
6. Position 5 of the radiant team (Player:Hero)       12. Position 5 of the dire team (Player:Hero)

And the string "team/player:hero" will be searched from history record and change to the numerical score to predict this game the radint will win or not.

Let's view how it looks like:

![alt text](some URL)


The first version I built only simple logistic regression model. For the performance, it's working pretty well base on the gambling game that I won.
16/18 not bad hmm?
