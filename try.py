"""
created by Nagaj at 02/06/2021
"""

from dataclasses import dataclass


@dataclass
class Capital:
    name: str
    location: str
    country = None


@dataclass
class Country:
    name: str
    pop: str
    capital: Capital

    def update_capital(self):
        self.capital.country = self


cairo = Capital("CAIRO", "NORTH")
egp = Country("egypt", "100M", cairo)

print(egp)
