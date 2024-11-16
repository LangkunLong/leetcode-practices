from collections import defaultdict

class Orderbook:
    def __init__(self) -> None:
        self.orderBook = defaultdict(tuple)
        self.buyOrders = defaultdict(int)
        self.sellOrders = defaultdict(int)

class ArtistBook:
    def __init__(self) -> None:
        self.artistbooks = defaultdict(Orderbook)
        
    def add_order(self, orderID, price, quantity, artist):
        self.artistbooks[artist].orderBook[orderID] = (price, quantity)
        if quantity > 0:
            self.artistbooks[artist].buyOrders[price] += quantity
        else:
            self.artistbooks[artist].sellOrders[price] += -quantity
        
    def del_order(self, orderID, artist):
        if orderID in self.artistbooks[artist].orderBook:
            price, quantity = self.artistbooks[artist].orderBook.pop(orderID)
            # if there is existing quantity, remove the order quantity, if quantity is 0, remove the order
            if quantity > 0: #buy order
                self.artistbooks[artist].buyOrders[price] -= quantity
                if self.artistbooks[artist].buyOrders[price] == 0:
                    del self.artistbooks[artist].buyOrders[price]
            else:
                self.artistbooks[artist].sellOrders[price] -= -quantity
                if self.artistbooks[artist].sellOrders[price] == 0:
                    del self.artistbooks[artist].sellOrders[price]
                    
    def delete_price_level(self, price, artist):
        if price in self.artistbooks[artist].buyOrders:
            del self.artistbooks[artist].buyOrders[price]
        if price in self.artistbooks[artist].sellOrders:
            del self.artistbooks[artist].sellOrders[price]
            
def process_operations(operations):
    
    artists_books = ArtistBook()
    for operation in operations[:-1]:
        tokens = operation.split()
        action = tokens[0]
        if action == "ADD":
            order_id = int(tokens[1])
            artist = tokens[2]
            price = int(tokens[3])
            quantity = int(tokens[4])
            artists_books.add_order(order_id, price, quantity, artist)
        
        elif action == "DEL":
            order_id = int(tokens[1])
            artist = tokens[2]
            artists_books.del_order(order_id, artist)
        
        elif action == "DEL_PRICE":
            artist = tokens[1]
            price = int(tokens[2])
            artists_books.delete_price_level(price, artist)
    
    # Last line indicates which artist and how many levels to view
    artist, num_levels = operations[-1].split()
    num_levels = int(num_levels)
    
    # Retrieve the buy and sell ladders
    book = artists_books.artistbooks[artist]
    buy_levels = sorted(book.buyOrders.items(), key=lambda x:x[0], reverse=True)  # Descending order
    sell_levels = sorted(book.sellOrders.items())  # Ascending order
    
    # Output result
    print(artist)
    for i in range(num_levels):
        if i < len(sell_levels):
            sell_price, sell_quantity = sell_levels[i]
            print(f"0 {sell_price} {sell_quantity}")
    
    for i in range(num_levels):
        if i < len(buy_levels):
            buy_price, buy_quantity = buy_levels[i]
            print(f"{buy_quantity} {buy_price} 0")
    
# Example Usage
operations = [
    "ADD 1 TaylorSwift 100  10",
    "ADD 2 TaylorSwift 101 -10",
    "ADD 3 TaylorSwift 99   5",
    "ADD 4 TaylorSwift 102 -5",
    "ADD 5 TaylorSwift 100  2",
    "DEL 1 TaylorSwift",
    "TaylorSwift 2"
]

process_operations(operations)