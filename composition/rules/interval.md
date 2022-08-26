
# **Types of Intervals Rule:**

## What the rule controls:  

##### The rule controls the types of intervals that can make up the chords <br>

## Note: Octaves/Unison intervals are always allowed

## Levels:

1. Chords can be made out of Minor 3rds/Major 6ths, Major 3rds/Minor 6ths, and Perfect 4ths/Perfect 5ths
    1. Example: C major (C, E, G) is an acceptable chord as C to E is a major 3rd, E to G is a minor 3rd, and C to G is a perfect 5th
        1. However a C dominant chord (C, E, G, Bb) isn't acceptable as C to Bb is a minor 7th. 

2. Chords can be made out of Minor 3rds/Major 6ths, Major 3rds/Minor 6ths, Perfect 4ths/Perfect 5ths, and Tritones 
    1. Example: (C, G#, C) is an acceptable chord as C to G# is a tritone, G# to C is a tritone, and C to C is an octave
        1. However a C dominant chord (C, E, G, Bb) isn't acceptable as C to Bb is a minor 7th. 

3. Chords can be made out of Minor 3rds/Major 6ths, Major 3rds/Minor 6ths, Perfect 4ths/Perfect 5ths, Tritones, and Major 2nds/Minor 7ths 
    1. Example: C dominant (C, E, G, Bb) is an acceptable chord as it is made up of one Major 2nd/Minor 7th interval, two Minor 3rd/Major 6th intervals, one Major 3rd/Minor 6th Interval, one Perfect 4th/Perfect 5th Interval, and one tritone interval.
        1. However a C major 7th chord (C, E, G, B) isn't acceptable as C to B is a major 7th.
    
4. Chords can be made out of all types of intervals
    1. All chord intervals are acceptable with this level


## How to Input:

1.  Input boolean values in a list corresponding to each interval in an interval vector.
    1. An interval vector is a list of the intervals that make up a chord
    2. It has six types of intervals that make it up
        1. [Minor 2nd/Major 7th, Major 2nd/Minor 7th, Minor 3rd/Major 6th, Major 3rd/Minor 6th, Perfect 4th/Perfect 5th, Tritone] in that order
    3. Example: If you want Minor 3rds, Major 3rds, and Perfect 4ths you would input the following: [false,false,true,true,true,false]