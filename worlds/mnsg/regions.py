from typing import Dict, List, NamedTuple
from BaseClasses import Region

class MNSGRegion(Region):
    game = "Mystical Ninja Starring Goemon"

    def __init__(self, name: str, player: int, game: str):
        super().__init__(name, player, game)

class MNSGRegionData(NamedTuple):
    connecting_regions: List[str] = []

region_data_table = {
    "Menu": MNSGRegionData(connecting_regions=["Oedo Town"]),
    "Oedo Town": MNSGRegionData(connecting_regions=["Menu", "Kai Highway"]),
    "Kai Highway": MNSGRegionData(connecting_regions=["Oedo Town", "Mt. Fuji"]),
    "Mt. Fuji": MNSGRegionData(connecting_regions=["Kai Highway"]),
    "Oedo Castle": MNSGRegionData(connecting_regions=["Oedo Town"]),
    "Musashi": MNSGRegionData(connecting_regions=["Oedo Town", "Iga"]),
    "Iga": MNSGRegionData(connecting_regions=["Musashi", "Zazen Town"]),
    "Zazen Town": MNSGRegionData(connecting_regions=["Iga", "Yamato"]),
    "Yamato": MNSGRegionData(connecting_regions=["Zazen Town", "Awaji Island"]),
    "Awaji Island": MNSGRegionData(connecting_regions=["Yamato", "Folkypoke Village"]),
    "Kompira Mountain": MNSGRegionData(connecting_regions=["Folkypoke Village"]),
    "Folkypoke Village": MNSGRegionData(connecting_regions=["Awaji Island", "Kompira Mountain"]),
    
}