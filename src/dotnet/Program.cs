using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using dotnet.system;

namespace dotnet
{
    class Program
    {
        static async Task Main(string[] args)
        {
            var obj = new extensions();
            var watch = System.Diagnostics.Stopwatch.StartNew();
            var files = await obj.find(new List<string>(){ "/home/", "/var/", "/media/", "/opt/"});
            watch.Stop();
            string elapsed = watch.Elapsed.ToString();

            Console.WriteLine(files.Count);
            Console.WriteLine(elapsed);
        }
    }
}
