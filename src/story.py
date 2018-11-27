import curses

def read_input(window):
    return window.getch()

class StoryScreen:
    def __init__(self, screen):
        self.screen = screen                                         # hold current screen
        self.pressed_key = ord('z')                                  # hold the pressed key in the menu
        
    #Print the Story-Screen to given screen.
    def print(self): 
        self.screen.clear() 
        screen_size = self.screen.getmaxyx()
        story_win = curses.newwin(screen_size[0], screen_size[1], 0, 0)
        story_win.addstr(1, 1, "Story 1")
    
        story = curses.newwin(int(screen_size[0] * 0.66),
                        int(screen_size[1] - 5), 2, 3)
        story.border()
        story_size = story.getmaxyx()
        story.addstr(int(1), int(1), "Lorem ipsum dolor sit amet, consetetur sadipscing elitr") 
    
        #story_win.addstr(map_size[0] + 2, map_size[1] - 10, "Weiter (w)") 
    
        story_win.refresh()
        story.refresh()
    
        self.pressed_key = read_input(story_win)
    
    
# init screen
screen = curses.initscr()   
s_screen = StoryScreen(screen)	    
    
    
while s_screen.pressed_key != ord('q'):								 # check pressed key in test_menu
    s_screen.print()
    
curses.endwin()
    