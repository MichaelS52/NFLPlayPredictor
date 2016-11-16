# NFLPlayPredictor

Using SKLearn in python to create a Random Forest Classifier to predict upcoming NFL plays based on other parameters.
Training features include:
- Quarter
- Time remaining in Quarter
- Current Down
- Togo in down
- Yardline
- Yardline Direction (ie. OWN, OPP)
- Formation

Labels used (total of 38 labels):
set(['', 'EXCEPTION', 'RUSH LEFT TACKLE', 'PASS SHORT LEFT', 'FUMBLES', 'SACK', 'PASS INTENDED FOR', 'TIMEOUT', 'PASS MIDDLE TO', 'RUSH LEFT GUARD', 'PASS', 'PASS INTERCEPTED BY', 'PASS PASS RULING,', 'PASS SHORT MIDDLE', 'PASS DEEP LEFT', 'PASS KESSLER THROUGH', 'PASS NOT LISTED', 'RUSH CENTER', 'PUNT', 'KICK OFF', 'PASS DEEP RIGHT', 'EXTRA POINT', 'SCRAMBLE', 'QB KNEEL', 'RUSH', 'NO PLAY', 'PENALTY', 'PASS SHORT RIGHT', 'RUSH LEFT END', 'RUSH RIGHT TACKLE', 'CLOCK STOP', 'TWO-POINT CONVERSION', 'RUSH RIGHT END', 'FIELD GOAL', 'RUSH RIGHT GUARD', 'PASS LEFT TO', 'PASS DEEP MIDDLE', 'PASS RIGHT TO'])

Test Sets:

~80% of the dataset for training and ~20% for testing, RandomForestClassifier algorithm, Options:[max_depth = 15, max_features = 3, min_samples_leaf = 6, n_estimators = 7].

Result: 46.324% accuracy.

This data can be used to see which teams are more/less predictable:

NE - 47.03% accuracy

CAR - 48.1% accuracy
