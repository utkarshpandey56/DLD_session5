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
//ABC + A'B'C' + BCD + B'C'D'

module CS25B051_session6(
    input a,
    input b,
    input c,
    input d,
    output z1
    );

wire na, nb, nc, nd, bc, nbc, o1, o2, o3, o4, o12, o34, o1234;

not(na,a);
not(nb,b);
not(nc,c);
not(nd,d);

and(bc, b, c);
and(nbc, nb, nc);

and(o1, a, bc);
and(o2, d, bc);
and(o3, na, nab);
and(o4, nd, nbc);

or(o12, o1, o2);
or(o34, o3, o4);
or(o1234, o12, o34);
assign z1 = o1234;

endmodule