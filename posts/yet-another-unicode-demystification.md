---
title: Yet another Unicode demystification
date: October 14, 2020
tags:
    - computer-science
location: Bharatpur
---

>    String is an array of characters. Each character is 1 byte.

But there's more to texts.

### Binary machines and ASCII

Computer memories are binary: slots which can store just zeros and ones.
Numbers and binaries get along pretty well. But for charecters and alphabets,
we need some way of encoding them into binary sequences.

A widespread encoding for alphabetic characters is ASCII(American Standard Code
for Information Interchange). It consists all the uppercase and lowercase
    English letters, numeric digits, some special characters like punctuations
    and some unprintable characters. We can see what the table looks like
    [here](https://en.wikipedia.org/wiki/Ascii).

ASCII table basically maps each alphabet/character to a number which can then
be stored in computer. There are 128 different ASCII characters which can be
represented by 7 bits. So, the word "Tom" would be represented in ASCII as:
`1010100 1101111 1101101`

Note that, when ASCII characters are represented as bytes then the first bit is
always 0.

This representation was going all well in the past until computers were adopted
world wide. Different parts of world used different encodings for their
character sets.

### Mighty Unicode
This unmoderated encodings being used all over the world produced many
incompatible systems as a result of which [The Unicode
Consortium](https://en.wikipedia.org/wiki/Unicode_Consortium) was established
to collect and catalog all the alphabets of all spoken languages in the world.
This was the first step towards a standard system for worldwide interchange,
processing and display of texts in various languages.

Strictly speaking, the standard organizes characters into scripts instead of
languages because different languages can use one script. For example, Latin
script can be used by many European and American languages.

Now, every character in each script has a unique identifying number which we
call a code point, usually written in hexadecimal and preceeded by U+. For
example, Unicode Codepoint for the character 'A'(`67 = 0x43`) is `U+0043`.
Corresponding to each code point is a glyph, which is the graphic
representation of the symbol. For example, the unicode value for the glyph क in
Devnagari script is `U+0915`.

The range of Unicode code space is `0` to `10FFFF` which is 21 bits. Because
computer memory is normally organized into 8-bit bytes, it would be possible to
use 3 bytes to store each code point with leading 3 bits unused. However, most
computers process information in chunks of 32 or 64 bits[as of 2020], it will
be effective to store each code point in a 32 bit(4 bytes) chunk even if the
leading 11 bits would useless and set to zero. This method of encoding is what
we've known or heard as UTF-32, UTF meaning Unicode Transfer Format.

>    As an example, let's see how the letter z is stored in UTF-32. It's ASCII
>    value is `0x7A` which gives the code point U+007A. Now we just need to prefix
>    the leading zeroes to get `0000 0000 0000 0000 0111 1010`

But!!

While UTF-32 is effective for processing texts, it is inefficient for storing
and transmitting them. If we have a file with mostly ASCII characters, three
fourth of the file space will be occupied by zeros.

### UTF-8 to the rescue
We must have seen utf-8 almost everywhere. This is a very popular encoding
which can represent the unicode code points with one to 3 bytes, using a single
byte for ASCII, without loosing compatibility with ASCII at all.

Here are the rules for UTF-8 encoding:

Code points from U+0000 to U+007F

These consist of our old ASCII friends. The first bit is 0 and the rest 7 bits
represent the characters.

Code points over U+007F

These obviously require more than 1 byte. The first byte contains information
about how many bytes will be used as well as some text data. The subsequent
bytes, called as continuation bytes will have first two bits set as 10 meaning
this is a continuation byte and last 6 bits to store codepoint data.

Now the first byte. If total of two bytes will be used, it will be prefixed by
110, for 3 bytes it will be prefixed by 1110 and for 4 btes it will be prefixed
by 11110. You can see the pattern here. The number of 1s in the prefix denote
the number of bytes. The 1s are immediately followed by a 0 after which the
remaining bits of the first byte are used for data. The remaining bits are
distributed to subsequent continuation bytes.

The following table clarifies the concept. Note that the xs denote data bits
for the codepoint. Source at the bottom

### An Example doesn't hurt

Now let's try it out with a code point U+1F923 whose corresponding emoticon is
'🤣' [Laughing at programmer's misery].

* First, note that it lies between U+10000 and U+1FFFFF.
* So, we need 4 bytes to represent this code point.
* The 21 bits are: 0 0001 1111 1001 0010 0011 each corresponding to 1, F, 9, 2 and 3.
* The first byte becomes 11110 000. Note the four leading 1's followed by a zero. The last 3 zeros are first 3
bits from above 21 bits.
* Let's construct second byte which is a continuation by prefixing with 10. We get: 10 01 1111.
* Similarly, the third byte becomes: 10 1001 00.
* And the last byte: 10 10 0011.
* Combining all of them, the UTF-8 bits are: 11110000 10011111 10100100 10100011 which, in hex, is: 0xF09F A4A3.

Pheww!! That was something. I hope Unicodes are now friendlier than before.

*Summarized from Computer Systems, J. Stanley Warford: Chapter 3*
