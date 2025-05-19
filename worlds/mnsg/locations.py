from typing import Callable, Dict, NamedTuple, Optional, TYPE_CHECKING
from BaseClasses import Location
from BaseClasses import LocationProgressType
from dataclasses import dataclass

if TYPE_CHECKING:
    from . import MNSGWorld

class MNSGLocation(Location):
    game = "Mystical Ninja Starring Goemon"

    def __init__(self, player, name, address, region, locked_item=None):
        super().__init__(player, name, address, region)
        self.locked_item = locked_item  # set locked_item here as an attribute
        
    def can_fill(self, state, item, check_access=True):
        # By default allow all items to fill here, or add custom logic
        return True
        



@dataclass
class MNSGLocationData:
    region: str
    address: int
    progression: bool = True
    item_rule: Optional[Callable[["MNSGWorld", int], bool]] = None
    access_rule: Optional[Callable[["MNSGWorld", int], bool]] = None
    always_allow: Optional[Callable[["MNSGWorld", int], bool]] = None
    never_allow: Optional[Callable[["MNSGWorld", int], bool]] = None
    progress_type: LocationProgressType = LocationProgressType.DEFAULT
    locked_item: Optional[str] = None  # You’re checking for this in `locked_locations`, but it’s not in the class!
    
    def can_create(self, world) -> bool:
        return True  # or your custom logic



location_data_table: Dict[str, MNSGLocationData] = {
    "Silver Fortune Doll Guards": MNSGLocationData(
        region="Oedo Town",
        address=1,
    ),
    "Received Map of Japan": MNSGLocationData(
        region="Kai Highway",
        address=2,
    ),
    "Silver Fortune Doll Kai Highway": MNSGLocationData(
        region="Kai Highway",
        address=3,
    ),
    "Silver Fortune Doll Mt. Fuji": MNSGLocationData(
        region="Mt. Fuji",
        address=4,
    ),
    "Talked to Mokubei": MNSGLocationData(
        region="Mt. Fuji",
        address=5,
    ),
    "Silver Fortune Doll Bridge to Oedo Castle": MNSGLocationData(
        region="Oedo Town",
        address=6,
    ),
    "Silver Key 1 Oedo Castle": MNSGLocationData(
        region="Oedo Castle",
        address=7,
    ),
    "Silver Key 2 Oedo Castle": MNSGLocationData(
        region="Oedo Castle",
        address=8,
    ),
    "Mr. Elly Fant Oedo Castle": MNSGLocationData(
        region="Oedo Castle",
        address=9,
    ),
    "Silver Fortune Doll Oedo Castle First Floor": MNSGLocationData(
        region="Oedo Castle",
        address=10,
    ),
    "Silver Key Tatami Oedo Castle": MNSGLocationData(
        region="Oedo Castle",
        address=11,
    ),
    "Gold Key Oedo Castle": MNSGLocationData(
        region="Oedo Castle",
        address=12,
    ),
    "Silver Key Falling Platform Oedo Castle": MNSGLocationData(
        region="Oedo Castle",
        address=13,
    ),
    "Silver Fortune Doll Oedo Castle Second Floor": MNSGLocationData(
        region="Oedo Castle",
        address=14,
    ),
    "Silver Key Spinning Room Oedo Castle": MNSGLocationData(
        region="Oedo Castle",
        address=15,
    ),
    "Mr. Arrow Oedo Castle": MNSGLocationData(
        region="Oedo Castle",
        address=16,
    ),
    "Silver Fortune Doll Oedo Castle Before Congo": MNSGLocationData(
        region="Oedo Castle",
        address=17,
    ),
    "Miracle Moon Pickup": MNSGLocationData(
        region="Oedo Castle",
        address=18,
    ),
    "Saved the Lord at Oedo Castle": MNSGLocationData(
        region="Oedo Castle",
        address=19,
    ),
    "Silver Fortune Doll Oedo Castle Behind Hand": MNSGLocationData(
        region="Oedo Castle",
        address=20,
    ),
    "Open Musashi Gate": MNSGLocationData(
        region="Oedo Town",
        address=21,
    ),
    "Silver Fortune Doll Musashi": MNSGLocationData(
        region="Musashi",
        address=22,
    ),
    "Wise Man's House": MNSGLocationData(
        region="Iga",
        address=23,
    ),
    "Defeated Kashiwagi": MNSGLocationData(
        region="Iga",
        address=24,
    ),
    "Recruited Yae": MNSGLocationData(
        region="Zazen Town",
        address=25,
    ),
    "Gold Fortune Doll Zazen Town": MNSGLocationData(
        region="Zazen Town",
        address=26,
    ),
    "Silver Fortune Doll Yamato Turtle Rock": MNSGLocationData(
        region="Yamato",
        address=27,
    ),
    "Surprise Pack Yamato Shrine": MNSGLocationData(
        region="Yamato",
        address=28,
    ),
    "Silver Fortune Doll Yamato Shrine Bottom": MNSGLocationData(
        region="Yamato",
        address=29,
    ),
    "Silver Fortune Doll Yamato Shrine Top": MNSGLocationData(
        region="Yamato",
        address=30,
    ),
    "Silver Fortune Doll Awaji Island Husband Wife Rocks": MNSGLocationData(
        region="Awaji Island",
        address=31,
    ),
    "Surprise Pack Awaji Island Coffee Shop": MNSGLocationData(
        region="Awaji Island",
        address=32,
    ),
    "Silver Fortune Doll Awaji Island Cliffside": MNSGLocationData(
        region="Awaji Island",
        address=33,
    ),
    "Talked to Benkei": MNSGLocationData(
        region="Zazen Town",
        address=34,
    ),
    "Collected 3 Blue Fish for Ushiwaka": MNSGLocationData(
        region="Zazen Town",
        address=35,
    ),
    "Collected 5 Yellow Fish for Ushiwaka": MNSGLocationData(
        region="Zazen Town",
        address=36,
    ),
    "Collected 8 Red Fish for Ushiwaka": MNSGLocationData(
        region="Zazen Town",
        address=37,
    ),
    "Recieved Achilles' Heel": MNSGLocationData(
        region="Zazen Town",
        address=38,
    ),
    "Recieved Broken Sasuke": MNSGLocationData(
        region="Zazen Town",
        address=39,
    ),
    "Opened Yamato Shrine": MNSGLocationData(
        region="Yamato",
        address=40,
    ),
    "Defeated Mind Control Machine": MNSGLocationData(
        region="Awaji Island",
        address=41,
    ),
    "Rescued Koryuta": MNSGLocationData(
        region="Kompira Mountain",
        address=42,
    ),
    #"Dummy Location 1": MNSGLocationData(
    #    region="Oedo Town",
    #    address=26,
    #    progress_type=LocationProgressType.EXCLUDED,
    #),
    #"Dummy Location 2": MNSGLocationData(
    #    region="Oedo Town",
    #    address=27,
    #    progress_type=LocationProgressType.EXCLUDED,
    #),
    #"Dummy Location 3": MNSGLocationData(
    #    region="Oedo Town",
    #    address=28,
    #    progress_type=LocationProgressType.EXCLUDED,
    #),
    #"Dummy Location 4": MNSGLocationData(
    #    region="Oedo Town",
    #    address=29,
    #    progress_type=LocationProgressType.EXCLUDED,
    #),
    #"Dummy Location 5": MNSGLocationData(
    #    region="Oedo Town",
    #    address=30,
    #    progress_type=LocationProgressType.EXCLUDED,
    #),
    #"Dummy Location 6": MNSGLocationData(
    #    region="Oedo Town",
    #    address=31,
    #    progress_type=LocationProgressType.EXCLUDED,
    #),
    #"Dummy Location 7": MNSGLocationData(
    #    region="Oedo Town",
    #    address=32,
    #    progress_type=LocationProgressType.EXCLUDED,
    #),
    #"Dummy Location 8": MNSGLocationData(
    #    region="Oedo Town",
    #    address=33,
    #    progress_type=LocationProgressType.EXCLUDED,
    #),
    #"Dummy Location 9": MNSGLocationData(
    #    region="Oedo Town",
    #    address=34,
    #    progress_type=LocationProgressType.EXCLUDED,
    #),
    #"Dummy Location 10": MNSGLocationData(
    #    region="Oedo Town",
    #    address=35,
    #    progress_type=LocationProgressType.EXCLUDED,
    #),
    #"Dummy Location 11": MNSGLocationData(
    #    region="Oedo Town",
    #    address=36,
    #    progress_type=LocationProgressType.EXCLUDED,
    #),
    #"Dummy Location 12": MNSGLocationData(
    #    region="Oedo Town",
    #    address=37,
    #    progress_type=LocationProgressType.EXCLUDED,
    #),
}

location_table = {name: data.address for name, data in location_data_table.items() if data.address is not None}


locked_locations = {name: data for name, data in location_data_table.items() if data.locked_item}


