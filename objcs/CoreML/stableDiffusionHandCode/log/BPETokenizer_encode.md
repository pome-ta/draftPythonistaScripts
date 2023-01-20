# logs

<details>
<summary>Pythonista3 asparagus</summary>

```log
prev a :current s
prev s :current p
prev p :current a
prev a :current r
prev r :current a
prev a :current g
prev g :current u
prev u :current s</w>
while --- ---
pairs
<pyStableDiffusion.tokenizer.BPETokenizer.TokenPair object at 0x122a64240>
 (first: "g", second: "u") <pyStableDiffusion.tokenizer.BPETokenizer.TokenPair object at 0x122a64128>
 (first: "s", second: "p") <pyStableDiffusion.tokenizer.BPETokenizer.TokenPair object at 0x122a64278>
 (first: "u", second: "s</w>") <pyStableDiffusion.tokenizer.BPETokenizer.TokenPair object at 0x122a64198>
 (first: "a", second: "r") <pyStableDiffusion.tokenizer.BPETokenizer.TokenPair object at 0x122a64160>
 (first: "p", second: "a") <pyStableDiffusion.tokenizer.BPETokenizer.TokenPair object at 0x122a64080>
 (first: "a", second: "s") <pyStableDiffusion.tokenizer.BPETokenizer.TokenPair object at 0x122a64208>
 (first: "a", second: "g") <pyStableDiffusion.tokenizer.BPETokenizer.TokenPair object at 0x122a641d0>
 (first: "r", second: "a")
---
canMerge
<pyStableDiffusion.tokenizer.BPETokenizer.TokenPair object at 0x122a64240>
 (first: "g", second: "u") <pyStableDiffusion.tokenizer.BPETokenizer.TokenPair object at 0x122a64128>
 (first: "s", second: "p") <pyStableDiffusion.tokenizer.BPETokenizer.TokenPair object at 0x122a64278>
 (first: "u", second: "s</w>") <pyStableDiffusion.tokenizer.BPETokenizer.TokenPair object at 0x122a64198>
 (first: "a", second: "r") <pyStableDiffusion.tokenizer.BPETokenizer.TokenPair object at 0x122a64160>
 (first: "p", second: "a") <pyStableDiffusion.tokenizer.BPETokenizer.TokenPair object at 0x122a64080>
 (first: "a", second: "s") <pyStableDiffusion.tokenizer.BPETokenizer.TokenPair object at 0x122a64208>
 (first: "a", second: "g") <pyStableDiffusion.tokenizer.BPETokenizer.TokenPair object at 0x122a641d0>
 (first: "r", second: "a")
---
min
<pyStableDiffusion.tokenizer.BPETokenizer.TokenPair object at 0x122a64240>
 (first: "g", second: "u")
 189
<pyStableDiffusion.tokenizer.BPETokenizer.TokenPair object at 0x122a64128>
 (first: "s", second: "p")
 77
<pyStableDiffusion.tokenizer.BPETokenizer.TokenPair object at 0x122a64278>
 (first: "u", second: "s</w>")
 207
<pyStableDiffusion.tokenizer.BPETokenizer.TokenPair object at 0x122a64198>
 (first: "a", second: "r")
 5
<pyStableDiffusion.tokenizer.BPETokenizer.TokenPair object at 0x122a64160>
 (first: "p", second: "a")
 254
<pyStableDiffusion.tokenizer.BPETokenizer.TokenPair object at 0x122a64080>
 (first: "a", second: "s")
 76
<pyStableDiffusion.tokenizer.BPETokenizer.TokenPair object at 0x122a64208>
 (first: "a", second: "g")
 91
<pyStableDiffusion.tokenizer.BPETokenizer.TokenPair object at 0x122a641d0>
 (first: "r", second: "a")
 48
shouldMerge
<pyStableDiffusion.tokenizer.BPETokenizer.TokenPair object at 0x122a64198>
 (first: "a", second: "r")
----
update tokens merging
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
while loop
index: 0
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 0
-- --newTokens append 1

tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 1
while loop
index: 1
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
s p a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
2
index: 1
tokens slice
['s']
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
index: 3
while loop
index: 3
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
--- remainingTokens
a r a g u s</w>
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
---- ---- bigram.first: a
-- --startMatchIndex
0
index: 3
-- --newTokens append 1
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a
tokens: ['a', 's', 'p', 'a', 'r', 'a', 'g', 'u', 's</w>']
-- --newTokens append 3
a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a a s a

```

</details>

<details>
<summary>dogs</summary>

```log
dogs
["dogs"]
prev d :current o
prev o :current g
prev g :current s</w>
while
--- pairs
▿ 3 members
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "o"
    - second: "g"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "g"
    - second: "s</w>"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "d"
    - second: "o"
--- canMerge
▿ 3 members
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "o"
    - second: "g"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "g"
    - second: "s</w>"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "d"
    - second: "o"
$0
▿ Optional(834)
  - some: 834
$1
▿ Optional(11031)
  - some: 11031
$0
▿ Optional(128)
  - some: 128
$1
▿ Optional(834)
  - some: 834
should
▿ StableDiffusion.BPETokenizer.TokenPair
  - first: "d"
  - second: "o"
update tokens merging
▿ 4 elements
  - "d"
  - "o"
  - "g"
  - "s</w>"
while loop
▿ 4 elements
  - "d"
  - "o"
  - "g"
  - "s</w>"
index:  0
--- remainingTokens
▿ 4 elements
  - "d"
  - "o"
  - "g"
  - "s</w>"
▿ 4 elements
  - "d"
  - "o"
  - "g"
  - "s</w>"
-- --startMatchIndex
0
index:  0
tokens slice
- 0 elements
-- --newTokens append 1
- 0 elements
▿ 4 elements
  - "d"
  - "o"
  - "g"
  - "s</w>"
-- --newTokens append 2
▿ 1 element
  - "do"
▿ 4 elements
  - "d"
  - "o"
  - "g"
  - "s</w>"
index:  2
while loop
▿ 4 elements
  - "d"
  - "o"
  - "g"
  - "s</w>"
index:  2
--- remainingTokens
▿ 2 elements
  - "g"
  - "s</w>"
▿ 4 elements
  - "d"
  - "o"
  - "g"
  - "s</w>"
break else
▿ 2 elements
  - "g"
  - "s</w>"
-- --newTokens append 4
▿ 3 elements
  - "do"
  - "g"
  - "s</w>"
▿ 4 elements
  - "d"
  - "o"
  - "g"
  - "s</w>"
index:  2
return newTokens ---
▿ 3 elements
  - "do"
  - "g"
  - "s</w>"
▿ 4 elements
  - "d"
  - "o"
  - "g"
  - "s</w>"
update tokens
▿ 3 elements
  - "do"
  - "g"
  - "s</w>"
prev do :current g
prev g :current s</w>
while
--- pairs
▿ 2 members
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "g"
    - second: "s</w>"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "do"
    - second: "g"
--- canMerge
▿ 2 members
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "g"
    - second: "s</w>"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "do"
    - second: "g"
$0
▿ Optional(3815)
  - some: 3815
$1
▿ Optional(834)
  - some: 834
should
▿ StableDiffusion.BPETokenizer.TokenPair
  - first: "g"
  - second: "s</w>"
update tokens merging
▿ 3 elements
  - "do"
  - "g"
  - "s</w>"
while loop
▿ 3 elements
  - "do"
  - "g"
  - "s</w>"
index:  0
--- remainingTokens
▿ 3 elements
  - "do"
  - "g"
  - "s</w>"
▿ 3 elements
  - "do"
  - "g"
  - "s</w>"
-- --startMatchIndex
1
index:  0
tokens slice
▿ 1 element
  - "do"
-- --newTokens append 1
▿ 1 element
  - "do"
▿ 3 elements
  - "do"
  - "g"
  - "s</w>"
-- --newTokens append 2
▿ 2 elements
  - "do"
  - "gs</w>"
▿ 3 elements
  - "do"
  - "g"
  - "s</w>"
index:  3
return newTokens ---
▿ 2 elements
  - "do"
  - "gs</w>"
▿ 3 elements
  - "do"
  - "g"
  - "s</w>"
update tokens
▿ 2 elements
  - "do"
  - "gs</w>"
prev do :current gs</w>
while
--- pairs
▿ 1 member
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "do"
    - second: "gs</w>"
--- canMerge
▿ 1 member
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "do"
    - second: "gs</w>"
should
▿ StableDiffusion.BPETokenizer.TokenPair
  - first: "do"
  - second: "gs</w>"
update tokens merging
▿ 2 elements
  - "do"
  - "gs</w>"
while loop
▿ 2 elements
  - "do"
  - "gs</w>"
index:  0
--- remainingTokens
▿ 2 elements
  - "do"
  - "gs</w>"
▿ 2 elements
  - "do"
  - "gs</w>"
-- --startMatchIndex
0
index:  0
tokens slice
- 0 elements
-- --newTokens append 1
- 0 elements
▿ 2 elements
  - "do"
  - "gs</w>"
-- --newTokens append 2
▿ 1 element
  - "dogs</w>"
▿ 2 elements
  - "do"
  - "gs</w>"
index:  2
return newTokens ---
▿ 1 element
  - "dogs</w>"
▿ 2 elements
  - "do"
  - "gs</w>"
update tokens
▿ 1 element
  - "dogs</w>"
while
--- pairs
- 0 members
--- canMerge
- 0 members
return tokens
▿ 1 element
  - "dogs</w>"
```

</details>

<details>
<summary>dog</summary>

```log
dog
["dog"]
prev d :current o
prev o :current g</w>
while
--- pairs
▿ 2 members
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "o"
    - second: "g</w>"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "d"
    - second: "o"
--- canMerge
▿ 2 members
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "o"
    - second: "g</w>"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "d"
    - second: "o"
$0
▿ Optional(128)
  - some: 128
$1
▿ Optional(8044)
  - some: 8044
should
▿ StableDiffusion.BPETokenizer.TokenPair
  - first: "d"
  - second: "o"
update tokens merging
▿ 3 elements
  - "d"
  - "o"
  - "g</w>"
while loop
▿ 3 elements
  - "d"
  - "o"
  - "g</w>"
index:  0
--- remainingTokens
▿ 3 elements
  - "d"
  - "o"
  - "g</w>"
▿ 3 elements
  - "d"
  - "o"
  - "g</w>"
-- --startMatchIndex
0
index:  0
tokens slice
- 0 elements
-- --newTokens append 1
- 0 elements
▿ 3 elements
  - "d"
  - "o"
  - "g</w>"
-- --newTokens append 2
▿ 1 element
  - "do"
▿ 3 elements
  - "d"
  - "o"
  - "g</w>"
index:  2
while loop
▿ 3 elements
  - "d"
  - "o"
  - "g</w>"
index:  2
--- remainingTokens
▿ 1 element
  - "g</w>"
▿ 3 elements
  - "d"
  - "o"
  - "g</w>"
break else
▿ 1 element
  - "g</w>"
-- --newTokens append 4
▿ 2 elements
  - "do"
  - "g</w>"
▿ 3 elements
  - "d"
  - "o"
  - "g</w>"
index:  2
return newTokens ---
▿ 2 elements
  - "do"
  - "g</w>"
▿ 3 elements
  - "d"
  - "o"
  - "g</w>"
update tokens
▿ 2 elements
  - "do"
  - "g</w>"
prev do :current g</w>
while
--- pairs
▿ 1 member
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "do"
    - second: "g</w>"
--- canMerge
▿ 1 member
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "do"
    - second: "g</w>"
should
▿ StableDiffusion.BPETokenizer.TokenPair
  - first: "do"
  - second: "g</w>"
update tokens merging
▿ 2 elements
  - "do"
  - "g</w>"
while loop
▿ 2 elements
  - "do"
  - "g</w>"
index:  0
--- remainingTokens
▿ 2 elements
  - "do"
  - "g</w>"
▿ 2 elements
  - "do"
  - "g</w>"
-- --startMatchIndex
0
index:  0
tokens slice
- 0 elements
-- --newTokens append 1
- 0 elements
▿ 2 elements
  - "do"
  - "g</w>"
-- --newTokens append 2
▿ 1 element
  - "dog</w>"
▿ 2 elements
  - "do"
  - "g</w>"
index:  2
return newTokens ---
▿ 1 element
  - "dog</w>"
▿ 2 elements
  - "do"
  - "g</w>"
update tokens
▿ 1 element
  - "dog</w>"
while
--- pairs
- 0 members
--- canMerge
- 0 members
return tokens
▿ 1 element
  - "dog</w>"
```

</details>

<details>
<summary>asparagus</summary>

```log
asparagus
["asparagus"]
prev a :current s
prev s :current p
prev p :current a
prev a :current r
prev r :current a
prev a :current g
prev g :current u
prev u :current s</w>
while
--- pairs
▿ 8 members
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "g"
    - second: "u"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "a"
    - second: "s"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "a"
    - second: "r"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "s"
    - second: "p"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "r"
    - second: "a"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "a"
    - second: "g"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "u"
    - second: "s</w>"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "p"
    - second: "a"
--- canMerge
▿ 8 members
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "g"
    - second: "u"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "a"
    - second: "s"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "a"
    - second: "r"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "s"
    - second: "p"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "r"
    - second: "a"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "a"
    - second: "g"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "u"
    - second: "s</w>"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "p"
    - second: "a"
$0
▿ Optional(76)
  - some: 76
$1
▿ Optional(189)
  - some: 189
$0
▿ Optional(5)
  - some: 5
$1
▿ Optional(76)
  - some: 76
$0
▿ Optional(77)
  - some: 77
$1
▿ Optional(5)
  - some: 5
$0
▿ Optional(48)
  - some: 48
$1
▿ Optional(5)
  - some: 5
$0
▿ Optional(91)
  - some: 91
$1
▿ Optional(5)
  - some: 5
$0
▿ Optional(207)
  - some: 207
$1
▿ Optional(5)
  - some: 5
$0
▿ Optional(254)
  - some: 254
$1
▿ Optional(5)
  - some: 5
should
▿ StableDiffusion.BPETokenizer.TokenPair
  - first: "a"
  - second: "r"
update tokens merging
▿ 9 elements
  - "a"
  - "s"
  - "p"
  - "a"
  - "r"
  - "a"
  - "g"
  - "u"
  - "s</w>"
while loop
▿ 9 elements
  - "a"
  - "s"
  - "p"
  - "a"
  - "r"
  - "a"
  - "g"
  - "u"
  - "s</w>"
index:  0
--- remainingTokens
▿ 9 elements
  - "a"
  - "s"
  - "p"
  - "a"
  - "r"
  - "a"
  - "g"
  - "u"
  - "s</w>"
▿ 9 elements
  - "a"
  - "s"
  - "p"
  - "a"
  - "r"
  - "a"
  - "g"
  - "u"
  - "s</w>"
bigram a
-- --startMatchIndex
0
index:  0
tokens slice
- 0 elements
-- --newTokens append 1
- 0 elements
▿ 9 elements
  - "a"
  - "s"
  - "p"
  - "a"
  - "r"
  - "a"
  - "g"
  - "u"
  - "s</w>"
-- --newTokens append 3
▿ 1 element
  - "a"
▿ 9 elements
  - "a"
  - "s"
  - "p"
  - "a"
  - "r"
  - "a"
  - "g"
  - "u"
  - "s</w>"
index:  1
while loop
▿ 9 elements
  - "a"
  - "s"
  - "p"
  - "a"
  - "r"
  - "a"
  - "g"
  - "u"
  - "s</w>"
index:  1
--- remainingTokens
▿ 8 elements
  - "s"
  - "p"
  - "a"
  - "r"
  - "a"
  - "g"
  - "u"
  - "s</w>"
▿ 9 elements
  - "a"
  - "s"
  - "p"
  - "a"
  - "r"
  - "a"
  - "g"
  - "u"
  - "s</w>"
bigram a
-- --startMatchIndex
3
index:  1
tokens slice
▿ 2 elements
  - "s"
  - "p"
-- --newTokens append 1
▿ 3 elements
  - "a"
  - "s"
  - "p"
▿ 9 elements
  - "a"
  - "s"
  - "p"
  - "a"
  - "r"
  - "a"
  - "g"
  - "u"
  - "s</w>"
-- --newTokens append 2
▿ 4 elements
  - "a"
  - "s"
  - "p"
  - "ar"
▿ 9 elements
  - "a"
  - "s"
  - "p"
  - "a"
  - "r"
  - "a"
  - "g"
  - "u"
  - "s</w>"
index:  5
while loop
▿ 9 elements
  - "a"
  - "s"
  - "p"
  - "a"
  - "r"
  - "a"
  - "g"
  - "u"
  - "s</w>"
index:  5
--- remainingTokens
▿ 4 elements
  - "a"
  - "g"
  - "u"
  - "s</w>"
▿ 9 elements
  - "a"
  - "s"
  - "p"
  - "a"
  - "r"
  - "a"
  - "g"
  - "u"
  - "s</w>"
bigram a
-- --startMatchIndex
5
index:  5
tokens slice
- 0 elements
-- --newTokens append 1
▿ 4 elements
  - "a"
  - "s"
  - "p"
  - "ar"
▿ 9 elements
  - "a"
  - "s"
  - "p"
  - "a"
  - "r"
  - "a"
  - "g"
  - "u"
  - "s</w>"
-- --newTokens append 3
▿ 5 elements
  - "a"
  - "s"
  - "p"
  - "ar"
  - "a"
▿ 9 elements
  - "a"
  - "s"
  - "p"
  - "a"
  - "r"
  - "a"
  - "g"
  - "u"
  - "s</w>"
index:  6
while loop
▿ 9 elements
  - "a"
  - "s"
  - "p"
  - "a"
  - "r"
  - "a"
  - "g"
  - "u"
  - "s</w>"
index:  6
--- remainingTokens
▿ 3 elements
  - "g"
  - "u"
  - "s</w>"
▿ 9 elements
  - "a"
  - "s"
  - "p"
  - "a"
  - "r"
  - "a"
  - "g"
  - "u"
  - "s</w>"
bigram a
break else
▿ 3 elements
  - "g"
  - "u"
  - "s</w>"
-- --newTokens append 4
▿ 8 elements
  - "a"
  - "s"
  - "p"
  - "ar"
  - "a"
  - "g"
  - "u"
  - "s</w>"
▿ 9 elements
  - "a"
  - "s"
  - "p"
  - "a"
  - "r"
  - "a"
  - "g"
  - "u"
  - "s</w>"
index:  6
return newTokens ---
▿ 8 elements
  - "a"
  - "s"
  - "p"
  - "ar"
  - "a"
  - "g"
  - "u"
  - "s</w>"
▿ 9 elements
  - "a"
  - "s"
  - "p"
  - "a"
  - "r"
  - "a"
  - "g"
  - "u"
  - "s</w>"
update tokens
▿ 8 elements
  - "a"
  - "s"
  - "p"
  - "ar"
  - "a"
  - "g"
  - "u"
  - "s</w>"
prev a :current s
prev s :current p
prev p :current ar
prev ar :current a
prev a :current g
prev g :current u
prev u :current s</w>
while
--- pairs
▿ 7 members
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "p"
    - second: "ar"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "a"
    - second: "g"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "a"
    - second: "s"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "ar"
    - second: "a"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "s"
    - second: "p"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "g"
    - second: "u"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "u"
    - second: "s</w>"
--- canMerge
▿ 7 members
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "p"
    - second: "ar"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "a"
    - second: "g"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "a"
    - second: "s"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "ar"
    - second: "a"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "s"
    - second: "p"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "g"
    - second: "u"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "u"
    - second: "s</w>"
$0
▿ Optional(91)
  - some: 91
$1
▿ Optional(188)
  - some: 188
$0
▿ Optional(76)
  - some: 76
$1
▿ Optional(91)
  - some: 91
$0
▿ Optional(23650)
  - some: 23650
$1
▿ Optional(76)
  - some: 76
$0
▿ Optional(77)
  - some: 77
$1
▿ Optional(76)
  - some: 76
$0
▿ Optional(189)
  - some: 189
$1
▿ Optional(76)
  - some: 76
$0
▿ Optional(207)
  - some: 207
$1
▿ Optional(76)
  - some: 76
should
▿ StableDiffusion.BPETokenizer.TokenPair
  - first: "a"
  - second: "s"
update tokens merging
▿ 8 elements
  - "a"
  - "s"
  - "p"
  - "ar"
  - "a"
  - "g"
  - "u"
  - "s</w>"
while loop
▿ 8 elements
  - "a"
  - "s"
  - "p"
  - "ar"
  - "a"
  - "g"
  - "u"
  - "s</w>"
index:  0
--- remainingTokens
▿ 8 elements
  - "a"
  - "s"
  - "p"
  - "ar"
  - "a"
  - "g"
  - "u"
  - "s</w>"
▿ 8 elements
  - "a"
  - "s"
  - "p"
  - "ar"
  - "a"
  - "g"
  - "u"
  - "s</w>"
bigram a
-- --startMatchIndex
0
index:  0
tokens slice
- 0 elements
-- --newTokens append 1
- 0 elements
▿ 8 elements
  - "a"
  - "s"
  - "p"
  - "ar"
  - "a"
  - "g"
  - "u"
  - "s</w>"
-- --newTokens append 2
▿ 1 element
  - "as"
▿ 8 elements
  - "a"
  - "s"
  - "p"
  - "ar"
  - "a"
  - "g"
  - "u"
  - "s</w>"
index:  2
while loop
▿ 8 elements
  - "a"
  - "s"
  - "p"
  - "ar"
  - "a"
  - "g"
  - "u"
  - "s</w>"
index:  2
--- remainingTokens
▿ 6 elements
  - "p"
  - "ar"
  - "a"
  - "g"
  - "u"
  - "s</w>"
▿ 8 elements
  - "a"
  - "s"
  - "p"
  - "ar"
  - "a"
  - "g"
  - "u"
  - "s</w>"
bigram a
-- --startMatchIndex
4
index:  2
tokens slice
▿ 2 elements
  - "p"
  - "ar"
-- --newTokens append 1
▿ 3 elements
  - "as"
  - "p"
  - "ar"
▿ 8 elements
  - "a"
  - "s"
  - "p"
  - "ar"
  - "a"
  - "g"
  - "u"
  - "s</w>"
-- --newTokens append 3
▿ 4 elements
  - "as"
  - "p"
  - "ar"
  - "a"
▿ 8 elements
  - "a"
  - "s"
  - "p"
  - "ar"
  - "a"
  - "g"
  - "u"
  - "s</w>"
index:  5
while loop
▿ 8 elements
  - "a"
  - "s"
  - "p"
  - "ar"
  - "a"
  - "g"
  - "u"
  - "s</w>"
index:  5
--- remainingTokens
▿ 3 elements
  - "g"
  - "u"
  - "s</w>"
▿ 8 elements
  - "a"
  - "s"
  - "p"
  - "ar"
  - "a"
  - "g"
  - "u"
  - "s</w>"
bigram a
break else
▿ 3 elements
  - "g"
  - "u"
  - "s</w>"
-- --newTokens append 4
▿ 7 elements
  - "as"
  - "p"
  - "ar"
  - "a"
  - "g"
  - "u"
  - "s</w>"
▿ 8 elements
  - "a"
  - "s"
  - "p"
  - "ar"
  - "a"
  - "g"
  - "u"
  - "s</w>"
index:  5
return newTokens ---
▿ 7 elements
  - "as"
  - "p"
  - "ar"
  - "a"
  - "g"
  - "u"
  - "s</w>"
▿ 8 elements
  - "a"
  - "s"
  - "p"
  - "ar"
  - "a"
  - "g"
  - "u"
  - "s</w>"
update tokens
▿ 7 elements
  - "as"
  - "p"
  - "ar"
  - "a"
  - "g"
  - "u"
  - "s</w>"
prev as :current p
prev p :current ar
prev ar :current a
prev a :current g
prev g :current u
prev u :current s</w>
while
--- pairs
▿ 6 members
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "p"
    - second: "ar"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "ar"
    - second: "a"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "a"
    - second: "g"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "g"
    - second: "u"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "as"
    - second: "p"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "u"
    - second: "s</w>"
--- canMerge
▿ 6 members
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "p"
    - second: "ar"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "ar"
    - second: "a"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "a"
    - second: "g"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "g"
    - second: "u"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "as"
    - second: "p"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "u"
    - second: "s</w>"
$0
▿ Optional(23650)
  - some: 23650
$1
▿ Optional(188)
  - some: 188
$0
▿ Optional(91)
  - some: 91
$1
▿ Optional(188)
  - some: 188
$0
▿ Optional(189)
  - some: 189
$1
▿ Optional(91)
  - some: 91
$0
▿ Optional(17303)
  - some: 17303
$1
▿ Optional(91)
  - some: 91
$0
▿ Optional(207)
  - some: 207
$1
▿ Optional(91)
  - some: 91
should
▿ StableDiffusion.BPETokenizer.TokenPair
  - first: "a"
  - second: "g"
update tokens merging
▿ 7 elements
  - "as"
  - "p"
  - "ar"
  - "a"
  - "g"
  - "u"
  - "s</w>"
while loop
▿ 7 elements
  - "as"
  - "p"
  - "ar"
  - "a"
  - "g"
  - "u"
  - "s</w>"
index:  0
--- remainingTokens
▿ 7 elements
  - "as"
  - "p"
  - "ar"
  - "a"
  - "g"
  - "u"
  - "s</w>"
▿ 7 elements
  - "as"
  - "p"
  - "ar"
  - "a"
  - "g"
  - "u"
  - "s</w>"
bigram a
-- --startMatchIndex
3
index:  0
tokens slice
▿ 3 elements
  - "as"
  - "p"
  - "ar"
-- --newTokens append 1
▿ 3 elements
  - "as"
  - "p"
  - "ar"
▿ 7 elements
  - "as"
  - "p"
  - "ar"
  - "a"
  - "g"
  - "u"
  - "s</w>"
-- --newTokens append 2
▿ 4 elements
  - "as"
  - "p"
  - "ar"
  - "ag"
▿ 7 elements
  - "as"
  - "p"
  - "ar"
  - "a"
  - "g"
  - "u"
  - "s</w>"
index:  5
while loop
▿ 7 elements
  - "as"
  - "p"
  - "ar"
  - "a"
  - "g"
  - "u"
  - "s</w>"
index:  5
--- remainingTokens
▿ 2 elements
  - "u"
  - "s</w>"
▿ 7 elements
  - "as"
  - "p"
  - "ar"
  - "a"
  - "g"
  - "u"
  - "s</w>"
bigram a
break else
▿ 2 elements
  - "u"
  - "s</w>"
-- --newTokens append 4
▿ 6 elements
  - "as"
  - "p"
  - "ar"
  - "ag"
  - "u"
  - "s</w>"
▿ 7 elements
  - "as"
  - "p"
  - "ar"
  - "a"
  - "g"
  - "u"
  - "s</w>"
index:  5
return newTokens ---
▿ 6 elements
  - "as"
  - "p"
  - "ar"
  - "ag"
  - "u"
  - "s</w>"
▿ 7 elements
  - "as"
  - "p"
  - "ar"
  - "a"
  - "g"
  - "u"
  - "s</w>"
update tokens
▿ 6 elements
  - "as"
  - "p"
  - "ar"
  - "ag"
  - "u"
  - "s</w>"
prev as :current p
prev p :current ar
prev ar :current ag
prev ag :current u
prev u :current s</w>
while
--- pairs
▿ 5 members
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "ag"
    - second: "u"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "u"
    - second: "s</w>"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "ar"
    - second: "ag"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "p"
    - second: "ar"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "as"
    - second: "p"
--- canMerge
▿ 5 members
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "ag"
    - second: "u"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "u"
    - second: "s</w>"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "ar"
    - second: "ag"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "p"
    - second: "ar"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "as"
    - second: "p"
$0
▿ Optional(207)
  - some: 207
$1
▿ Optional(3411)
  - some: 3411
$0
▿ Optional(40991)
  - some: 40991
$1
▿ Optional(207)
  - some: 207
$0
▿ Optional(188)
  - some: 188
$1
▿ Optional(207)
  - some: 207
$0
▿ Optional(17303)
  - some: 17303
$1
▿ Optional(188)
  - some: 188
should
▿ StableDiffusion.BPETokenizer.TokenPair
  - first: "p"
  - second: "ar"
update tokens merging
▿ 6 elements
  - "as"
  - "p"
  - "ar"
  - "ag"
  - "u"
  - "s</w>"
while loop
▿ 6 elements
  - "as"
  - "p"
  - "ar"
  - "ag"
  - "u"
  - "s</w>"
index:  0
--- remainingTokens
▿ 6 elements
  - "as"
  - "p"
  - "ar"
  - "ag"
  - "u"
  - "s</w>"
▿ 6 elements
  - "as"
  - "p"
  - "ar"
  - "ag"
  - "u"
  - "s</w>"
bigram p
-- --startMatchIndex
1
index:  0
tokens slice
▿ 1 element
  - "as"
-- --newTokens append 1
▿ 1 element
  - "as"
▿ 6 elements
  - "as"
  - "p"
  - "ar"
  - "ag"
  - "u"
  - "s</w>"
-- --newTokens append 2
▿ 2 elements
  - "as"
  - "par"
▿ 6 elements
  - "as"
  - "p"
  - "ar"
  - "ag"
  - "u"
  - "s</w>"
index:  3
while loop
▿ 6 elements
  - "as"
  - "p"
  - "ar"
  - "ag"
  - "u"
  - "s</w>"
index:  3
--- remainingTokens
▿ 3 elements
  - "ag"
  - "u"
  - "s</w>"
▿ 6 elements
  - "as"
  - "p"
  - "ar"
  - "ag"
  - "u"
  - "s</w>"
bigram p
break else
▿ 3 elements
  - "ag"
  - "u"
  - "s</w>"
-- --newTokens append 4
▿ 5 elements
  - "as"
  - "par"
  - "ag"
  - "u"
  - "s</w>"
▿ 6 elements
  - "as"
  - "p"
  - "ar"
  - "ag"
  - "u"
  - "s</w>"
index:  3
return newTokens ---
▿ 5 elements
  - "as"
  - "par"
  - "ag"
  - "u"
  - "s</w>"
▿ 6 elements
  - "as"
  - "p"
  - "ar"
  - "ag"
  - "u"
  - "s</w>"
update tokens
▿ 5 elements
  - "as"
  - "par"
  - "ag"
  - "u"
  - "s</w>"
prev as :current par
prev par :current ag
prev ag :current u
prev u :current s</w>
while
--- pairs
▿ 4 members
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "par"
    - second: "ag"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "u"
    - second: "s</w>"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "as"
    - second: "par"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "ag"
    - second: "u"
--- canMerge
▿ 3 members
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "ag"
    - second: "u"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "par"
    - second: "ag"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "u"
    - second: "s</w>"
$0
▿ Optional(11355)
  - some: 11355
$1
▿ Optional(3411)
  - some: 3411
$0
▿ Optional(207)
  - some: 207
$1
▿ Optional(3411)
  - some: 3411
should
▿ StableDiffusion.BPETokenizer.TokenPair
  - first: "u"
  - second: "s</w>"
update tokens merging
▿ 5 elements
  - "as"
  - "par"
  - "ag"
  - "u"
  - "s</w>"
while loop
▿ 5 elements
  - "as"
  - "par"
  - "ag"
  - "u"
  - "s</w>"
index:  0
--- remainingTokens
▿ 5 elements
  - "as"
  - "par"
  - "ag"
  - "u"
  - "s</w>"
▿ 5 elements
  - "as"
  - "par"
  - "ag"
  - "u"
  - "s</w>"
bigram u
-- --startMatchIndex
3
index:  0
tokens slice
▿ 3 elements
  - "as"
  - "par"
  - "ag"
-- --newTokens append 1
▿ 3 elements
  - "as"
  - "par"
  - "ag"
▿ 5 elements
  - "as"
  - "par"
  - "ag"
  - "u"
  - "s</w>"
-- --newTokens append 2
▿ 4 elements
  - "as"
  - "par"
  - "ag"
  - "us</w>"
▿ 5 elements
  - "as"
  - "par"
  - "ag"
  - "u"
  - "s</w>"
index:  5
return newTokens ---
▿ 4 elements
  - "as"
  - "par"
  - "ag"
  - "us</w>"
▿ 5 elements
  - "as"
  - "par"
  - "ag"
  - "u"
  - "s</w>"
update tokens
▿ 4 elements
  - "as"
  - "par"
  - "ag"
  - "us</w>"
prev as :current par
prev par :current ag
prev ag :current us</w>
while
--- pairs
▿ 3 members
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "as"
    - second: "par"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "par"
    - second: "ag"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "ag"
    - second: "us</w>"
--- canMerge
▿ 1 member
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "par"
    - second: "ag"
should
▿ StableDiffusion.BPETokenizer.TokenPair
  - first: "par"
  - second: "ag"
update tokens merging
▿ 4 elements
  - "as"
  - "par"
  - "ag"
  - "us</w>"
while loop
▿ 4 elements
  - "as"
  - "par"
  - "ag"
  - "us</w>"
index:  0
--- remainingTokens
▿ 4 elements
  - "as"
  - "par"
  - "ag"
  - "us</w>"
▿ 4 elements
  - "as"
  - "par"
  - "ag"
  - "us</w>"
bigram par
-- --startMatchIndex
1
index:  0
tokens slice
▿ 1 element
  - "as"
-- --newTokens append 1
▿ 1 element
  - "as"
▿ 4 elements
  - "as"
  - "par"
  - "ag"
  - "us</w>"
-- --newTokens append 2
▿ 2 elements
  - "as"
  - "parag"
▿ 4 elements
  - "as"
  - "par"
  - "ag"
  - "us</w>"
index:  3
while loop
▿ 4 elements
  - "as"
  - "par"
  - "ag"
  - "us</w>"
index:  3
--- remainingTokens
▿ 1 element
  - "us</w>"
▿ 4 elements
  - "as"
  - "par"
  - "ag"
  - "us</w>"
bigram par
break else
▿ 1 element
  - "us</w>"
-- --newTokens append 4
▿ 3 elements
  - "as"
  - "parag"
  - "us</w>"
▿ 4 elements
  - "as"
  - "par"
  - "ag"
  - "us</w>"
index:  3
return newTokens ---
▿ 3 elements
  - "as"
  - "parag"
  - "us</w>"
▿ 4 elements
  - "as"
  - "par"
  - "ag"
  - "us</w>"
update tokens
▿ 3 elements
  - "as"
  - "parag"
  - "us</w>"
prev as :current parag
prev parag :current us</w>
while
--- pairs
▿ 2 members
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "as"
    - second: "parag"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "parag"
    - second: "us</w>"
--- canMerge
▿ 1 member
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "as"
    - second: "parag"
should
▿ StableDiffusion.BPETokenizer.TokenPair
  - first: "as"
  - second: "parag"
update tokens merging
▿ 3 elements
  - "as"
  - "parag"
  - "us</w>"
while loop
▿ 3 elements
  - "as"
  - "parag"
  - "us</w>"
index:  0
--- remainingTokens
▿ 3 elements
  - "as"
  - "parag"
  - "us</w>"
▿ 3 elements
  - "as"
  - "parag"
  - "us</w>"
bigram as
-- --startMatchIndex
0
index:  0
tokens slice
- 0 elements
-- --newTokens append 1
- 0 elements
▿ 3 elements
  - "as"
  - "parag"
  - "us</w>"
-- --newTokens append 2
▿ 1 element
  - "asparag"
▿ 3 elements
  - "as"
  - "parag"
  - "us</w>"
index:  2
while loop
▿ 3 elements
  - "as"
  - "parag"
  - "us</w>"
index:  2
--- remainingTokens
▿ 1 element
  - "us</w>"
▿ 3 elements
  - "as"
  - "parag"
  - "us</w>"
bigram as
break else
▿ 1 element
  - "us</w>"
-- --newTokens append 4
▿ 2 elements
  - "asparag"
  - "us</w>"
▿ 3 elements
  - "as"
  - "parag"
  - "us</w>"
index:  2
return newTokens ---
▿ 2 elements
  - "asparag"
  - "us</w>"
▿ 3 elements
  - "as"
  - "parag"
  - "us</w>"
update tokens
▿ 2 elements
  - "asparag"
  - "us</w>"
prev asparag :current us</w>
while
--- pairs
▿ 1 member
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "asparag"
    - second: "us</w>"
--- canMerge
▿ 1 member
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "asparag"
    - second: "us</w>"
should
▿ StableDiffusion.BPETokenizer.TokenPair
  - first: "asparag"
  - second: "us</w>"
update tokens merging
▿ 2 elements
  - "asparag"
  - "us</w>"
while loop
▿ 2 elements
  - "asparag"
  - "us</w>"
index:  0
--- remainingTokens
▿ 2 elements
  - "asparag"
  - "us</w>"
▿ 2 elements
  - "asparag"
  - "us</w>"
bigram asparag
-- --startMatchIndex
0
index:  0
tokens slice
- 0 elements
-- --newTokens append 1
- 0 elements
▿ 2 elements
  - "asparag"
  - "us</w>"
-- --newTokens append 2
▿ 1 element
  - "asparagus</w>"
▿ 2 elements
  - "asparag"
  - "us</w>"
index:  2
return newTokens ---
▿ 1 element
  - "asparagus</w>"
▿ 2 elements
  - "asparag"
  - "us</w>"
update tokens
▿ 1 element
  - "asparagus</w>"
while
--- pairs
- 0 members
--- canMerge
- 0 members
return tokens
▿ 1 element
  - "asparagus</w>"
(lldb) 
```

</details>

<details>
<summary>elephant</summary>

```log
elephant
["elephant"]
prev e :current l
prev l :current e
prev e :current p
prev p :current h
prev h :current a
prev a :current n
prev n :current t</w>
while
--- pairs
▿ 7 members
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "n"
    - second: "t</w>"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "e"
    - second: "p"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "h"
    - second: "a"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "a"
    - second: "n"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "e"
    - second: "l"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "l"
    - second: "e"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "p"
    - second: "h"
--- canMerge
▿ 7 members
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "n"
    - second: "t</w>"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "e"
    - second: "p"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "h"
    - second: "a"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "a"
    - second: "n"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "e"
    - second: "l"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "l"
    - second: "e"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "p"
    - second: "h"
$0
▿ Optional(667)
  - some: 667
$1
▿ Optional(2696)
  - some: 2696
$0
▿ Optional(49)
  - some: 49
$1
▿ Optional(667)
  - some: 667
$0
▿ Optional(3)
  - some: 3
$1
▿ Optional(49)
  - some: 49
$0
▿ Optional(33)
  - some: 33
$1
▿ Optional(3)
  - some: 3
$0
▿ Optional(23)
  - some: 23
$1
▿ Optional(3)
  - some: 3
$0
▿ Optional(234)
  - some: 234
$1
▿ Optional(3)
  - some: 3
should
▿ StableDiffusion.BPETokenizer.TokenPair
  - first: "a"
  - second: "n"
update tokens merging
▿ 8 elements
  - "e"
  - "l"
  - "e"
  - "p"
  - "h"
  - "a"
  - "n"
  - "t</w>"
while loop
▿ 8 elements
  - "e"
  - "l"
  - "e"
  - "p"
  - "h"
  - "a"
  - "n"
  - "t</w>"
index:  0
--- remainingTokens
▿ 8 elements
  - "e"
  - "l"
  - "e"
  - "p"
  - "h"
  - "a"
  - "n"
  - "t</w>"
▿ 8 elements
  - "e"
  - "l"
  - "e"
  - "p"
  - "h"
  - "a"
  - "n"
  - "t</w>"
-- --startMatchIndex
5
index:  0
tokens slice
▿ 5 elements
  - "e"
  - "l"
  - "e"
  - "p"
  - "h"
-- --newTokens append 1
▿ 5 elements
  - "e"
  - "l"
  - "e"
  - "p"
  - "h"
▿ 8 elements
  - "e"
  - "l"
  - "e"
  - "p"
  - "h"
  - "a"
  - "n"
  - "t</w>"
-- --newTokens append 2
▿ 6 elements
  - "e"
  - "l"
  - "e"
  - "p"
  - "h"
  - "an"
▿ 8 elements
  - "e"
  - "l"
  - "e"
  - "p"
  - "h"
  - "a"
  - "n"
  - "t</w>"
index:  7
while loop
▿ 8 elements
  - "e"
  - "l"
  - "e"
  - "p"
  - "h"
  - "a"
  - "n"
  - "t</w>"
index:  7
--- remainingTokens
▿ 1 element
  - "t</w>"
▿ 8 elements
  - "e"
  - "l"
  - "e"
  - "p"
  - "h"
  - "a"
  - "n"
  - "t</w>"
break else
▿ 1 element
  - "t</w>"
-- --newTokens append 4
▿ 7 elements
  - "e"
  - "l"
  - "e"
  - "p"
  - "h"
  - "an"
  - "t</w>"
▿ 8 elements
  - "e"
  - "l"
  - "e"
  - "p"
  - "h"
  - "a"
  - "n"
  - "t</w>"
index:  7
return newTokens ---
▿ 7 elements
  - "e"
  - "l"
  - "e"
  - "p"
  - "h"
  - "an"
  - "t</w>"
▿ 8 elements
  - "e"
  - "l"
  - "e"
  - "p"
  - "h"
  - "a"
  - "n"
  - "t</w>"
update tokens
▿ 7 elements
  - "e"
  - "l"
  - "e"
  - "p"
  - "h"
  - "an"
  - "t</w>"
prev e :current l
prev l :current e
prev e :current p
prev p :current h
prev h :current an
prev an :current t</w>
while
--- pairs
▿ 6 members
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "e"
    - second: "l"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "l"
    - second: "e"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "e"
    - second: "p"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "h"
    - second: "an"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "an"
    - second: "t</w>"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "p"
    - second: "h"
--- canMerge
▿ 6 members
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "e"
    - second: "l"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "l"
    - second: "e"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "e"
    - second: "p"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "h"
    - second: "an"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "an"
    - second: "t</w>"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "p"
    - second: "h"
$0
▿ Optional(23)
  - some: 23
$1
▿ Optional(33)
  - some: 33
$0
▿ Optional(667)
  - some: 667
$1
▿ Optional(23)
  - some: 23
$0
▿ Optional(1034)
  - some: 1034
$1
▿ Optional(23)
  - some: 23
$0
▿ Optional(262)
  - some: 262
$1
▿ Optional(23)
  - some: 23
$0
▿ Optional(234)
  - some: 234
$1
▿ Optional(23)
  - some: 23
should
▿ StableDiffusion.BPETokenizer.TokenPair
  - first: "l"
  - second: "e"
update tokens merging
▿ 7 elements
  - "e"
  - "l"
  - "e"
  - "p"
  - "h"
  - "an"
  - "t</w>"
while loop
▿ 7 elements
  - "e"
  - "l"
  - "e"
  - "p"
  - "h"
  - "an"
  - "t</w>"
index:  0
--- remainingTokens
▿ 7 elements
  - "e"
  - "l"
  - "e"
  - "p"
  - "h"
  - "an"
  - "t</w>"
▿ 7 elements
  - "e"
  - "l"
  - "e"
  - "p"
  - "h"
  - "an"
  - "t</w>"
-- --startMatchIndex
1
index:  0
tokens slice
▿ 1 element
  - "e"
-- --newTokens append 1
▿ 1 element
  - "e"
▿ 7 elements
  - "e"
  - "l"
  - "e"
  - "p"
  - "h"
  - "an"
  - "t</w>"
-- --newTokens append 2
▿ 2 elements
  - "e"
  - "le"
▿ 7 elements
  - "e"
  - "l"
  - "e"
  - "p"
  - "h"
  - "an"
  - "t</w>"
index:  3
while loop
▿ 7 elements
  - "e"
  - "l"
  - "e"
  - "p"
  - "h"
  - "an"
  - "t</w>"
index:  3
--- remainingTokens
▿ 4 elements
  - "p"
  - "h"
  - "an"
  - "t</w>"
▿ 7 elements
  - "e"
  - "l"
  - "e"
  - "p"
  - "h"
  - "an"
  - "t</w>"
break else
▿ 4 elements
  - "p"
  - "h"
  - "an"
  - "t</w>"
-- --newTokens append 4
▿ 6 elements
  - "e"
  - "le"
  - "p"
  - "h"
  - "an"
  - "t</w>"
▿ 7 elements
  - "e"
  - "l"
  - "e"
  - "p"
  - "h"
  - "an"
  - "t</w>"
index:  3
return newTokens ---
▿ 6 elements
  - "e"
  - "le"
  - "p"
  - "h"
  - "an"
  - "t</w>"
▿ 7 elements
  - "e"
  - "l"
  - "e"
  - "p"
  - "h"
  - "an"
  - "t</w>"
update tokens
▿ 6 elements
  - "e"
  - "le"
  - "p"
  - "h"
  - "an"
  - "t</w>"
prev e :current le
prev le :current p
prev p :current h
prev h :current an
prev an :current t</w>
while
--- pairs
▿ 5 members
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "h"
    - second: "an"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "an"
    - second: "t</w>"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "le"
    - second: "p"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "e"
    - second: "le"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "p"
    - second: "h"
--- canMerge
▿ 5 members
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "h"
    - second: "an"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "an"
    - second: "t</w>"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "le"
    - second: "p"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "e"
    - second: "le"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "p"
    - second: "h"
$0
▿ Optional(262)
  - some: 262
$1
▿ Optional(1034)
  - some: 1034
$0
▿ Optional(48373)
  - some: 48373
$1
▿ Optional(262)
  - some: 262
$0
▿ Optional(1573)
  - some: 1573
$1
▿ Optional(262)
  - some: 262
$0
▿ Optional(234)
  - some: 234
$1
▿ Optional(262)
  - some: 262
should
▿ StableDiffusion.BPETokenizer.TokenPair
  - first: "p"
  - second: "h"
update tokens merging
▿ 6 elements
  - "e"
  - "le"
  - "p"
  - "h"
  - "an"
  - "t</w>"
while loop
▿ 6 elements
  - "e"
  - "le"
  - "p"
  - "h"
  - "an"
  - "t</w>"
index:  0
--- remainingTokens
▿ 6 elements
  - "e"
  - "le"
  - "p"
  - "h"
  - "an"
  - "t</w>"
▿ 6 elements
  - "e"
  - "le"
  - "p"
  - "h"
  - "an"
  - "t</w>"
-- --startMatchIndex
2
index:  0
tokens slice
▿ 2 elements
  - "e"
  - "le"
-- --newTokens append 1
▿ 2 elements
  - "e"
  - "le"
▿ 6 elements
  - "e"
  - "le"
  - "p"
  - "h"
  - "an"
  - "t</w>"
-- --newTokens append 2
▿ 3 elements
  - "e"
  - "le"
  - "ph"
▿ 6 elements
  - "e"
  - "le"
  - "p"
  - "h"
  - "an"
  - "t</w>"
index:  4
while loop
▿ 6 elements
  - "e"
  - "le"
  - "p"
  - "h"
  - "an"
  - "t</w>"
index:  4
--- remainingTokens
▿ 2 elements
  - "an"
  - "t</w>"
▿ 6 elements
  - "e"
  - "le"
  - "p"
  - "h"
  - "an"
  - "t</w>"
break else
▿ 2 elements
  - "an"
  - "t</w>"
-- --newTokens append 4
▿ 5 elements
  - "e"
  - "le"
  - "ph"
  - "an"
  - "t</w>"
▿ 6 elements
  - "e"
  - "le"
  - "p"
  - "h"
  - "an"
  - "t</w>"
index:  4
return newTokens ---
▿ 5 elements
  - "e"
  - "le"
  - "ph"
  - "an"
  - "t</w>"
▿ 6 elements
  - "e"
  - "le"
  - "p"
  - "h"
  - "an"
  - "t</w>"
update tokens
▿ 5 elements
  - "e"
  - "le"
  - "ph"
  - "an"
  - "t</w>"
prev e :current le
prev le :current ph
prev ph :current an
prev an :current t</w>
while
--- pairs
▿ 4 members
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "ph"
    - second: "an"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "le"
    - second: "ph"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "an"
    - second: "t</w>"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "e"
    - second: "le"
--- canMerge
▿ 3 members
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "ph"
    - second: "an"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "e"
    - second: "le"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "an"
    - second: "t</w>"
$0
▿ Optional(1573)
  - some: 1573
$1
▿ Optional(8220)
  - some: 8220
$0
▿ Optional(262)
  - some: 262
$1
▿ Optional(1573)
  - some: 1573
should
▿ StableDiffusion.BPETokenizer.TokenPair
  - first: "an"
  - second: "t</w>"
update tokens merging
▿ 5 elements
  - "e"
  - "le"
  - "ph"
  - "an"
  - "t</w>"
while loop
▿ 5 elements
  - "e"
  - "le"
  - "ph"
  - "an"
  - "t</w>"
index:  0
--- remainingTokens
▿ 5 elements
  - "e"
  - "le"
  - "ph"
  - "an"
  - "t</w>"
▿ 5 elements
  - "e"
  - "le"
  - "ph"
  - "an"
  - "t</w>"
-- --startMatchIndex
3
index:  0
tokens slice
▿ 3 elements
  - "e"
  - "le"
  - "ph"
-- --newTokens append 1
▿ 3 elements
  - "e"
  - "le"
  - "ph"
▿ 5 elements
  - "e"
  - "le"
  - "ph"
  - "an"
  - "t</w>"
-- --newTokens append 2
▿ 4 elements
  - "e"
  - "le"
  - "ph"
  - "ant</w>"
▿ 5 elements
  - "e"
  - "le"
  - "ph"
  - "an"
  - "t</w>"
index:  5
return newTokens ---
▿ 4 elements
  - "e"
  - "le"
  - "ph"
  - "ant</w>"
▿ 5 elements
  - "e"
  - "le"
  - "ph"
  - "an"
  - "t</w>"
update tokens
▿ 4 elements
  - "e"
  - "le"
  - "ph"
  - "ant</w>"
prev e :current le
prev le :current ph
prev ph :current ant</w>
while
--- pairs
▿ 3 members
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "le"
    - second: "ph"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "e"
    - second: "le"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "ph"
    - second: "ant</w>"
--- canMerge
▿ 1 member
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "e"
    - second: "le"
should
▿ StableDiffusion.BPETokenizer.TokenPair
  - first: "e"
  - second: "le"
update tokens merging
▿ 4 elements
  - "e"
  - "le"
  - "ph"
  - "ant</w>"
while loop
▿ 4 elements
  - "e"
  - "le"
  - "ph"
  - "ant</w>"
index:  0
--- remainingTokens
▿ 4 elements
  - "e"
  - "le"
  - "ph"
  - "ant</w>"
▿ 4 elements
  - "e"
  - "le"
  - "ph"
  - "ant</w>"
-- --startMatchIndex
0
index:  0
tokens slice
- 0 elements
-- --newTokens append 1
- 0 elements
▿ 4 elements
  - "e"
  - "le"
  - "ph"
  - "ant</w>"
-- --newTokens append 2
▿ 1 element
  - "ele"
▿ 4 elements
  - "e"
  - "le"
  - "ph"
  - "ant</w>"
index:  2
while loop
▿ 4 elements
  - "e"
  - "le"
  - "ph"
  - "ant</w>"
index:  2
--- remainingTokens
▿ 2 elements
  - "ph"
  - "ant</w>"
▿ 4 elements
  - "e"
  - "le"
  - "ph"
  - "ant</w>"
break else
▿ 2 elements
  - "ph"
  - "ant</w>"
-- --newTokens append 4
▿ 3 elements
  - "ele"
  - "ph"
  - "ant</w>"
▿ 4 elements
  - "e"
  - "le"
  - "ph"
  - "ant</w>"
index:  2
return newTokens ---
▿ 3 elements
  - "ele"
  - "ph"
  - "ant</w>"
▿ 4 elements
  - "e"
  - "le"
  - "ph"
  - "ant</w>"
update tokens
▿ 3 elements
  - "ele"
  - "ph"
  - "ant</w>"
prev ele :current ph
prev ph :current ant</w>
while
--- pairs
▿ 2 members
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "ph"
    - second: "ant</w>"
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "ele"
    - second: "ph"
--- canMerge
▿ 1 member
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "ele"
    - second: "ph"
should
▿ StableDiffusion.BPETokenizer.TokenPair
  - first: "ele"
  - second: "ph"
update tokens merging
▿ 3 elements
  - "ele"
  - "ph"
  - "ant</w>"
while loop
▿ 3 elements
  - "ele"
  - "ph"
  - "ant</w>"
index:  0
--- remainingTokens
▿ 3 elements
  - "ele"
  - "ph"
  - "ant</w>"
▿ 3 elements
  - "ele"
  - "ph"
  - "ant</w>"
-- --startMatchIndex
0
index:  0
tokens slice
- 0 elements
-- --newTokens append 1
- 0 elements
▿ 3 elements
  - "ele"
  - "ph"
  - "ant</w>"
-- --newTokens append 2
▿ 1 element
  - "eleph"
▿ 3 elements
  - "ele"
  - "ph"
  - "ant</w>"
index:  2
while loop
▿ 3 elements
  - "ele"
  - "ph"
  - "ant</w>"
index:  2
--- remainingTokens
▿ 1 element
  - "ant</w>"
▿ 3 elements
  - "ele"
  - "ph"
  - "ant</w>"
break else
▿ 1 element
  - "ant</w>"
-- --newTokens append 4
▿ 2 elements
  - "eleph"
  - "ant</w>"
▿ 3 elements
  - "ele"
  - "ph"
  - "ant</w>"
index:  2
return newTokens ---
▿ 2 elements
  - "eleph"
  - "ant</w>"
▿ 3 elements
  - "ele"
  - "ph"
  - "ant</w>"
update tokens
▿ 2 elements
  - "eleph"
  - "ant</w>"
prev eleph :current ant</w>
while
--- pairs
▿ 1 member
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "eleph"
    - second: "ant</w>"
--- canMerge
▿ 1 member
  ▿ StableDiffusion.BPETokenizer.TokenPair
    - first: "eleph"
    - second: "ant</w>"
should
▿ StableDiffusion.BPETokenizer.TokenPair
  - first: "eleph"
  - second: "ant</w>"
update tokens merging
▿ 2 elements
  - "eleph"
  - "ant</w>"
while loop
▿ 2 elements
  - "eleph"
  - "ant</w>"
index:  0
--- remainingTokens
▿ 2 elements
  - "eleph"
  - "ant</w>"
▿ 2 elements
  - "eleph"
  - "ant</w>"
-- --startMatchIndex
0
index:  0
tokens slice
- 0 elements
-- --newTokens append 1
- 0 elements
▿ 2 elements
  - "eleph"
  - "ant</w>"
-- --newTokens append 2
▿ 1 element
  - "elephant</w>"
▿ 2 elements
  - "eleph"
  - "ant</w>"
index:  2
return newTokens ---
▿ 1 element
  - "elephant</w>"
▿ 2 elements
  - "eleph"
  - "ant</w>"
update tokens
▿ 1 element
  - "elephant</w>"
while
--- pairs
- 0 members
--- canMerge
- 0 members
return tokens
▿ 1 element
  - "elephant</w>"
```

</details>

<details>
<summary>cat</summary>
