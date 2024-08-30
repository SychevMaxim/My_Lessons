players_dict = {

    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},

    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},

    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},

    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},

    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},

    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},

    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},

    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}

}
a_training = []
b_training = []
c_training = []
for player in players_dict.values():
	if player['team'] == 'A' and player['status'] == 'Rest':
		a_training.append(player)
	if player['team'] == 'B' and player['status'] == 'Training':
		b_training.append(player)
	if player['team'] == 'С' and player['status'] == 'Travel':
		c_training.append(player)
print('a training', a_training)
print('b rest', b_training)
print('c travel', c_training)