#!/usr/bin/python

# This file contains a test implementation of the application class.
# It allows me to test some basic functionalities.
# I have selected to use libtcod as example code for this library was readily
# available in our first project.

import libtcodpy as libtcod
from class_structure import Game, CONSTANTS

#actual size of the window
SCREEN_WIDTH = 85 
SCREEN_HEIGHT = 50
 
LIMIT_FPS = 20  #20 frames-per-second maximum
PANEL_HEIGHT = 7

class Application():
    """
    This class represents a running instance of the application.
    It connects the game logic to the user interface
    """
    
    _game = None
    @property
    def game(self):
        """
        The game object used by this application
        """
        return self._game
    
    def __init__(self):
        self.initializeLibtcod()
        
        """
        img = libtcod.image_load('./media/menu_background.png')
 
        while not libtcod.console_is_window_closed():
            #show the background image, at twice the regular console resolution
            libtcod.image_blit_2x(img, 0, 0, 0)
     
            #show the game's title, and some credits!
            libtcod.console_set_default_foreground(0, libtcod.light_yellow)
            libtcod.console_print_ex(0, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-4, libtcod.BKGND_NONE, libtcod.CENTER,
                                     'Journey through the Underdeep')
            libtcod.console_print_ex(0, SCREEN_WIDTH/2, SCREEN_HEIGHT-2, libtcod.BKGND_NONE, libtcod.CENTER, 
            'By The #! Python Group')
            
            #show options and wait for the player's choice
            choice = menu('', ['Play a new game', 'Continue last game', 'Quit'], 24)
     
            if choice == 0:  #new game
                #new_game()
                #play_game()
                race_menu()
            if choice == 1:  #load last game
                try:
                    load_game()
                except:
                    msgbox('\n No saved game to load.\n', 24)
                    continue
                play_game()
            elif choice == 2:  #quit
                break
        """

    def initializeLibtcod(self):
        libtcod.console_set_custom_font('./media/arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
        libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Crunchbang Project', False)
        libtcod.sys_set_fps(LIMIT_FPS)
        con = libtcod.console_new(CONSTANTS.MAP_WIDTH, CONSTANTS.MAP_HEIGHT)
        panel = libtcod.console_new(SCREEN_WIDTH, PANEL_HEIGHT)

    def newGame(self):
        self._game = Game(self)
        
        """
        global player, inventory, game_msgs, game_state, dungeon_level
        global killerrabbit_death , wearing_amulet, monster_population
        
        #Frost# Need to get rid of this later
        global killerrabbit_death
        killerrabbit_death = False
        wearing_amulet = False
        
        #Create new MonsterPopulation that will be used in this game
        monster_population = MonsterPopulation(config)

     
        #create object representing the player
        if race == 'Dwarf':
            fighter_component = Fighter(hp=120, defense=1, power=2, xp=0, death_function=player_death)
        elif race == 'Elf':
            fighter_component = Fighter(hp=100, defense=2, power=2, xp=0, death_function=player_death)
        elif race == 'Human':
            fighter_component = Fighter(hp=100, defense=1, power=3, xp=0, death_function=player_death)
    
        player = Object(0, 0, '@', 'player', libtcod.white, blocks=True, fighter=fighter_component)
     
        player.level = 1
     
        #generate map (at this point it's not drawn to the screen)
        dungeon_level = 1
        
        make_map()
        initialize_fov()
     
        game_state = 'playing'
        inventory = []
     
        #create the list of game messages and their colors, starts empty
        game_msgs = []
     
        #a warm welcoming message!
        message('The UNDERDEEP greets you with a cold breeze that smells of evil. (Press "?" for HELP)', libtcod.red)
    
        #initial equipment: a dagger
        equipment_component = Equipment(slot='right hand', power_bonus=2)
        obj = Object(0, 0, '-', 'dagger', libtcod.sky, equipment=equipment_component)
        inventory.append(obj)
        equipment_component.equip()
        obj.always_visible = True
        """
                    
    def playGame(self):
        mouse = libtcod.Mouse()
        key = libtcod.Key()
        #main loop
        while not libtcod.console_is_window_closed():
            libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)
        
        """
        global key, mouse
     
        player_action = None
     
        mouse = libtcod.Mouse()
        key = libtcod.Key()
        #main loop
        while not libtcod.console_is_window_closed():
            libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)
            #render the screen
            render_all()
     
            libtcod.console_flush()
     
            #level up if needed
            check_level_up()
           
            #erase all objects at their old locations, before they move
            for object in objects:
                object.clear()
     
            #handle keys and exit game if needed
            player_action = handle_keys()
            if player_action == 'exit':
                save_game()
                break
     
            #let monsters take their turn
            if game_state == 'playing' and player_action != 'didnt-take-turn':
                for object in objects:
                    if object.ai:
                        object.ai.take_turn()
        """
#Test code
if __name__ == '__main__':
    myApplication = Application()
    myApplication.newGame()
    print myApplication.game.levels[0].map.width
    print myApplication.game.levels[0].map.height
    myApplication.playGame()
    
    


