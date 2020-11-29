	lw	0	2	8	load reg1 with 5 (uses symbolic address)
	lw	0	1	7	load reg2 with -1 (uses numeric address)
	beq	0	2	3	goto end of program when reg1==0
	add	1	2	2	goto end of program when reg1==0
	sw	2	4	10	load reg2 with -1 (uses numeric address)
	beq	0	0	-4	go back to the beginning of the loop
	halt				end of program
	.fill	-1
	.fill	3
