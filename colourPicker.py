import pandas as pd
import pygame
def Change_Rating(colour_temp_one, colour_temp_two):
	Ra = colour_temp_one["rating"]
	Rb = colour_temp_two["rating"]
	Sa = 1
	Sb = 0
	K = 32

	Ea = 1/(1+10**((Rb-Ra)/400))
	Eb = 1/(1+10**((Ra-Rb)/400))

	
	
	colour_temp_one["rating"] = Ra+K*(Sa-Ea)
	colour_temp_two["rating"] = Rb+K*(Sb-Eb)
	print(colours.index[colours["colour_name"] == colour_temp_one["colour_name"]].tolist())
	colours.iloc[colours.index[colours["colour_name"] == colour_temp_one["colour_name"]].tolist()] = colour_temp_one
	colours.iloc[colours.index[colours["colour_name"] == colour_temp_two["colour_name"]].tolist()] = colour_temp_two
	
	colours.sort_values(by=["rating"], ascending=False).to_excel("colours.xlsx", index=False)
	
def pick_random_colours(colours):
	#output 2 random colours
	two_random_colours = colours.sample(n=2)
		
	return two_random_colours.iloc[0], two_random_colours.iloc[1]

# Convert HTML-like colour hex-code to integer triple tuple
# E.g.: "#892da0" -> ( 137, 45, 160 )
def hexToColour( hash_colour ):
    """Convert a HTML-hexadecimal colour string to an RGB triple-tuple"""
    red   = int( hash_colour[1:3], 16 )
    green = int( hash_colour[3:5], 16 )
    blue  = int( hash_colour[5:7], 16 )
    return ( red, green, blue )
	

colours = pd.read_excel(r"colours.xlsx")


pygame.init()
pygame.display.set_caption('Colour picker')
screen = pygame.display.set_mode((1080, 700))
background = pygame.Surface((1080, 700))
background.fill(pygame.Color('#000000'))
width, height = pygame.display.get_surface().get_size()

colour_one, colour_two = pick_random_colours(colours)
	
is_running = True

while is_running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_pos = event.pos
			if buttonOne.collidepoint(mouse_pos):
				
				Change_Rating(colour_one, colour_two)
				colour_one, colour_two = pick_random_colours(colours)
				
			if buttonTwo.collidepoint(mouse_pos):
				Change_Rating(colour_two, colour_one)
				colour_one, colour_two = pick_random_colours(colours)
	buttonOne = pygame.Rect(0, 0, width/2, height)
	pygame.draw.rect(screen, hexToColour(str(colour_one["hex"])), buttonOne)
	buttonTwo = pygame.Rect(width/2, 0, width/2, height)
	pygame.draw.rect(screen, hexToColour(str(colour_two["hex"])), buttonTwo)

	pygame.display.update()
