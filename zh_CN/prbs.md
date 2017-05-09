# PRBS算法

## 简介
PRBS全称 **pseudorandom binary sequence** ，是一种为随机算法。序列开始取决于种子(seed)，序列循环的长度取决于LFSR多项式。详细可以参考wiki上关于
[RPBS的介绍](https://en.wikipedia.org/wiki/Pseudorandom_binary_sequence) 和[LFSR的介绍](https://en.wikipedia.org/wiki/Linear-feedback_shift_register), 下表为常见的LFSR多项式，以PRBS7为例。

Verilog HDL code可以表示为:

```verilog
assign  next_lfsr = {lfsr[5:0], lfsr[6] ^ lfsr[5] };
```


LFSR多项式表

|        Bits        |  Feedback polynomial                             |        Period        |   
|------------------- | ------------------------------------------------ | -------------------- | 
|n                   |                                                  | $2^n -1$             |  
|2                   |    $x^2 + x +1$                                  | 3                    | 
|3                   |    $x^3 + x^2 + 1$                               | 7                    | 
|4                   |    $x^4 + x^3 +1$                                | 15                   | 
|5                   |    $x^5 + x^3 +1$                                | 31                   | 
|6                   |    $x^6 + x^5 +1$                                | 63                   | 
|7                   |    $x^7 + x^6 +1$                                | 127                  | 
|8                   |    $x^8 + x^6 + x^5 +x^4+ 1$                     | 255                  | 
|9                   |    $x^9 + x^5 +1$                                | 511                  | 
|10                  |    $x^{10} + x^7 +1$                             | 1023                 | 
|11                  |    $x^{11} + x^9 +1$                             | 2047                 | 
|12                  |    $x^{12} + x^{11} + x^{10} +x^4+1$             | 4095                 | 
|13                  |    $x^{13} + x^{12} + x^{11} +x^8+1$             | 8191                 | 
|14                  |    $x^{14} + x^{13} + x^{12} +x^2+1$             | 16383                | 
|15                  |    $x^{15} + x^{14} +1$                          | 32767                | 
|16                  |    $x^{16} + x^{15} + x^{13}+x^4+1$              | 65535                | 
|17                  |    $x^{17} + x^{14} +1$                          | 131071               | 
|18                  |    $x^{18} + x^{11} +1$                          | 262143               | 
|19                  |    $x^{19} +x^{18}+x^{17}+x^{14}+1$              | 524287               | 

## Python实现代码

Python的实现如下代码,改变taps系数，可以实现各种不同的多项式，seed是起始的种子

{% include file=../code/lfsr.py, class=linenums %}
{% endinclude %}





