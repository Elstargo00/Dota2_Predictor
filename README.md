# Dota2_Predictor

One day I've learned (Andrew Ng) neural networks course from Coursera. There is one assignment that wants me to program ML that's able to classify a binary problem ('cat' or 'NOT cat.'). After doing that, I seek somewhere that I can utilize it with excitement. But where the hell can I use 'cat' or 'NOT cat' application in my routine? I need to come up with a side project that, likewise, able to classify a thing (binary problem) and a bit fun and useable. And that's a Dota2 Predictor


I'm a big fan of Dota2. If you have no idea what Dota2 is, here are very brief explanations. Dota2 is a MOBA game.
There are two teams with 5 players on each. Each player will pick their hero (can't be the same).
Finally, the game has only one winning team, which could be 'Team Dire' or 'Team Radiant.'
What I want to build is ML that's able to classify <b> the picture of the victory </b> of the radiant team.
If the output = 1, it means "Radiant Victory." Else (the output = 0), means "NOT Radiant Victory". It's pretty much the same concept with 'cat' or 'NOT cat.'

So how <b> the picture of the victory </b> team will look like?

I have to build up some criteria that can represent the achievements of the team, player and hero, and that's criteria shold be quantitative enough to tell who gonna win the match. Look at the picture might help you to get some the idea.

Pre-feature: string match record =>
![alt text](https://github.com/Elstargo00/Dota2_Predictor/blob/master/images/history.png?raw=true)


feature: Numercial float match score record =>

![alt text](https://github.com/Elstargo00/Dota2_Predictor/blob/master/images/num_history.png?raw=true)

In the example, I've changed from 'string record' to 'numerical record.' Why I choose "team, player, hero" as a pre-feature? 
Since they're reliable statistics that have been used throughout Dota2 history programs, you will often see the record win/lose of Player: Hero shown up.


So the idea is to train a machine to know the picture of the winning match (high value of pixel above) or the losing match (low value of pixel above).

Each time we predict, it requires information of:
1. (The radiant team) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  7. (The radiant team)  
2. Position 1 of the radiant team (Player:Hero) &nbsp;  8. Position 1 of the dire team (Player:Hero)
3. Position 2 of the radiant team (Player:Hero) &nbsp;  9. Position 2 of the dire team (Player:Hero)
4. Position 3 of the radiant team (Player:Hero) &nbsp; 10. Position 3 of the dire team (Player:Hero)
5. Position 4 of the radiant team (Player:Hero) &nbsp; 11. Position 4 of the dire team (Player:Hero)
6. Position 5 of the radiant team (Player:Hero) &nbsp; 12. Position 5 of the dire team (Player:Hero)

And the string "team/player: hero" will be searched from the historical records (shown above) and change to the numerical score to predict this game the radiant will win or not.


Let's view how it looks like:

![alt text](https://github.com/Elstargo00/Dota2_Predictor/blob/master/images/1.png?raw=true)

![alt text](https://github.com/Elstargo00/Dota2_Predictor/blob/master/images/1.png?raw=true)

![alt text](https://github.com/Elstargo00/Dota2_Predictor/blob/master/images/3.png?raw=true)

![alt text](https://github.com/Elstargo00/Dota2_Predictor/blob/master/images/4.png?raw=true)


The first version that I built is only a simple logistic regression model. For the performance, it's working pretty well based on the gambling game that I won.
(16/18 which's not bad) However, the dynamic for the user is suck. I didn't build the DB forming system that can automatically pull the name of team/player: hero. When one fills in the input of team/player: hero, it required exact string input to search for in the score database. If you fill the wrong name, then the result could be worse.
