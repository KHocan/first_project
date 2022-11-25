#DNA 염기서열 순서 변경작업
#(상보적)AATTGGCC -> TTAACCGG
#(역순)AATTGGCC -> CCGGTTAA
#(상보적역순)AATTGGCC -> GGCCAATT


def comp(seq):
    comp_dict = {'A':'T','T':'A','C':'G','G':'C'}
    seq_comp = "" # 공백 대입하여 초기화
    for char in seq:
        seq_comp = seq_comp + comp_dict[char]
    return seq_comp

def rev(seq):
    seq_Rev = "".join(reversed(seq))
    return seq_Rev

def rev_comp(seq):
    tmp = comp(seq)
    return rev(tmp)

src = input("DNA sequence :")
cnvt = int(input("1(comp), 2(Rev), 3(Rev_Comp) : "))
if (cnvt >= 1 and cnvt <=3):
    if(cnvt == 1):
        rst = comp(src)
    elif(cnvt == 2):
        rst = rev(src)
    else :
        rst = rev_comp(src)
    print(src, "->", rst)
else :
    print("1(comp), 2(Rev), 3(Rev_comp)!!")


