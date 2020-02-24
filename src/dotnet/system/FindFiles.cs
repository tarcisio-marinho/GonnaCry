using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

namespace dotnet.system
{
    public class Files
    {
        private IList<string> filesFound { get; }
        public Files()
        {
            this.filesFound = new List<string>();
        }

        public async Task<IList<string>> find(IList<string> path)
        {
            List<Task> tasks = new List<Task>();
            path.ToList().ForEach(p =>
            {
                tasks.Add(Task.Run(() => _find(p)));
            });
            await Task.WhenAll(tasks);
            return this.filesFound;
        }

        public void _find(string path)
        {
            try
            {
                foreach (string directory in Directory.GetDirectories(path))
                {
                    foreach (string file in Directory.GetFiles(directory))
                    {
                        if (FileExtensions.allowedExtensions.ContainsKey(Path.GetExtension(file.ToUpper())))
                        {
                            this.filesFound.Add(file);
                        }
                    }
                    _find(directory);
                }
            }
            catch (Exception ex)
            {
                var msg = ex.Message;
            }
        }
    }
}