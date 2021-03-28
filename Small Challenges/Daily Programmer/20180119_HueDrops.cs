using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;

namespace HueDropSolver
{
    class HueDrop
    {
        private char[][] board;
        private int height;
        private int width;
        public char target;
        private int[,] deltas = {
            {-1,0},
            {1,0},
            {0,1},
            {0,-1}
        };

        public HueDrop(StreamReader src)
        {
            // Board dimensions
            string[] dimensions = src.ReadLine().Split(' ');
            width = int.Parse(dimensions[0]);
            height = int.Parse(dimensions[1]);

            // Load board
            board = new char[height][];
            for (int row = 1; row <= height; row++)
            {
                string[] rowStrings = src.ReadLine().Split(' ');
                board[row - 1] = new char[width];
                for (int letter = 0; letter < width; letter++)
                {
                    board[row-1][letter] = Convert.ToChar(rowStrings[letter]);
                }
            }

            target = Convert.ToChar(src.ReadLine());
        }

        public HueDrop(HueDrop original)
        {
            target = original.target;
            height = original.getDimensions()[0];
            width = original.getDimensions()[1];
            board = new char[height][];
            for (int row = 0; row < height; row++)
            {
                board[row] = new char[width];
                for (int col = 0; col < width; col++)
                {
                    board[row][col] = original.getBoard()[row][col];
                }
            }
        }

        public Dictionary<int[], char> adjTiles(List<int> coord)
        {
            Dictionary<int[], char> output = new Dictionary<int[], char>();
            for (int delta = 0; delta < 4; delta++)
            {
                int newRow = coord[0] + deltas[delta, 0];
                int newCol = coord[1] + deltas[delta, 1];
                if (newRow >= 0 && newRow < height &&
                            newCol >= 0 && newCol < width)
                {
                    output.Add(new[] {newRow, newCol}, board[newRow][newCol]);
                }
            }
            return output;
        }

        public bool checkColour(char colour)
        {
            changeColour('X');
            int changeCount = changeColour(colour);
            return (changeCount == height * width) && (target == colour);
        }

        public int changeColour(char colour)
        {
            
            char startColour = board[0][0];
            int changeCounter = 0;
            Stack<List<int>> toCheck = new Stack<List<int>>();
            toCheck.Push(new [] { 0, 0 }.ToList());

            // Find an convert all connected tiles
            while (toCheck.Count != 0)
            {
                List<int> current = toCheck.Pop();
                if (board[current[0]][current[1]] == startColour)
                {
                    changeCounter++;
                    board[current[0]][current[1]] = colour;

                    // Check all adjascent tiles
                    Dictionary<int[], char> surrounds = adjTiles(current);
                    foreach (int[] adj in surrounds.Keys)
                    {
                        if (surrounds[adj] == startColour)
                        {
                            toCheck.Push(adj.ToList());
                        }
                    }
                }
            }
            // Return if all colours have been converted
            return changeCounter;
        }

        public void printBoard()
        {
            foreach (char[] row in board)
            {
                Console.WriteLine(row);
            }
        }

        public char[][] getBoard()
        {
            return board;
        }

        public int[] getDimensions()
        {
            return new[] { height, width };
        }
    }
    

    class Program
    {
        const int moveLimit = 25;
        static readonly char[] colourList = { 'R', 'O', 'Y', 'G', 'B', 'V' };

        private static char findNextColour(HueDrop game)
        {
            char originColour = game.getBoard()[0][0];
            List<int[]> leafTiles = new List<int[]>();
            Stack<int[]> toCheck = new Stack<int[]>();
            List<int[]> visited = new List<int[]>();
            toCheck.Push(new [] {0,0});
            while (toCheck.Count != 0)
            {
                int[] current = toCheck.Pop();
                Dictionary<int[], char> adj = game.adjTiles(current.ToList());
                game.getBoard()[current[0]][current[1]] = 'X';

                foreach (int[] coord in adj.Keys)
                {
                    if (adj[coord] == originColour)
                    {
                        toCheck.Push(coord);
                        visited.Add(coord);
                    }
                }
            }

            Dictionary<char, int> leafColours = new Dictionary<char, int>();
            foreach (char colour in colourList)
            {
                HueDrop currGame = new HueDrop(game);
                currGame.changeColour(colour);
                leafColours.Add(colour, currGame.changeColour('X'));
            }

            int max = game.changeColour(game.target); 
            char maxCol = game.target;
            foreach (char colour in leafColours.Keys)
            {
                if (leafColours[colour] > max) {
                    max = leafColours[colour];
                    maxCol = colour;
                }
            }
            return maxCol;
        }

        // Requires args[0] to be the path of a valid input file
        static void Main(string[] args)
        {
            HueDrop problem = new HueDrop(
                new StreamReader(new FileStream(args[0], FileMode.Open)));

            int numMoves = 0;
            while (numMoves <= moveLimit)
            {
                char nextColour = findNextColour(problem);
                Console.Write(nextColour.ToString() + " ");
                if (problem.checkColour(nextColour))
                {
                    break;
                }
                
                numMoves++;
            }


            Console.Write("\n");
            if (numMoves > moveLimit)
            {
                Console.WriteLine("No solution found");
                
            }

            problem.printBoard();
            Console.ReadLine();
        }
    }
}
