import string

flag = "rtkw{cf0bj_czbv_nv'cc_y4mv_kf_kip_re0kyvi_uivjj1ex_5vw89s3r44901831}"
f = "r"
encrypted = ""
# shift = int(open("secret_shift.txt").read().strip())

for i in f:
  if i in string.ascii_lowercase:
    for num in range (1,100):
      result = chr(((ord(i) - 97 + num) % 26)+97)
      if result == "a":
        shift = num

for i in flag:
    if i in string.ascii_lowercase:
        encrypted += chr(((ord(i) - 97 + shift) % 26)+97)
    else:
        encrypted += i

print(encrypted)