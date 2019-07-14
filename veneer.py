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
        self.listing.append(new_listing)

    def remove_listing(self, listing):
        self.listing.remove(listing)

    def show_listings(self):
        for listing in self.listings:
            print(listing)


class Client:
    def __init__(self, name, is_museum, location="Private Collection"):
        self.name = name
        self.location = location
        self.is_museum = is_museum


veneer = Marketplace()

# print(veneer.show_listings())

edytta = Client("Edytta Halpirt", False)
moma = Client("The MOMA", "New York", True)

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", 1910, "oil in canvas", edytta)

print(girl_with_mandolin)




