'''
A text adventure game where a player can move between Rooms and pick up
and use items.



Classes:
--------

Item: an item that can be pickup and used in a game.

Room: A location within the game that has a description and exits to other
      Rooms

TextWorld: The main game class.  A player can take actions within a game 

'''

class InventoryItem:
    '''
    An item found in a text adventure world that can be picked up
    or dropped.
    '''
    def __init__(self, short_description):
        self.name = short_description
        self.long_description = ''
        self.aliases = []


    def add_alias(self, new_alias):
        '''
        Add an alias (alternative name) to the InventoryItem.
        For example if an inventory item has the short description
        'credit card' then a useful alias is 'card'.

        Parameters:
        -----------
        new_alias: str
            The alias to add.  For example, 'card'

        '''
        self.aliases.append(new_alias)


class InventoryHolder:
    '''
    Encapsulates the logic for adding and removing an InventoryItem
    This simulates "picking up" and "dropping" items in a TextWorld 
    '''
    def __init__(self):
        #inventory just held in a list interally
        self.inventory = []

    def list_inventory(self):
        '''
        Return a string representation of InventoryItems held.
        '''
        msg = ''
        for item in self.inventory:
            msg += f'{item.name}\n'

        return msg

    def add_inventory(self, item):
        '''
        Add an InventoryItem
        '''
        self.inventory.append(item)

    def get_inventory(self, item_name):
        '''
        Returns an InventoryItem from Room.
        Removes the item from the Room's inventory

        Params:
        ------
        item_name: str
            Key identifying item.

        Returns
        -------
        InventoryItem

        Raises:
        ------
        KeyError
            Raised when an InventoryItem without a matching alias.
        '''
        selected_item, selected_index = self.find_inventory(item_name)
         
        #remove at index and return
        del self.inventory[selected_index]
        return selected_item

    def find_inventory(self, item_name):
        '''
        Find an inventory item and return it and its index 
        in the collection.
        '''
        selected_item = None
        selected_index = -1
        for index, item in zip(range(len(self.inventory)), self.inventory):
            if item_name in item.aliases:
                selected_item = item
                selected_index = index
                break
    
        if selected_item == None:
            raise KeyError('You cannot do that.')  

        return selected_item, selected_index

    
class Room(InventoryHolder):
    '''
    Encapsulates a location/room within a TextWorld.

    A `Room` has a number of exits to other `Room` objects

    A `Room` is-a type of `InventoryHolder`
    '''
    def __init__(self, name):
        self.name = name
        self.description = ""
        self.exits = {}

        super().__init__()

    def __repr__(self):
        '''
        String representation of the class 
        '''
        desc = f"Room(name='{self.name}'"
        desc += f", description='{self.description[:20]}'"
        desc += f', n_exits={len(self.exits)}'
        desc += f', n_items={len(self.inventory)})'
        return desc
                

    def add_exit(self, room, direction):
        '''
        Add an exit to the room

        Params:
        ------
        room: Room
            a Room object to link 

        direction: str
            The str command to access the room
        '''
        self.exits[direction] = room

    
    def exit(self, direction):
        '''
        Exit the room in the specified direction

        Params:
        ------
        direction: str
            A command string representing the direction.
        '''
        if direction in self.exits:
            return self.exits[direction]
        else:
            raise ValueError()

    def describe(self):
        msg = self.description
        if len(self.inventory) > 0:
            msg += '\nYou can also see:\n'
            msg += self.list_inventory()
        return msg

       
class TextWorld(InventoryHolder):
    '''
    A TextWorld encapsulate the logic and Room objects that comprise the game.

    A `Room` is-a type of `InventoryHolder` although in practice you may
    want to seperate out this logic into a `Player` class.
    '''
    def __init__(self, name, rooms, start_index=0):
        '''
        Constructor method for World

        Parameters:
        ----------
        name: str
            Game name

        rooms: list
            A list of rooms in the world.

        start_index: int, optional (default=0)
            The index of the room where the player begins their adventure.

        '''
        super().__init__()
        self.name = name
        self.rooms = rooms
        self.current_room = self.rooms[start_index]
        self.legal_exits = ['n', 'e', 's', 'w']
        self.legal_commands =['look', 'inv', 'get', 'drop', 'ex', 'quit']
        #aliaises for the use 
        self.use_aliases = []
        self.n_actions = 0
        
        #true while the game is active.
        self.active = True

    
    def __repr__(self):
        '''
        String representation of the class 
        '''
        desc = f"TextWorld(name='{self.name}', "
        desc += f'n_rooms={len(self.rooms)}, '
        desc += f'legal_exits={self.legal_exits},\n'
        desc += f'\tlegal_commands={self.legal_commands},\n'
        desc += f'\tcurrent_room={self.current_room})'
        return desc 


    def add_use_command_alias(self, alias):
        '''
        Add use alias.
        '''
        self.use_aliases.append(alias)

    def take_action(self, command):
        '''
        Take an action in the TextWorld

        Parameters:
        -----------
        command: str
            A command to parse and execute as a game action

        Returns:
        --------
        str: a string message to display to the player.
        '''

        #no. of actions taken
        self.n_actions += 1

        #handle action to move room
        if command in self.legal_exits:
            msg = ''
            try:
                self.current_room = self.current_room.exit(command)
                msg = self.current_room.describe()
            except ValueError:
                msg = 'You cannot go that way.'
            finally:
                return msg

        #split into array
        parsed_command = command.split()
        parsed_command[0] == parsed_command[0].lower()
        
        if parsed_command[0] in self.legal_commands:
            #handle command
            if parsed_command[0] == 'look':
                return self.current_room.describe()
            elif parsed_command[0] == 'get':
                try:
                    item = self.current_room.get_inventory(parsed_command[1])
                    self.add_inventory(item)
                    return f'okay.'
                except KeyError:
                    return f"You cannot do that here."
            elif parsed_command[0] == 'drop':
                try:
                    item = self.get_inventory(parsed_command[1])
                    self.current_room.add_inventory(item)
                    return f'okay.'
                except KeyError:
                    return f"You cannot do that here."
            elif parsed_command[0] == 'inv':
                msg = self.list_inventory()
                return msg
            elif parsed_command[0] == 'ex':
                item, _ = self.find_inventory(parsed_command[1])
                return item.long_description
            elif parsed_command[0] == 'quit':
                self.active = False
                return 'You have quit the game.'
            
        else:
            #handle command error
            return f"I don't know how to {command}"

    
def hospital_with_inventory():
    # Let's instantiate some Room objects to represent our network of rooms

    #start fo the game = reception
    reception = Room(name="reception")
    reception.description = """You are stood in the busy hospital reception.
    To the south, east and west are wards with COVID19 restricted areas. 
    To the north is a corridor."""

    corridor = Room(name='corridor')
    corridor.description = """A long corridor branching in three directions. 
    To the north is signposted 'WARD'.  
    The south is  signposted 'RECEPTION'.
    The east is signposted 'THEATRE'"""

    ward = Room(name="ward")
    ward.description = """You are on the general medical ward. There are 10 beds
    and all seem to be full today.  There is a smell of disinfectant. 
    The exit is to the south"""

    theatre = Room(name="theatre")
    theatre.description = """You are in the operating theatre. Its empty today as
    all of the elective operations have been cancelled.
    An exit is to the west."""

    #add the exits by calling the add_exit() method  
    reception.add_exit(corridor, 'n')
    corridor.add_exit(reception, 's')
    corridor.add_exit(ward, 'n')
    corridor.add_exit(theatre, 'e')
    ward.add_exit(corridor, 's')
    theatre.add_exit(corridor, 'w')

    rooms_collection = [reception, corridor, ward, theatre]
    
    #add inventory items
    clipboard = InventoryItem('a medical clipboard')
    clipboard.long_description = """It a medical clipboard from the 1980s. 
    It doesn't seem very secure to leave this hanging around."""
    clipboard.add_alias('clipboard')
    clipboard.add_alias('clip')
    clipboard.add_alias('board')
    
    grapes = InventoryItem('a bunch of grapes')
    grapes.long_description = """A bunch of juicy green grapes. 
    From Lidl according to the sticker """
    grapes.add_alias('grapes')
    grapes.add_alias('bunch')
    
    ward.add_inventory(grapes)
    reception.add_inventory(clipboard)
    
    #create the game room
    adventure = TextWorld(name='text hospital world', rooms=rooms_collection, 
                          start_index=0)

    #set the legal commands for the game
    #directions a player can move and command they can issue.

    adventure.opening = """Welcome to your local hospital! Unfortunatly due to the 
    pandemic most of the hospital is under restrictions today. But there are a few
    areas where it is safe to visit.
    """
    
    return adventure

        





    

    

