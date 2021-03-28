using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace MusicalDice
{
    class MusicalDiceGen
    {
        public const int COMPLENGTH = 16;

        public const int BARLENGTH = 3;

        /* Generate Chart to lookup measures for dice rolls
         * See Main() for how chartpath is selected
         * Returns a jagged array int[x][y] where x is the measure number
         * and y is the dice roll - 2
         */
        static int[][] GenDiceChart(string chartPath)
        {
            StreamReader src = new StreamReader(new FileStream(chartPath,
                FileMode.Open, FileAccess.Read)); // reader for chart

            int[][] chart = new int[COMPLENGTH][]; // jagged array for lookup
            for (int row = 0; row < chart.Length; row++)
            { //Split each line into individual numbers and parse individually
                string[] inStr = src.ReadLine().Split(null);
                chart[row] = new int[inStr.Length]; // initialise row
                for (int num = 0; num < inStr.Length; num++)
                { // parse each row element into the array
                    chart[row][num] = int.Parse(inStr[num]);
                }
            }

            src.Close();
            return chart;
        }

        /* Generate the starting compositon into a string array
         * Takes a file path for the source
         * Returns an array of strings, each row being an entry from the source
         * The function reads the first entry, then each subsequent entry is
         * preceeded by a new line char. The result is split by \n
         */
        static string[] GenerateSource(string path)
        {
            StreamReader src = new StreamReader(new FileStream(path,
                FileMode.Open, FileAccess.Read)); // source stream
            string outStr = src.ReadLine(); // read first line
            while (!src.EndOfStream) // while there is still data
            { // add each line to the string
                outStr += "\n" +src.ReadLine();
            }
            src.Close();
            return outStr.Split(new char[] { '\n' }); // split by new line
        }

        /* Generate a measure based on the beat given
         * Finds the corrosponding beat in the source and returns an array
         * With notes that are within the measure
         */
        static string[] GenerateMeasure(string[] src, float start)
        {
            int currentLine = (int)start; // start of the measure as int
            
            // Find starting line, which matches the starting beat given
            while (float.Parse((src[currentLine]).Split(null)[1]) != start)
            {
                currentLine++;
            }

            // Add first line, so subsequent lines seperated by \n
            string measure = src[currentLine];
            currentLine++;
            while (currentLine < src.Length) // while lines are available
            {
                string note = src[currentLine]; // retrieved note and beat
                float currentBeat = float.Parse(note.Split(null)[1]);
                if (currentBeat >= start + 3) // break if note not in measure
                {
                    break;
                }
                measure += "\n" + note; // else add note
                currentLine++; // increment to next line
            }

            return measure.Split(new char[] {'\n'}); // return array of lines
        }

        /* Input Arguments
         * 0: Starting composition (list of measures)
         * 1: Chart for mapping dice rolls to measure number
         * 2: Output file
         */
        public static void generateComposition(string[] args)
        {   // Generate source and dicechart from input arguments
            string[] src = GenerateSource(args[0]);
            int[][] diceChart = GenDiceChart(args[1]);

            StreamWriter output = new StreamWriter(new FileStream(args[2],
                FileMode.Create, FileAccess.Write)); // output file

            Random dice = new Random(); // randomiser for dice rolls

            for (int meas = 0; meas < COMPLENGTH; meas++) // generate measures
            {   // Note: beats are 0-indexed while measures are 1-indexed
                int diceRoll = dice.Next(6) + dice.Next(6); // roll two dice
                float startBeat = BARLENGTH * (diceChart[meas][diceRoll]-1);
                string[] measure = GenerateMeasure(src, startBeat);
                float currentBeat = BARLENGTH * meas; // beat in composition
                // prevBeat is the previous beat according to the source
                // This is used to check for changes in the beat number
                float prevBeat = float.Parse(measure[0].Split(null)[1]);

                foreach (string line in measure)
                {   // split the note into components
                    string[] note = line.Split(null);
                    float noteBeat = float.Parse(note[1]);
                    if (noteBeat != prevBeat)
                    {   // If on a different beat, increment current beat
                        currentBeat += noteBeat - prevBeat;
                        prevBeat = noteBeat;
                    }
                    // Generate output string based on the current beat
                    string outStr = note[0] + " " + currentBeat + " " + note[2];
                    output.WriteLine(outStr); // write into file
                }
            }
            output.Flush();
            output.Close();
        }
    }
}
