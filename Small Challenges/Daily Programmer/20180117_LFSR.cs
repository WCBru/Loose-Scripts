using System;

namespace LFSR
{
    class ShiftRegister
    {
        private int[] taps;
        private int type; // only supports XOR and XNOR
        private int start;
        private int length;
        private int current;
        private int period;
        private int steps;
        public int finalPeriod;

        public ShiftRegister(string input)
        {
            // String of format "[taps] type start steps"
            string[] src = input.Split(' ');

            // Taps
            string[] tapList = src[0].Split(',');
            tapList[0] = tapList[0].Substring(1); // remove brackets
            tapList[tapList.Length - 1] = tapList[tapList.Length - 1]
                .Substring(0, tapList[tapList.Length - 1].Length - 1);
            taps = new int[tapList.Length];
            for (int tap = 0; tap < tapList.Length; tap++)
            {
                taps[tap] = int.Parse(tapList[tap]);
            }

            // Type: XNOR -> 1, XOR -> 0, defaults to XOR
            type = src[1].ToUpper().Equals("XNOR") ? 1 : 0;
            start = int.Parse(src[2]);
            length = src[2].Length;
            current = start;
            steps = int.Parse(src[3]);
            period = 0;
            finalPeriod = 0;
        }

        public bool nextStep() {
            bool returnVal = false;

            // Print out current state
            if (period <= steps)
            {
                Console.WriteLine(period.ToString() + " " + 
                    Convert.ToString(current,2)
                    .PadLeft(3, '0'));
                returnVal = true;
            }

            // Check if period complete
            if (current == start && period != 0)
            {
                finalPeriod = period;
            }
            else if (finalPeriod == 0) {
                returnVal = true;
            }

            // Advance to next step
            int nextIn = type;
            foreach (int tap in taps)
            {
                nextIn ^= type ^ ((current >> (length - tap - 1)) % 2);
            }
            
            current = current >> 1;
            current |= (nextIn << length - 1);

            period++;
            return returnVal;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            ShiftRegister shiftReg = new ShiftRegister(Console.ReadLine());
            while (shiftReg.nextStep()) { }
            Console.WriteLine("Period = " + shiftReg.finalPeriod.ToString());
            Console.ReadLine(); // wait for terminal to be closed
        }
    }
}
