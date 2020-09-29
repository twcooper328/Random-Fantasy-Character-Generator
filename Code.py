import random
import os 
import time

clear = lambda: os.system('cls')

#Prints a row of stars
def stars ():
    print("**************************************")

#Generated and returns randomized stats - returns a dictionary 
def stats_gen ():
    #randomly fills stats 
    stats = {"Vit: ": 0, "Pow: ": 0, "Int: ": 0, "Dex: ": 0, "Will: ": 0, "Con: ": 0} 
    stats["Vit: "] = random.randint(75, 100)  
    stats["Pow: "] = random.randint(35, 50) 
    stats["Int: "] = random.randint(35, 50)
    stats["Dex: "] = random.randint(30, 40)
    stats["Will: "] = random.randint(35, 50) 
    stats["Con: "] = random.randint(35, 50)   

    return stats

#Generates a name randomy - Returnes a string
def name_gen():
    #generates class modifier
    num = random.randint(0, 10)

    class_mod_list = ["Arcane ", "Peerless ", "Stealthy ", "Veteran ", "Well-Rounded ",
     "Master ", "Tainted ", "Bandit ", "Undead ", "Holy ", "Skilled "]

    for x in range(11):
        if x == num:
            class_mod = class_mod_list[num]

    #generate class name
    num2 = random.randint(0, 8)

    class_name_list = ["Hero", "Rogue", "Knight", "Gladiator", "Mage",
     "Assassin", "Skeleton", "Archer", "Vampire"]

    for y in range(9):
        if y == num2:
            class_name = class_name_list[num2]

    full_name = str(class_mod) + str(class_name)

    if full_name == "Undead Vampire":
        full_name = "Immortal Vampire"
    if full_name == "Undead Skeleton":
        full_name = "Ageless Skeleton"

    return full_name
    
#Modifies stats based on unit class name - returns a list
def stat_mod(str, list):
    stats = list
    name = str

    name_list = ["Hero", "Rogue", "Knight", "Gladiator", "Mage",
     "Assassin", "Skeleton", "Archer", "Vampire"]
    # class mod modifier
    if "Arcane " in name:
        stats["Pow: "] = int(stats["Pow: "]) - 20 
        stats["Int: "] = int(stats["Int: "]) + 20
    if "Peerless " in name:
        stats["Pow: "] = int(stats["Pow: "]) + 20 
        stats["Int: "] = int(stats["Int: "]) - 20
    if "Stealthy " in name:
        stats["Vit: "] = int(stats["Vit: "]) - 10 
        stats["Dex: "] = int(stats["Dex: "]) + 20
        stats["Con: "] = int(stats["Con: "]) - 10 
    if "Veteran " in name:
        stats["Dex: "] = int(stats["Dex: "]) + 10
        if int(stats["Pow: "]) > int(stats["Int: "]):
            stats["Pow: "] = int(stats["Pow: "]) + 10
        else:
            stats["Int: "] = int(stats["Int: "]) + 10
    if "Well-Rounded " in name:
        low_stat = (min(stats, key=stats.get))
        stats[low_stat] = stats[low_stat] + 10

        high_stat = (max(stats, key=stats.get))
        stats[high_stat] = stats[high_stat] - 10
    if "Master " in name:
        stats["Vit: "] = int(stats["Vit: "]) + 10
        stats["Pow: "] = int(stats["Pow: "]) + 10
        stats["Int: "] = int(stats["Int: "]) + 10 
        stats["Dex: "] = int(stats["Dex: "]) + 10
        stats["Will: "] = int(stats["Will: "]) + 10
        stats["Con: "] = int(stats["Con: "]) + 10
    if "Tainted " in name:
        stats["Vit: "] = int(stats["Vit: "]) - 20
        stats["Pow: "] = int(stats["Pow: "]) + 30
        stats["Con: "] = int(stats["Con: "]) - 10
    if "Bandit " in name:
        stats["Int: "] = int(stats["Int: "]) + 10 
        stats["Dex: "] = int(stats["Dex: "]) + 10
        stats["Dex: "] = int(stats["Dex: "]) - 10
        stats["Con: "] = int(stats["Con: "]) - 10
    if "Undead " in name:
        if "Vampire" in name:
            stats["Vit: "] = int(stats["Vit: "]) + 20
            stats["Int: "] = int(stats["Int: "]) + 20
        else:
            stats["Vit: "] = int(stats["Vit: "]) - 10
            stats["Dex: "] = int(stats["Dex: "]) - 20
            stats["Con: "] = int(stats["Con: "]) + 10
            stats["Will: "] = int(stats["Will: "]) - 10
    if "Holy " in name:
        stats["Will: "] = int(stats["Will: "]) + 20
        stats["Pow: "] = int(stats["Pow: "]) - 10
    if "Skilled " in name:
        high_stat = (max(stats, key=stats.get))
        stats[high_stat] = stats[high_stat] + 10

        if int(stats["Pow: "]) > int(stats["Int: "]):
            stats["Pow: "] = int(stats["Pow: "]) + 10
        else:
            stats["Int: "] = int(stats["Int: "]) + 10

    if "Hero" in name:
        stats["Pow: "] = int(stats["Pow: "]) + 10 
        stats["Dex: "] = int(stats["Dex: "]) - 20
        stats["Will: "] = int(stats["Will: "]) + 10
        if "Tainted" in name:
            stats["Vit: "] = int(stats["Vit: "]) - 10
        else:
            stats["Vit: "] = int(stats["Vit: "]) + 10
        if "Master " in name:
            stats["Vit: "] = int(stats["Vit: "]) + 20
    if "Rogue" in name: 
        stats["Dex: "] = int(stats["Dex: "]) + 20
        stats["Will: "] = int(stats["Will: "]) - 10
        stats["Con: "] = int(stats["Con: "]) - 10
    if "Knight" in name: 
        stats["Dex: "] = int(stats["Dex: "]) - 20
        stats["Will: "] = int(stats["Will: "]) + 10
        stats["Con: "] = int(stats["Con: "]) + 20
        if "Holy" in name:
            stats["Will: "] = int(stats["Will: "]) + 10
    if "Gladiator" in name:
        stats["Pow: "] = int(stats["Pow: "]) + 20
        stats["Dex: "] = int(stats["Dex: "]) - 10
        stats["Will: "] = int(stats["Will: "]) - 10
    if "Mage" in name:
        stats["Int: "] = int(stats["Int: "]) + 20 
        stats["Dex: "] = int(stats["Dex: "]) - 10
        stats["Con: "] = int(stats["Con: "]) - 10
    if "Assassin" in name:
        stats["Vit: "] = int(stats["Vit: "]) - 10
        stats["Pow: "] = int(stats["Pow: "]) + 10
        stats["Dex: "] = int(stats["Dex: "]) + 10
        stats["Con: "] = int(stats["Con: "]) - 10
    if "Skeleton" in name:
        stats["Vit: "] = int(stats["Vit: "]) - 10
        stats["Int: "] = int(stats["Int: "]) - 10 
        stats["Con: "] = int(stats["Con: "]) + 20
    if "Archer" in name:
        stats["Dex: "] = int(stats["Dex: "]) + 10
        stats["Will: "] = int(stats["Will: "]) + 10
        stats["Con: "] = int(stats["Con: "]) - 10
    if "Vampire" in name:
        stats["Int: "] = int(stats["Int: "]) + 10 
        stats["Dex: "] = int(stats["Dex: "]) + 10
        stats["Will: "] = int(stats["Will: "]) - 30
        stats["Con: "] = int(stats["Con: "]) + 10


    return stats

#Determines most effective attack method - Returns either "Pow: " or "Int: "
#If called with a 5th argument "TRUE" - then will return the damage output instead
def atk_info(pow, inl, will, con, damage = False):
    #figue out pow v con
    con_percent = con / 100
    atk_reduced = (pow - (pow * .20))
    damage_blocked = atk_reduced * float(con_percent)
    hit = round(atk_reduced - damage_blocked)

    #figure out inl v will
    will_percent = will / 100
    spl_reduced = (inl - (inl * .20))
    damage_reflected = spl_reduced * float(will_percent)
    spell = round(spl_reduced - damage_reflected)

    if damage == False:
        if spell > hit:
            return "Int: "
        else:
            return "Pow: "
    else:
        if spell > hit:
            return spell
        else:
            return hit

#Generates flavor text based on name - prints flavor text
def atk_description(unit, method):
    name = str(unit)
    atk_method = method

    num = random.randint(0, 1)

    if atk_method == "Pow: ":
        if "Archer" in name or "Rogue" in name:
            arch_list = ["Snipes with pin-point accuracy", "Rapid arrows fired in succession"]
            print(arch_list[num])
        elif "Arcane" in name or "Mage" in name:
            mag_list = ["Enchantments bestow fearsome might", "Summoned swords swarm and slash"]
            print(mag_list[num])
        elif "Master" in name or "Immortal" in name or "Ageless" in name:
            mast_list = ["Summons the magic from a forgotten age", "Calls forth spirits from realms unknown"]
            print(mast_list[num])
        elif "Tainted" in name or "Vampire" in name:
            evl_list = ["Wielder of an evil sword", "Cuts with deadly intent"]
            print(evl_list[num])
        else:
            norm_list = ["Attacks with fearsome blows", "Slashes with powerful force"]
            print(norm_list[num])

    if atk_method == "Int: ":
        if "Archer" in name or "Rogue" in name:
            arch_list = ["Fires magic bolts from a bow ", "Lightning, fire, and ice arrows"]
            print(arch_list[num])
        elif "Assassin" in name or "Stealthy" in name or "Rogue" in name:
            mag_list = ["A magic dagger strikes from the shadows", "Spells that strike from darkness"]
            print(mag_list[num])
        elif "Master" in name or "Immortal" in name or "Ageless" in name:
            mast_list = ["Wields Timeless sorceries", "Bends magic and the elements"]
            print(mast_list[num])
        elif "Tainted" in name or "Vampire" in name:
            evl_list = ["Wields darks magic", "Employs evil curses"]
            print(evl_list[num])
        else:
            norm_list = ["Casts powerful spells", "Summons fiery magic"]
            print(norm_list[num])

#compares units dexterity and reurns 1 hot a hit - or 0 for a miss
def dodge_chance(accuracy, evasion):
    num = 1

    if evasion >= 40 + accuracy:
        num = random.randint(0, 1)
    elif evasion >= 20 + accuracy:
        num = random.randint(0, 2)
    elif evasion >= 10 + accuracy:
        num = random.randint(0, 3)
    elif evasion >= 5 + accuracy:
        num = random.randint(0, 5)
    elif evasion >= accuracy:
        num = random.randint(0, 10)
    
    if num == 0:
        return 0
    else:
        return 1

#START - intro phase
clear()

stars()
print("Thomas Cooper             ICSTARS:C47")
stars()

time.sleep( 1.5 )
clear()

#random-name phase
x = 0
while x < 1:
    stars()
    print("       WELCOME TO RANDOM BATTLE!!!")
    stars()
    print("     Enter 'go' to generate warriors")
    print("         and simulate a battle.")
    stars()

    choice_menu = input("ENTER 'Go' TO CONTINUE:")
    
    menu_choice = str(choice_menu).lower()

    if str(menu_choice) == "go" or str(menu_choice) == "f":
      clear()
      break
        
    else:
      clear()
      continue
    

main_loop = True

while main_loop == True:
    unit1 = "unit1"
    unit2 = "unit2"


    x = 0
    #scramble effect phase 
    while x < 11:
    
        stars()
    
        unit1 = name_gen()
        print(str(unit1))

        stars()

        unit2 = name_gen()
        print(str(unit2))

        stars()

        x += 1
    
        time.sleep(0.05)
        clear()

    #generate unit 1
    hero_name = name_gen()
    hero_stats = stats_gen()
    
    hero_stats_mod = stat_mod(hero_name, hero_stats)

    #generate unit 2
    enemy_name = name_gen()
    enemy_stats = stats_gen()
    
    enemy_stats_mod = stat_mod(enemy_name, enemy_stats)

    #diplays units information: stats and a description of how they will be attacking
    stars()

    print(hero_name)
    print(hero_stats_mod)

    hero_atk_stat = atk_info(hero_stats_mod["Pow: "], hero_stats_mod["Int: "],
     enemy_stats_mod["Will: "], enemy_stats_mod["Con: "])
    
    atk_description(hero_name, hero_atk_stat)

    stars()
    print("             // VS //")
    stars()

    print(enemy_name) 
    print(enemy_stats_mod)

    enemy_atk_stat = atk_info(enemy_stats_mod["Pow: "], enemy_stats_mod["Int: "],
     hero_stats_mod["Will: "], hero_stats_mod["Con: "])
    
    atk_description(enemy_name, enemy_atk_stat)
    stars()

    #get units damage output
    hero_damage = atk_info(hero_stats_mod["Pow: "], hero_stats_mod["Int: "],
     enemy_stats_mod["Will: "], enemy_stats_mod["Con: "], True)

    enemy_damage = atk_info(enemy_stats_mod["Pow: "], enemy_stats_mod["Int: "],
     hero_stats_mod["Will: "], hero_stats_mod["Con: "], True)

    #estabish battle variables
    hero_health = hero_stats_mod["Vit: "]
    enemy_health = enemy_stats_mod["Vit: "]
    hero_first = 1
    enemy_dodge_count = 0 
    hero_dodge_count = 0 
    round_count = 0

    #determine which unit attacks first based on vitality stat
    if hero_stats_mod["Vit: "] > enemy_stats_mod["Vit: "]:
      hero_first = 0
      print(enemy_name + " gets the first strike!\n")
        
    else:
      hero_first = 1
      print(hero_name + " gets the first strike!\n")

    #simulates battle between unit 1 and unit 2
    var = 0
    while var == 0:
      round_count += 1
      
      if hero_first == 1:  
          battle_hit = dodge_chance(hero_stats_mod["Dex: "], enemy_stats_mod["Dex: "])
          
          if battle_hit == 1:
              enemy_health = enemy_health - hero_damage
              
              if enemy_health <= 0 or hero_health <= 0:
                  break
          else:
              enemy_dodge_count +=1 


      fight_hit = dodge_chance(enemy_stats_mod["Dex: "], hero_stats_mod["Dex: "])
      
      if fight_hit == 1:
          hero_health = hero_health - enemy_damage
          
          if enemy_health <= 0 or hero_health <= 0:
              break
      else:
          hero_dodge_count += 1

      if hero_first == 0:  
          battle_hit = dodge_chance(hero_stats_mod["Dex: "], enemy_stats_mod["Dex: "])
            
          if battle_hit == 1:
              enemy_health = enemy_health - hero_damage

              if enemy_health <= 0 or hero_health <= 0:
                  break
          else:
              enemy_dodge_count +=1 

    #prints the units damage per hit
    print(hero_name + " deals " + str(hero_damage) + " damage a hit!\n")
    
    print(enemy_name + " deals " + str(enemy_damage) + " damage a hit!\n")

    print("The battle lasted for " + str(round_count) + " rounds!\n")
    
    #prints unit 1's dodged attacks
    if hero_dodge_count >= 1:   
        if enemy_atk_stat == "Pow: ":
          print(hero_name + " dodged " + str(hero_dodge_count) + " attacks!\n")
        else:
          print(hero_name + " dodged " + str(hero_dodge_count) + " spells!\n")
    
    #prints unit 2's dodged attacks
    if enemy_dodge_count >= 1:  
        if hero_atk_stat == "Pow: ":
          print(enemy_name + " dodged " + str(enemy_dodge_count) + " attacks!\n")
        else:
          print(enemy_name + " dodged " + str(enemy_dodge_count) + " spells!\n")

    #prints the winner + remaining health
    if hero_health >= 1:
      print("The " + hero_name + " is victorious! " + str(hero_health) + " health remaining!")
    else:
      print("The " + enemy_name + " is victorious! " + str(enemy_health) + " health remaining!")
    
    stars()
           
    choice = input("ENTER 'a' TO FIGHT AGAIN: ")
    
    real_choice = str(choice).lower()

    if str(real_choice) == "fight" or str(real_choice) == "f":
      clear()
      continue
        
    else:
      clear()
      continue
