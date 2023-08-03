org 0x7c00
jmp start

string: db 'pneumoultramicroscopicossilicovulcanoconiotico',0

start:
    xor ax, ax
    mov bx, ax
    mov cx, ax
    mov dx, ax
    mov es, ax
    mov ds, ax
    mov si, string
    push ax

get_vowels:
    lodsb
; Letras Minusculas
    cmp al, 'a'
    je Add
    cmp al, 'e'
    je Add
    cmp al, 'i'
    je Add
    cmp al, 'o'
    je Add
    cmp al, 'u'
    je Add
; Letras Maiusculas
    cmp al, 'A'
    je Add
    cmp al, 'E'
    je Add
    cmp al, 'I'
    je Add
    cmp al, 'O'
    je Add
    cmp al, 'U'
    je Add
    cmp al, 0   ; Fim da string
    je get_number
    jmp get_vowels

Add:
    inc cx
    jmp get_vowels

get_number:
    mov ax, cx
    mov bl, 10
    loop:
        div bl
        add ah, '0'
        push ax
        cmp al, 0
        je print
        mov ah, 0
        jmp loop

print:
    pop ax
    mov al, ah
    cmp al, 0
    je end
    mov ah, 0xe
    int 10h
    jmp print

end:
    jmp $

times 510-($-$$) db 0
dw 0xaa55
