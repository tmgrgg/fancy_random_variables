# fancy_random_variables
My attempt to capture 'the point' with random variables... if you're trying to understand random variables then working through this code might help things click.

Essentially, they allow you to vary the underlying model easily and still answer all your questions - they're not REALLY supposed to be a computational tool like I've used them here... they're a mathematical formalism that allows you to treat each statistical experiment in the same manner. As a mathematician, once you've constructed your model and identified your sample space and relevant random variables for answering your questions... then you've solved the problem and the rest is for the computer! But it is pretty awesome to quickly code out and show the power of this idea.

Play around with the underlying model... develop your own model with the same syntax I've used here. (Warning: I haven't rounded so there may be minor floating point errors present throughout i.e. 0.999999999... is probably 1.0 etc.)

To play around with this idea... run the `.py` file interactively.


The default sample space and distribution I've defined for you is the rolling of a fair dice.

This space is called `dice`.

You can define your own experiment, but first I'd mess around with `dice`.

You can update `dice`'s distribution parameters by doing:

`update_distribution_params(dice, ['one', 'two', 'three', 'four', 'five', 'six'], [p1, p2, p3, p4, p5, p6])`

(NOTE: you need to make sure that the probabilities add to 1, otherwise you'll get an error)

You can define your own random variables for `dice` as dictionaries

`rv = {'one': v1, 'two': v2, 'three': v3, 'four': v4, 'five': v5, 'six': v6}`

The default random variables I have defined are: `is_even`, `is_prime`, `identity` and `money_game`

the `money_game` random_variable refers to a simple game where
you lose $50 if you roll a 1 or a 2, and win 10, 20, 40, 100 dollars respectively if you roll a 3, 4, 5 or 6.

You can use `probability(experiment, random_variable, comparator, value)` to ask questions about the probability of events in the sample space using any defined random variables!

e.g. `probability(dice, is_even, '==', 1)` asks what the probability of a dice roll being even is. In my opinion, getting the hang of this function is a key step in understanding the concept of a random variable!

`expected_value(experiment, random_variable)` should calculate the expected value of a random_variable for the given experiment. e.g.

`expected_value(dice, money_game)` should tell you the number of dollars you'd be expected to win (if you played this game forever more!)

If you have any questions you can email me on thomasggrigg@gmail.com! I'll probably update this to make it cleaner soon, I'm just releasing it now since I thought it could possibly be helpful to some.
