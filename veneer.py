class Art:
    def __init__(self, artist, title, year, medium, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        return "{artist}. \"{title}\". {year}, {medium}, {ownername}, {ownerlocation}.".format(artist=self.artist,
                                                                                               title=self.title,
                                                                                               year=self.year,
                                                                                               medium=self.medium,
                                                                                               ownername=self.owner.name,
                                                                                               ownerlocation=self.owner.location)


class Marketplace:
    def __init__(self):
        self.listings = []

    def add_listings(self, new_listing):
        self.listings.append(new_listing)

    def remove_listing(self, listing):
        self.listings.remove(listing)

    def show_listings(self):
        for listing in self.listings:
            print(listing)


class Client:
    def __init__(self, name, is_museum, wallet, location="Private Collection"):
        self.name = name
        self.location = location
        self.is_museum = is_museum
        self.wallet = wallet

    def sell_artwork(self, artwork, price):
        if artwork.owner == self:
            listing = Listing(artwork, price, self.name)
            veneer.add_listings(listing)

    def buy_artwork(self, artwork):
        if artwork.owner != self:
            count = 0
            for listing in veneer.listings:
                if listing.art == artwork:
                    self.wallet -= listing.price
                    artwork.owner.wallet += listing.price
                    artwork.owner = self
                    veneer.remove_listing(listing)
                count += 1


class Listing:
    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        return "\"{name}\", The price: ${price}M (USD).".format(name=self.art.title, price=self.price)


veneer = Marketplace()

# print(veneer.show_listings())

edytta = Client("Edytta Halpirt", False, 10)
moma = Client("The MOMA", True, 10, "New York")

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", 1910, "oil in canvas", edytta)

# print(girl_with_mandolin)
print("${}M (USD).".format(moma.wallet))
print("${}M (USD).".format(edytta.wallet))

edytta.sell_artwork(girl_with_mandolin, 6)

moma.buy_artwork(girl_with_mandolin)

print(girl_with_mandolin)

veneer.show_listings()

print("${}M (USD).".format(moma.wallet))
print("${}M (USD).".format(edytta.wallet))











