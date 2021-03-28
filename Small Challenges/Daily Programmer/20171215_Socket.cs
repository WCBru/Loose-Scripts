using System;
using System.Net.Sockets;
using System.Net;
using System.Text;

// Note: I have no idea what I'm doing
// Thanks to: http://www.i-programmer.info/programming/cc/9993-c-sockets-no-need-for-a-web-server.html
// There is also basically no checking in this
namespace websocket
{
    class Program
    {
        static void Main(string[] args)
        {   // Takes a web address as first input arg, port as second
            // TODO: check if input is simply an ipaddress, not a url which requires dns lookup
            // The input args used for this was: http://httpbin.org 80

            string[] redoneString = args[0].Trim().Split('/');
            string ipStr;
            if (redoneString.Length > 2)
            {
                ipStr = redoneString[2];
            }
            else
            {
                ipStr = args[0];
            }
            IPHostEntry rawIP = Dns.GetHostEntry(ipStr);
            int port;
            if (int.TryParse(args[1], out port))
            {
                foreach (var addr in rawIP.AddressList)
                {
                    Console.WriteLine(addr.ToString());
                }

                Console.WriteLine("Attempting Connect...");

                string proIP = rawIP.AddressList[0].ToString().Trim();
                IPAddress address = IPAddress.Parse(proIP);
                Socket sock = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.IP);
                IPEndPoint target = new IPEndPoint(address, port);
                sock.Connect(target);
                // TODO: add a check to ensure connection is actually up
                string header = String.Format("GET /get HTTP/1.1\r\nHost: {0}\r\n\r\n",
                    ipStr);
                Console.WriteLine(header);
                sock.Send(Encoding.ASCII.GetBytes(header));

                // receive
                byte[] Buffer = new byte[1024];
                sock.Receive(Buffer);
                // Is this able to handle long amounts of data automatically?
                Console.Write(Encoding.ASCII.GetString(Buffer));

                sock.Close();
            }
            else
            {
                Console.WriteLine("Error!, invalid port format entered");
            }
                     
            Console.ReadLine();
        }
    }
}
