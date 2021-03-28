using System;

namespace baum
{
    class Program
    {
        static int noOddZeroBlock(int num)
        {
            int oddSeqCount = 0;
            foreach (char digit in Convert.ToString(num, 2))
            {
                //Console.WriteLine(digit.Equals('0'));
                if (digit == '0')
                {
                    oddSeqCount++;
                }
                else if (oddSeqCount % 2 == 1)
                {
                    return 0;
                }
                else
                {
                    oddSeqCount = 0;
                }
                
            }

            return oddSeqCount % 2 == 1 ? 0 : 1;
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Baum-Sweet Sequencer\n");
            string inputNum = "";
            int stopNum = 0;
            while (!int.TryParse(inputNum, out stopNum))
            {
                Console.Write("Enter a stopping point: ");
                inputNum = Console.ReadLine();
            }

            Console.Write("1, ");
            for (int n = 1; n < stopNum; n++)
            {
                Console.Write(noOddZeroBlock(n).ToString() + ", ");
            }
            Console.Write(noOddZeroBlock(stopNum).ToString());
            Console.ReadLine();
        }
    }
}
