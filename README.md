# pig_bots

Write code for an AI to play the dice game of "Pig".

All pig bots will play against each other in an epic battle royale. Will your bot be the best?

## Rules

Your submission will consist of one function named `choice()` . The game will pass to the function three arguments:

* `round_score` - the score for the current round
* `my_score` - the bot's current banked score
* `opponent_score` - the opponent's current banked score

The function should return a Boolean representing the choice:

* `True` - roll again
* `False` - stop and bank the round score

It's up to you to determine how the bot chooses what to do.

Here's a really simple example - a bot that rolls until it gets more than 12 points:

```python
def choice(round_score, my_score, opponent_score):
    return round_score <= 12
```

## Testing

You can use the `pig.py` program to play against your bot and test if it works. Replace the `choice()` function with yours.

## Submitting your bot

1. Click the "Add file" button above and choose "Create new file".
2. In the "Name your file..." box, you *must* name your bot `bot_username.py` so it can be identified as belonging to you.
3. Paste your `choice()` function in the box, and then click the green *Propose new file* button.
4. Click the green *Create pull request* button to submit your bot.

You may submit up to 5 bots, just name each one with a 2, 3, 4, etc., such as `bot_bradfield2.py`.
