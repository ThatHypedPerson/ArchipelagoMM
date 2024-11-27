from typing import Callable, Dict

from BaseClasses import CollectionState, MultiWorld

def universal_item_rule(item):
    pass

def can_play_song(song, state, player):
    return state.has(song, player) and state.has("Ocarina of Time", player)

def can_get_magic_beans(state, player):
    return state.has("Magic Bean", player) and state.has("Deku Mask", player) and state.can_reach("Deku Palace", 'Region', player)

def has_bombchus(state, player):
    return state.has("Bombchu (1)", player) or state.has("Bombchu (5)", player) or state.has("Bombchu (10)", player)

def has_explosives(state, player):
    return state.has("Progressive Bomb Bag", player) or has_bombchus(state, player) or state.has("Blast Mask", player),

def has_hard_projectiles(state, player):
    return state.has("Progressive Bow", player) or state.has("Zora Mask", player) or state.has("Hookshot", player)

def has_projectiles(state, player):
    return (state.has("Deku Mask", player) and state.has("Progressive Magic Upgrade", player)) or has_hard_projectiles(state, player)

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

def has_bottle(state, player):
    return state.has("Bottle", player) or state.has("Bottle of Chateau Romani", player) or state.has("Bottle of Red Potion", player)

def can_plant_beans(state, player):
    return can_get_magic_beans(state, player) and (has_bottle(state, player) or can_play_song("Song of Storms", state, player))

def can_use_powder_keg(state, player):
    return state.has("Powder Keg", player) and state.has("Goron Mask", player)

def can_use_magic_arrow(item, state, player):
    return state.has(item, player) and state.has("Progressive Bow", player) and state.has("Progressive Magic Upgrade", player)

def can_use_fire_arrows(state, player):
    return can_use_magic_arrow("Fire Arrow", state, player)

def can_use_ice_arrows(state, player):
    return can_use_magic_arrow("Ice Arrow", state, player)

def can_use_light_arrows(state, player):
    return can_use_magic_arrow("Light Arrow", state, player)

def has_gilded_sword(state, player):
    return state.has("Progressive Sword", player, 3)

def get_region_rules(player):
    return {
        "Clock Town -> The Moon":
            lambda state: state.has("Ocarina of Time", player) and state.has("Oath to Order", player) and state.has("Odolwa's Remains", player) and state.has("Goht's Remains", player) and state.has("Gyorg's Remains", player) and state.has("Twinmold's Remains", player),
        "Southern Swamp -> Southern Swamp (Deku Palace)":
            lambda state: state.has("Bottle of Red Potion", player) and has_hard_projectiles(state, player) and state.has("Deku Mask", player), # or state.has("Pictograph Box", player)
        "Southern Swamp (Deku Palace) -> Swamp Spider House":
            lambda state: state.has("Deku Mask", player) and can_use_fire_arrows(state, player),
        "Southern Swamp (Deku Palace) -> Deku Palace":
            lambda state: state.has("Deku Mask", player),
        "Southern Swamp (Deku Palace) -> Woodfall":
            lambda state: state.has("Deku Mask", player),
        "Woodfall -> Woodfall Temple":
            lambda state: can_play_song("Sonata of Awakening", state, player),
        "Termina Field -> Path to Mountain Village":
            lambda state: state.has("Progressive Bow", player),
        "Path to Mountain Village -> Mountain Village":
            lambda state: state.has("Goron Mask", player) or has_explosives(state, player) or can_use_fire_arrows(state, player),
        "Path to Snowhead -> Snowhead Temple":
            lambda state: state.has("Goron Mask", player) and can_play_song("Goron's Lullaby", state, player) and state.has("Progressive Magic Upgrade", player),
        "Termina Field -> Great Bay":
            lambda state: can_play_song("Epona's Song", state, player),
        "Great Bay -> Ocean Spider House":
            lambda state: has_explosives(state, player) and state.has("Hookshot", player), 
        "Great Bay -> Pirates' Fortress":
            lambda state: state.has("Zora Mask", player),
        "Pirates' Fortress -> Pirates' Fortress (Interior)":
            lambda state: state.has("Goron Mask", player) or state.has("Hookshot", player),
        "Zora Cape -> Great Bay Temple":
            lambda state: can_play_song("New Wave Bossa Nova", state, player) and state.has("Hookshot", player) and state.has("Zora Mask", player),
        "Road to Ikana -> Ikana Graveyard":
            lambda state: can_play_song("Epona's Song", state, player),
        "Road to Ikana -> Ikana Canyon":
            lambda state: can_play_song("Epona's Song", state, player) and state.has("Hookshot", player) and (state.has("Garo Mask", player) or state.has("Gibdo Mask", player)),
        "Ikana Canyon -> Secret Shrine":
            lambda state: can_use_light_arrows(state, player),
        "Ikana Canyon -> Beneath the Well":
            lambda state: can_use_ice_arrows(state, player) and state.has("Gibdo Mask", player) and has_bottle(state, player),
        "Ikana Canyon -> Ikana Castle":
            lambda state: can_use_ice_arrows(state, player) and (can_use_light_arrows(state, player) or (state.has("Gibdo Mask", player) and state.has("Mirror Shield", player) and has_bottle(state, player))),
        "Stone Tower -> Stone Tower Temple":
            lambda state: can_use_ice_arrows(state, player) and can_play_song("Elegy of Emptiness", state, player) and state.has("Goron Mask", player) and state.has("Zora Mask", player),
        "Stone Tower -> Stone Tower (Inverted)":
            lambda state: can_use_light_arrows(state, player) and can_play_song("Elegy of Emptiness", state, player),
    }

def get_location_rules(player):
    return {
        "Keaton Quiz":
            lambda state: state.has("Keaton Mask", player),
        "Clock Tower Happy Mask Salesman #1":
            lambda state: state.has("Ocarina of Time", player),
        "Clock Tower Happy Mask Salesman #2":
            lambda state: state.has("Ocarina of Time", player),
        "Clock Town Postbox":
            lambda state: state.has("Postman's Hat", player),
        "Clock Town Hide-and-Seek":
            lambda state: has_projectiles(state, player),
        "Laundry Pool Kafei's Request":
            lambda state: state.has("Letter to Kafei", player),
        "Laundry Pool Curiosity Shop Salesman #1":
            lambda state: state.has("Letter to Kafei", player),
        "Laundry Pool Curiosity Shop Salesman #2":
            lambda state: state.has("Letter to Kafei", player),
        "South Clock Town Corner Chest":
            lambda state: state.has("Hookshot", player),
        "South Clock Town Final Day Tower Chest":
            lambda state: state.has("Hookshot", player) or (state.has("Deku Mask", player) and state.has("Moon's Tear", player)),
        "East Clock Town Couples Mask on Mayor":
            lambda state: state.has("Couple's Mask", player),
        "East Clock Town Shooting Gallery 40-49 Points":
            lambda state: state.has("Progressive Bow", player),
        "East Clock Town Shooting Gallery Perfect 50 Points":
            lambda state: state.has("Progressive Bow", player),
        "East Clock Town Honey and Darling Any Day":
            lambda state: state.has("Progressive Bow", player) or state.has("Progressive Bomb Bag", player) or has_bombchus(state, player),
        "East Clock Town Honey and Darling All Days":
            lambda state: state.has("Progressive Bow", player) and state.has("Progressive Bomb Bag", player) and has_bombchus(state, player),
        "East Clock Town Treasure Game Chest (Goron)":
            lambda state: state.has("Goron Mask", player),
        "East Clock Town Sewer Chest":
            lambda state: state.can_reach("Clock Town Hide-and-Seek", 'Location', player) and has_explosives(state, player),
        "East Clock Town Astral Observatory":
            lambda state: has_projectiles(state, player),
        "North Clock Town Deku Playground Any Day":
            lambda state: state.has("Deku Mask", player),
        "North Clock Town Deku Playground All Days":
            lambda state: state.has("Deku Mask", player),
        "North Clock Town Save Old Lady":
            lambda state: state.has("Progressive Sword", player) or state.has("Great Fairy Sword", player),
        "North Clock Town Great Fairy Reward (Has Transformation Mask)":
            lambda state: state.has("Stray Fairy (Clock Town)", player) and (state.has("Deku Mask", player) or state.has("Goron Mask", player) or state.has("Zora Mask", player)),
        "North Clock Town Great Fairy Reward":
            lambda state: state.has("Stray Fairy (Clock Town)", player),
        "West Clock Town Swordsman Expert Course":
            lambda state: state.has("Progressive Sword", player),
        "West Clock Town Postman Counting":
            lambda state: state.has("Bunny Hood", player),
        "West Clock Town Dancing Sisters":
            lambda state: state.has("Kamaro Mask", player),
        "West Clock Town Bank 200 Rupees":
            lambda state: state.has("Progressive Sword", player) and state.has("Progressive Wallet", player),
        "West Clock Town Bank 500 Rupees":
            lambda state: state.has("Fierce Deity's Mask", player) and state.has("Great Fairy Sword", player) and state.has("Progressive Wallet", player),
        "West Clock Town Bank 1000 Rupees":
            lambda state: state.has("Fierce Deity's Mask", player) and state.has("Great Fairy Sword", player) and state.has("Progressive Wallet", player, 2),
        "West Clock Town Priority Mail to Postman":
            lambda state: state.has("Priority Mail", player),
        "Moon's Tear Trade":
            lambda state: state.has("Moon's Tear", player),
        "Top of Clock Tower (Ocarina of Time)":
            lambda state: has_projectiles(state, player),
        "Top of Clock Tower (Song of Time)":
            lambda state: has_projectiles(state, player),
        "Stock Pot Inn Midnight Meeting":
            lambda state: state.has("Kafei's Mask", player) and state.has("Deku Mask", player) and state.has("Room Key", player),
        "Stock Pot Inn Upstairs Middle Room Chest"
            lambda state: state.has("Room Key", player),
        "Stock Pot Inn Midnight Toilet Hand":
            lambda state: has_paper(state, player),
        "Stock Pot Inn Granny Story #1":
            lambda state: state.has("All-Night Mask", player),
        "Stock Pot Inn Granny Story #2":
            lambda state: state.has("All-Night Mask", player),
        "Stock Pot Inn Anju and Kafei":
            lambda state: state.has("Kafei's Mask", player) and can_play_song("Epona's Song", state, player) and state.has("Letter to Kafei", player) and state.has("Pendant of Memories", player) and state.has("Hookshot", player) and (state.has("Garo Mask", player) or state.has("Gibdo Mask", player)),
        "Milk Bar Show":
            lambda state: state.has("Romani Mask", player) and state.has("Deku Mask", player) and state.has("Goron Mask", player) and state.has("Zora Mask", player) and state.has("Ocarina of Time", player),
        "Milk Bar Priority Mail to Aroma":
            lambda state: state.has("Romani Mask", player) and state.has("Kafei's Mask", player) and state.has("Priority Mail", player),


        "Termina Stump Chest":
            lambda state: state.has("Hookshot", player) or can_plant_beans(state, player),
        "Termina Underwater Chest":
            lambda state: state.has("Zora Mask", player),
        "Termina Peahat Grotto Chest":
            lambda state: can_smack_hard(state, player),
        "Termina Dodongo Grotto Chest":
            lambda state: can_smack_hard(state, player),
        "Termina Bio Baba Grotto HP":
            lambda state: has_explosives(state, player) and state.has("Goron Mask", player) and state.has("Zora Mask", player) and has_projectiles(state, player),
        "Termina Northern Midnight Dancer":
            lambda state: state.has("Ocarina of Time", player) and state.has("Song of Healing", player),
        "Termina Gossip Stones HP":
            lambda state: (state.has("Deku Mask", player) and can_play_song("Sonata of Awakening", state, player)) and (state.has("Goron Mask", player) and can_play_song("Goron's Lullaby", state, player)) and (state.has("Zora Mask", player) and can_play_song("New Wave Bossa Nova", state, player)),
        "Termina Moon's Tear Scrub HP":
            lambda state: state.can_reach("East Clock Town Astral Observatory", 'Location', player) and state.has("Moon's Tear", player) and state.has("Progressive Wallet", player),
        "Milk Road Gorman Ranch Race":
            lambda state: state.has("Ocarina of Time", player) and state.has("Epona's Song", player),
        "Road to Swamp Tree HP":
            lambda state: has_projectiles(state, player),
        "Swamp Shooting Gallery 2120 Points":
            lambda state: state.has("Progressive Bow", player),
        "Swamp Shooting Gallery 2180 Points":
            lambda state: state.has("Progressive Bow", player),


        "Romani Ranch Grog":
            lambda state: state.has("Bremen Mask", player),
        "Romani Ranch Helping Cremia":
            lambda state: can_use_powder_keg(state, player) and state.has("Progressive Bow", player),
        "Romani Dog Racetrack Chest":
            lambda state: state.has("Hookshot", player),
        "Romani Ranch Romani Game":
            lambda state: can_use_powder_keg(state, player) and state.has("Progressive Bow", player),


        "Southern Swamp Deku Trade":
            lambda state: state.has("Land Title Deed", player),
        "Southern Swamp Deku Trade Freestanding HP":
            lambda state: state.has("Land Title Deed", player) and state.has("Deku Mask", player),
        "Southern Swamp Tour Witch Gift":
            lambda state: state.has("Bottle of Red Potion", player),
        "Southern Swamp Near Swamp Spider House Grotto Chest":
            lambda state: state.has("Deku Mask", player),
        "Southern Swamp Song Tablet":
            lambda state: state.has("Deku Mask", player),


        "Swamp Spider House First Room Pot Near Entrance Token":
            lambda state: can_smack(state, player),
        "Swamp Spider House First Room Crawling In Water Token":
            lambda state: can_smack(state, player),
        "Swamp Spider House First Room Crawling Right Column Token":
            lambda state: can_smack(state, player) and state.has("Hookshot", player),
        "Swamp Spider House First Room Crawling Left Column Token":
            lambda state: can_smack(state, player) and state.has("Hookshot", player),
        "Swamp Spider House First Room Against Far Wall Token":
            lambda state: can_smack(state, player) and state.has("Hookshot", player) and can_plant_beans(state, player),
        "Swamp Spider House First Room Lower Left Bugpatch Token":
            lambda state: can_smack(state, player) and has_bottle(state, player),
        "Swamp Spider House First Room Lower Right Bugpatch Token":
            lambda state: can_smack(state, player) and has_bottle(state, player),
        "Swamp Spider House First Room Upper Right Bugpatch Token":
            lambda state: can_smack(state, player) and has_bottle(state, player),
        "Swamp Spider House Monument Room Left Crate Token":
            lambda state: can_smack(state, player),
        "Swamp Spider House Monument Room Right Crate Token":
            lambda state: can_smack(state, player),
        "Swamp Spider House Monument Room Crawling Wall Token":
            lambda state: can_smack(state, player) and state.has("Hookshot", player) and can_plant_beans(state, player),
        "Swamp Spider House Monument Room Crawling On Monument Token":
            lambda state: can_smack(state, player) and state.has("Hookshot", player) and can_plant_beans(state, player),
        "Swamp Spider House Monument Room Behind Torch Token":
            lambda state: can_smack(state, player),
        "Swamp Spider House Pottery Room Beehive #1 Token":
            lambda state: can_smack(state, player) and has_projectiles(state, player),
        "Swamp Spider House Pottery Room Beehive #2 Token":
            lambda state: can_smack(state, player) and has_projectiles(state, player),
        "Swamp Spider House Pottery Room Small Pot Token":
            lambda state: can_smack(state, player),
        "Swamp Spider House Pottery Room Left Large Pot Token":
            lambda state: can_smack(state, player),
        "Swamp Spider House Pottery Room Right Large Pot Token":
            lambda state: can_smack(state, player),
        "Swamp Spider House Pottery Room Behind Vines Token":
            lambda state: can_smack_hard(state, player),
        "Swamp Spider House Pottery Room Upper Wall Token":
            lambda state: can_smack(state, player) and can_play_song("Sonata of Awakening", state, player) and state.has("Deku Mask", player) and state.has("Hookshot", player),
        "Swamp Spider House Golden Room Crawling Left Wall Token":
            lambda state: can_smack(state, player) and state.has("Hookshot", player) and can_play_song("Sonata of Awakening", state, player) and state.has("Deku Mask", player),
        "Swamp Spider House Golden Room Crawling Right Column Token":
            lambda state: can_smack(state, player) and state.has("Hookshot", player),
        "Swamp Spider House Golden Room Against Far Wall Token":
            lambda state: can_smack(state, player) and state.has("Hookshot", player) and can_plant_beans(state, player),
        "Swamp Spider House Golden Room Beehive Token":
            lambda state: can_smack(state, player) and has_projectiles(state, player),
        "Swamp Spider House Tree Room Tall Grass #1 Token":
            lambda state: can_smack(state, player),
        "Swamp Spider House Tree Room Tall Grass #2 Token":
            lambda state: can_smack(state, player),
        "Swamp Spider House Tree Room Tree #1 Token":
            lambda state: can_smack(state, player),
        "Swamp Spider House Tree Room Tree #2 Token":
            lambda state: can_smack(state, player),
        "Swamp Spider House Tree Room Tree #3 Token":
            lambda state: can_smack(state, player),
        "Swamp Spider House Tree Room Beehive Token":
            lambda state: can_smack(state, player) and has_projectiles(state, player),
        "Swamp Spider House Reward":
            lambda state: state.has("Swamp Skulltula Token", player, 30),


        "Deku Palace Bean Seller":
            lambda state: state.has("Deku Mask", player),
        "Deku Palace Bean Grotto Chest":
            lambda state: can_plant_beans(state, player) and state.has("Hookshot", player),
        "Deku Palace Monkey Song":
            lambda state: state.has("Ocarina of Time", player) and can_plant_beans(state, player) and state.has("Deku Mask", player),
        "Deku Palace Butler Race":
            lambda state: can_clear_woodfall(state, player) and has_bottle(state, player),


        "Woodfall Great Fairy Reward":
            lambda state: state.has("Stray Fairy (Woodfall)", player, 15),


        "Woodfall Temple Dragonfly Chest":
            lambda state: state.has("Small Key (Woodfall)", player),
        "Woodfall Temple Black Boe Room Chest":
            lambda state: state.has("Small Key (Woodfall)", player),
        "Woodfall Temple Wooden Flower Switch Chest":
            lambda state: state.has("Progressive Bow", player),
        "Woodfall Temple Dinolfos Chest":
            lambda state: state.has("Progressive Bow", player) and can_smack_hard(state, player),
        "Woodfall Temple Boss Key Chest":
            lambda state: state.has("Progressive Bow", player),
        "Woodfall Temple Wooden Flower Bubble SF":
            lambda state: state.has("Progressive Bow", player),
        "Woodfall Temple Moving Flower Platform Room Beehive SF":
            lambda state: has_projectiles(state, player) and state.has("Great Fairy Mask", player),
        "Woodfall Temple Push Block Skulltula SF":
            lambda state: state.has("Small Key (Woodfall)", player) and can_smack_hard(state, player),
        "Woodfall Temple Push Block Bubble SF":
            lambda state: state.has("Small Key (Woodfall)", player) and has_projectiles(state, player) and state.has("Great Fairy Mask", player),
        "Woodfall Temple Push Block Beehive SF":
            lambda state: state.has("Small Key (Woodfall)", player) and has_projectiles(state, player) and state.has("Great Fairy Mask", player),
        "Woodfall Temple Final Room Right Lower Platform SF":
            lambda state: state.has("Progressive Bow", player),
        "Woodfall Temple Final Room Right Upper Platform SF":
            lambda state: state.has("Progressive Bow", player),
        "Woodfall Temple Final Room Left Upper Platform SF":
            lambda state: state.has("Progressive Bow", player),
        "Woodfall Temple Final Room Bubble SF":
            lambda state: state.has("Progressive Bow", player) and state.has("Great Fairy Mask", player),
        "Woodfall Temple Heart Container":
            lambda state: state.has("Progressive Bow", player) and (state.has("Boss Key (Woodfall)", player) or state.has("Odolwa's Remains", player)),
        "Woodfall Temple Odolwa's Remains":
            lambda state: state.has("Progressive Bow", player) and (state.has("Boss Key (Woodfall)", player) or state.has("Odolwa's Remains", player)),
            
            
        "Tour Witch Target Shooting":
            lambda state: can_clear_woodfall(state, player) and (state.has("Bottle of Red Potion", player) or state.has("Bottle of Chateau Romani", player)) and state.has("Progressive Bow", player),
            
            
        "Mountain Village Invisible Ladder Cave Healing Invisible Goron":
            lambda state: state.has("Lens of Truth", player) and state.has("Progressive Magic Upgrade", player) and can_play_song("Song of Healing", state, player),
        "Mountain Village Feeding Freezing Goron":
            lambda state: state.has("Goron Mask", player) and can_use_fire_arrows(state, player),
        "Mountain Village Spring Ramp Grotto":
            lambda state: can_clear_snowhead(state, player),
        "Don Gero Mask Frog Song HP":
            lambda state: state.has("Don Gero Mask", player) and can_clear_snowhead(state, player) and state.can_reach("Woodfall Boss Key Chest", 'Location', player) and state.can_reach("Great Bay Temple", 'Region', player) and can_use_ice_arrows(player, state) and can_use_fire_arrows(player, state),
        "Mountain Village Smithy Day 1":
            lambda state: state.has("Progressive Wallet", player) and (can_clear_snowhead(state, player) or (has_bottle(state, player) and state.can_reach("Mountain Village Darmani", 'Location', player)) or can_use_fire_arrows(state, player)),
        "Mountain Village Smithy Day 2":
            lambda state: state.has("Bottle of Gold Dust", player) and state.can_reach("Mountain Village Smithy Day 1", 'Location', player),
            
            
        "Twin Islands Ramp Grotto Chest":
            lambda state: has_explosives(state, player) and (state.has("Goron Mask", player) or state.has("Hookshot", player)),
        "Twin Islands Hot Water Grotto Chest":
            lambda state: has_explosives(state, player) and ((can_use_fire_arrows(state, player) or state.can_reach("Mountain Village Darmani", 'Location', player)) or can_clear_snowhead(state, player)),
        "Twin Islands Spring Underwater Cave Chest":
            lambda state: state.has("Zora Mask", player) and can_clear_snowhead(state, player),
        "Twin Islands Spring Underwater Near Ramp Chest":
            lambda state: state.has("Zora Mask", player) and can_clear_snowhead(state, player),
        "Goron Racetrack Bottle Prize":
             lambda state: state.has("Powder Keg", player) and can_clear_snowhead(state, player),
        "Gorons Lullaby Intro":
             lambda state: state.has("Goron Mask", player) and ((state.can_reach("Mountain Village Darmani", 'Location', player) and has_bottle(state, player)) or can_use_fire_arrows(state, player)),
            
            
        "Goron Village Lens Cave Rock Chest":
            lambda state: has_explosives(state, player),
        "Gorons Lullaby":
            lambda state: state.has("Goron Mask", player) and (state.can_reach("Mountain Village Darmani", 'Location', player) or can_use_fire_arrows(state, player)),
        "Mountain Title Deed":
            lambda state: state.has("Deku Mask", player) and state.has("Swamp Title Deed", player),
        "Goron Village Freestanding HP":
            lambda state: state.can_reach("Mountain Title Deed", 'Location', player),
        "Powder Keg Goron Reward":
            lambda state: state.has("Powder Keg", player) and (can_clear_snowhead(state, player) or can_use_fire_arrows(state, player)),
        "Goron Village Deku Scrub Bomb Bag":
            lambda state: state.has("Goron Mask", player) and state.has("Progressive Wallet", player), 
            
            
        "Path to Snowhead Grotto Chest":
            lambda state: state.has("Goron Mask", player) and state.has("Progressive Magic Upgrade", player) and has_explosives(state, player),
        "Path to Snowhead HP":
            lambda state: state.has("Goron Mask", player) and state.has("Progressive Magic Upgrade", player) and state.has("Lens of Truth", player),
            
            
        "Snowhead Great Fairy Reward":
            lambda state: state.has("Stray Fairy (Snowhead)", player, 15),
            
       # Snowhead has 3 small keys     
        "Snowhead Temple Initial Runway Under Platform Bubble SF":
            lambda state: state.has("Great Fairy Mask", player) and state.has("Progressive Bow", player),
        "Snowhead Temple Initial Runway Tower Bubble SF":
            lambda state: state.has("Great Fairy Mask", player) and state.has("Progressive Bow", player) and state.has("Lens of Truth", player),
        "Snowhead Temple Grey Door Near Bombable Stairs Box SF":
            lambda state: state.has("Small Key (Snowhead)", player) and state.has("Great Fairy Mask", player) and has_explosives(state, player),
        "Snowhead Temple Timed Switch Room Bubble SF":
            lambda state: state.has("Small Key (Snowhead)", player) and state.has("Great Fairy Mask", player) and state.has("Progressive Bow", player) and state.has("Lens of Truth", player) and has_explosives(state, player),
        "Snowhead Temple Snowmen Bubble SF":
            lambda state: state.has("Small Key (Snowhead)", player) and state.has("Great Fairy Mask", player) and state.has("Progressive Bow", player) and has_explosives(state, player),
        "Snowhead Temple Dinolfos Room First SF":
            lambda state: state.has("Small Key (Snowhead)", player) and has_explosives(state, player) and can_use_fire_arrows(state, player),
        "Snowhead Temple Dinolfos Room Second SF":
            lambda state: state.has("Small Key (Snowhead)", player) and has_explosives(state, player) and can_use_fire_arrows(state, player),
        "Snowhead Temple Initial Runway Ice Blowers Chest":
            lambda state: can_use_fire_arrows(state, player),
        "Snowhead Temple Green Door Freezards Chest":
            lambda state: can_use_fire_arrows(state, player),
        "Snowhead Temple Orange Door Upper Chest":
            lambda state: state.has("Hookshot", player) or (state.has("Small Key (Snowhead)", player) and can_use_fire_arrows(state, player)),
        "Snowhead Temple Grey Door Center Chest":
            lambda state: state.has("Small Key (Snowhead)", player),
        "Snowhead Temple Grey Door Upper Chest":
            lambda state: state.has("Small Key (Snowhead)", player) and can_use_fire_arrows(state, player),
        "Snowhead Temple Upstairs 2F Icicle Room Hidden Chest":
            lambda state: state.has("Small Key (Snowhead)", player) and state.has("Lens of Truth", player) and has_explosives(state, player),
        "Snowhead Temple Upstairs 2F Icicle Room Snowball Chest":
            lambda state: state.has("Small Key (Snowhead)", player) and state.has("Progressive Bow", player) and has_explosives(state, player),
        "Snowhead Temple Elevator Room Invisible Platform Chest":
            lambda state: state.has("Lens of Truth", player) and (can_use_fire_arrows(state, player) or (state.has("Small Key (Snowhead)", player) and has_explosives(state, player))),
        "Snowhead Temple 1st Wizzrobe Chest":
            lambda state: state.has("Small Key (Snowhead)", player) and has_explosives(state, player),
        "Snowhead Temple Column Room 2F Hidden Chest":
            lambda state: state.has("Small Key (Snowhead)", player) and state.has("Lens of Truth", player) and has_explosives(state, player) and (state.has("Hookshot", player) or (state.has("Deku Mask", player) and can_use_fire_arrows(state, player))),
        "Snowhead Temple 2nd Wizzrobe Chest":
            lambda state: state.has("Small Key (Snowhead)", player) and can_use_fire_arrows(state, player) and has_explosives(state, player),
        "Snowhead Temple Heart Container":
            lambda state: can_use_fire_arrows(state, player) and ((state.has("Boss Key (Snowhead)", player) and state.has("Small Key (Snowhead)", player) and has_explosives(state, player)) or state.has("Goht's Remains", player)),
        "Snowhead Temple Goht's Remains":
            lambda state: can_use_fire_arrows(state, player) and ((state.has("Boss Key (Snowhead)", player) and state.has("Small Key (Snowhead)", player) and has_explosives(state, player)) or state.has("Goht's Remains", player)),
            
        
        "Great Bay Scarecrow Ledge HP":
            lambda state: state.has("Hookshot", player) and can_plant_beans(state, player),
        "Great Bay Coast Healing Zora":
            lambda state: state.can_play_song("Song of Healing", state, player),
        # ~ Can grab this without Goron/Hook from entrance ledge
        "Fisherman House":
            lambda state: state.has("Zora Mask", player) and state.has("Pictograph Box", player) and (state.has("Hookshot", player) or state.has("Goron Mask", player)),
        "Pinnacle Rock HP":
            lambda state: state.has("Zora Mask", player) and state.has("Progressive Magic Upgrade", player) and state.has("Pictograph Box", player) and has_bottle(state, player),
        "Pinnacle Rock Upper Eel Chest":
            lambda state: state.has("Zora Mask", player) and state.has("Progressive Magic Upgrade", player) and state.has("Pictograph Box", player) and has_bottle(state, player),
        "Pinnacle Rock Lower Eel Chest":
            lambda state: state.has("Zora Mask", player) and state.has("Progressive Magic Upgrade", player) and state.has("Pictograph Box", player) and has_bottle(state, player),
        # ~ maybe require 3 bottles for eggs
        "Zora Baby Egg Delivery Song":
            lambda state: state.has("Zora Mask", player) and state.has("Progressive Magic Upgrade", player) and has_bottle(state, player) and state.has("Hookshot", player),
        "Fisherman Island Game HP":
            lambda state: can_clear_greatbay(state, player),
        
            
        "Ocean Spider House Ramp Upper Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Ramp Lower Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Lobby Ceiling Token":
            lambda state: state.has("Hookshot", player) and can_use_fire_arrows(state, player),
        "Ocean Spider House First Room Rafter Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House First Room Open Pot #1 Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House First Room Open Pot #2 Token":
            lambda state: state.has("Hookshot", player) and can_use_fire_arrows(state, player),
        "Ocean Spider House First Room Wall Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Library Top Bookcase Token":
            lambda state: state.has("Hookshot", player) and can_use_fire_arrows(state, player),
        "Ocean Spider House Library Passage Behind Bookcase Front Token":
            lambda state: state.has("Hookshot", player) and can_use_fire_arrows(state, player),
        "Ocean Spider House Library Passage Behind Bookcase Rear Token":
            lambda state: state.has("Hookshot", player) and can_use_fire_arrows(state, player),
        "Ocean Spider House Libary Painting #1 Token":
            lambda state: state.has("Hookshot", player) and can_use_fire_arrows(state, player),
        "Ocean Spider House Library Painting #2 Token":
            lambda state: state.has("Hookshot", player) and can_use_fire_arrows(state, player),
        "Ocean Spider House Library Rafter Token":
            lambda state: state.has("Hookshot", player) and can_use_fire_arrows(state, player),
        "Ocean Spider House Library Bookshelf Hole Token":
            lambda state: state.has("Hookshot", player) and can_use_fire_arrows(state, player),
        "Ocean Spider House First Room Downstairs Rafter Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House First Room Downstairs Pot Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House First Room Downstairs Behind Staircase Token":
            lambda state: state.has("Hookshot", player) and can_use_fire_arrows(state, player),
        "Ocean Spider House First Room Downstairs Crate Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House First Room Downstairs Wall Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Dining Room Pot Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Dining Room Painting Token":
            lambda state: state.has("Hookshot", player),
        "Ocean Spider House Dining Room Ceiling Token":
            lambda state: state.has("Hookshot", player),
        "Ocean spider House Dining Room Chandelier #1 Token":
            lambda state: state.has("Hookshot", player) and state.has("Goron Mask", player),
        "Ocean Spider House Dining Room Chandelier #2 Token":
            lambda state: state.has("Hookshot", player) and state.has("Goron Mask", player),
        "Ocean Spider House Dining Room Chandelier #3 Token ":
            lambda state: state.has("Hookshot", player) and state.has("Goron Mask", player),
        "Ocean Spider House Storage Room SW Token":
            lambda state: state.has("Hookshot", player) and can_use_fire_arrows(state, player),
        "Ocean Spider House Storage Room North Wall Token":
            lambda state: state.has("Hookshot", player) and can_use_fire_arrows(state, player),
        "Ocean Spider House Storage Room Crate Token":
            lambda state: state.has("Hookshot", player) and can_use_fire_arrows(state, player),
        "Ocean Spider House Storage Room Hidden Hole Token":
            lambda state: state.has("Hookshot", player) and can_use_fire_arrows(state, player),
        "Ocean Spider House Storage Room Ceiling Barrel Token":
            lambda state: state.has("Hookshot", player) and can_use_fire_arrows(state, player),
        "Ocean Spider House Coloured Mask Sequence HP":
            lambda state: state.has("Hookshot", player) and state.has("Captain's Hat", player) and state.has("Progressive Bow", player),
        "Ocean Spider House Reward":
            lambda state: state.has("Ocean Skulltula Token", player, 30),
        
        # Couldn't find a call to these locations but the logic is sound, would recommend adding bow for the guards though. Deku snot doesn't work on guards.
        # ~ "Pirates' Fortress Tunnels HP":
            # ~ lambda state: state.has("Goron's Mask", player),
        # ~ "Pirates' Fortress Tunnels Cage Chest":
            # ~ lambda state: state.has("Goron's Mask", player),
        # ~ "Pirates' Fortress Tunnels Mines Chest":
            # ~ lambda state: state.has("Goron's Mask", player),
        # ~ "Pirates' Fortress Tunnels Lower Mines Chest":
            # ~ lambda state: state.has("Goron's Mask", player),
        # ~ "Pirates' Fortress Fish Tank Chest":
            # ~ lambda state: state.has("Hookshot", player),
        # ~ "Pirates' Fortress Pirates Surrounding Chest":
            # ~ lambda state: has_projectiles(state, player),
        # ~ "Pirates' Fortress Hub Lower Chest":
            # ~ lambda state: state.has("Goron's Mask", player) or state.has("Hookshot", player),
        # ~ "Pirates' Fortress Hub Upper Chest":
            # ~ lambda state: state.has("Hookshot", player),
            
            
        "Zora Cape Near Great Fairy Grotto Chest":
            lambda state: state.has("Goron Mask", player) or has_explosives(state, player),
        "Zora Cape Underwater Chest":
            lambda state: state.has("Zora Mask", player),
        "Zora Cape Underwater Like-Like HP":
            lambda state: state.has("Zora Mask", player) and state.has("Progressive Magic", player),
        "Zora Cape Pot Game Silver Rupee":
            lambda state: state.has("Zora Mask", player),
        "Zora Cape First High Ledge Chest":
            lambda state: state.has("Hookshot", player),
        "Zora Cape Second High Ledge Chest":
            lambda state: state.has("Hookshot", player),
        "Beaver Bros. Race Bottle Reward":
            lambda state: state.has("Hookshot", player) and state.has("Zora Mask", player),
        "Beaver Bros. Race HP":
            lambda state: state.has("Hookshot", player) and state.has("Zora Mask", player),
            
            
        "Zora Hall Piano Zora Song":
            lambda state: state.has("Zora Mask", player),
        "Zora Hall Torches Reward":
            lambda state: can_use_fire_arrows(state, player),
        "Zora Hall Deku Scrub Trade":
            lambda state: state.has("Zora Mask", player) and state.has("Mountain Title Deed", player),
        "Zora Hall HP":
            lambda state: state.has("Deku Mask", player) and can_reach("Zora Hall Deku Scrub Trade", 'Location', player),
            
            
        "Great Bay Great Fairy Reward":
            lambda state: state.has("Stray Fairy (Great Bay)", player, 15),
            
            
        "Great Bay Temple Four Torches Chest":
            lambda state: can_use_fire_arrows(state, player),
        "Great Bay Temple Waterwheel Room Skulltula SF"
            lambda state: state.has("Progressive Bow", player) and state.has("Great Fairy Mask", player),
        "Great Bay Temple Waterwheel Room Bubble Under Platform SF"
            lambda state: state.has("Zora Mask", player) and state.has("Progressive Bow", player) and state.has("Great Fairy Mask", player),
        "Great Bay Temple Blender Room Barrel SF"
            lambda state: state.has("Zora Mask", player) and state.has("Progressive Bow", player) and state.has("Great Fairy Mask", player),
        "Great Bay Temple Pot At Bottom Of Blender SF"
            lambda state: state.has("Zora Mask", player) and state.has("Progressive Bow", player) and state.has("Great Fairy Mask", player),
        "Great Bay Temple Red-Green Pipe First Room Chest"
            lambda state: can_use_ice_arrows(state, player) and state.has("Zora Mask", player) and state.has("Progressive Bow", player) and state.has("Hookshot", player),
        "Great Bay Temple Red-Green Pipe First Room Pot SF"
            lambda state: can_use_ice_arrows(state, player) and state.has("Zora Mask", player) and state.has("Progressive Bow", player),
        "Great Bay Temple Bio-Baba Hall Chest"
            lambda state.has("Zora Mask", player) and state.has("Progressive Bow", player) and state.has("Hookshot", player),
        "Great Bay Temple Froggy Entrance Room Pot SF":
            lambda state: state.has("Zora Mask", player) and state.has("Progressive Bow", player) and state.has("Great Fairy Mask", player),
        "Great Bay Temple Froggy Entrance Room Upper Chest"
            lambda state: state.has("Zora Mask", player) and has("Hookshot", player),
        "Great Bay Temple Froggy Entrance Room Caged Chest":
            lambda state: can_use_ice_arrows(state, player) and can_use_fire_arrows(state, player),
        "Great Bay Temple Froggy Entrance Room Underwater Chest"
            lambda state: state.has("Zora Mask", player),
        "Great Bay Temple Behind Locked Door Chest":
            lambda state: state.has("Progressive Bow", player) and can_use_explosives(state, player) and state.has("Great Fairy's Sword", player) and state.has("Hero's Shield", player),
        "Great Bay Temple Room Behind Waterfall Ceiling Chest":
            lambda state: can_use_ice_arrows(state, player),
        "Great Bay Temple Green Pipe Freezable Waterwheel Upper Chest":
            lambda state: can_use_ice_arrows(state, player),
        "Great Bay Temple Green Pipe Freezable Waterwheel Lower Chest":
            lambda state: can_use_ice_arrows(state, player),
        "Great Bay Temple Seesaw Room Underwater Barrel SF":
            lambda state: state.has("Zora Mask" player) and can_use_ice_arrows(state, player),
        "Great Bay Temple Seesaw Room Chest":
            lambda state: can_use_ice_arrows(state, player) and can_use_fire_arrows(state, player),
        "Great Bay Temple Before Boss Room Underneath Platform Bubble SF"
            lambda state.has("Zora Mask" player) and can_use_ice_arrows(state, player) and state.has("Great Fairy Mask", player),
        "Great Bay Temple Before Boss Room Exit Tunnel Bubble SF"
            lambda state.has("Zora Mask" player) and state.has("Great Fairy Mask", player),
        "Great Bay Temple Heart Container":
            lambda state: (can_use_ice_arrows(state, player) and can_use_fire_arrows(state, player) and state.has("Small Key (Great Bay Temple)", player) and state.has("Boss Key (Great Bay Temple)", player)) or (state.has("Gyorg's Remains", player) and state.has("Progressive Bow", player)),
        "Great Bay Temple Gyorg's Remains":
            lambda state: (can_use_ice_arrows(state, player) and can_use_fire_arrows(state, player) and state.has("Small Key (Great Bay Temple)", player) and state.has("Boss Key (Great Bay Temple)", player)) or (state.has("Gyorg's Remains", player) and state.has("Progressive Bow", player)),
        

        "Road to Ikana Pillar Chest":
            lambda state: state.has("Hookshot", player),
        "Road to Ikana Rock Grotto Chest":
            lambda state: state.has("Goron Mask", player),
        "Road to Ikana Stone Soldier":
            lambda state: can_play_song("Epona's Song", state, player) and has_bottle(state, player) and state.has("Progressive Magic Upgrade", player) and state.has("Lens of Truth", player),
            
            
        "Graveyard Day 1 Bats Chest":
            lambda state: state.has("Captain's Hat", player) and can_smack_hard(state, player),
        "Graveyard Day 2 Iron Knuckle Chest":
            lambda state: state.has("Captain's Hat", player) and can_smack_hard(state, player) and has_explosives(state, player),
        "Graveyard Day 3 Dampe Big Poe Chest":
            lambda state: state.has("Captain's Hat", player) and state.has("Progressive Bow", player),
        "Graveyard Sonata To Wake Sleeping Skeleton Chest":
            lambda state: can_play_song("Sonata of Awakening", state, player) and can_smack_hard(state, player) and state.has("Progressive Bow", player),
        "Graveyard Day 1 Iron Knuckle Song":
            lambda state: state.has("Captain's Hat", player) and can_smack_hard(state, player) and can_use_fire_arrows(state, player),
       # Does this account for Upper Ikana Canyon access?     
        "Ikana Canyon Pamela's Father":
            lambda state: can_use_ice_arrows(state, player) and state.has("Hookshot", player) and (state.has("Gibdo Mask", player) or state.has("Garo Mask", player)) and can_play_song("Song of Healing", state, player) and can_play_song("Song of Storms", state, player) and (has_explosives(state, player) or state.has("Stone Mask", player)),
       # If so this and HP can be acquired without Ice Arrows 
        "Ikana Canyon Deku Scrub Trade":
            lambda state: can_use_ice_arrows(state, player) and state.has("Hookshot", player) and (state.has("Gibdo Mask", player) or state.has("Garo Mask", player)) and state.has("Zora Mask", player) and state.has("Ocean Title Deed", player),
        "Ikana Canyon HP":
            lambda state:state.has("Deku Mask", player) and can_reach("Ikana Canyon Deku Scrub Trade", 'Location', player),
            
            
        "Stone Temple Great Fairy Reward":
            lambda state: state.has("Stray Fairy (Stone Tower)", player, 15),
            
        
        "Secret Shrine Left Chest":
            lambda state: can_smack_hard(state, player),
        "Secret Shrine Middle-Left Chest":
            lambda state: can_smack_hard(state, player) and has_projectiles(state, player),
        "Secret Shrine Middle-Right Chest":
            lambda state: can_smack_hard(state, player) and has_projectiles(state, player) and has_explosives(state, player),
        "Secret Shrine Right Chest":
            lambda state: can_smack_hard(state, player),
        "Secret Shrine Center Chest":
            lambda state: state.can_reach("Secret Shrine Left Chest", 'Location', player) and state.can_reach("Secret Shrine Middle-Left Chest", 'Location', player) and state.can_reach("Secret Shrine Middle-Right Chest", 'Location', player) and state.can_reach("Secret Shrine Right Chest", 'Location', player),
            
            # Recommend 2-3 bottles for Well in baby logic
        "Beneath the Well Rightside Torch Chest":
            lambda state: has_bottle(state, player) and can_plant_beans(state, player),
        "Beneath the Well Invisible Chest":
            lambda state: has_bottle(state, player) and (state.has("Progressive Wallet", player) or state.has("Mask of Scents", player)),
        "Beneath the Well Final Chest":
            lambda state: can_use_light_arrows(state, player) or (has_bottle(state, player) and can_plant_beans(state, player)),
            
            
        "Ikana Castle Pillar Freestanding HP":
            lambda state: state.has("Deku Mask", player) and state.has("Lens of Truth", player) and can_use_fire_arrows(state, player), 
        "Ikana Castle King Song":
            lambda state: state.has("Deku Mask", player) and state.has("Lens of Truth", player) and can_use_fire_arrows(state, player) and .has("Powder Keg", player) and .has("Goron Mask", player) and has.("Mirror Shield" player),
        "Stone Tower Inverted Outside Left Chest":
            lambda state: can_plant_beans(state, player),
        "Stone Tower Inverted Outside Middle Chest":
            lambda state: can_plant_beans(state, player),
        "Stone Tower Inverted Outside Right Chest":
            lambda state: can_plant_beans(state, player),


        "Stone Tower Temple Entrance Room Eye Switch Chest"
            lambda state: state.has("Progressive Bow", player)
        "Stone Tower Temple Armos Room Back Chest":
            lambda state: can_use_light_arrows(state, player) or (state.has("Mirror Shield", player) and has_explosives(state, player)),
        "Stone Tower Temple Armos Room Upper Chest":
            lambda state: state.has("Hookshot", player) and (has_explosives(state, player)
        "Stone Tower Temple Armos Room Lava Chest"
            lambda state: state.has("Goron Mask", player) and has_explosives(state, player)
        "Stone Tower Temple Eyegore Room Switch Chest":
            lambda state: can_use_light_arrows(state, player) or state.has("Mirror Shield", player),
        "Stone Tower Temple Eyegore Room Dexi Hand Ledge Chest":
            lambda state: state.has("Zora Mask", player),
        "Stone Tower Temple Eastern Water Room Underwater Chest":
            lambda state: can_use_light_arrows(state, player) and can_use_ice_arrows(state, player),
        "Stone Tower Temple Eastern Water Room Sun Block Chest"
            lambda state: (can_use_light_arrows(state, player) and state.has("Mirror Shield", player)),
        "Stone Tower Temple Mirror Room Sun Block Chest":
            lambda state: state.has("Small Key (Stone Tower Temple)", player) and state.has("Stone Mask", player) and (can_use_light_arrows(state, player) and state.has("Mirror Shield", player)),
        "Stone Tower Temple Mirror Room Sun Face Chest":
            lambda state: state.has("Small Key (Stone Tower Temple)", player) and state.has("Stone Mask", player) and (can_use_light_arrows(state, player) and state.has("Mirror Shield", player)),
        "Stone Tower Temple Air Gust Room Side Chest":
            lambda state: state.has("Small Key (Stone Tower Temple)", player) and state.has("Deku Mask", player) and (can_use_light_arrows(state, player) and state.has("Mirror Shield", player)),
        #Possibly remove mirror for here since you can hard require hitting the sun switch to make the room less shit for baby logic?
        "Stone Tower Temple Air Gust Room Goron Switch Chest":
            lambda state: state.has("Small Key (Stone Tower Temple)", player) and state.has("Deku Mask", player) and (can_use_light_arrows(state, player) and state.has("Mirror Shield", player)),
        "Stone Tower Temple Garo Master Chest":
            lambda state: can_smack_hard(state, player) and state.has("Small Key (Stone Tower Temple)", player) and state.has("Deku Mask", player) and (can_use_light_arrows(state, player) or state.has("Mirror Shield", player)),
        "Stone Tower Temple After Garo Upside Down Chest":
            lambda state: state.has("Small Key (Stone Tower Temple)", player) and state.has("Deku Mask", player) and can_use_light_arrows(state, player),
        "Stone Tower Temple Eyegore Chest":
            lambda state: state.has("Small Key (Stone Tower Temple)", player) and state.has("Deku Mask", player) and (can_use_light_arrows(state, player) or state.has("Mirror Shield", player)),
        "Stone Tower Temple Inverted Entrance Room Sun Face Chest":
            lambda state: (can_use_light_arrows(state, player),
        "Stone Tower Temple Inverted Eastern Air Gust Room Fire Chest":
            lambda state: state.has("Deku Mask", player),
        "Stone Tower Temple Inverted Eastern Air Gust Room Ice Eye Switch":
            lambda state: state.has("Deku Mask", player) and can_use_fire_arrows(state, player),
        "Stone Tower Temple Inverted Eastern Air Gust Room Hall Floor Switch Chest":
            lambda state: state.has("Deku Mask", player),
        "Stone Tower Temple Inverted Wizzrobe Chest":
            lambda state: state.has("Small Key (Stone Tower Temple)", player) and state.has("Deku Mask", player),
        "Stone Tower Temple Inverted Death Armos Maze Chest":
            lambda state: state.has("Small Key (Stone Tower Temple)", player) and state.has("Deku Mask", player),
        "Stone Tower Temple Inverted Gomess Chest":
            lambda state: state.has("Small Key (Stone Tower Temple)", player) and state.has("Deku Mask", player) and (state.has("Great Fairy's Sword", player) or state.has("Fierce Deity's Mask", player)),
        "Stone Tower Temple Inverted Eyegore Chest":
            lambda state: state.has("Small Key (Stone Tower Temple)", player) and state.has("Deku Mask", player),
        "Stone Tower Temple Heart Container":
            lambda state: state.has("Small Key (Stone Tower Temple)", player) and state.has("Deku Mask", player) and state.has("Giant's Mask", player) and (state.has("Boss Key (Stone Tower Temple)", player) or state.has("Twinmold's Remains", player)),
        "Stone Tower Temple Twinmold's Remains":
            lambda state: state.has("Small Key (Stone Tower Temple)", player) and state.has("Deku Mask", player) and state.has("Giant's Mask", player) and (state.has("Boss Key (Stone Tower Temple)", player) or state.has("Twinmold's Remains", player)),


        "Moon Deku Trial HP":
            lambda state: state.has("Deku Mask", player),
        "Moon Goron Trial HP":
            lambda state: state.has("Goron Mask", player) and state.has("Progressive Magic Upgrade", player),
        "Moon Zora Trial HP":
            lambda state: state.has("Zora Mask", player) and state.has("Progressive Magic Upgrade", player),
        "Moon Link Trial Garo Master Chest"
            lambda state: state.has("Fierce Deity's Mask", player) and state.has("Progressive Magic Upgrade", player) and state.has("Great Fairy Sword", player) and has_gilded_sword(state, player) and state.has("Progressive Bow", player),
        "Moon Link Trial Iron Knuckle Lower Chest"
            lambda state: state.has("Fierce Deity's Mask", player) and state.has("Progressive Magic Upgrade", player) and state.has("Great Fairy Sword", player) and has_gilded_sword(state, player),
        "Moon Link Trial HP"
            lambda state: state.has("Fierce Deity's Mask", player) and state.has("Progressive Magic Upgrade", player) and state.has("Great Fairy Sword", player) and has_gilded_sword(state, player) and state.has("Progressive Bow", player) and has_explosives(state, player),
        "Defeat Majora":
            lambda state: state.has("Fierce Deity's Mask", player) and state.has("Progressive Magic Upgrade", player) and state.has("Great Fairy Sword", player) and has_gilded_sword(state, player) and state.has("Progressive Bow", player) and state.has("Light Arrow", player)
    }
