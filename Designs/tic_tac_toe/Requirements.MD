## Questions to Ask
- Will the game be played amongst only 2 players or can there be any number of players in future?
- Is the board size restricted to 3x3 or can it be any NxN?

## Feature Suggestions:
- Do we want to time a move? Skip/ Declare the other person as winner if the move doesn’t happen within x seconds.
- Do we want to support undo operation?
- Can there be some players who are just watching? Not playing.
- Do we want to store analytics? Basically previous games, who played what move etc.
- Can one of the players be a bot?
- Support for tournaments? Basically a set of matches, each match between 2 players of the tournament.
- Can there be different ways to win?

## Expectations
- The code should be working and functionally correct
- Good software design practices should be followed:
- Code should be modular, readable, extensible
- Separation of concern should be addressed
- Project structured well across multiple files/ packages
- No need of GUI

# Problem Requirements
- Computer application.
- Board can be of any NxN size.
- There can be any number of players. Each player will be allotted a symbol.
- The players can be either humans or bots(max 1). Each human player will have a name.
- We should allow support to undo any number of moves.
- There can be different ways to win. (and In a game there can be multiple types of strategies to win)
- Bot can have different difficulty
- Game ends when anyone win/ Draw
- players make move in a random order
- check if someone has won in O(1).

## Interaction Format
- Command Line based interactive application.
- Input/ Outputs:
- ```Game Start```
- Allows to start the game with a given number of players, board size, and symbols of every player.

StartGame [Number of Players] [... User ID and Symbol for each player separated by space ...] [Board Size]


Example:

StartGame 2 u1 X u2 O 3


If a player is a computer, their user id will be C.
