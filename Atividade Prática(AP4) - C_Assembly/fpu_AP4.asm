section .text

global V_cone

V_cone:
    enter 0,0
    finit
    fld dword[ebp + 12] ;; h em st0
    fldpi 
    fmulp st1, st0 ;; St0 -> pi*h
    fld dword[ebp + 8] ;; St0 -> r
    fmul st0, st0 ;; St0 -> r²
    fmulp st1, st0 ;; St0 -> pi*h*r²
    fld1
    fadd st0,st0 ;;St0 -> 2
    fld1 
    faddp 
    fdivp st1, st0
    leave ;; destroi stack frame
    ret
