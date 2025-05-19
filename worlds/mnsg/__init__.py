from typing import List, Dict, Any

from BaseClasses import Region, Tutorial
from worlds.AutoWorld import WebWorld, World
from .items import MNSGItem, item_data_table, item_table
from .locations import MNSGLocation, location_data_table, location_table, locked_locations
from .regions import MNSGRegion, region_data_table
from .rules import set_rules


#class MNSGWeb(WebWorld):
    #setup_en = Tutorial(
        #"setup",
        #"A guide to setting up Mystical Ninja Starring Goemon Multiworld Randomizer",
        #"en",
        #"setup_en.md",
        #"setup/en",
        #["NightOwl35"]
    #)
   # tutorials = [setup_en]


class MNSGWorld(World):

    game = "Mystical Ninja Starring Goemon"
    #web = MNSGWebWorld()
    #options: CliqueOptions
    #options_dataclass = CliqueOptions
    location_name_to_id = location_table
    item_name_to_id = item_table
    
    def generate_basic(self) -> None:
        set_rules(self)
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Miracle Moon", self.player)
        self.multiworld.progression_balancing[self.player] = False

    def create_item(self, name: str) -> MNSGItem:
        data = item_data_table[name]
        return MNSGItem(name, data.type, data.code, self.player)

    def create_items(self) -> None:
        item_pool: List[MNSGItem] = []

        # Add all items from the item_data_table that can be created
        for name, item in item_data_table.items():
            if item.code and item.can_create(self):
                item_pool.append(self.create_item(name))

        print(f"Created items: {[item.name for item in item_pool]} (count {len(item_pool)})")  # Debug print

        #Calculate number of filler items needed
        required_fillers = len(location_data_table) - len(item_pool)
        if required_fillers < 0:
            raise Exception(
                f"Too many progression items: {len(item_pool)} for {len(location_data_table)} locations."
            )

        #Add filler items as needed
        for i in range(required_fillers):
            filler = self.create_item("Ryo (50)")
            filler.name = f"Ryo (50) ({i+1})"
            item_pool.append(filler)

        self.multiworld.itempool += item_pool
        print(f"Total itempool count after adding fillers: {len(self.multiworld.itempool)}")  # Debug print
        
        def access_rule_example(world, player):
            result = some_condition_check(world, player)
            print(f"Checking access for ExampleLocation: {result}")
            return result


    def create_regions(self) -> None:
        regions = {}

        for region_name in region_data_table.keys():
            region = MNSGRegion(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)
            regions[region_name] = region

        for region_name, region_data in region_data_table.items():
            region = regions[region_name]

            locs_for_region = {
                loc_name: loc_data for loc_name, loc_data in location_data_table.items()
                if loc_data.region == region_name and loc_data.can_create(self)
            }

            region.add_locations(
                {loc_name: loc_data.address for loc_name, loc_data in locs_for_region.items()},
                MNSGLocation
            )

            # Assign locked_item AFTER location creation
            for loc_name, loc_data in locs_for_region.items():
                location = self.multiworld.get_location(loc_name, self.player)
                if loc_data.locked_item:
                    location.locked_item = loc_data.locked_item

            print(f"Locations count in region '{region_name}': {len(region.locations)}")
            for loc in region.locations:
                print(f"  Location: {loc.name}")

            region.add_exits(region_data.connecting_regions)
            
        # At the end of create_regions()
        seen_addresses = {}
        for loc in self.multiworld.get_locations(self.player):
            if loc.address in seen_addresses:
                print(f"[DUPLICATE] {loc.name} has duplicate address {loc.address}")
                print(f"Already assigned to: {seen_addresses[loc.address]}")
            else:
                seen_addresses[loc.address] = loc.name