# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
speler1 = 'Ruud Gullit'
speler2 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = f'{speler1} {goal_0}, {speler2} {goal_1}'

report = f"{speler1} scored in the {goal_0}nd minute\n{speler2} scored in the {goal_1}th minute"

player = 'Ruud Gullit'
first_name = (player[:4])
last_name_len = (len(player[5:]))
name_short = (f"R. {(player[5:])}")
chant = (f"{first_name}! "*4 ).rstrip()
#good_chant = (chant!= [ ])
good_chant = ((chant[-1]) != [ ])
print (good_chant)

