
# **Number of Shared Tones Rule:**

## What the rule controls:  

##### The rule controls the number of pitches that two adjacent chords in the progression must share. <br>

For example, if one chord contains an E and a G, and the next chord in the progression contains an E, then the chords share one pitch.

## Levels:

1. Adjacent chords share at least 5 pitches (only applicable when num notes is 6)
    1. Example: If the current chord is C11 (C, E, G, B flat, D, F), then the next chord must have at least 5 of the following notes in it: C, E, G, B flat, D, F.

2. Adjacent chords must share at least 4 pitches (only applicable when num notes is greater than or equal to 5)
    1. Example: If the current chord is C11 (C, E, G, B flat, D, F), then the next chord must have at least 4 of the following notes in it: C, E, G, B flat, D, F.
    
3. Adjacent chords must share at least 3 pitches (only applicable when num notes is greater than or equal to 4)
    1. Example: If the current chord is C dominant (C, E, G, B flat) then the next chord must have at least 3 of the following notes in it: C, E, G, B flat

4. Adjacent chords must share at least 2 pitches (only applicable when num notes is greater than or equal to 3)
    1. Example: If the current chord is C major (C, E, G), then the next chord must have, at the least, a C and E, C and G, or an E and G in it
5. Adjacent chords must share at least 1 pitch
    1. Example: If the current chord is C major (C, E, G), then the next chord must have a C, E, or G

6. Adjacent chords may share no pitches
    1. All chords are allowed under this level


## How to Input:

1.  Input integer values corresponding to the number of pitches shared between chords (0-5)
    1. Example: If you want chords to share 2 notes you would input, "2"
    2. WARNING: The SharedTone value should not be higher or equal to the value of NumNotes or else no progressions will be generated that fit these rules