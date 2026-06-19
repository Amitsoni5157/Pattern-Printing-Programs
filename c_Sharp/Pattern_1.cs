// Console.WriteLine("Square Star Pattern");
// /*  ****
//     ****
//     ****
//     ****
// */

// for(int i = 0; i < 4; i++)
// {
//     for (int j = 0; j < 4; j++)
//     {
//      Console.Write("*");           
//     }
//     Console.WriteLine("");
// }

Console.WriteLine("Hollow Square Star Pattern");
/*  
    ****
    *  *
    *  *
    ****
*/

for(int i = 0; i< 4; i++)
{
    for (int j = 0; j < 4; j++)
    {
        if((j == 1 || j == 2) && (i == 1 | i == 2))
        {
            Console.Write(" ");
        }
        else
        {
            Console.Write("*");                    
        }
    }
        Console.WriteLine("");     
}
