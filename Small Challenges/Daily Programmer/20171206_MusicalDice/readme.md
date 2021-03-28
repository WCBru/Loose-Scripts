# Musical Dice Daily Programmer Challenge

This seemed like an interesting challenge, so I used it as an excuse to try my hand at an app in C#. The app can be found in the releases tab (Since .exe files aren't allowed by GitHub) along with the resources needed to run the application. The app uses .NET Framework 4.0.

The **Template Composition** is known as the starting composition from the challenge, and is the source of all measures used in the final composition. The **Dice Chart** maps a dice roll to a measure in the starting composition, as per the challenge. The **Output** is the generated composition. By default, the composition takes each of these files from the current directory, under the default name "startingNotes.txt", "diceChart.txt" and "output.txt" respectively. Also note that the output file will be overwritten.

In order to play generated compositions, copy and paste the contents of the output file to [this website](http://ufx.space/stuff/mozart-dice/). This is by the author of the challenge, found [here](https://www.reddit.com/r/dailyprogrammer/comments/7i1ib1/20171206_challenge_343_intermediate_mozarts/).