print('Welcome to Adventure')

char_name = input("Please input your character's name: ")

class_selected = False

while not class_selected:
    print('Please select a class:')
    print('1 - Warrior')
    print('2 - Archer')

    selection = input()

    if selection == '1':
        char_class = 'Warrior'
        attack = 3
        defense = 7
        hp = 12
        max_hp = 12
        weapon = 'Sword'
        gold = 10
        class_selected = True
    elif selection == '2':
        char_class = 'Archer'
        attack = 5
        defense = 4
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

def display_stats():
    print('Current Stats:')
    print('{} the {}'.format(char_name, char_class))
    print('HP:      {}/{}'.format(hp, max_hp))
    print('Attack:  {}'.format(attack))
    print('Defense: {}'.format(defense))
    print('Weapon:  {}'.format(weapon))
    print('Gold:    {}'.format(gold))


def fight_monster():
    print('Fight monster')


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
        elif selecton == '2':
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
