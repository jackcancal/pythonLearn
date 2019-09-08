# 秘钥
secret_key = "P"
# 信息
message = input()
secret_text = ''
# 加密算法
for key in message:
    ord_key = ord(key)
    ord_sec = ord(secret_key)
    if ord_key >= ord_sec:
        ord_key = ord_key + 3
    else:
        ord_key = ord_key - 3
    secret_text += chr(ord_key ^ ord_sec)

print('加密后的内容:', secret_text)
msg = ''
# 解密算法
for key in secret_text:
    ord_sec = ord(secret_key)
    ord_key = ord(key) ^ ord_sec
    if ord_key > ord_sec:
        msg += chr(ord_key - 3)
    else:
        msg += chr(ord_key + 3)
print('解密后的内容:', msg)

