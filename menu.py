def menu(menu_items):
    
    while True:
        for index, item in enumerate(menu_items):
            print('{} - {}'.format(index + 1, item))

        choice = input()
        print()

        if choice in [str(index + 1) for index in range(len(menu_items))]:
            return menu_items[int(choice) - 1]          

        print('Please try again')

