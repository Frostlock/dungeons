Class design
============
This document attempts to explain the high level class structure of this project. I strongly recommend to first read through this doc before digging into the code. It should help you understand the general layout
of the project much faster.

Not every class is mentioned in this document, only the most important ones.In the class definitions you will also find additional comments that explain each class in more detail.

Main classes
------------
These are the main classes:
* <b>Application</b> is the class that gets "started", it links game logic to user interface.
* <b>Game</b> is the top level class for all game logic, once initialized it will have multiple levels.
* <b>Level</b> represents one level of the game, each level has at least
   * one <b>Map</b> object
   * multiple <b>Character</b> objects
   * multiple <b>Item</b> objects
Note that <b>Level</b>, <b>Character</b> and <b>Item</b> are generic classes, they define generic interfaces to allow easy polymorphism of their subclasses. Ideally we only use these generic classes in our code. That way we write code that works for future specialized sub classes as well.
The following specialised sub classes are there at the moment, we can of course add more.

* Level
   * GeneratedLevel
   * TownLevel
* Character
   * Player
   * NPC
   * Monster
* Item
   * Equipment
   * Consumable
   * QuestItem    

Supporting classes
------------------
<b>Libraries</b><br>
   To avoid hardcoding monster and item data in the code I would propose
   to externalize this data. Using a Library class to access it.

<b>AI</b><br>
I'm not entirely sure yet on how to implement AI, I propose to start with something basic. We can add more specialised AIs to this structure.
    AI (generic class to be used for polymorphism)
        BasicMonsterAI
        ConfusedMonsterAI
        PlayerAI
        
   You will notice some other more specialised classes below as well.

