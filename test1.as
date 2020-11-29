	lw	0	2	11	load reg2 with 3 the multiple
	lw	0	3	12	
	lw	0	4	12	
	lw	0	1	10	load reg2 with -1 (uses numeric address)
	beq	0	2	4	goto end of program when reg2==0
	add	3	4	3	goto
	add	1	2	2	d
	sw	3	4	10	load reg2 with -1 (uses numeric address)
	beq	0	0	-5	go back to the beginning of the loop
	halt				end of program
	.fill	-1  
	.fill	3   
	.fill	2	   
