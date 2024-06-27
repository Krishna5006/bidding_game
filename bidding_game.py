print("Welcome To The Auction")
bid_record={}
no_of_player=int(input("Enter the no of player playing the game"))
def bidding(no_of_player):
  for i in range(no_of_player):
    name=input("Enter your name? ")
    bid=int(input("What's your Bid: ₹"))
    bid_record[name]=bid
  #print(bid_record)

def bid_winner():
  bid_list=[]
  name_list=[]
  for money in bid_record:
    bid_list.append(bid_record[money])
    name_list.append(money)
  #print(bid_list)
  #print(name_list)
  maximum_bid=max(bid_list)

  index_bid=bid_list.index(maximum_bid)

  bid_winner_name=name_list[index_bid]
  print(f"The winner is {bid_winner_name} with a bid of ₹{maximum_bid}")

bidding(no_of_player)
bid_winner()