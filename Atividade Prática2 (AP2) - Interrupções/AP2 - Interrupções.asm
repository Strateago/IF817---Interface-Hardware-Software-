org 0x7c00
jmp main

dado: times 100 db 0
msg1: db "Digite uma string: ", 0
msg2: db "String salva:) : ", 0

interrupcao:
    push bp
    ;; sp -> bp antigo
    mov bp, sp
    ;;  bp -> sp -> bp antigo
    ;;  bp + 2 -> flags
    ;;  bp + 4 -> IP
    ;;  bp + 6 -> CS
    ;;  bp + 8 -> msg2
    ;;  bp + 10 -> dado
    mov si, [bp+8]
print_msg2:
    lodsb
    cmp al, 0
    je end_msg2
    call print
    jmp print_msg2
end_msg2:
    mov si, [bp+10]
loop1:
    lodsb
    call print
    cmp al, 0xd
    je end_int
    jmp loop1
end_int:
    pop bp
    iret

main:
    xor ax, ax
    mov bx, ax
    mov cx, ax
    mov dx, ax
    push ds
    mov di, 100h
    mov word[di],interrupcao
    mov word[di+2], 0
    pop ds
    mov si, msg1
    call print_msg1
    call scanf
    push dado
    push msg2
    int 40h
    jmp $

scanf:
    mov di, dado
loop:
    mov ah, 0
    int 16h
    stosb
    call print
    cmp al, 0xd ;;Tecla Enter
    je end
    jmp loop
end:
    mov al, 0xa
    call print
    ret

print_msg1:
    lodsb
    cmp al, 0
    je end_msg1
    call print
    jmp print_msg1
end_msg1:
    ret

print:
    mov ah, 0xe
    int 10h
    ret

times 510 - ($-$$) db 0
dw 0xaa55
