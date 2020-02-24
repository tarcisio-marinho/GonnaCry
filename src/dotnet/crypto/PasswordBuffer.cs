using System;
using System.Collections.Generic;
using System.Linq;
using System.Security;

namespace dotnet.crypto
{
    public class PasswordBuffer : IDisposable
    {
        private IList<SecureString> AESKeys { get; set; }

        public void Dispose()
        {
            AESKeys.ToList().ForEach(k =>
            {
                k.Clear();
                k.Dispose();
            });
        }

        public void Insert(SecureString s){
            this.AESKeys.Add(s);
        }
    }
}