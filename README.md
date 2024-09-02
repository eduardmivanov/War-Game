# War-Game
Welcome to the War Card Game repository! This project is an implementation of the classic card game "War" using Python. The game is simple, fun, and a great way to learn and practice programming skills, particularly in object-oriented programming (OOP).

Game Rules
"War" is a simple card game typically played by two players. The game uses a standard 52-card deck, and the goal is to win all the cards.

Setup: The deck is shuffled, and each player is dealt half of the cards (26 cards each).
Gameplay:
Both players draw the top card of their deck and reveal it simultaneously.
The player with the higher-ranked card wins the round and takes both cards, placing them at the bottom of their deck.
If the cards are of the same rank, a "war" is declared:
Both players place three cards face down and then one card face up.
The player with the higher face-up card wins all the cards in play.
If there is another tie, the "war" process repeats.
Winning the Game: The game continues until one player has all 52 cards or until a pre-determined number of rounds have been played.
Features
Full Game Logic: Implements the full logic of the War card game, including shuffling, dealing, and the "war" scenario.
Object-Oriented Design: Uses OOP principles to define classes for Card, Deck, and Player.
Simple User Interface: Command-line interface to play the game, with clear prompts and output.
Randomized Deck: Ensures a random and fair shuffle for each game session.
Game Replay: Players can choose to play multiple rounds in one session.
