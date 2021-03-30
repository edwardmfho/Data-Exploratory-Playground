import random

BATCH = 3
DECISION_TIME = 100000

STRATEGIES = {
	1 : 'B only',
	2 : 'A+B'
}

PREDICTIONS = ['Correct', 'Incorrect'] # one box or two boxes
DISTRIBUTION = [.1, .9] # 99% correct prediction

INITIAL_BOX_A = 1
INITIAL_BOX_B = 100

win = 0
lose = 0

def score_average(lst):
	return sum(lst)/len(lst)

def outcome(parameter_list):
	strategy = parameter_list[0]
	prediction = parameter_list[1]


	if prediction == ['Correct']: # If prediction correct
		if strategy == STRATEGIES[1]:
			# print('correctly predicted')
			BOX_B = 0
			SCORED = (BOX_B)
		
		else:
			BOX_A = INITIAL_BOX_A
			BOX_B = 0
			SCORED = (BOX_A + BOX_B)

	else:		   # If prediction incorrect 
		if strategy == STRATEGIES[1]:
			BOX_B = INITIAL_BOX_B
			SCORED = (BOX_B)

		else:
			BOX_A = INITIAL_BOX_A
			BOX_B = INITIAL_BOX_B
			SCORED = (BOX_A + BOX_B)	

	return SCORED

p1_scores = []
p2_scores = []

for batch in range(BATCH):
	P1_SCORE = 0
	P2_SCORE = 0 


	for each in range(DECISION_TIME):
		# Computer Prediction
		prediction = random.choices(PREDICTIONS, DISTRIBUTION)
		P1_parameters = [STRATEGIES[1], prediction, win, lose]
		P2_parameters = [STRATEGIES[2], prediction, win, lose]

		P1_SCORED = outcome(P1_parameters)
		P2_SCORED = outcome(P2_parameters)

		P1_SCORE += P1_SCORED
		P2_SCORE += P2_SCORED

	p1_scores.append(P1_SCORE)
	p2_scores.append(P2_SCORE)


	print('\n \n //// BATCH #{}'.format(str(batch + 1)))
	print('---------------------------------------------------------------')
	print('{}: WON ${} out of {} games'.format(STRATEGIES[1],
																	str(P1_SCORE), 
																	str(DECISION_TIME)))
	print('---------------------------------------------------------------')
	print('{}: WON ${} out of {} games'.format(STRATEGIES[2],
																	str(P2_SCORE), 
																	str(DECISION_TIME)))
p1_scores_avg = score_average(p1_scores)
p2_scores_avg = score_average(p2_scores)
print('===================================================================')
print('For every {} games: '.format(DECISION_TIME))
print('Average Earning for picking {}: {}'.format(STRATEGIES[1], str(p1_scores_avg)))
print('Average Earning for picking {}: {}'.format(STRATEGIES[2], str(p2_scores_avg)))

