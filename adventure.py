import random

print('Welcome to Adventure')

char_name = input("Please input your character's name: ")

class_selected = False

while not class_selected:
    print('Please select a class:')
    print('1 - Warrior')
    print('2 - Archer')

    selection = input()
    print()

    if selection == '1':
        char_level = 1
        char_class = 'Warrior'
        attack = 3
        defense = 2
        hp = 12
        max_hp = 12
        weapon = 'Sword'
        weapon_bonus = 0
        gold = 10
        class_selected = True
    elif selection == '2':
        char_level = 1
        char_class = 'Archer'
        attack = 5
        defense = 1
        hp = 10
        max_hp = 10
        weapon = 'Bow'
        weapon_bonus = 0
        gold = 10
        class_selected = True
    elif selection == '3':
        print('SECRET UNLOCKED')
        char_level = 1
        char_class = 'Ninja Turtle'
        attack = 20
        defense = 20
        hp = 45
        max_hp = 45
        weapon = 'Fists'
        weapon_bonus = 0
        gold = 0
        class_selected = True
    else:
        print('Please enter 1 or 2.')

print('Introducing {}, the brave {}!!'.format(char_name, char_class))

game_over = False
game_won = False


def visit_shop():
    print('Shopkeeper: "Welcome to my shop."')
    print('''Shopkeeper: "Here's what we have for sale..."''')

    done_shopping = False
    global gold

    while not done_shopping:
        print('Shopkepper: "What looks good to you?"')
        print('1 - Big Sword - 30 Gold')
        print('2 - Big Bow - 35 Gold')
        print('3 - Best Weapon in the Game - 100 gold')
        print('4 - Leave the shop')
        print('You have {} gold.'.format(gold))

        selection = input()
        print()

        if selection == '1':
            if char_class == 'Warrior':
                if gold >= 30:
                    print('I see you have an eye for quality')
                    print('Enjoy your new Big Sword!')
                    gold = gold - 30
                    weapon = 'Big Sword'
                    weapon_bonus = 7
                else:
                    print('Sorry {}, you need more gold for that.'.format(char_class))
            else:
                print("{}s can't use that. It's for warriors only.".format(char_class))

        if selection == '2':
            if char_class == 'Archer':
                if gold >= 35:
                    print('I see you have an eye for quality')
                    print('Enjoy your new Big Bow!')
                    gold = gold - 35
                    weapon = 'Big Bow'
                    weapon_bonus = 10

                else:
                    print('Sorry {}, you need more gold for that.'.format(char_class))
            else:
                print("{}s can't use that. It's for archers only.".format(char_class))

        if selection == '3':
            if gold >= 100:
                print('With this weapon... nothing can stop you. Your destiny awaits...')
                gold = gold - 100
                weapon = 'Best Weapon in the Game'
                weapon_bonus = 20

            else:
                print('Sorry {}, you need more gold for that.'.format(char_class))

        elif selection == '4':
            done_shopping = True
        else:
            print('Please select 1, 2, 3, or 4.')

        print('Shopkepper: "Thank you, come again!"')


def display_stats():
    print('Current Stats:')
    print('{} - Level {} {}'.format(char_name, char_level, char_class))
    print('HP:      {}/{}'.format(hp, max_hp))
    print('Attack:  {}'.format(attack))
    print('Defense: {}'.format(defense))
    print('Weapon:  {}'.format(weapon))
    print('Gold:    {}'.format(gold))


def battle(monster, monster_hp, monster_attack, monster_defense, monster_level):
    print('You approach the {} and start fighting'.format(monster))

    hero_died = False
    monster_died = False
    ran_away = False

    global hp
    global max_hp
    global attack
    global defense
    global weapon_bonus
    global weapon
    global game_over
    global char_level
    global gold
    global game_won

    while not (hero_died or monster_died or ran_away):
        print('{}: {} HP  -- {}: {} HP'.format(char_name, hp, monster, monster_hp))

        valid_selection = False
        while not valid_selection:
            print('What do you do?')
            print('1 - Light attack')
            print('2 - Heavy attack')
            print('3 - Run away')

            selection = input()
            print()

            number = random.randint(1, 10)

            miss = False
            critical = False

            if selection == '1':
                valid_selection = True
                print('You try a light attack.')

                damage = attack + weapon_bonus


                if number == 1:
                    miss = True
                elif number == 2:
                    critical = True

            elif selection == '2':
                valid_selection = True
                print('You try a heavy attack.')

                damage = 2 * attack + weapon_bonus

                if number < 5:
                    miss = True
                elif number > 7:
                    critical = True

            elif selection == '3':
                valid_selection = True
                print('You try to run away.')

                if number < 8:
                    print('You run away like the coward you are, disgracing all other {}s throughout history.'.format(char_class))
                    ran_away = True
                else:
                    print("You couldn't run!")

            else:
                print('Please select 1, 2, or 3')


        if not ran_away:
            if miss:
                print('Oh no, your attack missed!')
                damage = 0
            if critical:
                print('CRITICAL HIT!')
                damage = damage * 2

            damage = damage - monster_defense

            if damage < 0:
                damage = 0

            print('You used your {} and did {} damage to the {}.'.format(weapon, damage, monster))
            monster_hp = monster_hp - damage

            if monster_hp <= 0:
                print('You slayed the {}!'.format(monster))

                gold_drop = random.randint(8, 15)

                print('You got {} gold.'.format(gold_drop))

                char_level = char_level + monster_level

                max_hp = max_hp + 2 * monster_level
                hp = max_hp
                attack = attack + 3 * monster_level
                defense = defense + monster_level

                gold = gold + gold_drop

                display_stats()

                monster_died = True

                if monster == 'Kodban':
                    game_won = True
            else:
                print('The {} attacks you.'.format(monster))

                number = random.randint(1, 10)

                if number < 2:
                    print('You gracefully dodge the attack')
                else:
                    damage = monster_attack - defense

                    if damage < 0:
                        damage = 0

                    print('The {} does {} damage!!!'.format(monster, damage))
                    hp = hp - damage

                if hp <= 0:
                    print('You died!!!')
                    game_over = True
                    hero_died = True


def fight_monster():
    print('You head out looking for trouble.')

    monster_selected = False
    ran_away = False

    while not (monster_selected or ran_away):
        print('You see some monsters who want to fight.')
        print('(Order is easiest to hardest.)')
        print('1 - Giant Rat')
        print('2 - Troll')
        print('3 - Wondering Bandit')
        print('4 - Dragon')
        print('6 - ??????')
        print('6 - Head back to town')

        selection = input()
        print()

        if selection == '1':
            monster_selected = True
            battle(monster = 'Giant Rat', monster_hp = 5, monster_attack = 5, monster_defense = 1, monster_level = 1)
        elif selection == '2':
            monster_selected = True
            battle(monster = 'Troll', monster_hp = 15, monster_attack = 8, monster_defense = 3, monster_level = 2)
        elif selection == '3':
            monster_selected = True
            battle(monster = 'Wondering Bandit', monster_hp = 35, monster_attack = 15, monster_defense = 10, monster_level = 3)
        elif selection == '4':
            monster_selected = True
            battle(monster = 'Dragon', monster_hp = 50, monster_attack = 23, monster_defense = 18, monster_level = 7)
        elif selection == '5':
            monster_selected = True
            battle(monster = 'Kodban', monster_hp = 500, monster_attack = 100, monster_defense = 100, monster_level = 100)
        elif selection == '6':
            ran_away = True
        else:
            print('Please select 1, 2, 3, 4 , 5 or 6')

    if ran_away:
        print('You decide not to fight right now')


def visit_inn():
    print('You saunter into the local inn.')
    print('''Inn Keeper: "Welcome to my inn. It's 5g a night."''')

    global gold

    valid_choice = False
    while not valid_choice:
        print('Inn Keeper: "Care to stay for the night?"')
        print('(Staying at the inn heals all your hp)')
        print('1 - Stay')
        print('2 - Leave')
        stay = input()
        print()

        if stay == '1':
            valid_choice = True
            if gold >= 5:
                print('Enjoy your stay!')
                gold = gold - 5
                hp = max_hp
                print('...')
                print('You wake up feeling totally refreshed!')
            else:
                print('You need more gold.')
        elif stay == '2':
            valid_choice = True
            print('Inn Keeper: "Stay safe out there {}!"'.format(char_class))
        else:
            print('Please select 1 or 2')


def visit_town():
    print('Welcome to the local town.')

    done_in_town = False

    while not (done_in_town or game_over):
        print('What would you like to do in town?')
        print('1 - Visit the shop')
        print('2 - Visit the inn')
        print('3 - Talk to someone')
        print('4 - Leave town')

        selection = input()
        print()

        if selection == '1':
            visit_shop()
        elif selection == '2':
            visit_inn()
        elif selection == '3':
            print('You walk up to a local townsperson.')
            print('Townsperson: "To win the game, kill the final monster."')
        elif selection == '4':
            done_in_town = True
        else:
            print('Please enter 1, 2, 3, or 4.')

    print('You decided to leave the town')


while not (game_over or game_won):
    print('What will you do next, {}?'.format(char_name))
    print('1 - Display stats')
    print('2 - Fight a monster')
    print('3 - Visit town')
    print('4 - End game')

    selection = input()
    print()

    if selection == '1':
        display_stats()
    elif selection == '2':
        fight_monster()
    elif selection == '3':
        visit_town()
    elif selection == '4':
        game_over = True
    else:
        print('Please enter 1, 2, 3, or 4.')

if game_over:
    print('GAME OVER')

if game_won:
    print('Congradulations {}, you have slain the monsters! You are a true hero of the people!'.format(char_name))
else:
    print('Thanks for playing!')
