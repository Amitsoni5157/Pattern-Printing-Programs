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

// Console.WriteLine("Hollow Square Star Pattern");
/*  
    ****
    *  *
    *  *
    ****
*/

// for(int i = 0; i< 4; i++)
// {
//     for (int j = 0; j < 4; j++)
//     {
//         if((j == 1 || j == 2) && (i == 1 | i == 2))
//         {
//             Console.Write(" ");
//         }
//         else
//         {
//             Console.Write("*");                    
//         }
//     }
//         Console.WriteLine("");     
// }

// //
// Console.WriteLine("Rhombus Star Pattern");

//         //    ****
//         //     ****
//         //      ****
//         //       ****
// int size = 4;

// for (int i = 0; i < size; i++)//Row
// {
//         for (int j = 0 ; j < i; j++)
//         {    
//             Console.Write(" ");
//         }
//         for (int k = 0; k < size; k++)
//         {
//             Console.Write("*");                                     
//         }   
//         Console.WriteLine(""); 
// }

// Console.WriteLine("Rectangle Star Pattern");
// // ******
// // ******
// // ******
// // ******
// int row = 4;
// int Coulm = 6;

// for (int i = 0; i < row; i++)
// {
//     for (int j = 0; j < Coulm; j++)
//     {
//          Console.Write("*");   
//     }
//      Console.WriteLine("");  
// }


// Console.WriteLine("Mirrored Rhombus Star Pattern");
// //     ****
// //    ****
// //   ****
// //  ****
// int size = 4;

// for(int i =0; i< size; i++)
// {
//     for (int j = size; j > i; j--)
//     {
//          Console.Write(" ");           
//     }

//     for (int k = 0; k < size; k++)
//     {
//         Console.Write("*");   
//     }

//     Console.WriteLine("");   

// }

Console.WriteLine("Triangle Star Pattern");

// *
// **
// ***
// ****
int size = 4;
for (int i = 0; i < size; i++)
{
    for (int j = 0; j <= i; j++)
    {
        Console.Write("*"); 
    }
     Console.WriteLine(""); 
}