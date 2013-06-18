#!/usr/bin/python

#This file contains a rough class outline for a roguelike to be built with
#libtcod or another graphical front-end.
#Focus at the moment is on game logic, not the graphics.
#
#I have tried to focus on the main aspects but the model should evolve over 
#time. Hopefully we can mainly add additional more specialised classes. 
#Complete overhaul of the basic structure will not be easy.
#
#This file is written in python syntax and should compile, however there is no 
#sense in running it, there are too many gaps that remain to be filled :-)
#
# -Frost


########## Rough outline ##############

# Key Design Elements
#	Application links game logic to user interface
#   Game is top level for all game logic
#		consists of several levels
#	Level represents one level, each level has
#		one map
#		multiple characters
#		multiple items
#	Character is a generic class to represent moving personae
#	Item


############# Class to make constants available everywhere #################
class CONSTANTS():
	#size of the map
	MAP_WIDTH = 85
	MAP_HEIGHT = 43




############# Classes related to User interface #################
class Application():
    """
    This class represents a running instance of the application.
    It connects the game logic to the user interface
    """

############# Classes related to Game logic #################
class Game():
    """
    The game class contains the logic to run the game.
    It knows about turns
    It has pointers to all the other stuff, via the Game object you can drill 
    down to all components
    It can save and load
    It keeps track of the levels and knows which is the current level
    At the moment I don't see the need for sub classes 
    """
    
    _application = None
    @property
    def application():
        """
        The Application object that owns this game Object
        """
        return self._application
        
    #Simple array to store Level objects
    _levels =[]
    @property
    def levels(self):
        return self._levels
    @property
    def currentLevel(self):
        return self._levels
    
    #constructor
    def __init__(self, owner):
        """
        Constructor to create a new game.
        Arguments
            owner - Application object that owns this game
        """
        self._application = owner
        self.resetGame()
        
    #functions (not exhaustive)
    def resetGame(self):
        #clear existing levels
        self._levels = []
        #generate new level 
        myLevel = GeneratedLevel(self)
        self._levels.append(myLevel)
        return
    
    def loadGame(self):
        return
    
    def saveGame(self):
        return
    
class Utility():
    """
    Reusable utilities and logic go here
    At the moment I don't see the need for sub classes 
    """
    #examples
    # random number generator
    # rolling a hitdie
    # debug messages

 


##########
# LEVELS #
##########
class Level(object):
    """
    Class representing one level.
    This is the generic version containing the shared logic that is inherited 
    by the sub classes
    """
    #keep track of the game that owns this level
    _game = None
    @property
    def game(self):
        return self._game
            
    #store a link to the map object
    _map = None
    @property
    def map(self):
        return self._map
    
    #keep track of all the characters
    _characters = []
    @property
    def characters(self):
        return self._characters
    
    #keep track of all the items
    _items = []
    @property
    def items(self):
        return self._items
            
    #constructor
    def __init__(self, owner):
        """
        Constructor to create a new level.
        Arguments
            owner - Game object that owns this level
        """
        self._game = owner
        
    #functions
        
        
class GeneratedLevel(Level):
    """
    Class representing a randomly generated level
    Specialised logic to generate a random map.
    We may have different flavors (algorithms of these
    """
    #constructor
    def __init__(self, owner):
        """
        Constructor to create a new generated level.
        Arguments
            owner - Game object that owns this level
        """
        #call constructor of super class
        super(GeneratedLevel,self).__init__(owner)
        #generate the map
        self._map = Map(CONSTANTS.MAP_WIDTH,CONSTANTS.MAP_HEIGHT)

class TownLevel(Level):
    """
    Class representing a fixed town level
    Specalised class that uses a fixed map and fixed characters (for example 
    town vendors)
    """


#######
# MAP #
#######
class Map():
    """
    Describes the 2D layout of a level
    Contains logic to calculate distance, intersection, field of view, ...
    """
    _tiles = None
    @property
    def tiles(self):
        """
        Returns the tiles that make up this map.
        """
        return self._tiles
    
    @property
    def width(self):
        """
        Returns an integer indicating the width of the map
        """
        if self._tiles:
            return len(self._tiles)
        else:
            return 0
    
    @property
    def height(self):
        """
        Returns an integer indicating the height of the map
        """
        if self._tiles:
            return len(self._tiles[0])
        else:
            return 0
            
    #Every map has a Tile object which contains the entry point
    _entryTile = None
    @property
    def entryTile(self):
        """
        Returns Tile on which entry is located
        """
        return self._entryTile

    #Every map has a Tile object which contains the entry point
    _exitTile = None
    @property
    def exitTile(self):
        """
        Returns Tile on which exit is located
        """
        return self._exitTile
    
    #Constants used to generate map
    ROOM_MAX_SIZE = 10
    ROOM_MIN_SIZE = 6
    MAX_ROOMS = 30

    def __init__(self, MapWidth, MapHeight):
        """
        Constructor to create a new map
        Arguments
            MapWidth - Map width in tiles
            MapHeight - Map height in tiles
        """
        #Create a big empty map
        self._tiles = [[ Tile(map,x,y)
               for y in range(MapHeight) ]
           for x in range(MapWidth) ]
        
        #Block the entire map
        #for y in range(MapHeight):
            #for x in range(MapWidth):
                #myTile = self.tiles[x][y]
                #myTile.blocked = True
                #myTile.blockSight = True
    
class Room():
    """
    Describes a rectangular section of a map
    """
    #Frost: TODO: clean up properties and comments of this class
    
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h
 
    def center(self):
        center_x = (self.x1 + self.x2) / 2
        center_y = (self.y1 + self.y2) / 2
        return (center_x, center_y)
 
    def intersect(self, other):
        #returns true if this rectangle intersects with another one
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and
                self.y1 <= other.y2 and self.y2 >= other.y1)

#classes could be added for corridors in case we want to place stuff in corridors?

class Tile():
    """
    represents a Tile on the map
    """
        
    _x = 0
    @property
    def x(self):
        """
        Returns x coordinate of tile relevant to map
        """
        return self._x

    _y = 0
    @property
    def y(self):
        """
        Returns y coordinate of tile relevant to map
        """
        return self._y
    
    _map = None
    @property
    def map(self):
        """
        Returns the map on which this tile is located
        """
        return self._map
    
    _explored = False
    @property
    def explored(self):
        """
        Returns a boolean indicating if this tile has been explored.
        """
        return self._explored
    @explored.setter
    def explored(self, isExplored):
        self._explored = isExplored
    
    _blocked = False
    @property
    def blocked(self):
        """
        Returns a boolean indicating if this tile is blocked.
        """
        return self._blocked
    @blocked.setter
    def blocked(self, isBlocked):
        self._blocked = isBlocked
        #Blocked tiles also block line of sight
        if isBlocked == True: self._block_sight = True
        
    _block_sight = False
    @property
    def blockSight(self):
        """
        Returns a boolean indicating if this tile blocks line of sight.
        """
        return self._blocked
    @blockSight.setter
    def blockSight(self, blocksLineOfSight):
        self._blockSight = blocksLineOfSight
            
    def __init__(self, map, x, y):
        """
        Constructor to create a new tile, all tiles are created empty
        (unexplored, unblocked and not blocking line of sight)
        Arguments
            map - Map object of which this tile is a part
            x - x coordinate of the tile on the map
            y - y coordinate of the tile on the map
        """
        self._map = map
        self._x = x
        self._y = y
            
##############
# CHARACTERS #
##############
class Character(object):
    """
    Base class for characters that can move around and interact
    Should probably not be instatiated but describes the general interface of 
    a character
    Basic logic is in here, more specialised logic will be in the subclasses
    Every character has an AI that governs it
    Every character manages an inventory of items
    """

    _inventoryItems = []
    @property
    def inventoryItems(self):
        """
        Returns a list of items representing this characters inventory.
        These are the unequiped items only.
        """
        return self._inventoryItems
    
    _equipedItems = []
    @property
    def equipedItems(self):
        """
        Returns a list of items that this characters has equiped.
        These are the equiped items only.
        """
        return self._equipedItems
        
    @property
    def allItems(self):
        """
        Returns a list of all items in this characters possession.
        Includes equiped and unequiped items.
        """
        return self._inventoryItems.append(_equipedItems)
        
    _tile = None
    @property
    def tile(self):
        """
        Returns tile on which this character is located (might be None)
        """
        return self._tile
        
class Player(Character):
    """
    Sub class representing a player
    """

class NPC(Character):
    """
    Sub class representing a NPC, for example a vendor
    Probably we'll need to override some inventory concepts
    """

class Monster(Character):
    """
    Sub class representing a monster
    Later we can consider more specialised subclasses 
    for example Humanoid, Undead, Animal
    """

#########
# ITEMS #
#########
class Item(object):
    """
    Base class for items
    Should probably not be instatiated but describes the general interface of 
    an item
    """


class Equipment(Item):
    """
    Sub class for equipment = items that can be equiped
    Might need more subclasses for weapons versus armor
    """

class Consumable(Item):
    """
    Sub class for items that can be used.
    Not sure we might want a different class for scrolls and potions
    """

class QuestItem(Item):
    """
    Sub class for quest items
    Probably don't need this in the beginning but it would fit in here :)
    """


######
# AI #
######
class AI(object):
    """
    Base class for AI logic
    Methods are empty, to be implemented by subclasses
    """
    
    def take_turn(self):
        """
        Take one turn
        """
        return

class PlayerAI(AI):
    """
    AI sub class that provides player control over characters
    """

class BasicMonsterAI(AI):
    """
    AI sub class that provides AI implementation for basic monsters.
    """
     #AI for a basic monster.
    def take_turn(self):
        #a basic monster takes its turn. if you can see it, it can see you
        monster = self.owner
        if libtcod.map_is_in_fov(fov_map, monster.x, monster.y):
 
            #move towards player if far away
            if monster.distance_to(player) >= 2:
                monster.move_towards(player.x, player.y)
 
            #close enough, attack! (if the player is still alive.)
            elif player.fighter.hp > 0:
                monster.fighter.attack(player)

class ConfusedMonsterAI(AI):
    """
    AI sub class that provides AI implementation for confused monsters.
    """

#Questions
#   which class is responsible to calculate field of view? Map or Level? Answer the class that has enough information to do it. Should be Map I guess.



if __name__ == '__main__':
    print("There is not much sense in running this file.")
