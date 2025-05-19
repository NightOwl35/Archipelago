from typing import Callable, Dict, NamedTuple, Optional, TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from . import MNSGWorld


class MNSGItem(Item):
    game = "Mystical Ninja Starring Goemon"
    
    def __init__(self, name, classification, code, player):
        super().__init__(name, classification, code, player)


class MNSGItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    can_create: Callable[["MNSGWorld"], bool] = lambda world: True


item_data_table: Dict[str, MNSGItemData] = {
    "Silver Fortune Doll (Oedo Town Guards)": MNSGItemData(
        code=1001,
        type=ItemClassification.useful,
    ),
    "Silver Fortune Doll (Kai Highway)": MNSGItemData(
        code=1002,
        type=ItemClassification.useful,
    ),
    "Silver Fortune Doll (Mt. Fuji)": MNSGItemData(
        code=1003,
        type=ItemClassification.useful,
    ),
    "Chain Pipe": MNSGItemData(
        code=1004,
        type=ItemClassification.progression,
    ),
    "Silver Fortune Doll (Oedo Town Bridge)": MNSGItemData(
        code=1005,
        type=ItemClassification.useful,
    ),
    "Silver Key (Oedo Castle First Room)": MNSGItemData(
        code=1006,
        type=ItemClassification.useful,
    ),
    "Silver Key (Oedo Castle Second Room)": MNSGItemData(
        code=1007,
        type=ItemClassification.useful,
    ),
    "Silver Fortune Doll (Oedo Castle First Floor)": MNSGItemData(
        code=1008,
        type=ItemClassification.useful,
    ),
    "Silver Key (Oedo Castle Tatami Room)": MNSGItemData(
        code=1009,
        type=ItemClassification.useful,
    ),
    "Gold Key (Oedo Castle)": MNSGItemData(
        code=1010,
        type=ItemClassification.useful,
    ),
    "Silver Key (Oedo Castle Falling Platform)": MNSGItemData(
        code=1011,
        type=ItemClassification.useful,
    ),
    "Silver Fortune Doll (Oedo Castle Falling Platform Room)": MNSGItemData(
        code=1012,
        type=ItemClassification.useful,
    ),
    "Silver Key (Oedo Castle Spinning Spike Room)": MNSGItemData(
        code=1013,
        type=ItemClassification.useful,
    ),
    "Silver Fortune Doll (Oedo Castle Before Congo)": MNSGItemData(
        code=1014,
        type=ItemClassification.useful,
    ),
    "Miracle Moon": MNSGItemData(
        code=1015,
        type=ItemClassification.progression,
    ),
    "Lord's Super Pass": MNSGItemData(
        code=1016,
        type=ItemClassification.progression,
    ),
    "Silver Fortune Doll (Oedo Castle Congo Hand)": MNSGItemData(
        code=1017,
        type=ItemClassification.useful,
    ),
    "Silver Fortune Doll (Musashi)": MNSGItemData(
        code=1018,
        type=ItemClassification.useful,
    ),
    "Triton Shell": MNSGItemData(
        code=1019,
        type=ItemClassification.progression,
    ),
    "Yae": MNSGItemData(
        code=1020,
        type=ItemClassification.progression,
    ),
    "Map of Japan": MNSGItemData(
        code=1021,
        type=ItemClassification.useful,
    ),
    "Oedo Castle Map": MNSGItemData(
        code=1022,
        type=ItemClassification.useful,
    ),
    "Oedo Castle Map Boss Marker": MNSGItemData(
        code=1023,
        type=ItemClassification.useful,
    ),
    "Gold Fortune Doll (Zazen Town)": MNSGItemData(
        code=1024,
        type=ItemClassification.useful,
    ),
    "Achilles' Heel": MNSGItemData(
        code=1025,
        type=ItemClassification.progression,
    ),
    "Silver Fortune Doll (Yamato Turtle Rock)": MNSGItemData(
        code=1026,
        type=ItemClassification.useful,
    ),
    "Surprise Pack (Yamato Shrine)": MNSGItemData(
        code=1027,
        type=ItemClassification.filler,
    ),
    "Silver Fortune Doll (Yamato Shrine Bottom)": MNSGItemData(
        code=1028,
        type=ItemClassification.useful,
    ),
    "Silver Fortune Doll (Yamato Shrine Top)": MNSGItemData(
        code=1029,
        type=ItemClassification.useful,
    ),
    "Silver Fortune Doll (Awaji Island Husband Wife Rocks)": MNSGItemData(
        code=1030,
        type=ItemClassification.useful,
    ),
    "Surprise Pack (Awaji Island Coffee Shop)": MNSGItemData(
        code=1031,
        type=ItemClassification.filler,
    ),
    "Silver Fortune Doll (Awaji Island Cliffside)": MNSGItemData(
        code=1032,
        type=ItemClassification.useful,
    ),
    "Flute": MNSGItemData(
        code=1033,
        type=ItemClassification.progression,
    ),
    "Ryo (50)": MNSGItemData(
        code=1900,
        type=ItemClassification.filler,
    ),
}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}