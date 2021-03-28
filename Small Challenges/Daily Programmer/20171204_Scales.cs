using System;

namespace _20171204
{
    class Program
    {
        public static string[] notes = 
            {"C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"};

        public static string[] solfege =
            {"Do", "Re", "Mi", "Fa", "So", "La", "Ti"};

        /* A completely unnecessary search function. The .Find method
         * works in this context and would reduce the program by 13 Lines
         */
        static int findElement(string[] src,string note)
        {
            for (int elm = 0; elm < src.Length; elm++)
            {
                if (note.Equals(src[elm]))
                {
                    return elm;
                }
            }
            return -1;
        }

        static string note(string note, string solf)
        {
            int solfIndex = findElement(solfege, solf);
            int noteIndex = (solfIndex> 2) ? 2*solfIndex - 1: 2*solfIndex;
            int startIndex = findElement(notes, note);
            if (noteIndex >= 0 && startIndex >= 0)
            {
                return notes[(noteIndex+startIndex) %notes.Length];
            }
            else {
                return "Invalid Solfege";
            }
        }

        static void Main(string[] args)
        {
            Console.WriteLine(note("C", "Do"));
            Console.WriteLine(note("C", "Re"));
            Console.WriteLine(note("C", "Mi"));
            Console.WriteLine(note("D", "Mi"));
            Console.WriteLine(note("A#", "Fa"));
            Console.ReadLine();
        }
    }
}
