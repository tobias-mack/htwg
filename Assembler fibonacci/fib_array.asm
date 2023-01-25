# Beispiel aus der Vorlesung
# Schreibt Fibonacci-Zahlen von 1 bis 20 in Array A
# C-Code:
# void main() {
#	int A[20];
#	n=20;
#	A[0]=1;
#	A[1]=1;
#	i=2;
# 	while (i<=n) {
#		A[i]=A[i-1]+A[i];
# 	}
# }
# Lernziele:
# - Kennenlernen von Mars
# - Array mit fester Adresse 
# - Implementieren einer Schleife
# - Laden und Speichern von Arrayelementen
	addi $s0,$zero,0x10020000    	# Adresse von A
	addi $s1,$zero,20		# n=20

	addi $t1,$zero,1
	sw $zero,0($s0)			# A[0]=0
	sw $t1,4($s0)			# A[1]=1

	addi $t0,$zero,2		# i=2

LOOP:	slt $t2, $s1, $t0		# t2==1 wenn i>n
	bne $t2,$zero,EXIT		# not(i<=n) ==> aus Schleife
	sll $t3,$t0,2			# t3 -> 4*i
	add $t3,$s0,$t3			# addr(A[i])=addr(A)+4*i
	lw $t4,-4($t3)			# A[i-1] laden
	lw $t5,-8($t3)			# A[i-2] laden
	add $t4,$t4,$t5			# summieren
	sw $t4,0($t3)			# speichern
	addi $t0,$t0,1			# i inkrementieren
	j LOOP				
EXIT:	
