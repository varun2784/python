import pytest
import sys

def lcs(txt1, txt2):
    if not txt1 or not txt2:
        return '', 0
    if txt1[0] == txt2[0]:
        txt, len = lcs(txt1[1:], txt2[1:])
        return txt1[0] + str(txt), len + 1
    else:
        txt, len1 = lcs(txt1[1:], txt2)
        txt_t, len2 = lcs(txt1, txt2[1:])
        if len1 > len2:
            return txt, len1
        else:
            return txt_t, len2

def diff(src, common, dest):
    diff_txt = ''
    for x in src:
        if x not in common:
            diff_txt += "-"
            diff_txt += x
    for y in dest:
        if y not in common:
            diff_txt += '+'
            diff_txt += y
    return diff_txt

if __name__ == "__main__":
    txt1 = "axxxxbxxxxxcdfgh"
    txt2 = "ayyyyxyyybbcg"
    txt, len = lcs(txt1, txt2)
    print txt, len
    print diff(txt1, txt, txt2)

