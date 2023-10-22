using System;
using System.Text;
using System.Threading.Tasks;
using models;

class MainContext
{
    static void Main(string[] args)
    {
        // See https://aka.ms/new-console-template for more information
        Console.WriteLine("Hello, World!");

        _Vector3 newVector3 = new _Vector3(99999.2377788888f, 5, 6);
        Console.WriteLine($"x: {newVector3.x}, y: {newVector3.y}, z: {newVector3.z}");
        // Console.WriteLine($"User Input: {Console.ReadLine()}");

        Console.WriteLine($"sending: {newVector3.x}");
        byte[] someBytes = BitConverter.GetBytes(newVector3.x);

        string s1 = "";
        foreach (int i in someBytes)
        {
            // Console.WriteLine(i);
            s1 += (char)i;
        }
        
        Console.WriteLine($"string: {s1}, length: {s1.Length}");

        byte[] decBytes1 = new byte[4];
        for (int i=0; i<4; i++)
        {
            // Console.WriteLine(s1[i]);
            decBytes1[i] = Convert.ToByte(s1[i]);
            // Console.WriteLine(decBytes1[i]);
        }
        
        float receivedNum = BitConverter.ToSingle(decBytes1);

        Console.WriteLine($"receiving: {receivedNum}");
    }
}