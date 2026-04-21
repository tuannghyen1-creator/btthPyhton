#bai 6

s = input("Nhập chuỗi S: ")
word_to_find = input("Nhập từ cần đếm: ")

words_list = s.split()


count = words_list.count(word_to_find)

print(f"Số từ {word_to_find} là {count}")

#bai 13
import re

def chuan_hoa_chuoi(s):
   
    s = " ".join(s.split())
    
   
    s = re.sub(r'\s+([.,])', r'\1', s)
    
    s = re.sub(r'([.,])(?=\S)', r'\1 ', s)
    
    return s


bai_tho_loi = """
   Quê  hương  là   chùm khế ngọt .
  Cho con  trèo hái mỗi ngày  .  
"""

dong_da_chuan_hoa = [chuan_hoa_chuoi(line) for line in bai_tho_loi.strip().split('\n')]
ket_qua = "\n".join(dong_da_chuan_hoa)

print(ket_qua)
