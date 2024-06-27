# Auction Bidding Script

This is a simple auction bidding script written in Python. It allows multiple players to enter their bids, records these bids, and then determines the highest bidder as the winner.

## Description

This repository contains two versions of a simple auction bidding script written in Python:

1. **Fixed Number of Players Version**: In this version, the number of players is fixed, and user inputs are taken for each player's name and bid amount. The script records these bids and determines the highest bidder as the winner after all bids are entered.

$ python auction_bidding.py
Welcome To The Auction
Enter the no of player playing the game: 3
Enter your name? Alice
What's your Bid: ₹100
Enter your name? Bob
What's your Bid: ₹150
Enter your name? Charlie
What's your Bid: ₹120
The winner is Bob with a bid of ₹150


2. **Dynamic Bidders Version**: In this version, the script continuously accepts bids until no more bidders remain. After each bid, the user is prompted to indicate if there are additional bidders. The script records these bids and determines the highest bidder as the winner once all bids are entered.

$ python auction_bidding.py
Welcome To The Auction
Are there any other bidders? Type Y or N: Y
Enter your name? Alice
What's your Bid: ₹100
Are there any other bidders? Type Y or N: Y
Enter your name? Bob
What's your Bid: ₹150
Are there any other bidders? Type Y or N: Y
Enter your name? Charlie
What's your Bid: ₹120
Are there any other bidders? Type Y or N: N
The winner is Bob with a bid of ₹150
