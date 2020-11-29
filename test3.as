	lw	0	0	skip	
	lw	5	1	toend	
	lw	5	2	smoop	
	lw	5	3	done	
skip	jalr	2	4	
toend	jalr	3	4	
smoop	noop
jumpBack	jalr	0	4	
done	halt	