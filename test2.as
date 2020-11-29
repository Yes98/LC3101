	lw	0	2	three	load reg2 with 3 the multiple
	lw	0	3	two	
	lw	0	4	two	
	lw	0	1	10	load reg2 with -1 (uses numeric address)
start	beq	0	2	done	goto end of program when reg2==0
	add	3	4	3	goto
	add	1	2	2	d
	sw	3	4	10	load reg2 with -1 (uses numeric address)
	beq	0	0	start	go back to the beginning of the loop
done	halt				end of program
neg	.fill	-1  
three	.fill	3   
two	.fill	2	   