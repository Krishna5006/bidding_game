print("Welcome To The Auction")
bid_record={}
play=input("Are there any other bidders? Type  Y or N: ")

def bidding():
  name=input("Enter your name? ")
  bid=int(input("What's your Bid: ₹"))
  bid_record[name]=bid

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

while play=="Y":
  bidding()
  play=input("Are there any other bidders? Type  Y or N: ")
  
else: 
  bid_winner()