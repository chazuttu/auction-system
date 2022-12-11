import logging

from auction_system.auction import Auction
from auction_system.auction_house import AuctionHouse
from auction_system.participant import Participant

from auction_system.item import Item

__author__ = "Guillaume Pouilloux <gui.pouilloux@gmail.com>"

logging.getLogger().setLevel(logging.INFO)


# Main test - auction house scenario
def main():
    auction_house = AuctionHouse()

    guillaume = Participant("Guillaume")
    antonin = Participant("Antonin")

    painting_name = "Van Gogh's painting"
    painting = Item(painting_name, 1000)
    auction_painting = Auction(painting)

    auction_house.add_auction(auction_painting)
    # should fail - auction already added
    auction_house.add_auction(auction_painting)

    # auction has not been started yet
    guillaume.bid(auction_painting, 101)

    auction_painting.start()

    guillaume.bid(auction_painting, 101)
    antonin.bid(auction_painting, 999)
    # guillaume should bid more than 999
    guillaume.bid(auction_painting, 102)
    guillaume.bid(auction_painting, 1002)

    auction_painting.stop()

    logging.info(auction_house.latest_auction_by_item_name(painting_name))

    # should fail
    Auction(painting)

    # should fail
    auction_painting.start()


if __name__ == '__main__':
    main()
