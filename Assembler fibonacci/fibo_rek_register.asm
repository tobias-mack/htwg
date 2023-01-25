# Beispiel aus der Vorlesung: Rekursive Berechnung von Fibonacci-Zahlen
	addi $a0,$zero,20	# n=20
	jal fibo		# call fibo(20)
	j END
	
fibo:	
	# if (n<0) return -1;
	slti $t0,$a0,0		# a0<0 ==> $t0=1
	bne $t0,$zero,EXIT	# t0=1 ==> EXIT
	
	# if (n==0) return 0;
	beq $a0,$zero,EXIT0	# $t0=0 ==> EXIT1
	# if (n==1) return 1;
	addi $t0,$zero,1	# t1 = 1
	beq $a0,$t0,EXIT1	# $t0=0 ==> EXIT1

	addi $sp,$sp,-12	# Register auf Stack sichern
	sw $s0,0($sp)	# nutzen $s0 für n
	sw $s1,4($sp)   # nutzen $s1 für fibo(n-1)
	sw $ra,8($sp)
	addi $s0,$a0,0		# n in $s0 sichern

			
	# fibo(n-1)+fibo(n-2)
	addi $a0,$s0,-1
	jal fibo		# fibo(n-1) berechnen
				# $a0 kann überschrieben werden
				# $s0 wird nicht überschrieben
	addi $s1,$v0,0		# Zwischenergebnis in $s1 sichern
	
	addi $a0,$s0,-2		# fibo(n-2) berechnen
	jal fibo
	
	add $v0,$v0,$s1		# fibo(n-1)+fibo(n-2)
	
	# Stack wiederherstellen
	lw $s0,0($sp)
	lw $s1,4($sp)
	lw $ra,8($sp)
	addi $sp,$sp,12		# $s0 und $ra auf Stack sichern
	jr $ra			# Rücksprung

EXIT:	addi $v0,$zero,-1
	jr $ra
	
EXIT0:	addi $v0,$zero,0
	jr $ra

EXIT1:	addi $v0,$zero,1
	jr $ra

END:
