import random

print('Welcome to Adventure')

char_name = input("Please input your character's name: ")

class_selected = False

while not class_selected:
    print('Please select a class:')
    print('1 - Warrior')
    print('2 - Archer')

    selection = input()

    if selection == '1':
        char_level = 1
        char_class = 'Warrior'
        attack = 3
        defense = 2
        hp = 12
        max_hp = 12
        weapon = 'Sword'
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
        gold = 10
        class_selected = True
    else:
        print('Please enter 1 or 2.')

print('Introducing {}, the brave {}!!'.format(char_name, char_class))

game_over = False
game_won = False


items_for_sale = ['Big Sword', 'Big Bow', 'The best weapon in the game']
items_prices = [30, 40, 100]


def visit_shop():
    print('Shopkeeper: "Welcome to my shop."')
    print('''Shopkeeper: "Here's what we have for sale..."''')

    done_shopping = False

    while not done_shopping:
        for i in range(len(items_for_sale)):
            print('1 - {} : {} Gold'.format(i+1, items_for_sale[i], items_prices[i]))

        print('Shopkepper: "What looks good to you?"')
        print('Type "0" to leave the shop.')

        selection = input()

        if selection == '1':
            print('Buy the {}'.format(selection))
        elif selection == '0':
            done_shopping = True
        else:
            print('Please select a valid choice.')

        print('Shopkepper: "Thank you, come again!"')


def display_stats():
    print('Current Stats:')
    print('{} - Level {} {}'.format(char_name, char_level, char_class))
    print('HP:      {}/{}'.format(hp, max_hp))
    print('Attack:  {}'.format(attack))
    print('Defense: {}'.format(defense))
    print('Weapon:  {}'.format(weapon))
    print('Gold:    {}'.format(gold))


def battle(monster, monster_hp, monster_attack, monster_defense):
    print('You approach the {} and start fighting'.format(monster))

    hero_died = False
    monster_died = False
    ran_away = False

    global hp

    while not (hero_died or monster_died or ran_away):
        print('{}: {} HP  -- {}: {} HP'.format(char_name, hp, monster, monster_hp))

        valid_selection = False
        while not valid_selection:
            print('What do you do?')
            print('1 - Light attack')
            print('2 - Heavy attack')
            print('3 - Run away')

            selection = input()

            number = random.randint(1, 10)

            if selection == '1':
                valid_selection = True
                print('You try a light attack.')
                
                damage = attack

                miss = False
                critical = False

                if number == 1:
                    miss = True
                elif number == 2:
                    critical = True

            elif selection == '2':
                valid_selection = True
                print('You try a heavy attack.')

                damage = 2 * attack

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

            print('You did {} damage to the {}.'.format(damage, monster))
            monster_hp = monster_hp - damage 

            if monster_hp <= 0:
                print('You slayed the {}!'.format(monster))
                monster_died = True
            else:
                print('The monster attacks you.')

                number = random.randint(1, 10)

                if number < 2:
                    print('You gracefully dodge the attack')
                else:
                    damage = monster_attack - defense

                    if damage < 0:
                        damage = 0

                    print('The monster does {} damage!!!'.format(damage))
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
        print('You see some monsters who want to fight')
        print('1 - Giant Rat')
        print('2 - Troll')
        print('3 - Wondering Bandit')
        print('4 - Dragon')
        print('5 - Head back to town')

        selection = input()
        
        if selection == '1':
            monster_selected = True
            battle(monster = 'Giant Rat', monster_hp = 5, monster_attack = 2, monster_defense = 1)
        elif selection == '2':
            monster_selected = True
            battle(monster = 'Troll', monster_hp = 5, monster_attack = 2, monster_defense = 1)
        elif selection == '3':
            monster_selected = True
            battle(monster = 'Wondering Bandit', monster_hp = 5, monster_attack = 2, monster_defense = 1)
        elif selection == '4':
            monster_selected = True
            battle(monster = 'Dragon', monster_hp = 5, monster_attack = 2, monster_defense = 1)
        elif selection == '5':
            ran_away = True
        else:
            print('Please select 1, 2, 3, 4 or 5')

    if ran_away:
        print('You decide not to fight right now')


def visit_town():
    print('Welcome to the local town.')

    done_in_town = False

    while not done_in_town:
        print('What would you like to do in town?')
        print('1 - Visit the shop')
        print('2 - Visit the inn')
        print('3 - Talk to someone')
        print('4 - Leave town')

        selection = input()

        if selection == '1':
            print('The shop')
        elif selection == '2':
            print('The inn')
        elif selection == '3':
            print('Talk to someone')
        elif selection == 4:
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
    print('Congradulations {}, you are a true hero of the people!')
else:
    print('Thanks for playing!')
