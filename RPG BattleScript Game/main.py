from Games.game import person, bcolors
from Games.magic import spell


fire = spell("Fire", 10, 100, "Black")
thunder = spell("Thunder", 10, 100, "Black")
blizzard = spell("Blizzard", 10, 100, "Black")
meteor = spell("Meteor", 10, 100, "Black")
quake = spell("Quake", 10, 100, "Black")

cure = spell("Cure", 20, 100, "White")
cura = spell("Cura", 22, 120, "White")


player= person(460, 65, 60, 34, [fire, thunder, blizzard, meteor, quake, cure, cura])
enemy= person(1200, 65, 45, 25, [])

running = True
i=0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACK!" + bcolors.ENDC)

while running:
        print("========================")
        player.choose_actions()
        choice = input("Choose Action:")
        index = int(choice)-1

        if index == 0:
                dmg = player.generate_damage()
                enemy.take_damage(dmg)
                print("You attacked for", dmg, "points of damage.")

        elif index == 1:
                player.choose_magic()
                magic_choice = int(input("Choose Magic:")) - 1

                spell = player.magic[magic_choice]
                magic_damage = spell.generate_spell_damage()

                current_mp = player.get_mp()

                if spell.cost > current_mp:
                        print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                        continue
                player.reduce_mp(spell.cost)

                if spell.type == "White":
                        player.heal(magic_damage)
                        print(bcolors.OKBLUE + "\n" + spell.name + "heals for", str(magic_damage), "HP." + bcolors.ENDC)

                elif spell.type == "Black":
                        enemy.take_damage(magic_damage)
                        print(bcolors.OKBLUE + "\n" + spell.name + "deals", str(magic_damage), "points of damage" + bcolors.ENDC)



        enemy_choice = 1

        enemy_dmg = enemy.generate_damage()
        player.take_damage(enemy_dmg)
        print("Enemy attacks for", enemy_dmg)

        print("--------------------------")
        print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
        print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC + "\n")
        print("Your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")

        if enemy.get_hp() == 0:
                print(bcolors.OKGREEN + "You Win!" + bcolors.ENDC)
                running = False
        elif player.get_hp() == 0:
                print(bcolors.FAIL + "You Lose!" + bcolors.ENDC)
                running = False

1