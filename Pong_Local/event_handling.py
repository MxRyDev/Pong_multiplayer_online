# Defines the custom library to aide with event handling in pygame.

import pygame

if __name__ == '__main__':
    print('''
    This file is used to define a library that aides with 
    event handling in pygame.  It includes two classes.
    
    This ".
    on its own, it provides no functionality.
    
    HAFF A GUD DAY
    ''')



def ignore():
    pass


# EVENT_EXE class
'''
Each object needs to be passed a pygame event and 
two fucntions or "actions" upon creation.
The first will occur when the pygame event is a KEYDOWN
and the second will respond to KEYUP.

... at least that's the dream.

'''


class Event_exe():
    def __init__(self, event, press_action, release_action, actions_list):
        self.event = event
        self.press_action = press_action
        self.release_action = release_action
        actions_list.append(self)
    
    def pressed(self):
        self.press_action
        print('pressed')
    def released(self):
        self.release_action
        print('released')
    
    
class Event_conductor():
    def __init__(self, actions_list):
        self.actions_list = actions_list
        
    def handle_events(self, events_list):
        for event in events_list:
            for action in self.actions_list:
                # if the event is keyup or keydown...
                if event.type in [pygame.KEYDOWN, pygame.KEYUP]:
                    print('we have a key press')
                    # and if it is a keypress we are looking for...
                    if event.key == action.event:
                        print('we have a keypress we were looking for')
                        if event.type == pygame.KEYDOWN:
                            print('triggering...')
                            action.pressed()
                        elif event.type == pygame.KEYUP:
                            print('triggering')
                            action.released()
                                