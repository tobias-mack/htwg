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

	addi $sp,$sp,-12 # Platz auf Stack (Sichern von Zwischenergebnis eingeplant)
	sw $a0,8($sp)	 # Argument auf Stack sichern ($a0=n)
	sw $ra,4($sp)    # Rücksprungadresse sichern
	
			
	# fibo(n-1)+fibo(n-2)
	addi $a0,$a0,-1		# n ist auf Stack gesichert
	jal fibo		# fibo(n-1) berechnen
				# $a0 kann überschrieben werden
				# $s0 wird nicht überschrieben
	sw $v0,0($sp)
	
	lw $a0,8($sp)		# n vom Stack holen
	addi $a0,$a0,-2		# fibo(n-2) berechnen
	jal fibo
	
	lw $t0,0($sp)		# Zwischenergebnis (fibo(n-1)) vom Stack holen
	add $v0,$v0,$t0		# fibo(n-1)+fibo(n-2)
	
	# Stack wiederherstellen (hier günstiger)
	lw $ra,4($sp)
	addi $sp,$sp,12		# $s0 und $ra auf Stack sichern
	jr $ra			# Rücksprung

EXIT:	addi $v0,$zero,-1
	jr $ra
	
EXIT0:	addi $v0,$zero,0
	jr $ra

EXIT1:	addi $v0,$zero,1
	jr $ra

END:
