x = {
    'ice': {'bids': [10, 20, 30], 'bidders': ['ace', 'ken', 'kyle']},
    'candy': {'bids': [50, 20, 10], 'bidders': ['ace', 'ken', 'kyle']}
}

result_dict_list = []

for item_name, item_data in x.items():
    bids = item_data['bids']
    bidder_names = item_data['bidders']

    highest_bid_index = bids.index(max(bids))
    highest_bid = bids[highest_bid_index]
    highest_bidder_name = bidder_names[highest_bid_index]

    result_dict = {
        'Item': item_name,
        'HighestBid': highest_bid,
        'HighestBidder': highest_bidder_name,
        'IndexofHighestBid': highest_bid_index
    }

    result_dict_list.append(result_dict)

print(result_dict_list)
