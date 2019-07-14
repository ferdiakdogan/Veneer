class Art:
    def __init__(self, artist, title, year, medium):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year

    def __repr__(self):
        return "{artist}. \"{title}\". {year}, {medium}.".format(artist=self.artist, title=self.title, year=self.year,
                                                                 medium=self.medium)


class Marketplace:
    def __init__(self):
        self.listings = []

    def add_listings(self, new_listing):
        self.listing.append(new_listing)

    def remove_listing(self, listing):
        self.listing.remove(listing)

    def show_listings(self):
        for listing in self.listings:
            print(listing)


girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", 1910, "oil in canvas")

# print(girl_with_mandolin)

veneer = Marketplace()

print(veneer.show_listings())



