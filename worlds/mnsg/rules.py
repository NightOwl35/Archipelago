from BaseClasses import CollectionState
from worlds.generic.Rules import set_rule

def set_rules(world):
    player = world.player

    def L(name): 
        return world.get_location(name)

    def all_required(state, items):
        return all(state.has(item, player) for item in items)

    def require_items(items):
        def rule(state):
            print(f"[DEBUG] Rule Check: requires {items}")
            return all_required(state, items)
        return rule

    def require_items_and_flag(items, flag):
        def rule(state):
            print(f"[DEBUG] Rule Check: requires {items} and flag '{flag}'")
            return all_required(state, items) and state.has(flag, player)
        return rule

    def debug_rule(location_name):
        def rule(state: CollectionState):
            print(f"[DEBUG] Checking access for: {location_name}")
            return True
        return rule

    # New helper to wrap set_rule with logging info about what requirements the location has
    def set_rule_with_log(location, rule_func, reqs_desc=None):
        loc_name = location.name if hasattr(location, 'name') else str(location)
        print(f"[DEBUG] Setting rule for location: '{loc_name}' with requirements: {reqs_desc}")
        set_rule(location, rule_func)

    # === Basic Locations Always Accessible ===
    always_accessible = [
        "Silver Fortune Doll Guards",
        "Received Map of Japan",
        "Silver Fortune Doll Kai Highway",
        "Silver Fortune Doll Mt. Fuji",
        "Talked to Mokubei",
    ]

    # === Oedo Castle Requirements ===
    chainpipe = ["Chain Pipe"]
    silver1 = chainpipe + ["Silver Key (Oedo Castle First Room)"]
    silver_tatami = silver1 + ["Silver Key (Oedo Castle Second Room)"]
    gold_key = silver_tatami + ["Silver Key (Oedo Castle Tatami Room)"]
    falling_platform = gold_key + ["Gold Key (Oedo Castle)"]
    spinning_key = falling_platform + ["Silver Key (Oedo Castle Falling Platform)"]
    pre_boss = spinning_key + ["Silver Key (Oedo Castle Spinning Spike Room)"]

    # Location Rules with item requirements and logging
    set_rule_with_log(L("Silver Key 1 Oedo Castle"), require_items(chainpipe), chainpipe)
    set_rule_with_log(L("Silver Key 2 Oedo Castle"), require_items(silver1), silver1)
    set_rule_with_log(L("Mr. Elly Fant Oedo Castle"), require_items(silver1), silver1)
    set_rule_with_log(L("Silver Fortune Doll Oedo Castle First Floor"), require_items(silver1), silver1)
    set_rule_with_log(L("Silver Key Tatami Oedo Castle"), require_items(silver_tatami), silver_tatami)
    set_rule_with_log(L("Gold Key Oedo Castle"), require_items(gold_key), gold_key)
    set_rule_with_log(L("Silver Key Falling Platform Oedo Castle"), require_items(falling_platform), falling_platform)
    set_rule_with_log(L("Silver Fortune Doll Oedo Castle Second Floor"), require_items(falling_platform), falling_platform)
    set_rule_with_log(L("Silver Key Spinning Room Oedo Castle"), require_items(spinning_key), spinning_key)
    set_rule_with_log(L("Mr. Arrow Oedo Castle"), require_items(spinning_key), spinning_key)
    set_rule_with_log(L("Silver Fortune Doll Oedo Castle Before Congo"), require_items(pre_boss), pre_boss)
    set_rule_with_log(L("Miracle Moon Pickup"), require_items(pre_boss), pre_boss)
    set_rule_with_log(L("Saved the Lord at Oedo Castle"), require_items(pre_boss), pre_boss)
    set_rule_with_log(
        L("Silver Fortune Doll Oedo Castle Behind Hand"), require_items_and_flag(pre_boss, "Saved the Lord at Oedo Castle"), f"{pre_boss} + ['Saved the Lord at Oedo Castle']")

    # === Musashi Region ===
    musashi_access = ["Lord's Super Pass"]
    set_rule_with_log(L("Open Musashi Gate"), require_items(musashi_access), musashi_access)
    set_rule_with_log(L("Silver Fortune Doll Musashi"), require_items(musashi_access), musashi_access)

    # === Kashiwagi Boss and Wise Man's House ===
    after_kashiwagi = musashi_access + ["Triton Shell"]
    set_rule_with_log(L("Wise Man's House"), require_items(after_kashiwagi), after_kashiwagi)
    set_rule_with_log(L("Defeated Kashiwagi"), require_items(after_kashiwagi), after_kashiwagi)
    
    # === Zazen Town ===
    set_rule_with_log(L("Recruited Yae"), require_items(musashi_access), musashi_access)
    set_rule_with_log(L("Talked to Benkei"), require_items(musashi_access), musashi_access)
    set_rule_with_log(L("Gold Fortune Doll Zazen Town"), require_items(musashi_access), musashi_access)
    set_rule_with_log(
        L("Collected 3 Blue Fish for Ushiwaka"), require_items_and_flag(musashi_access, "Talked to Benkei"), f"{musashi_access} + ['Talked to Benkei']")
    set_rule_with_log(
        L("Collected 5 Yellow Fish for Ushiwaka"), require_items_and_flag(musashi_access, "Collected 3 Blue Fish for Ushiwaka"), f"{musashi_access} + ['Collected 3 Blue Fish for Ushiwaka']")
    set_rule_with_log(
        L("Collected 8 Red Fish for Ushiwaka"), require_items_and_flag(musashi_access, "Collected 5 Yellow Fish for Ushiwaka"), f"{musashi_access} + ['Collected 5 Yellow Fish for Ushiwaka']")
    set_rule_with_log(
        L("Collected 3 Blue Fish for Ushiwaka"), require_items_and_flag(musashi_access, "Talked to Benkei"), f"{musashi_access} + ['Talked to Benkei']")
    set_rule_with_log(
        L("Recieved Achilles' Heel"), require_items_and_flag(musashi_access, "Collected 8 Red Fish for Ushiwaka"), f"{musashi_access} + ['Collected 8 Red Fish for Ushiwaka']")
    
    
    # === Beating Benkei and Unlocking Yamato ===
    benkei = musashi_access + ["Achilles' Heel"]
    set_rule_with_log(
        L("Recieved Broken Sasuke"), require_items_and_flag(benkei, "Recieved Achilles' Heel"), f"{musashi_access} + ['Recieved Achilles' Heel']")
    set_rule_with_log(
        L("Opened Yamato Shrine"), require_items_and_flag(benkei, "Recieved Broken Sasuke"), f"{musashi_access} + ['Recieved Broken Sasuke']")
    set_rule_with_log(
        L("Silver Fortune Doll Yamato Turtle Rock"), require_items_and_flag(benkei, "Recieved Broken Sasuke"), f"{musashi_access} + ['Recieved Broken Sasuke']")
    set_rule_with_log(
        L("Surprise Pack Yamato Shrine"), require_items_and_flag(benkei, "Recieved Broken Sasuke"), f"{musashi_access} + ['Recieved Broken Sasuke']")
    set_rule_with_log(
        L("Silver Fortune Doll Yamato Shrine Bottom"), require_items_and_flag(benkei, "Recieved Broken Sasuke"), f"{musashi_access} + ['Recieved Broken Sasuke']")
    set_rule_with_log(
        L("Silver Fortune Doll Yamato Shrine Top"), require_items_and_flag(benkei, "Recieved Broken Sasuke"), f"{musashi_access} + ['Recieved Broken Sasuke']")
    set_rule_with_log(
        L("Silver Fortune Doll Awaji Island Husband Wife Rocks"), require_items_and_flag(benkei, "Recieved Broken Sasuke"), f"{musashi_access} + ['Recieved Broken Sasuke']")
    set_rule_with_log(
        L("Surprise Pack Awaji Island Coffee Shop"), require_items_and_flag(benkei, "Recieved Broken Sasuke"), f"{musashi_access} + ['Recieved Broken Sasuke']")
    set_rule_with_log(
        L("Silver Fortune Doll Awaji Island Cliffside"), require_items_and_flag(benkei, "Recieved Broken Sasuke"), f"{musashi_access} + ['Recieved Broken Sasuke']")
    
    # === Mind Control Machine ===
    set_rule_with_log(
        L("Defeated Mind Control Machine"), require_items_and_flag(benkei, "Recieved Broken Sasuke"), f"{musashi_access} + ['Recieved Broken Sasuke']")
    set_rule_with_log(
        L("Rescued Koryuta"), require_items_and_flag(benkei, "Recieved Broken Sasuke"), f"{musashi_access} + ['Recieved Broken Sasuke']")
