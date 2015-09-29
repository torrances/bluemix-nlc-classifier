############################################################################
### author:		craigtrim@gmail.com 									####
###	created:	29-Sept-2105											####
### notes:																####
###	1. usage of '\r' on macos											####
############################################################################

QUESTION_TYPES = [
	"verification",
	"disjunctive",
	"concept_completion",
	"example",
	"feature_specification",
	"quantification",
	"definition",
	"comparison",
	"interpretation",
	"casual_antecedent",
	"causal_consequence",
	"goal_orientation",
	"procedural",
	"enablement",
	"expectation",
	"judgemental"
];

f 		= open('training.csv','r')
f_out 	= open('training.dat', 'w+')

for line in f.read().split('\r'):
	tokens = line.split(",")
	
	total = len(tokens)
	start = total - len(QUESTION_TYPES)

	question = ''.join(tokens[0:start])
	if total < len(QUESTION_TYPES) : continue

	ctr = 0;
	for question_type in QUESTION_TYPES :
		if (ctr + start) >= total : continue
		value = tokens[ctr + start]
		if not not value:
			for x in range(0, int(value)):
				f_out.write (question + ", " + question_type + '\r')
		ctr = ctr + 1

f.close()
f_out.close()