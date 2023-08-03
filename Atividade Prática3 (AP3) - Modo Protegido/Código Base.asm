; Today's code first boot up the system in 16-bit.
; Then config it to be a protected 32-bit. 
; Finally, we print "Hello World!" use buffer rather than control interrupt.
;
; Give credits to http://3zanders.co.uk/2017/10/16/writing-a-bootloader2/
; Comments partially added by Yu Wang
; -------------------------------------------------------------------

; initial 16 bit boot code
bits 16 	
org 0x7c00

boot:
	; enable A20 bit
	mov ax, 0x2401
	int 0x15

	; set vga to be normal mode 
	mov ax, 0x3
	int 0x10

	cli 					; Clear interrupt flag;
	lgdt [gdt_pointer] 		; Load Global/Interrupt Descriptor Table Register 
	
	mov eax, cr0 			; CR0 has various control flags that modify the basic operation of the processor
	or eax,0x1 				; EAX |= 0x01 set the protected mode bit on special CPU reg cr0
	mov cr0, eax			;
	jmp CODE_SEG:boot2		; jump to CODE_SEG boot2
gdt_start:
	dq 0x0
gdt_code:
	dw 0xFFFF	; Bits 0-15 do tamanho limite do segmento
	dw 0x0		; Bits 0-15 do endereço base do segmento
	db 0x0		; Bits 16-23 do endereço base do segmento
	db 10011010b
	;  |||||||| Bit de acesso (Memória virtual)
	;  |||||||
	;  ||||||| Leitura/Escrita :
	;  ||||||	0 => Só leitura (Dados) / Só executa (Código)
	;  ||||||	1 => Leitura e Escrita (Dados) / Leitura e Execução (Código)
	;  ||||||
	;  |||||| Direção de expansão (se de dados); Conformidade (se de código)
	;  |||||
	;  ||||| Tipo de segmento, se executável (0 = Seg. de Dados ; 1 = Seg. de Cód.)
	;  ||||
	;  |||| Bit que indica se esse descritor é do tipo de sistema (0) ou de código/dados (1)
	;  |||
	;  ||| Bits do privilégio do segmento (00 = Max ; 11 = Min)
	;  |
	;  | Bit que indica se o segmento tá na memória (0 = Não ; 1 = Sim)

	db 11001111b
	;  |||||||| Bits 16-19 do tamanho limite do segmento
	;  ||||
	;  |||| Bit que indica se o segmento é disponível a programadores de sistemas
	;  |||
	;  ||| Bit que indica se é um segmento de código 64bit
	;  ||
	;  || Tamanho padrão de operações (0 = segmento de 16bit; 1 = segmento de 32bit)
	;  |	       
	;  | Granularidade (0 = limite c/ granularidade de bytes; 1 = limite c/ granularidade de páginas)
	
	db 0x0		; Bits 24-31 do endereço base do segmento
gdt_data:
	dw 0xFFFF
	dw 0x0
	db 0x0
	db 10010010b
	db 11001111b
	db 0x0
gdt_end:
gdt_pointer:
	dw gdt_end - gdt_start-1
	dd gdt_start

CODE_SEG equ gdt_code - gdt_start
DATA_SEG equ gdt_data - gdt_start

bits 32

boot2:
	; now, initial stack to data segment
	mov ax, DATA_SEG
	mov ds, ax
	mov es, ax
	mov fs, ax
	mov gs, ax
	mov ss, ax
	mov esi,hello
	mov ebx,0xb8000

; Note that, since we are in protected mode, we cannot call BIOS INT any more. 
; Instead, we feed ASCII to buffer, which is [ebx]
.loop:
	lodsb 				; load string byte from [DS:SI] into AL
	or al,al			; 
	jz halt 			; the above two lines => jump if AL==0. Equivalent to CMP AL; JE halt
	or eax,0x0100 		; config text color to be 1 (blue)  [4bit bg color][4bit text color][8bit ascii]
						; more color info can be found in https://en.wikipedia.org/wiki/Video_Graphics_Array#Color_palette
	mov word [ebx], ax	; feed ASCII and color to buffer in memory
	add ebx,2 			; increase ebx by two bytes (1byte for color, 1byte for ASCII)
	jmp .loop
halt:
	cli
	hlt
hello: db "Hello world!",0

times 510 - ($-$$) db 0
dw 0xaa55
