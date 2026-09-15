`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 09/15/2026 02:35:04 PM
// Design Name: 
// Module Name: CS25B051_session6
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////
//Z1 is the output for Q1

module CS25B051_session6(
    input a,
    input b,
    input c,
    input d,
    input e,
    output z1
    );

wire temp11, temp12, o1, temp21, temp22, nb, o2, na, temp31, temp32, o3, o4, ne, o12, fin;

and(temp11, a, b);
and(temp12, c, d);
and(o1, temp11, temp12);
not(nb, b);
and(temp21, nb, c);
and(temp22, d, e);
and(o2, temp21, temp22);
not(na, a);
and(o3, na, nb);
not(ne, e);
and(temp31, b, c);
and(temp32, ne, temp31);
or(o4, temp32, o3);
or(o12, o1, o2);
or(fin, o12, o4);
assign z1 = fin;

endmodule