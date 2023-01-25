# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
speler1 = 'Ruud Gullit'
speler2 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = speler1 + ' ' + str(goal_0) + ', ' + speler2 + ' ' + str(goal_1)
report = f"{speler1} scored in the {goal_0}nd minute\n{speler2} scored in the {goal_1}th minute"

player = 'Ruud Gullit'
first_name = player[:player.find(' ')]
last_name_len = len(player[player.find(' '):-1])
name_short = player[:1] + '.' + player[player.find(' '):]
chant = (f"{first_name}! "*4 ).rstrip()
good_chant = ((chant[-1]) !='')
print (good_chant)

