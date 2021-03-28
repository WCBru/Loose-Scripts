using System;
using System.Collections.Generic;
using System.IO;

namespace alg
{
    class Process
    {
        public int[] alloc;
        public int[] max;
        public string id;

        public Process(string inLine, int length, int idNo)
        {
            alloc = new int[length];
            max = new int[length];
            string[] rawIn = inLine.Split();
            if (rawIn.Length != 2 * length)
            {
                Console.WriteLine("Warning! Length Mismatch");
            }
            rawIn[0] = rawIn[0].Substring(1);
            rawIn[rawIn.Length - 1] = rawIn[rawIn.Length - 1].Substring(0, rawIn[rawIn.Length - 1].Length - 1);
            while (rawIn.Length < 2 * length)
            {
                rawIn[rawIn.Length] = "0";
            }
            for (int slot = 0; slot < length; slot++)
            {
                alloc[slot] = int.Parse(rawIn[slot]);
                max[slot] = int.Parse(rawIn[slot + length]);
            }

            id = "P" + idNo.ToString();
        }

        public bool allocMet(int[] avaResc)
        {
            int[] total = new int[alloc.Length];
            for (int slot = 0; slot < alloc.Length; slot++)
            {
                if (max[slot] > alloc[slot] + avaResc[slot])
                {
                    return false;
                }
            }
            return true;
        }

        public int[] DotAdd(int[] inArr)
        {
            int[] outArr = new int[alloc.Length];
            for (int col = 0; col < inArr.Length; col++)
            {
                outArr[col] = inArr[col] + alloc[col];
            }
            return outArr;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            StreamReader data = new StreamReader(new FileStream(args[0], FileMode.Open));

            // Read in first line
            string[] tmpArray = data.ReadLine().Split();
            int slots = tmpArray.Length;
            int[] avaResrc = new int[slots];
            tmpArray[0] = tmpArray[0].Substring(1);
            tmpArray[slots - 1] = tmpArray[slots - 1].Substring(0,tmpArray[slots-1].Length - 1);

            for (int col = 0; col < slots; col++)
            {
                int.TryParse(tmpArray[col], out avaResrc[col]);
            }

            // Read in rest of lines into classes
            int progNum = 0;
            List<Process> progList = new List<Process>();
            while (!data.EndOfStream)
            {
                progList.Add(new Process(data.ReadLine(), slots, progNum));
                progNum++;
            }

            string[] execOrder = new string[progList.Count];
            int progCounted = 0;
            int offset = 0;
            while (progList.Count > 0)
            {
                for (int cycle = 0; cycle < progList.Count; cycle++)
                {
                    Process current = progList[(offset + cycle) % progList.Count];
                    if (current.allocMet(avaResrc))
                    {
                        execOrder[progCounted] = current.id;
                        progCounted++;
                        avaResrc = current.DotAdd(avaResrc);
                        offset = (offset + cycle) % progList.Count;
                        progList.Remove(current);
                        break;
                    }
                    if (cycle == progList.Count-1)
                    {
                        Console.WriteLine("No solution found");
                        System.Environment.Exit(1);
                    }
                }
                
            }

            Console.Write(string.Join(", ", execOrder));
            
            Console.ReadLine();
        }
    }
}
