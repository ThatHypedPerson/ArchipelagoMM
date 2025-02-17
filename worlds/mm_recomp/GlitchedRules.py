from .Constants import *

def trick_enabled(state, player, options, tricks):
    return any(trick in tricks for trick in options.enabled_tricks)
    
def glitch_enabled(state, player, options, glitches):
    return any(glitch in glitches for glitch in options.enabled_glitches)

def can_play_song(song, state, player):
    return state.has(song, player) and state.has("Ocarina of Time", player)

def can_get_magic_beans(state, player):
    return state.has("Magic Bean", player) and state.has("Deku Mask", player) and state.can_reach("Deku Palace", 'Region', player)

def has_bombchus(state, player):
    return state.has("Bombchu (1)", player) or state.has("Bombchu (5)", player) or state.has("Bombchu (10)", player)

def has_explosives(state, player):
    return state.has("Progressive Bomb Bag", player) or has_bombchus(state, player) or state.has("Blast Mask", player)

def has_hard_projectiles(state, player):
    return state.has("Progressive Bow", player) or state.has("Zora Mask", player) or state.has("Hookshot", player)

def has_projectiles(state, player):
    return (state.has("Deku Mask", player) and state.has("Progressive Magic", player)) or has_hard_projectiles(state, player)

def can_smack_hard(state, player):
    return state.has("Progressive Sword", player) or state.has("Fierce Deity's Mask", player) or state.has("Great Fairy Sword", player) or state.has("Goron Mask", player) or state.has("Zora Mask", player)

def can_smack(state, player):
    return can_smack_hard(state, player) or state.has("Deku Mask", player)

def can_clear_woodfall(state, player):
    return state.can_reach("Woodfall Temple Odolwa's Remains", 'Location', player)

def can_clear_snowhead(state, player):
    return state.can_reach("Snowhead Temple Goht's Remains", 'Location', player)

def can_clear_greatbay(state, player):
    return state.can_reach("Great Bay Temple Gyorg's Remains", 'Location', player)

def can_clear_stonetower(state, player):
    return state.can_reach("Stone Tower Temple Twinmold's Remains", 'Location', player)

def has_paper(state, player):
    return state.has("Land Title Deed", player) or state.has("Swamp Title Deed", player) or state.has("Mountain Title Deed", player) or state.has("Ocean Title Deed", player) or state.has("Letter to Kafei", player) or state.has("Priority Mail", player)

def has_bottle(state, player, need_count=1):
    bottle_count = 0
    if state.has("Bottle", player, 2):
        bottle_count += 2
    elif state.has("Bottle", player):
        bottle_count += 1
    if state.has("Bottle of Chateau Romani", player):
        bottle_count += 1
    if state.has("Bottle of Red Potion", player):
        bottle_count += 1
    return bottle_count >= need_count

def can_plant_beans(state, player):
    return can_get_magic_beans(state, player) and (has_bottle(state, player) or can_play_song("Song of Storms", state, player))

def can_use_powder_keg(state, player):
    return state.has("Powder Keg", player) and state.has("Goron Mask", player)

def can_use_magic_arrow(item, state, player):
    return state.has(item, player) and state.has("Progressive Bow", player) and state.has("Progressive Magic", player)

def can_use_fire_arrows(state, player):
    return can_use_magic_arrow("Fire Arrow", state, player)

def can_use_ice_arrows(state, player):
    return can_use_magic_arrow("Ice Arrow", state, player)

def can_use_light_arrows(state, player):
    return can_use_magic_arrow("Light Arrow", state, player)

def has_gilded_sword(state, player):
    return state.has("Progressive Sword", player, 3)

def has_mirror_shield(state, player):
    return state.has("Progressive Shield", player, 2)

def can_use_lens(state, player):
    return state.has("Lens of Truth", player) and state.has("Progressive Magic", player)

def can_bring_to_player(state, player):
    return state.has("Hookshot", player) or state.has("Zora Mask", player)

def can_reach_scarecrow(state, player):
    return state.can_reach("Astral Observatory", 'Region', player) or state.can_reach("Trading Post", 'Region', player) and state.has("Hookshot", player),

def can_reach_seahorse(state, player):
    return state.can_reach("Fisherman's House", 'Region', player) and (state.has("Zora Mask", player) and state.has("Pictograph Box", player) and state.has("Hookshot", player) or state.has("Goron Mask", player))

def can_purchase(state, player, price):
    if price > 200:
        return state.has("Progressive Wallet", player, 2)
    elif price > 99:
        return state.has("Progressive Wallet", player)

    #Glitched definitions

def can_hover(state, player):
    return state.has("Progressive Shield", player) and (state.has("Blast Mask", player) or state.has("Progressive Bomb Bag", player) or state.has("Bombchu", player))

def can_longhover(state, player):
    return state.has("Progressive Shield", player) and (state.has("Progressive Bomb Bag", player, 2) or state.has("Blast Mask", player))

def can_actionswap(state, player):
    return state.has("Progressive Bow", player) and state.has("Progressive Shield", player)

def can_recoil(state, player):
    return state.has("Progressive Bomb Bag", player) and state.has("Progressive Shield", player)

def can_hess(state, player):
    return state.has("Progressive Bomb Bag", player)

def can_goron_damage_boost(state, player):
    return state.has("Goron Mask", player) and state.has("Progressive Bomb Bag", player)

def can_fierce_damage_boost(state, player):
    return state.has("Fierce Deity's Mask", player) and state.has("Progressive Bomb Bag", player)

def can_indexwarp(state, player):
    return state.has("Progressive Bow", player) and can_play_song("Song of Soaring", state, player)

    return True


def get_glitched_region_rules(player, options):
    return {
        "Clock Town -> Great Bay":
            lambda state: "Index Warp" in options.enabled_glitches,
        "Clock Town -> Snowhead":
            lambda state: "Index Warp" in options.enabled_glitches,
        "Deku Palace -> Mountain Village":
            lambda state: "Index Warp" in options.enabled_glitches,
        "Goron Village -> Stone Tower":
            lambda state: "Index Warp" in options.enabled_glitches,
        "Snowhead -> Woodfall":
            lambda state: "Index Warp" in options.enabled_glitches,
        "Ikana Graveyard -> Southern Swamp":
            lambda state: "Index Warp" in options.enabled_glitches,
        
        "Clock Town -> The Moon":
            lambda state: state.has("Ocarina of Time", player) and state.has("Oath to Order", player) and state.has("Odolwa's Remains", player) and state.has("Goht's Remains", player) and state.has("Gyorg's Remains", player) and state.has("Twinmold's Remains", player),
        "Southern Swamp -> Southern Swamp (Deku Palace)":
            lambda state: state.has("Bottle of Red Potion", player) or (has_hard_projectiles(state, player) and state.has("Deku Mask", player)) or (state.has("Pictograph Box", player) and state.has("Deku Mask", player)) or trick_enabled(state, player, options, ("Run Through Poisoned Water",)) or glitch_enabled(state, player, options, ("Long Bomb Hover",)),
        "Southern Swamp (Deku Palace) -> Swamp Spider House":
            lambda state: state.has("Deku Mask", player) or trick_enabled(state, player, options, ("Run Through Poisoned Water",)) or glitch_enabled(state, player, options, ("Long Bomb Hover",)),
        "Southern Swamp (Deku Palace) -> Deku Palace":
            lambda state: state.has("Deku Mask", player) or trick_enabled(state, player, options, ("Run Through Poisoned Water",)) or glitch_enabled(state, player, options, ("Long Bomb Hover",)),
        "Southern Swamp (Deku Palace) -> Woodfall":
            lambda state: state.has("Deku Mask", player) or trick_enabled(state, player, options, ("Fierce Deity Jumps",)) or glitch_enabled(state, player, options, ("Bomb Hover",)),
        "Woodfall -> Woodfall Temple":
            lambda state: can_play_song("Sonata of Awakening", state, player),
        "Termina Field -> Path to Mountain Village":
            lambda state: glitch_enabled(state, player, options, ("Seamwalk",)),
        "Path to Mountain Village -> Mountain Village":
            lambda state: trick_enabled(state, player, options, ("Backflip Over Snowballs",)),
        # I didn't add HESS logic to SHT entry cause I'm not a masochist or a sadist
        "Path to Snowhead -> Snowhead Temple":
            lambda state: (state.has("Goron Mask", player) and can_play_song("Goron Lullaby", state, player)) or glitch_enabled(state, player, options, ("Long Bomb Hover",)),
        "Termina Field -> Great Bay":
            lambda state: can_play_song("Epona's Song", state, player) or glitch_enabled(state, player, options, ("Bomb Hover",)) or trick_enabled(state, player, options, ("Goron Damage Boost", "Fierce Deity Damage Boost",)),
        "Great Bay -> Ocean Spider House":
            lambda state: has_explosives(state, player) and trick_enabled(state, player, options, ("Goron Damage Boost",)),
        "Great Bay -> Pirates' Fortress":
            lambda state: state.has("Zora Mask", player) or glitch_enabled(state, player, options, ("Long Bomb Hover",)),
        "Pirates' Fortress -> Pirates' Fortress (Sewers)":
            lambda state: state.has("Zora Mask", player) or glitch_enabled(state, player, options, ("Long Bomb Hover",)),
        "Pirates' Fortress -> Pirates' Fortress (Interior)":
            lambda state: state.has("Goron Mask", player) or state.has("Hookshot", player) or glitch_enabled(state, player, options, ("Bomb Hover",)),
        "Zora Cape -> Great Bay Temple":
            lambda state: can_play_song("New Wave Bossa Nova", state, player) and state.has("Hookshot", player) and state.has("Zora Mask", player) or (glitch_enabled(state, player, options, ("Bomb Hover", "Fierce Deity Jumps",)) and can_play_song("New Wave Bossa Nova", state, player) and state.has("Zora Mask", player)),
        "Road to Ikana -> Ikana Graveyard":
            lambda state: can_play_song("Epona's Song", state, player) or glitch_enabled(state, player, options, ("Bomb Hover",)) or trick_enabled(state, player, options, ("Goron Damage Boost",)),
        "Road to Ikana -> Ikana Canyon":
            lambda state: can_play_song("Epona's Song", state, player) and state.has("Hookshot", player) and (state.has("Garo Mask", player) or state.has("Gibdo Mask", player)) or trick_enabled(state, player, options, ("Goron Damage Boost", "Fierce Deity Gainer",)) or glitch_enabled(state, player, options, ("Bomb Hover",)),
        "Ikana Canyon -> Secret Shrine":
            lambda state: True,
        "Ikana Canyon -> Beneath the Well":
            lambda state: can_use_ice_arrows(state, player) and state.has("Hookshot", player) and state.has("Gibdo Mask", player) and has_bottle(state, player) or trick_enabled(state, player, options, ("Hookshot Pixelshots",)),
        "Ikana Canyon -> Ikana Castle":
            lambda state: can_use_ice_arrows(state, player) and state.has("Hookshot", player) and (can_use_light_arrows(state, player) or has_mirror_shield(state, player)) or trick_enabled(state, player, options, ("Hookshot Pixelshots", "Zora Gainer")),
        "Stone Tower -> Stone Tower Temple":
            lambda state: (can_play_song("Elegy of Emptiness", state, player) and state.has("Goron Mask", player) and state.has("Zora Mask", player)) or (glitch_enabled(state, player, options, ("Time Stop", "Bomb Hover",)) and glitch_enabled(state, player, options, ("Index Warp",))) or (trick_enabled(state, player, options, ("One Mask Climb"))),
        "Stone Tower -> Stone Tower (Inverted)":
            lambda state: (state.can_reach("Stone Tower Temple", 'Region', player) and can_use_light_arrows(state, player) and can_play_song("Elegy of Emptiness", state, player)) or (state.can_reach("Stone Tower Temple", 'Region', player) and glitch_enabled(state, player, options, ("Flip Stone Tower without Light Arrows",))) or (glitch_enabled(state, player, options, ("Flip Stone Tower without Light Arrows",)) and glitch_enabled(state, player, options, ("Index Warp",))),
    }

def get_glitched_location_rules(player, options):
    return {
        "Keaton Quiz":
            lambda state: state.has("Keaton Mask", player),
        "Clock Tower Happy Mask Salesman #1":
            lambda state: True,
        "Clock Tower Happy Mask Salesman #2":
            lambda state: True,
        "Clock Town Postbox":
            lambda state: state.has("Postman's Hat", player),
        "Clock Town Hide-and-Seek":
            lambda state: has_projectiles(state, player),
        "Laundry Pool Kafei's Request":
            lambda state: state.has("Letter to Kafei", player),
        "Laundry Pool Curiosity Shop Salesman #1":
            lambda state: state.has("Letter to Kafei", player) or glitch_enabled(state, player, options, ("Deku Recoil", "Fierce Deity Out Of Bounds",)) or trick_enabled(state, player, options, ("Zora Gainer",)),
        "Laundry Pool Curiosity Shop Salesman #2":
            lambda state: state.has("Letter to Kafei", player) or glitch_enabled(state, player, options, ("Deku Recoil", "Fierce Deity Out Of Bounds",)) or trick_enabled(state, player, options, ("Zora Gainer",)),
        "South Clock Town Moon's Tear Trade":
            lambda state: state.has("Moon's Tear", player),
        "South Clock Town Corner Chest":
            lambda state: state.has("Hookshot", player) or trick_enabled(state, player, options, ("One Sided Collision", "Fierce Deity Jumps", "One Sided Collision Itemless",)),
        "South Clock Town Final Day Tower Chest":
            lambda state: state.has("Hookshot", player) or (state.has("Deku Mask", player) and state.has("Moon's Tear", player)) or trick_enabled(state, player, options, ("Fierce Deity Jumps",)) or glitch_enabled(state, player, options, ("Bomb Hover",)),
        "East Clock Town Couples Mask on Mayor":
            lambda state: state.has("Couple's Mask", player),
        "East Clock Town Shooting Gallery 40-49 Points":
            lambda state: state.has("Progressive Bow", player),
        "East Clock Town Shooting Gallery Perfect 50 Points":
            lambda state: state.has("Progressive Bow", player),
        "East Clock Town Honey and Darling Any Day":
            lambda state: state.has("Progressive Bow", player) or (state.has("Progressive Bomb Bag", player) or has_bombchus(state, player)) or (state.has("Deku Mask", player) and state.has("Progressive Magic", player)),
        "East Clock Town Honey and Darling All Days":
            lambda state: state.has("Progressive Bow", player) and state.has("Progressive Bomb Bag", player) and has_bombchus(state, player),
        "East Clock Town Treasure Game Chest (Goron)":
            lambda state: state.has("Goron Mask", player),
        "Bomber's Hideout Chest":
            lambda state: state.can_reach("Clock Town Hide-and-Seek", 'Location', player) and has_explosives(state, player) or (trick_enabled(state, player, options, ("Backflip over Bomber Kids",)) and has_explosives(state, player)),
        "Bomber's Hideout Astral Observatory":
            lambda state: has_projectiles(state, player) or trick_enabled(state, player, options, ("Backflip over Bomber Kids",)),
        "North Clock Town Deku Playground Any Day":
            lambda state: state.has("Deku Mask", player),
        "North Clock Town Deku Playground All Days":
            lambda state: state.has("Deku Mask", player),
        "North Clock Town Save Old Lady":
            lambda state: state.has("Progressive Sword", player) or state.has("Great Fairy Sword", player) or state.has("Zora Mask", player) or state.has("Goron Mask", player),
        "North Clock Town Great Fairy Reward (Has Transformation Mask)":
            lambda state: (state.has("Stray Fairy (Clock Town)", player) and (state.has("Deku Mask", player) or state.has("Goron Mask", player) or state.has("Zora Mask", player))),
        "North Clock Town Great Fairy Reward":
            lambda state: state.has("Stray Fairy (Clock Town)", player),
        "Tingle Clock Town Map Purchase":
            lambda state: has_projectiles(state, player) or trick_enabled(state, player, options, ("Hit Tingle with a Sword", "Hit Tingle with Fierce Deity",)),
        "West Clock Town Swordsman Expert Course":
            lambda state: state.has("Progressive Sword", player),
        "West Clock Town Postman Counting":
            lambda state: state.has("Bunny Hood", player) or trick_enabled(state, player, options, ("Postman Counting Itemless",)),
        "West Clock Town Dancing Sisters":
            lambda state: state.has("Kamaro Mask", player),
        "West Clock Town Bank 200 Rupees":
            lambda state: True,
        "West Clock Town Bank 500 Rupees":
            lambda state: state.has("Progressive Wallet", player),
        "West Clock Town Bank 1000 Rupees":
            lambda state: state.has("Progressive Wallet", player, 2),
        "West Clock Town Priority Mail to Postman":
            lambda state: state.has("Priority Mail", player),
        "Top of Clock Tower (Ocarina of Time)":
            lambda state: has_projectiles(state, player) or trick_enabled(state, player, options, ("Hit Skull Kid with Explosives",)),
        "Top of Clock Tower (Song of Time)":
            lambda state: has_projectiles(state, player) or trick_enabled(state, player, options, ("Hit Skull Kid with Explosives",)),
        "Stock Pot Inn Midnight Meeting":
            lambda state: state.has("Kafei's Mask", player) and (state.has("Deku Mask", player) or state.has("Room Key", player) or trick_enabled(state, player, options, ("Stock Pot Inn with Zora", "Stock Pot Inn with Goron", "Fierce Deity Jumps", "Bomb Long Jumps",))),
        "Stock Pot Inn Upstairs Middle Room Chest":
            lambda state: state.has("Room Key", player),
        "Stock Pot Inn Midnight Toilet Hand":
            lambda state: has_paper(state, player),
        "Stock Pot Inn Granny Story #1":
            lambda state: state.has("All-Night Mask", player),
        "Stock Pot Inn Granny Story #2":
            lambda state: state.has("All-Night Mask", player),
        "Stock Pot Inn Anju and Kafei":
            lambda state: (state.has("Kafei's Mask", player) and can_play_song("Epona's Song", state, player) and state.has("Letter to Kafei", player) and state.has("Pendant of Memories", player) and state.has("Hookshot", player) and (state.has("Garo Mask", player) or state.has("Gibdo Mask", player))),
        "Milk Bar Show":
            lambda state: state.has("Romani Mask", player) and state.has("Deku Mask", player) and state.has("Goron Mask", player) and state.has("Zora Mask", player) and state.has("Ocarina of Time", player) or (state.has("Deku Mask", player) and state.has("Goron Mask", player) and state.has("Zora Mask", player) and state.has("Ocarina of Time", player) and glitch_enabled(state, player, options, ("Bomb Hover",))),
        "Milk Bar Priority Mail to Aroma":
            lambda state: state.has("Romani Mask", player) and state.has("Kafei's Mask", player) and state.has("Priority Mail", player) or (trick_enabled(state, player, options, ("Good Time Management",)) and state.has("Priority Mail", player) or (glitch_enabled(state, player, options, ("Bomb Hover",)) and state.has("Priority Mail", player))),


        "Termina Stump Chest":
            lambda state: state.has("Hookshot", player) or can_plant_beans(state, player) or glitch_enabled(state, player, options, ("Seamwalk",)),
        "Termina Underwater Chest":
            lambda state: state.has("Zora Mask", player),
        "Termina Peahat Grotto Chest":
            lambda state: True,
        "Termina Dodongo Grotto Chest":
            lambda state: True,
        "Termina Bio Baba Grotto HP":
            lambda state: has_explosives(state, player) and state.has("Zora Mask", player) or (state.has("Goron Mask", player) and state.has("Zora Mask", player)),
        "Termina Northern Midnight Dancer":
            lambda state: (state.has("Ocarina of Time", player) or glitch_enabled(state, player, options, ("Ocarina Items",))) and state.has("Song of Healing", player),
        "Termina Gossip Stones HP":
            lambda state: state.has("Deku Mask", player) and can_play_song("Sonata of Awakening", state, player) or (state.has("Goron Mask", player) and can_play_song("Goron Lullaby", state, player)) or (state.has("Zora Mask", player) and can_play_song("New Wave Bossa Nova", state, player)),
        "Termina Moon's Tear Scrub HP":
            lambda state: state.can_reach("Bomber's Hideout Astral Observatory", 'Location', player) and state.has("Ocarina of Time", player) and state.has("Progressive Wallet", player) or (state.has("Deku Mask", player) and state.has("Ocarina of Time", player) and state.has("Progressive Wallet", player)),
        "Termina Log Bombable Grotto Left Cow":
            lambda state: has_explosives(state, player) and can_play_song("Epona's Song", state, player) or (glitch_enabled(state, player, options, ("Ocarina Items",)) and state.has("Epona's Song", player) and has_explosives(state, player)),
        "Termina Log Bombable Grotto Right Cow":
            lambda state: has_explosives(state, player) and can_play_song("Epona's Song", state, player) or (glitch_enabled(state, player, options, ("Ocarina Items",)) and state.has("Epona's Song", player) and has_explosives(state, player)),
        "Milk Road Gorman Ranch Race":
            lambda state: state.has("Ocarina of Time", player) and state.has("Epona's Song", player) or (glitch_enabled(state, player, options, ("Ocarina Items",)) and state.has("Epona's Song", player)),
        "Tingle Romani Ranch Map Purchase":
            lambda state: has_projectiles(state, player) or state.can_reach("Twin Islands", 'Region', player) or (trick_enabled(state, player, options, ("Hit Tingle with Fierce Deity", "Fierce Deity Out Of Bounds",))) or (glitch_enabled(state, player, options, ("Seamwalk",)) and trick_enabled(state, player, options, ("Backflip Over Snowballs", "Hit Tingle with Fierce Deity",))),
        "Road to Swamp Tree HP":
            lambda state: has_projectiles(state, player) or trick_enabled(state, player, options("Climb Road to Southern Swamp Tree Itemless",)),
        "Tingle Woodfall Map Purchase":
            lambda state: has_projectiles(state, player) and state.can_reach("Clock Town", 'Region', player) or trick_enabled(state, player, options, ("Hit Tingle with a Sword", "Hit Tingle with Fierce Deity",)),
        "Swamp Shooting Gallery 2120 Points":
            lambda state: state.has("Progressive Bow", player),
        "Swamp Shooting Gallery 2180 Points":
            lambda state: state.has("Progressive Bow", player),


        "Southern Swamp Deku Trade":
            lambda state: state.has("Land Title Deed", player),
        "Southern Swamp Deku Trade Freestanding HP":
            lambda state: state.has("Land Title Deed", player) and state.has("Deku Mask", player) or trick_enabled(state, player, options,("One Sided Goron Collision", "Fierce Deity Gainer",)) or glitch_enabled(state, player, options("Bomb Hover",)),
        "Southern Swamp Tour Witch Gift":
            lambda state: state.has("Bottle of Red Potion", player),
        "Southern Swamp Tour Guide Winning Picture":
            lambda state: state.has("Pictograph Box", player),
        "Southern Swamp Tour Guide Good Picture":
            lambda state: state.has("Pictograph Box", player),
        "Southern Swamp Tour Guide Okay Picture":
            lambda state: state.has("Pictograph Box", player),
        "Southern Swamp Near Swamp Spider House Grotto Chest":
            lambda state: (state.has("Deku Mask", player) and has_projectiles(state, player)) or state.has("Zora Mask", player) or trick_enabled(state, player, options, ("Run Through Poisoned Water",)) or glitch_enabled(state, player, options, ("Long Bomb Hover",)),
        "Southern Swamp Song Tablet":
            lambda state: state.has("Deku Mask", player) or (trick_enabled(state, player, options, ("Fierce Deity Jumps",)) and trick_enabled(state, player, options, ("Run Through Poisoned Water",))) or glitch_enabled(state, player, options, ("Long Bomb Hover",)),
        "Southern Swamp Mystery Woods Day 2 Grotto Chest":
            lambda state: True,

        "Swamp Spider House First Room Pot Near Entrance Token":
            lambda state: can_smack(state, player) or trick_enabled(state, player, options, ("Kill with sticks",)),
        "Swamp Spider House First Room Crawling In Water Token":
            lambda state: can_smack(state, player) or trick_enabled(state, player, options, ("Kill with sticks",)),
        "Swamp Spider House First Room Crawling Right Column Token":
            lambda state: can_smack(state, player) or trick_enabled(state, player, options, ("Kill with sticks",)),
        "Swamp Spider House First Room Crawling Left Column Token":
            lambda state: can_smack(state, player) or trick_enabled(state, player, options, ("Kill with sticks",)),
        "Swamp Spider House First Room Against Far Wall Token":
            lambda state: (can_bring_to_player(state, player) and has_projectiles(state, player) or (state.has("Deku Mask", player) and state.has("Progressive Magic", player))) or glitch_enabled(state, player, options, ("Bomb Hover",)),
        "Swamp Spider House First Room Lower Left Bugpatch Token":
            lambda state: can_smack(state, player) and has_bottle(state, player),
        "Swamp Spider House First Room Lower Right Bugpatch Token":
            lambda state: can_smack(state, player) and has_bottle(state, player),
        "Swamp Spider House First Room Upper Right Bugpatch Token":
            lambda state: can_smack(state, player) and has_bottle(state, player),
        "Swamp Spider House Monument Room Left Crate Token":
            lambda state: can_smack(state, player) or trick_enabled(state, player, options, ("Kill with sticks",)),
        "Swamp Spider House Monument Room Right Crate Token":
            lambda state: can_smack(state, player) or trick_enabled(state, player, options, ("Kill with sticks",)),
        "Swamp Spider House Monument Room Crawling Wall Token":
            lambda state: can_smack(state, player) and can_bring_to_player(state, player) or (can_plant_beans(state, player) and has_explosives(state, player) or state.has("Goron Mask", player)),
        "Swamp Spider House Monument Room Crawling On Monument Token":
            lambda state: can_smack(state, player) and can_bring_to_player(state, player) and has_projectiles(state, player),
        "Swamp Spider House Monument Room Behind Torch Token":
            lambda state: can_smack(state, player) or trick_enabled(state, player, options, ("Kill with sticks",)),
        "Swamp Spider House Pottery Room Beehive #1 Token":
            lambda state: can_smack(state, player) and has_projectiles(state, player),
        "Swamp Spider House Pottery Room Beehive #2 Token":
            lambda state: can_smack(state, player) and has_projectiles(state, player),
        "Swamp Spider House Pottery Room Small Pot Token":
            lambda state: can_smack(state, player) or trick_enabled(state, player, options, ("Kill with sticks",)),
        "Swamp Spider House Pottery Room Left Large Pot Token":
            lambda state: can_smack(state, player) or trick_enabled(state, player, options, ("Kill with sticks",)),
        "Swamp Spider House Pottery Room Right Large Pot Token":
            lambda state: can_smack(state, player) or trick_enabled(state, player, options, ("Kill with sticks",)),
        "Swamp Spider House Pottery Room Behind Vines Token":
            lambda state: state.has("Progressive Sword", player) or (state.has("Great Fairy Sword", player) or state.has("Fierce Deity's Mask", player)),
        "Swamp Spider House Pottery Room Upper Wall Token":
            lambda state: can_smack(state, player) or trick_enabled(state, player, options, ("Kill with sticks",)),
        "Swamp Spider House Golden Room Crawling Left Wall Token":
            lambda state: can_smack(state, player) or trick_enabled(state, player, options, ("Kill with sticks",)),
        "Swamp Spider House Golden Room Crawling Right Column Token":
            lambda state: can_smack(state, player) or trick_enabled(state, player, options, ("Kill with sticks",)),
        "Swamp Spider House Golden Room Against Far Wall Token":
            lambda state: can_smack(state, player) and (can_bring_to_player(state, player) or (can_smack(state, player) and can_plant_beans(state, player))) or (trick_enabled(state, player, options, ("Kill with sticks",)) and can_plant_beans(state, player)),
        "Swamp Spider House Golden Room Beehive Token":
            lambda state: can_smack(state, player) and has_projectiles(state, player),
        "Swamp Spider House Tree Room Tall Grass #1 Token":
            lambda state: can_smack(state, player) or trick_enabled(state, player, options, ("Kill with sticks",)),
        "Swamp Spider House Tree Room Tall Grass #2 Token":
            lambda state: can_smack(state, player) or trick_enabled(state, player, options, ("Kill with sticks",)),
        "Swamp Spider House Tree Room Tree #1 Token":
            lambda state: can_smack(state, player) or trick_enabled(state, player, options, ("Kill with sticks",)),
        "Swamp Spider House Tree Room Tree #2 Token":
            lambda state: can_smack(state, player) or trick_enabled(state, player, options, ("Kill with sticks",)),
        "Swamp Spider House Tree Room Tree #3 Token":
            lambda state: can_smack(state, player) or trick_enabled(state, player, options, ("Kill with sticks",)),
        "Swamp Spider House Tree Room Beehive Token":
            lambda state: can_smack(state, player) and has_projectiles(state, player) or (trick_enabled(state, player, options, ("Kill with sticks",)) and has_projectiles(state, player)),
        "Swamp Spider House Reward":
            lambda state: state.has("Swamp Skulltula Token", player, 30),


        "Deku Palace Bean Seller":
            lambda state: True,
        "Deku Palace Bean Grotto Chest":
            lambda state: can_plant_beans(state, player) or state.has("Hookshot", player) or glitch_enabled(state, player, options, ("Bomb Hover",)),
        "Deku Palace Monkey Song":
            lambda state: state.has("Ocarina of Time", player) and can_plant_beans(state, player) and state.has("Deku Mask", player) or (trick_enabled(state, player, options, ("Deku Palace Bean Skip",)) and state.has("Ocarina of Time", player) and state.has("Deku Mask", player)),
        "Deku Palace Butler Race":
            lambda state: can_clear_woodfall(state, player) and has_bottle(state, player) and (state.has("Progressive Sword", player) or state.has("Great Fairy Sword", player) or state.has("Fierce Deity's Mask", player)),


        "Woodfall Great Fairy Reward":
            lambda state: state.has("Stray Fairy (Woodfall)", player, 15),
        "Woodfall Near Owl Statue Chest":
            lambda state: state.has("Deku Mask", player) or glitch_enabled(state, player, options, ("Bomb Hover",)) or trick_enabled(state, player, options, ("Fierce Deity Jumps",)),
        "Woodfall After Great Fairy Cave Chest":
            lambda state: state.has("Deku Mask", player) or glitch_enabled(state, player, options, ("Bomb Hover",)) or trick_enabled(state, player, options, ("Fierce Deity Jumps",)) or state.has("Hookshot", player),
        "Woodfall Near Swamp Entrance Chest":
            lambda state: state.has("Deku Mask", player) or glitch_enabled(state, player, options, ("Bomb Hover",)) or trick_enabled(state, player, options, ("Fierce Deity Jumps",)) or state.has("Hookshot", player),


        "Woodfall Temple Dragonfly Chest":
            lambda state: state.has("Small Key (Woodfall)", player) or state.has("Progressive Bow", player) or glitch_enabled(state, player, options, ("Bomb Hover",)) or trick_enabled(state, player, options, ("WFT Second Floor Skip",)),
        "Woodfall Temple Black Boe Room Chest":
            lambda state: state.has("Small Key (Woodfall)", player) or state.has("Progressive Bow", player) or glitch_enabled(state, player, options, ("Bomb Hover",)) or trick_enabled(state, player, options, ("WFT Second Floor Skip",)),
        "Woodfall Temple Wooden Flower Switch Chest":
            lambda state: state.has("Progressive Bow", player) or (trick_enabled(state, player, options, ("WFT Second floor skip",)) and trick_enabled(state, player, options, ("Bomb Long Jump",))),
        "Woodfall Temple Dinolfos Chest":
            lambda state: (state.has("Small Key (Woodfall)", player) and can_smack(state, player)) or state.has("Progressive Bow", player) or trick_enabled(state, player, options, ("WFT Second Floor Skip",)),
        "Woodfall Temple Boss Key Chest":
            lambda state: state.has("Progressive Bow", player) and can_smack(state, player) and (has_explosives(state, player) or state.has("Goron Mask", player)),
        "Woodfall Temple Wooden Flower Bubble SF":
            lambda state: state.has("Progressive Bow", player) and state.has("Great Fairy Mask", player) or can_use_fire_arrows(state, player),
        "Woodfall Temple Moving Flower Platform Room Beehive SF":
            lambda state: has_projectiles(state, player) or state.has("Progressive Bow", player),
        "Woodfall Temple Push Block Skulltula SF":
            lambda state: state.has("Small Key (Woodfall)", player) and can_smack(state, player) or state.has("Progressive Bow", player),
        "Woodfall Temple Push Block Bubble SF":
            lambda state: state.has("Small Key (Woodfall)", player) and has_projectiles(state, player) and state.has("Great Fairy Mask", player) or (state.has("Progressive Bow", player) and state.has("Great Fairy Mask", player)),
        "Woodfall Temple Push Block Beehive SF":
            lambda state: (state.has("Small Key (Woodfall)", player) and has_projectiles(state, player) or state.has("Progressive Bow", player)) or trick_enabled(state, player, options, ("WFT Second Floor Skip",)),
        "Woodfall Temple Final Room Right Lower Platform SF":
            lambda state: state.has("Progressive Bow", player) or can_use_fire_arrows(state, player),
        "Woodfall Temple Final Room Right Upper Platform SF":
            lambda state: state.has("Progressive Bow", player) or can_use_fire_arrows(state, player),
        "Woodfall Temple Final Room Left Upper Platform SF":
            lambda state: state.has("Progressive Bow", player) or can_use_fire_arrows(state, player),
        "Woodfall Temple Final Room Bubble SF":
            lambda state: state.has("Progressive Bow", player) or can_use_fire_arrows(state, player),
        "Woodfall Temple Heart Container":
            lambda state: state.has("Progressive Bow", player) and can_smack(state, player) and state.has("Boss Key (Woodfall)", player) or state.has("Odolwa's Remains", player) or glitch_enabled(state, player, options, ("WFT BK Skip",)),
        "Woodfall Temple Odolwa's Remains":
            lambda state: state.has("Progressive Bow", player) and can_smack(state, player) and state.has("Boss Key (Woodfall)", player) or state.has("Odolwa's Remains", player) or glitch_enabled(state, player, options, ("WFT BK Skip",)),


        "Tour Witch Target Shooting":
            lambda state: (can_clear_woodfall(state, player) and (state.has("Bottle of Red Potion", player) or state.has("Bottle of Chateau Romani", player)) and state.has("Progressive Bow", player)),


        "Mountain Village Invisible Ladder Cave Healing Invisible Goron":
            lambda state: can_use_lens(state, player) and can_play_song("Song of Healing", state, player),
        "Mountain Village Feeding Freezing Goron":
            lambda state: state.has("Goron Mask", player) and (can_play_song("Goron Lullaby", state, player) or can_use_fire_arrows(state, player)),
        "Mountain Village Spring Waterfall Chest":
            lambda state: can_clear_snowhead(state, player),
        "Mountain Village Spring Ramp Grotto":
            lambda state: can_clear_snowhead(state, player),
        "Don Gero Mask Frog Song HP":
            lambda state: state.has("Don Gero Mask", player) and can_clear_snowhead(state, player) and state.can_reach("Woodfall Temple Boss Key Chest", 'Location', player) and state.can_reach("Great Bay Temple", 'Region', player) and can_use_ice_arrows(player, state) and can_use_fire_arrows(player, state),
        # ~ "Mountain Village Smithy Day 1":
        # ~ lambda state: state.has("Progressive Wallet", player) and can_clear_snowhead(state, player) and has_bottle(state, player) and state.can_reach("Mountain Village Invisible Ladder Cave Healing Invisible Goron", 'Location', player) and can_use_fire_arrows(state, player),
        # ~ "Mountain Village Smithy Day 2":
        # ~ lambda state: state.has("Bottle of Gold Dust", player) and state.can_reach("Mountain Village Smithy Day 1", 'Location', player),

        "Tingle Snowhead Map Purchase":
            lambda state: has_projectiles(state, player) and state.can_reach("Southern Swamp", 'Region', player),
        "Twin Islands Ramp Grotto Chest":
            lambda state: has_explosives(state, player) and (state.has("Goron Mask", player) or state.has("Hookshot", player)),
        "Twin Islands Hot Water Grotto Chest":
            lambda state: (has_explosives(state, player) and can_use_fire_arrows(state, player)) or (state.can_reach("Mountain Village Invisible Ladder Cave Healing Invisible Goron", 'Location', player) and state.has("Goron Mask", player)) or can_clear_snowhead(state, player) or state.can_reach("Ikana Well Invisible Chest", 'Location', player),
        "Twin Islands Spring Underwater Cave Chest":
            lambda state: state.has("Zora Mask", player) and can_clear_snowhead(state, player),
        "Twin Islands Spring Underwater Near Ramp Chest":
            lambda state: state.has("Zora Mask", player) and can_clear_snowhead(state, player),
        "Goron Racetrack Bottle Prize":
            lambda state: state.has("Powder Keg", player) and can_clear_snowhead(state, player) or (can_clear_snowhead(state, player) and glitch_enabled(state, player, options, ("Bomb Hover",))),
        "Goron Song":
            lambda state: state.has("Goron Mask", player) and state.can_reach("Mountain Village Invisible Ladder Cave Healing Invisible Goron", 'Location', player) and (has_bottle(state, player) or can_use_fire_arrows(state, player) or glitch_enabled(state, player, options, ("Action Swap",))),


        "Goron Village Lens Cave Rock Chest":
            lambda state: has_explosives(state, player),
        "Goron Village Lens Cave Invisible Chest":
            lambda state: True,
        "Goron Village Lens Cave Center Chest":
            lambda state: True,
        "Goron Village Deku Trade":
            lambda state: state.has("Deku Mask", player) and state.has("Swamp Title Deed", player),
        "Goron Village Deku Trade Freestanding HP":
            lambda state: state.can_reach("Goron Village Deku Trade", 'Location', player) or glitch_enabled(state, player, options, ("Bomb Hover",)),
        "Powder Keg Goron Reward":
            lambda state: can_clear_snowhead(state, player) or (can_use_fire_arrows(state, player) and state.has("Goron Mask", player)) or (glitch_enabled(state, player, options, ("Action Swap",)) and state.has("Goron Mask", player)) or (trick_enabled(state, player, options, ("Melt Ice as Fierce Deity",)) and state.has("Goron Mask")),
        "Goron Village Deku Scrub Bomb Bag":
            lambda state: state.has("Goron Mask", player) and state.has("Progressive Wallet", player) or (state.can_reach("Goron Village Deku Trade Freestanding HP", 'Location', player) and state.can_reach("Southern Swamp Deku Trade Freestanding HP", 'Location', player) and state.has("Moon's Tear", player) and state.has("Progressive Wallet", player)),


        "Path to Snowhead Grotto Chest":
            lambda state: state.has("Goron Mask", player) and state.has("Progressive Magic", player) and has_explosives(state, player) or (trick_enabled(state, player, options, ("PTSH as Zora",)) and has_explosives(state, player)) or (trick_enabled(state, player, options, ("PTSH as Goron without Magic",)) and has_explosives(state, player)) or (trick_enabled(state, player, options, ("Fierce Deity Jumps",)) and has_explosives(state, player)) or (trick_enabled(state, player, options, ("PTSH as Link with Sword or Sticks",)) and has_explosives(state, player)) or glitch_enabled(state, player, options, ("Bomb Hover",)),
        "Path to Snowhead Scarecrow Pillar HP":
            lambda state: can_reach_scarecrow(state, player) and state.has("Goron Mask", player) and can_use_lens(state, player) and state.has("Hookshot", player) or glitch_enabled(state, player, options, ("Bomb Hover",)),


        "Snowhead Great Fairy Reward":
            lambda state: state.has("Stray Fairy (Snowhead)", player, 15),

        # Snowhead has 3 small keys
        "Snowhead Temple Initial Runway Under Platform Bubble SF":
            lambda state: state.has("Progressive Bow", player) and state.has("Great Fairy Mask", player) or trick_enabled(state, player, options, ("Recoil Flip",)),
        "Snowhead Temple Initial Runway Tower Bubble SF":
            lambda state: state.has("Great Fairy Mask", player) and state.has("Progressive Bow", player) or (can_use_fire_arrows(state, player) and can_smack_hard(state,player)) or trick_enabled(state, player, options, ("Difficult Jumps",)),
        "Snowhead Temple Grey Door Near Bombable Stairs Box SF":
            lambda state: state.has("Small Key (Snowhead)", player) and state.has("Great Fairy Mask", player) and has_explosives(state, player) or (state.has("Hookshot", player) and state.can_reach("Snowhead Temple Initial Runway Tower Bubble SF", 'Location', player) and has_explosives(state, player)) or trick_enabled(state, player, options, ("Fierce Deity Climbing", "Bomb Long Jump",)),
        # "Snowhead Temple Timed Switch Room Bubble SF" needs 2 small keys following the 'vanilla path' \/
        "Snowhead Temple Timed Switch Room Bubble SF":
            lambda state: (state.has("Small Key (Snowhead)", player, 2) and state.has("Great Fairy Mask", player) and state.has("Progressive Bow", player) and can_use_lens(state, player) and has_explosives(state, player) or (can_use_fire_arrows(state, player) and can_reach_scarecrow(state, player) and state.has("Hookshot", player) and state.has("Great Fairy Mask", player) and state.has("Progressive Bow", player) and can_use_lens(state, player))) or trick_enabled(state, player, options, ("Hookshot Pixelshots",)) and state.has("Great Fairy's Mask", player) or glitch_enabled(state, player, options, ("Bomb Hover",)),
        # "Snowhead Temple Snowmen Bubble SF" needs 3 small keys following the 'vanilla' path' - this is the final small key too. \/
        "Snowhead Temple Snowmen Bubble SF":
            lambda state: state.has("Small Key (Snowhead)", player, 3) and state.has("Great Fairy Mask", player) and state.has("Progressive Bow", player) and has_explosives(state, player) or (state.has("Small Key (Snowhead)", player) and can_use_fire_arrows(state, player) and state.has("Great Fairy Mask", player)) or (trick_enabled(state, player, options, ("Hookshot Pixelshot",)) and glitch_enabled(state, player, options, ("Bomb Hover",)) and state.has("Small Key (Snowhead)", player, 1)),
        # Both Dinolfos checks require 3 small keys following vanilla path
        "Snowhead Temple Dinolfos Room First SF":
            lambda state: state.has("Small Key (Snowhead)", player, 3) and has_explosives(state, player) and can_use_fire_arrows(state, player) or (state.has("Small Key (Snowhead)", player) and can_use_fire_arrows(state, player)) or (trick_enabled(state, player, options, ("Hookshot Pixelshot",)) and glitch_enabled(state, player, options, ("Bomb Hover",)) and state.has("Small Key (Snowhead)", player, 1)) or (trick_enabled(state, player, options, ("Hookshot Pixelshot",)) and can_use_fire_arrows(state, player) and state.has("Small Key (Snowhead)", player, 1)) or (trick_enabled(state, player, options, ("Hookshot Pixelshot",)) and glitch_enabled(state, player, options, ("Bomb Hover",))),
        "Snowhead Temple Dinolfos Room Second SF":
            lambda state: state.has("Small Key (Snowhead)", player, 3) and has_explosives(state, player) and can_use_fire_arrows(state, player) or (state.has("Small Key (Snowhead)", player) and can_use_fire_arrows(state, player)) or (trick_enabled(state, player, options, ("Hookshot Pixelshot",)) and glitch_enabled(state, player, options, ("Bomb Hover",)) and state.has("Small Key (Snowhead)", player, 1)) or (trick_enabled(state, player, options, ("Hookshot Pixelshot",)) and can_use_fire_arrows(state, player) and state.has("Small Key (Snowhead)", player, 1)) or (trick_enabled(state, player, options, ("Hookshot Pixelshot",)) and glitch_enabled(state, player, options, ("Bomb Hover",))),
        "Snowhead Temple Initial Runway Ice Blowers Chest":
            lambda state: can_use_fire_arrows(state, player) or state.has("Hookshot", player) or trick_enabled(state, player, options, ("Fierce Deity Jumps", "Bomb Long Jump",)),
        "Snowhead Temple Green Door Ice Blowers Chest":
            lambda state: can_use_fire_arrows(state, player) or glitch_enabled(state, player, options, ("Action Swap",)) or trick_enabled(state, player, options, ("SHT Green Door Shoot Through Torch",)),
        #  "Snowhead Temple Orange Door Upper Chest" only needs 1 small key
        "Snowhead Temple Orange Door Upper Chest":
            lambda state: (state.has("Hookshot", player) and state.has("Small Key (Snowhead)", player) or state.has("Small Key (Snowhead)", player) and can_use_fire_arrows(state, player)) or (glitch_enabled(state, player, options, ("Action Swap",)) and state.has("Zora Mask", player) or state.has("Fierce Deity Mask", player)) or trick_enabled(state, player, options("Fierce Deity Jumps",)) or glitch_enabled(player, state, options, ("Bomb Hover",)) or (state.has("Small Key (Snowhead)", player, 1) and trick_enabled(state, player, options, ("Bomb Long Jump",))),
        "Snowhead Temple Orange Door Behind Block Chest":
            lambda state: state.can_reach("Snowhead Temple Orange Door Upper Chest", 'Location', player),
        #  "Snowhead Temple Grey Door Center Chest" requires one key (either im colour blind or you are but that door is like, light blue)
        "Snowhead Temple Light Blue Door Center Chest":
            lambda state: state.has("Small Key (Snowhead)", player) or state.has("Hookshot", player) or trick_enabled(state, player, options, ("Fierce Deity Jumps", "Bomb Long Jumps",)),
        "Snowhead Temple Light Blue Door Upper Chest":
            lambda state: state.has("Small Key (Snowhead)", player) and can_use_fire_arrows(state, player) or (state.has("Hookshot", player) and can_use_fire_arrows(state, player)) or (trick_enabled(state, player, options, ("SHT Ice Block Switch Clip",)) and trick_enabled(state, player, options, ("Fierce Deity Jumps", "Zora Gainer",))),
        "Snowhead Temple Upstairs 2F Icicle Room Hidden Chest":
            lambda state: state.has("Small Key (Snowhead)", player) and can_use_lens(state, player) and has_explosives(state, player) and state.has("Progressive Bow", player) or (state.has("Small Key (Snowhead", player) and can_use_fire_arrows(state, player)) or state.has("Small Key (Snowhead", player) and can_reach_scarecrow(state, player) or glitch_enabled(state, player, options("Bomb Hover",)) or (can_reach_scarecrow(state, player) and state.has("Fierce Deity", player) and state.has("Small Key (Snowhead", player)) or (can_use_fire_arrows(state, player) and state.has("Fierce Deity", player) and state.has("Small Key (Snowhead", player)) or (can_use_fire_arrows(state, player) and state.has("Zora Mask", player) and state.has("Small Key (Snowhead", player)) or (can_reach_scarecrow(state, player) and state.has("Zora Mask", player) and state.has("Small Key (Snowhead", player)),
        "Snowhead Temple Upstairs 2F Icicle Room Snowball Chest":
            lambda state: state.has("Small Key (Snowhead)", player) and can_use_lens(state, player) and has_explosives(state, player) and state.has("Progressive Bow", player) or (state.has("Small Key (Snowhead", player) and can_use_fire_arrows(state, player)) or state.has("Small Key (Snowhead", player) and can_reach_scarecrow(state, player) or glitch_enabled(state, player, options("Bomb Hover",)) or (can_use_fire_arrows(state, player) and state.has("Fierce Deity", player) and state.has("Small Key (Snowhead", player)) or (can_use_fire_arrows(state, player) and state.has("Zora Mask", player) and state.has("Small Key (Snowhead", player)),
        "Snowhead Temple Elevator Room Invisible Platform Chest":
            lambda state: can_use_lens(state, player) and state.has("Small Key (Snowhead)", player, 2) and has_explosives(state, player) or can_use_lens(state, player) and can_use_fire_arrows(state, player) or glitch_enabled(state, player, options("Bomb Hover",)),
        "Snowhead Temple Elevator Room Lower Chest":
            lambda state: state.can_reach("Snowhead Temple Initial Runway Tower Bubble SF", 'Location', player),
        "Snowhead Temple 1st Wizzrobe Chest":
            lambda state: state.has("Small Key (Snowhead)", player, 2) and has_explosives(state, player) and has_projectiles(state, player) and can_smack(state, player) or can_use_fire_arrows(state, player) or trick_enabled(state, player, options("Hookshot Pixelshot",)) or glitch_enabled(state, player, options, ("Bomb Hover",)),
        "Snowhead Temple Column Room 2F Hidden Chest":
            lambda state: state.has("Small Key (Snowhead)", player, 3) and can_use_lens(state, player) and has_explosives(state, player) and state.has("Deku Mask", player) or (can_use_fire_arrows(state, player) and can_reach_scarecrow(state, player) and state.has("Hookshot", player)) or glitch_enabled(state, player, options, ("Bomb Hover",)) or trick_enabled(state, player, options, ("Hookshot Pixelshot", "SHT Jump to Hidden Wall in Main Room",)),
        "Snowhead Temple 2nd Wizzrobe Chest":
            lambda state: state.has("Small Key (Snowhead)", player, 3) and can_use_fire_arrows(state, player) and has_explosives(state, player) and can_smack(state, player) or state.has("Small Key (Snowhead)", player, 1) and can_use_fire_arrows(state, player) and can_reach_scarecrow(state, player) and state.has("Deku Mask", player) or glitch_enabled(state, player, options,("Long Bomb Hover",)),
        "Snowhead Temple Heart Container":
            lambda state: can_use_fire_arrows(state, player) and state.has("Boss Key (Snowhead)", player) and state.has("Small Key (Snowhead)", player, 3) and has_explosives(state, player) or state.has("Small Key (Snowhead)", player, 1) and can_use_fire_arrows(state, player) and state.has("Boss Key (Snowhead)", player) or can_use_fire_arrows(state, player) and state.has("Goht's Remains", player) or glitch_enabled(state, player, options, ("SHT BK Skip", "Action Swap", "Equip Swap", "Long Bomb Hover",)) or (glitch_enabled(state, player, options, ("SHT BK Skip", "Long Bomb Hover",)) and can_use_fire_arrows(state, player)) or (glitch_enabled(state, player, options, ("Long Bomb Hover",)) and can_use_fire_arrows(state, player) and state.has("Boss Key (Snowhead)", player)) or (state.has("Goht's Remains", player) and glitch_enabled(state, player, options, ("Action Swap", "Equip Swap",))),
        "Snowhead Temple Goht's Remains":
            lambda state: can_use_fire_arrows(state, player) and state.has("Boss Key (Snowhead)", player) and state.has("Small Key (Snowhead)", player, 3) and has_explosives(state, player) or state.has("Small Key (Snowhead)", player, 1) and can_use_fire_arrows(state, player) and state.has("Boss Key (Snowhead)", player) or can_use_fire_arrows(state, player) and state.has("Goht's Remains", player) or glitch_enabled(state, player, options, ("SHT BK Skip", "Action Swap", "Equip Swap", "Long Bomb Hover",)) or (glitch_enabled(state, player, options, ("SHT BK Skip", "Long Bomb Hover",)) and can_use_fire_arrows(state, player)) or (glitch_enabled(state, player, options, ("Long Bomb Hover",)) and can_use_fire_arrows(state, player) and state.has("Boss Key (Snowhead)", player)) or (state.has("Goht's Remains", player) and glitch_enabled(state, player, options, ("Action Swap", "Equip Swap",))),


        "Romani Ranch Breman March Baby Cuccos":
            lambda state: state.has("Bremen Mask", player),
        "Romani Ranch Helping Cremia":
            lambda state: can_use_powder_keg(state, player) and state.has("Progressive Bow", player) or (glitch_enabled(state, player, options, ("Fierce Deity Out Of Bounds",)) and state.has("Progressive Bow", player)) or (glitch_enabled(state, player, options, ("Bomb Hover",)) and state.has("Progressive Bow", player)),
        "Romani Ranch Doggy Racetrack Rooftop Chest":
            lambda state: state.has("Hookshot", player) or can_plant_beans(state, player) or trick_enabled(state, player, options, ("One Sided Collision Itemless", "One Sided Collision",)),
        "Romani Ranch Doggy Race":
            lambda state: state.has("Mask of Truth", player),
        "Romani Ranch Romani Game":
            lambda state: can_use_powder_keg(state, player) and state.has("Progressive Bow", player) or (glitch_enabled(state, player, options, ("Fierce Deity Out Of Bounds",)) and state.has("Progressive Bow", player)) or (glitch_enabled(state, player, options, ("Bomb Hover",)) and state.has("Progressive Bow", player)),
        "Romani Ranch Barn Free Cow":
            lambda state: can_use_powder_keg(state, player) and can_play_song("Epona's Song", state, player) or can_use_powder_keg(state, player) and state.has("Progressive Bow", player) or (glitch_enabled(state, player, options, ("Fierce Deity Out Of Bounds",)) and can_play_song("Epona's Song", state, player)) or (glitch_enabled(state, player, options, ("Bomb Hover",)) and can_play_song("Epona's Song", state, player)),
        "Romani Ranch Barn Stables Front Cow":
            lambda state: can_use_powder_keg(state, player) and can_play_song("Epona's Song", state, player) or can_use_powder_keg(state, player) and state.has("Progressive Bow", player) or (glitch_enabled(state, player, options, ("Fierce Deity Out Of Bounds",)) and can_play_song("Epona's Song", state, player)) or (glitch_enabled(state, player, options, ("Bomb Hover",)) and can_play_song("Epona's Song", state, player)),
        "Romani Ranch Barn Stables Back Cow":
            lambda state: can_use_powder_keg(state, player) and can_play_song("Epona's Song", state, player) or can_use_powder_keg(state, player) and state.has("Progressive Bow", player) or (glitch_enabled(state, player, options, ("Fierce Deity Out Of Bounds",)) and can_play_song("Epona's Song", state, player)) or (glitch_enabled(state, player, options, ("Bomb Hover",)) and can_play_song("Epona's Song", state, player)),


        "Great Bay Healing Zora":
            lambda state: can_play_song("Song of Healing", state, player) or (glitch_enabled(state, player, options, ("Ocarina Items",)) and can_play_song("Song of Healing", state, player)),
        "Great Bay Scarecrow Ledge HP":
            lambda state: can_plant_beans(state, player) and can_reach_scarecrow(state, player) or glitch_enabled(state, player, options, ("Bomb Hover", "Bomb Long Jumps",)),
        "Tingle Great Bay Map Purchase":
            lambda state: has_projectiles(state, player) and state.can_reach("Milk Road", 'Region', player),
        "Great Bay Ledge Grotto Left Cow":
            lambda state: state.has("Hookshot", player) and can_play_song("Epona's Song", state, player) or (glitch_enabled(state, player, options, ("Bomb Hover", "Bomb Long Jumps",)) and can_play_song("Epona's Song", state, player)),
        "Great Bay Ledge Grotto Right Cow":
            lambda state: state.has("Hookshot", player) and can_play_song("Epona's Song", state, player) or (glitch_enabled(state, player, options, ("Bomb Hover", "Bomb Long Jumps",)) and can_play_song("Epona's Song", state, player)),
        "Pinnacle Rock HP":
            lambda state: can_reach_seahorse(state, player) and has_bottle(state, player) and state.has("Zora Mask", player),
        "Pinnacle Rock Upper Eel Chest":
            lambda state: can_reach_seahorse(state, player) and has_bottle(state, player) and state.has("Zora Mask", player) or trick_enabled(state, options, player, ("Pinnacle Rock without Seahorse",)),
        "Pinnacle Rock Lower Eel Chest":
            lambda state: can_reach_seahorse(state, player) and has_bottle(state, player) and state.has("Zora Mask", player) or trick_enabled(state, options, player, ("Pinnacle Rock without Seahorse",)),
        # ~ maybe require 3 bottles for eggs
        "Zora Egg Delivery Song":
            lambda state: can_reach_seahorse(state, player) and has_bottle(state, player, 3) and state.can_reach("Pirates' Fortress Leader's Room Chest", "Location", player) or (trick_enabled(state, player, options, ("Pinnacle Rock without Seahorse", "Equip Swap",)) and has_bottle(state, player, 1)) or (trick_enabled(state, player, options, ("Pinnacle Rock without Seahorse",)) and glitch_enabled(state, player, options,("Bomb Hover",)) and has_bottle(state, player, 1)) or (trick_enabled(state, player, options, ("Pinnacle Rock without Seahorse",)) and state.has("Hookshot", player) and has_bottle(state, player, 1)) or (trick_enabled(state, player, options, ("Pinnacle Rock without Seahorse",)) and state.has("Hookshot", player)),
        "Fisherman Island Game HP":
            lambda state: can_clear_greatbay(state, player),


        "Ocean Spider House Ramp Upper Token":
            lambda state: state.has("Hookshot", player) or trick_enabled(state, player, options, ("Ocean Spider House Ramp Spiders with nothing",)) or trick_enabled(state, player, options, ("Ocean Spider House Ramp Spider with Goron",)),
        "Ocean Spider House Ramp Lower Token":
            lambda state: state.has("Hookshot", player) or trick_enabled(state, player, options, ("Ocean Spider House Ramp Spiders with nothing",)) or trick_enabled(state, player, options, ("Ocean Spider House Ramp Spider with Goron",)),
        "Ocean Spider House Lobby Ceiling Token":
            lambda state: state.has("Hookshot", player) and can_use_fire_arrows(state, player) or (trick_enabled(state, player, options, ("Goron Damage Boost",)) and glitch_enabled(state, player, options, ("Bomb Hover",))) or trick_enabled(state, player, options("Hookshot Pixelshots", "Goron Damage Boost",)),
        "Ocean Spider House First Room Rafter Token":
            lambda state: state.has("Hookshot", player) or trick_enabled(state, player, options, ("Ocean Spider House Tokens as Zora",)) or glitch_enabled(state, player, options, ("Bomb Hover",)),
        "Ocean Spider House First Room Open Pot #1 Token":
            lambda state: state.has("Hookshot", player) or trick_enabled(state, player, options, ("Ocean Spider House Tokens as Zora",)) or glitch_enabled(state, player, options, ("Bomb Hover",)),
        "Ocean Spider House First Room Open Pot #2 Token":
            lambda state: state.has("Hookshot", player) and can_use_fire_arrows(state, player) or trick_enabled(state, player, options, ("Ocean Spider House bonk webbed pot",)),
        "Ocean Spider House First Room Wall Token":
            lambda state: state.has("Hookshot", player) or state.has("Zora Mask", player) or glitch_enabled(state, player, options, ("Bomb Hover",)) or trick_enabled(state, player, options, ("Fierce Deity Jumps",)),
        "Ocean Spider House Library Top Bookcase Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Library Passage Behind Bookcase Front Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Library Passage Behind Bookcase Rear Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Libary Painting #1 Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Library Painting #2 Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Library Rafter Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Library Bookshelf Hole Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House First Room Downstairs Rafter Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House First Room Downstairs Open Pot Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House First Room Downstairs Behind Staircase Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House First Room Downstairs Crate Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House First Room Downstairs Wall Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Dining Room Open Pot Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Dining Room Painting Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Dining Room Ceiling Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Dining Room Chandelier #1 Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Dining Room Chandelier #2 Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Dining Room Chandelier #3 Token ":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Storage Room Web Token":
            lambda state: state.has("Hookshot", player) and can_use_fire_arrows(state, player),
        "Ocean Spider House Storage Room North Wall Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Storage Room Crate Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Storage Room Hidden Hole Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Storage Room Ceiling Pot Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Coloured Mask Sequence HP":
            lambda state: state.has("Hookshot", player) and state.has("Captain's Hat", player) and state.has("Progressive Bow", player),
        "Ocean Spider House Reward":
            lambda state: state.has("Ocean Skulltula Token", player, 30),

        # I added these using the names in locations.py, might wanna double check they're functional since i'm a dummy - muervo.
        "Pirates' Fortress Exterior Underwater Log Chest":
            lambda state: state.has("Zora Mask", player),
        "Pirates' Fortress Exterior Underwater Near Entrance Chest":
            lambda state: state.has("Zora Mask", player),
        "Pirates' Fortress Exterior Underwater Corner Near Fortress Chest":
            lambda state: state.has("Zora Mask", player),

        "Pirates' Fortress Sewers Push Block Maze Chest":
            lambda state: state.has("Goron Mask", player),
        "Pirates' Fortress Sewers Cage HP":
            lambda state: state.has("Goron Mask", player),
        "Pirates' Fortress Sewers Underwater Upper Chest":
            lambda state: state.has("Goron Mask", player),
        "Pirates' Fortress Sewers Underwater Lower Chest":
            lambda state: state.has("Goron Mask", player),

        "Pirates' Fortress Hub Lower Chest":
            lambda state: True,
        "Pirates' Fortress Hub Upper Chest":
            lambda state: state.has("Hookshot", player),
        "Pirates' Fortress Leader's Room Chest":
            lambda state: state.has("Hookshot", player) and state.has("Progressive Bow", player) or (state.has("Hookshot", player) and state.has("Deku Mask", player) and state.has("Progressive Magic", player)),
        "Pirates' Fortress Near Egg Chest":
            lambda state: state.has("Hookshot", player) and can_smack_hard(state, player),
        "Pirates' Fortress Pirates Surrounding Chest":
            lambda state: has_projectiles(state, player) and state.has("Hookshot", player),


        "Zora Cape Near Great Fairy Grotto Chest":
            lambda state: state.has("Goron Mask", player) or has_explosives(state, player),
        "Zora Cape Underwater Chest":
            lambda state: state.has("Zora Mask", player),
        "Zora Cape Underwater Like-Like HP":
            lambda state: state.has("Zora Mask", player),
        "Zora Cape Pot Game Silver Rupee":
            lambda state: state.has("Zora Mask", player),
        "Zora Cape Upper Chest":
            lambda state: state.has("Hookshot", player),
        "Zora Cape Tree Chest":
            lambda state: state.has("Hookshot", player) and state.has("Deku Mask", player),
        # petition to rename this to 'pixel and muervo bottle reward
        "Beaver Bros. Race Bottle Reward":
            lambda state: state.has("Hookshot", player) and state.has("Zora Mask", player),
        # petition to rename this to 'pixel and muervo's love'
        "Beaver Bros. Race HP":
            lambda state: state.has("Hookshot", player) and state.has("Zora Mask", player),


        "Zora Hall Piano Zora Song":
            lambda state: state.has("Zora Mask", player),
        "Zora Hall Torches Reward":
            lambda state: can_use_fire_arrows(state, player),
        "Zora Hall Good Picture of Lulu":
           lambda state: state.has("Pictograph Box", player) and state.has("Zora Mask", player),
        "Zora Hall Bad Picture of Lulu":
           lambda state: state.has("Pictograph Box", player) and state.has("Zora Mask", player),
        "Zora Hall Goron Scrub Trade":
            lambda state: state.has("Zora Mask", player) and state.has("Mountain Title Deed", player) and state.has("Goron Mask", player),
        "Zora Hall Goron Scrub Trade Freestanding HP":
            lambda state: state.has("Deku Mask", player) and state.can_reach("Zora Hall Goron Scrub Trade", 'Location', player),


        "Great Bay Great Fairy Reward":
            lambda state: state.has("Stray Fairy (Great Bay)", player, 15),


        "Great Bay Temple Four Torches Chest":
            lambda state: True,
        "Great Bay Temple Waterwheel Room Skulltula SF":
            lambda state: can_smack_hard(state, player),
        "Great Bay Temple Waterwheel Room Bubble Under Platform SF":
            lambda state: state.has("Zora Mask", player) or (has_projectiles(state, player) and state.has("Great Fairy Mask", player)),
        "Great Bay Temple Blender Room Barrel SF":
            lambda state: state.has("Zora Mask", player),
        "Great Bay Temple Pot At Bottom Of Blender SF":
            lambda state: state.has("Zora Mask", player) or (state.has("Progressive Bow", player) and state.has("Great Fairy Mask", player)),
        "Great Bay Temple Red-Green Pipe First Room Chest":
            lambda state: can_use_ice_arrows(state, player) and state.has("Zora Mask", player) or (state.has("Hookshot", player) and state.has("Zora Mask", player)),
        "Great Bay Temple Red-Green Pipe First Room Pot SF":
            lambda state: can_use_ice_arrows(state, player) or state.has("Zora Mask", player) or (state.has("Progressive Bow", player) and state.has("Great Fairy Mask", player)) or (state.has("Hookshot", player) and state.has("Great Fairy Mask", player)),
        "Great Bay Temple Bio-Baba Hall Chest":
            lambda state: state.has("Zora Mask", player),
        "Great Bay Temple Froggy Entrance Room Pot SF":
            lambda state: state.has("Zora Mask", player),
        "Great Bay Temple Froggy Entrance Room Upper Chest":
            lambda state: state.has("Zora Mask", player),
        "Great Bay Temple Froggy Entrance Room Caged Chest":
            lambda state: can_use_ice_arrows(state, player) and can_use_fire_arrows(state, player) and state.has("Zora Mask", player),
        "Great Bay Temple Froggy Entrance Room Underwater Chest":
            lambda state: state.has("Zora Mask", player),
        "Great Bay Temple Behind Locked Door Chest":
            lambda state: state.has("Small Key (Great Bay)", player) and state.has("Zora Mask", player) and can_smack_hard(state, player) or (state.has("Small Key (Great Bay)", player) and state.has("Zora Mask", player) and has_explosives(state, player)) or (state.has("Small Key (Great Bay)", player) and state.has("Zora Mask", player) and state.has("Progressive Bow", player)),
        "Great Bay Temple Room Behind Waterfall Ceiling Chest":
            lambda state: can_use_ice_arrows(state, player) and state.has("Hookshot", player) and state.has("Zora Mask", player),
        "Great Bay Temple Green Pipe Freezable Waterwheel Upper Chest":
            lambda state: can_use_ice_arrows(state, player) and state.has("Hookshot", player) and state.has("Zora Mask", player) and can_use_fire_arrows(state, player),
        "Great Bay Temple Green Pipe Freezable Waterwheel Lower Chest":
            lambda state: can_use_ice_arrows(state, player) and state.has("Hookshot", player) and state.has("Zora Mask", player) and can_use_fire_arrows(state, player),
        "Great Bay Temple Seesaw Room Underwater Barrel SF":
            lambda state: state.has("Zora Mask", player) and can_use_ice_arrows(state, player) and can_use_fire_arrows(state, player),
        "Great Bay Temple Seesaw Room Chest":
            lambda state: can_use_ice_arrows(state, player) and can_use_fire_arrows(state, player) and state.has("Zora Mask", player) and state.has("Hookshot", player),
        "Great Bay Temple Before Boss Room Underneath Platform Bubble SF":
            lambda state: state.has("Zora Mask", player) and can_use_ice_arrows(state, player) and can_use_fire_arrows(state, player),
        "Great Bay Temple Before Boss Room Exit Tunnel Bubble SF":
            lambda state: state.can_reach("Great Bay Temple Before Boss Room Underneath Platform Bubble SF", 'Location', player),
        "Great Bay Temple Heart Container":
            lambda state: state.can_reach("Great Bay Temple Before Boss Room Underneath Platform Bubble SF", 'Location', player) and state.has("Boss Key (Great Bay)", player) and state.has("Progressive Bow", player) and can_use_fire_arrows(state, player) or state.has("Gyorg's Remains", player),
        "Great Bay Temple Gyorg's Remains":
            lambda state: state.can_reach("Great Bay Temple Before Boss Room Underneath Platform Bubble SF", 'Location', player) and state.has("Boss Key (Great Bay)", player) and state.has("Progressive Bow", player) and can_use_fire_arrows(state, player) or state.has("Gyorg's Remains", player),


        "Road to Ikana Pillar Chest":
            lambda state: state.has("Hookshot", player),
        "Road to Ikana Rock Grotto Chest":
            lambda state: state.has("Goron Mask", player),
        "Road to Ikana Invisible Soldier":
            lambda state: can_play_song("Epona's Song", state, player) and state.has("Bottle of Red Potion", player) and can_use_lens(state, player),


        "Ikana Graveyard Bombable Grotto Chest":
            lambda state: has_explosives(state, player),
        "Graveyard Day 1 Bats Chest":
            lambda state: state.has("Captain's Hat", player) and can_smack(state, player),
        "Graveyard Day 2 Iron Knuckle Chest":
            lambda state: state.has("Captain's Hat", player) and can_smack_hard(state, player) and has_explosives(state, player),
        "Graveyard Day 3 Dampe Big Poe Chest":
            lambda state: (state.has("Captain's Hat", player) and state.has("Progressive Bow", player) or state.has("Zora Mask", player)),
        "Graveyard Sonata To Wake Sleeping Skeleton Chest":
            lambda state: can_play_song("Sonata of Awakening", state, player) and can_smack_hard(state, player) and state.has("Ocarina of Time", player),
        "Graveyard Day 1 Iron Knuckle Song":
            lambda state: state.has("Captain's Hat", player) and can_smack_hard(state, player),


        "Tingle Stone Tower Map Purchase":
            lambda state: has_projectiles(state, player) and state.can_reach("Great Bay", 'Region', player),
        "Ikana Canyon Music Box Mummy":
            lambda state: can_use_ice_arrows(state, player) and can_play_song("Song of Healing", state, player) and can_play_song("Song of Storms", state, player) and state.has("Ocarina of Time", player),
        "Ikana Canyon Zora Scrub Trade":
            lambda state: state.has("Zora Mask", player) and state.has("Ocean Title Deed", player),
        "Ikana Canyon Zora Trade Freestanding HP":
            lambda state: state.has("Deku Mask", player) and state.has("Zora Mask", player) and state.has("Ocean Title Deed", player),
        "Secret Shrine Grotto Chest":
            lambda state: True,

        "Stone Tower Great Fairy Reward":
            lambda state: state.has("Stray Fairy (Stone Tower)", player, 15) and can_use_ice_arrows(state, player),


        "Secret Shrine Left Chest":
            lambda state: can_smack_hard(state, player) and can_use_light_arrows(state, player),
        "Secret Shrine Middle-Left Chest":
            lambda state: can_smack_hard(state, player) and can_use_light_arrows(state, player),
        "Secret Shrine Middle-Right Chest":
            lambda state: can_smack_hard(state, player) and can_use_light_arrows(state, player),
        "Secret Shrine Right Chest":
            lambda state: can_use_light_arrows(state, player) and can_smack_hard(state, player),
        "Secret Shrine Center Chest":
            lambda state: state.can_reach("Secret Shrine Left Chest", 'Location', player) and state.can_reach("Secret Shrine Middle-Left Chest", 'Location', player) and state.can_reach("Secret Shrine Middle-Right Chest", 'Location', player) and state.can_reach("Secret Shrine Right Chest", 'Location', player),

        # Recommend 2-3 bottles for Well in logic
        "Ikana Well Torch Chest":
            lambda state: has_bottle(state, player) and can_plant_beans(state, player) or (can_use_light_arrows(state, player) and has_bottle(state, player)),
        "Ikana Well Invisible Chest":
            lambda state: (has_bottle(state, player) and state.has("Progressive Wallet", player) or state.has("Mask of Scents", player)),
        "Ikana Well Final Chest":
            lambda state: has_bottle(state, player) and can_plant_beans(state, player) and state.has("Progressive Bomb Bag", player) or (can_use_light_arrows(state, player) and has_bottle(state, player)),
        "Ikana Well Cow":
            lambda state: has_bottle(state, player) and can_plant_beans(state, player) and state.can_reach("Twin Islands Hot Water Grotto Chest", 'Location', player) or can_use_light_arrows(state, player) and (state.can_reach("Twin Islands Hot Water Grotto Chest", 'Location', player) or state.can_reach("Mountain Village Invisible Ladder Cave Healing Invisible Goron", 'Location', player) or state.can_reach("Ikana Well Invisible Chest", 'Location', player)),


        "Ikana Castle Pillar Freestanding HP":
            lambda state: state.has("Deku Mask", player) and can_use_lens(state, player) and can_use_fire_arrows(state, player),
        "Ikana Castle King Song":
            lambda state: state.has("Deku Mask", player) and can_use_lens(state, player) and can_use_fire_arrows(state, player) and state.has("Powder Keg", player) and state.has("Goron Mask", player) and has_mirror_shield(state, player) or (can_use_fire_arrows(state, player) and has_mirror_shield(state, player) and can_use_light_arrows(state, player)),

        "Stone Tower Inverted Outside Left Chest":
            lambda state: can_plant_beans(state, player),
        "Stone Tower Inverted Outside Middle Chest":
            lambda state: can_plant_beans(state, player),
        "Stone Tower Inverted Outside Right Chest":
            lambda state: can_plant_beans(state, player),

        # Stone Tower has 4 keys total
        "Stone Tower Temple Entrance Room Eye Switch Chest":
            lambda state: state.has("Progressive Bow", player),
        "Stone Tower Temple Entrance Room Lower Chest":
            lambda state: state.has("Small Key (Stone Tower)", player, 4) and state.has("Deku Mask", player) and can_use_light_arrows(state, player) and state.has("Hookshot", player),
        "Stone Tower Temple Armos Room Back Chest":
            lambda state: has_explosives(state, player) and has_mirror_shield(state, player) or can_use_light_arrows(state, player),
        "Stone Tower Temple Armos Room Upper Chest":
            lambda state: has_explosives(state, player) and state.has("Hookshot", player) and has_mirror_shield(state, player) or can_use_light_arrows(state, player) and state.has("Hookshot", player),
        "Stone Tower Temple Armos Room Lava Chest":
            lambda state: has_explosives(state, player) and has_mirror_shield(state, player) or can_use_light_arrows(state, player),
        "Stone Tower Temple Eyegore Room Switch Chest":
            lambda state: can_use_light_arrows(state, player) and can_use_ice_arrows(state, player) and state.has("Zora Mask", player),
        # "Stone Tower Temple Eyegore Room Dexi Hand Ledge Chest" Vanilla route requires 1 small key
        "Stone Tower Temple Eyegore Room Dexi Hand Ledge Chest":
            lambda state: state.has("Small Key (Stone Tower)", player) and state.has("Zora Mask", player) or can_use_light_arrows(state, player) and state.has("Zora Mask", player),
        # "Stone Tower Temple Eastern Water Room Underwater Chest" involves inverting STT then uninverting in vanilla gameplay, the Ice arrows allow you to bypass this, original logic was a 'trick' method
        "Stone Tower Temple Eastern Water Room Underwater Chest":
            lambda state: state.has("Small Key (Stone Tower)", player) and state.has("Zora Mask", player) and (can_use_light_arrows(state, player) or has_mirror_shield(state, player)),
        # Vanilla route requires you to route left through STT and end in the water room, this applies to check above
        # could clean code up below here removing light arrow requirements and using the can_reach function to massively reduce length of lines.
        # Also following vanilla routing, all checks below here in Uninverted STT require a second key
        "Stone Tower Temple Eastern Water Room Sun Block Chest":
            lambda state: state.has("Small Key (Stone Tower)", player) and state.has("Zora Mask", player) and can_use_light_arrows(state, player),
        "Stone Tower Temple Mirror Room Sun Block Chest":
            lambda state: state.has("Small Key (Stone Tower)", player, 1) and state.has("Zora Mask", player) and has_mirror_shield(state, player) or can_use_light_arrows(state, player) and state.has("Small Key (Stone Tower)", player),
        "Stone Tower Temple Mirror Room Sun Face Chest":
            lambda state: state.has("Small Key (Stone Tower)", player, 1) and state.has("Zora Mask", player) and has_mirror_shield(state, player) or can_use_light_arrows(state, player) and state.has("Small Key (Stone Tower)", player),
        "Stone Tower Temple Air Gust Room Side Chest":
            lambda state: state.has("Small Key (Stone Tower)", player, 1) and state.has("Zora Mask", player) and has_mirror_shield(state, player) and state.has("Deku Mask", player) or (can_use_light_arrows(state, player) and state.has("Small Key (Stone Tower)", player) and state.has("Deku Mask", player)),
        "Stone Tower Temple Air Gust Room Goron Switch Chest":
            lambda state: state.can_reach("Stone Tower Temple Mirror Room Sun Block Chest", 'Location', player) and state.has("Goron Mask", player),
        "Stone Tower Temple Garo Master Chest":
            lambda state: state.can_reach("Stone Tower Temple Air Gust Room Side Chest", 'Location', player) and can_smack_hard(state, player),
        "Stone Tower Temple After Garo Upside Down Chest":
            lambda state: state.can_reach("Stone Tower Temple Inverted Eyegore Chest", 'Location', player),
        "Stone Tower Temple Eyegore Chest":
            lambda state: state.can_reach("Stone Tower Temple Garo Master Chest", 'Location', player),
        "Stone Tower Temple Inverted Entrance Room Sun Face Chest":
            lambda state: can_use_light_arrows(state, player),
        "Stone Tower Temple Inverted Eastern Air Gust Room Fire Chest":
            lambda state: state.can_reach("Stone Tower Temple Entrance Room Eye Switch Chest", 'Location', player) and state.has("Small Key (Stone Tower)", player) and state.has("Zora Mask", player) and state.has("Deku Mask", player) and can_use_light_arrows(state, player),
        "Stone Tower Temple Inverted Eastern Air Gust Room Ice Eye Switch Chest":
            lambda state: can_use_light_arrows(state, player) and state.has("Deku Mask", player) and can_use_fire_arrows(state, player),
        "Stone Tower Temple Inverted Eastern Air Gust Room Hall Floor Switch Chest":
            lambda state: can_use_light_arrows(state, player) and state.has("Deku Mask", player),
        # "Stone Tower Temple Inverted Wizzrobe Chest" This is where the third key would be getting used on its way to that check
        "Stone Tower Temple Inverted Wizzrobe Chest":
            lambda state: can_use_light_arrows(state, player) and state.has("Deku Mask", player) and state.has("Small Key (Stone Tower)", player, 3) and state.has("Hookshot", player),
        "Stone Tower Temple Inverted Death Armos Maze Chest":
            lambda state:  state.can_reach("Stone Tower Temple Inverted Wizzrobe Chest", 'Location', player) and can_play_song("Elegy of Emptiness", state, player),
        "Stone Tower Temple Inverted Gomess Chest":
            lambda state: state.can_reach("Stone Tower Temple Inverted Wizzrobe Chest", 'Location', player) and can_use_light_arrows(state, player) and can_smack_hard(state, player),
        # "Stone Tower Temple Inverted Eyegore Chest" is where the fourth key would be getting used
        "Stone Tower Temple Inverted Eyegore Chest":
            lambda state: state.can_reach("Stone Tower Temple Inverted Wizzrobe Chest", 'Location', player) and state.has("Small Key (Stone Tower)", player, 4),
        "Stone Tower Temple Inverted Heart Container":
            lambda state: state.can_reach("Stone Tower Temple Inverted Eyegore Chest", 'Location', player) and state.has("Boss Key (Stone Tower)", player) and (state.has("Progressive Bow", player) or state.has("Fierce Deity's Mask", player) or (state.has("Giant's Mask", player) and state.has("Progressive Sword", player))) or state.has("Twinmold's Remains", player) and (state.has("Progressive Bow", player) or state.has("Fierce Deity's Mask", player) or (state.has("Giant's Mask", player) and state.has("Progressive Sword", player))),
        "Stone Tower Temple Inverted Twinmold's Remains":
            lambda state: state.can_reach("Stone Tower Temple Inverted Eyegore Chest", 'Location', player) and state.has("Boss Key (Stone Tower)", player) and (state.has("Progressive Bow", player) or state.has("Fierce Deity's Mask", player) or (state.has("Giant's Mask", player) and state.has("Progressive Sword", player))) or state.has("Twinmold's Remains", player) and (state.has("Progressive Bow", player) or state.has("Fierce Deity's Mask", player) or (state.has("Giant's Mask", player) and state.has("Progressive Sword", player))),

        "Moon Deku Trial HP":
            lambda state: state.has("Deku Mask", player),
        "Moon Goron Trial HP":
            lambda state: state.has("Goron Mask", player) and state.has("Progressive Magic", player),
        "Moon Zora Trial HP":
            lambda state: state.has("Zora Mask", player),
        "Moon Link Trial Garo Master Chest":
            lambda state: can_smack_hard(state, player) and state.has("Hookshot", player),
        "Moon Link Trial Iron Knuckle Lower Chest":
            lambda state: state.can_reach("Moon Link Trial Garo Master Chest", 'Location', player),
        "Moon Link Trial HP":
            lambda state: state.can_reach("Moon Link Trial Garo Master Chest", 'Location', player) or can_smack_hard(state, player) and has_bombchus(state, player) and state.has("Progressive Bow", player),
        "Defeat Majora":
            lambda state: can_smack_hard(state, player) and (((state.has("Zora Mask", player) or has_mirror_shield(state, player)) and can_use_light_arrows(state, player)) or (state.has("Fierce Deity's Mask", player) and state.has("Progressive Magic", player))),
    }