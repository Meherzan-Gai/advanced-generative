How to run program:

1. Open config file

2. Input melody as list of midi numbers (e.g. [60,64,67])

3. Input key signature (e.g. "C:min")

    1. This is optional and if no key signature (input "None" for this) is inputted the program will assume the key signature is C major

4. Input rules and their priorities

    1. Priority is lowest (most important) to highest (least important)

5. Input maxChords and maxRetries settings

    1. maxChords controls the number of chords generated and the maximum amount of branches from each progression

    2. maxRetries controls 2 things: the method for trimming progressions and the number of retries

        1. If maxRetries is less than or equal to 0, than the method for trimming progressions will be to take the chords generated from the previous rule if the current rule's trimming method results in no possible progressions (rules are sorted in order from priority)

        2. If maxRetries is greater than 0, than the program will deal with no possible progressions by recalling the generator and generating more chords to try and find some that fit all rules

6. Run the program from main.py