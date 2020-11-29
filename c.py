score=0

def round_a():
	import turtle
	import random

	#######################################################
	def segregate(charc,tuptoadd,movable,coin,J_list,E_list,bounds,barrier):
		if (charc == ' ') or (charc == '\t') or (charc == '.'):
			movable.append(tuptoadd)
			
			if (charc == '.'):
				coin.append(tuptoadd)
			
		if (charc == 'J'):
			J_list.append(tuptoadd)
			
		if (charc == 'E'):
			E_list.append(tuptoadd)
			
		if (charc == '+') or (charc=='-')or (charc=='|'):
			bounds.append(tuptoadd)
			
		if (charc == '#'):
			barrier.append(tuptoadd)
	############################################################
	def printboard(board,bob,sc,movable,coin,J_list,E_list,bounds,barrier):
		
		sc.setworldcoordinates(0,-1020,7200,100)
		bob.ht()
		bob.color('blue')
		bob.speed(10)
		sc.tracer(0,0)
		
		for i in range(len(board)):
			for j in range(len(board[i])):
				chartoseg=0
				bob.pu()
				bob.setpos(int(j*60),-int(i*30))
				bob.pd()
				chartoseg=board[i][j]
				if (board[i][j] == ' ') and ((i % j) not in [3,8,12]) and ((j % i) not in [3,8,12]):
					bob.write('.')
					chartoseg='.'
					segregate(chartoseg,(int(j*60),-int(i*30)),movable,coin,J_list,E_list,bounds,barrier)
					continue
				
				segregate(chartoseg,(int(j*60),-int(i*30)),movable,coin,J_list,E_list,bounds,barrier)
				bob.write(board[i][j])
				
		bob.pu()
		bob.setpos(0,-900)
		bob.pd()
		bob.write("SCORE:")
		bob.pu()
		bob.setpos(400,-900)
		bob.write(score)
		sc.update()
		sc.tracer(1)
	###############################################################################################################
	def jfind():
		global score
		E.pu()
		jpos=J.pos()
		epos=E.pos()
		if (epos==jpos) or (score == 1135):
			
			sc.bye()
			
		if jpos[0]-epos[0]>0:
			E.fd(60)
		elif jpos[0]-epos[0]<0:
			E.bk(60)
		else:
			pass
		fpos=E.pos()
		if fpos in barrier or fpos in bounds:
			num1=random.randint(1,1133)
			E.setpos(coin[num1])
				
			
		if jpos[1]-epos[1]>0:
			E.lt(90)
			E.fd(30)
			E.rt(90)
		elif jpos[1]-epos[1]<0:
			E.rt(90)
			E.fd(30)
			E.lt(90)
		else:
			pass	
		gpos=E.pos()
		if gpos in barrier or gpos in bounds:
			num2=random.randint(1,1133)
			E.setpos(coin[num2])
	################################################################################################################
		#####################################################################################################################
	def barriercheck(tuptobechecked):
		
		global score
		if (tuptobechecked not in bounds) and (tuptobechecked not in barrier) and (tuptobechecked in movable):
			J.setpos(tuptobechecked[0],tuptobechecked[1])
			if  (tuptobechecked not in aldreadydone) and (tuptobechecked in coin):
				
				
				J.write("z")
				
				aldreadydone.append(tuptobechecked)
				score = score+1
				
				turt.clear()
				turt.setpos(400,-900)
				turt.write(score)
				
	
				
			
	def up():
		p1=J.pos()
		xcor1=p1[0]
		ycor1=p1[1]
		ycor1=ycor1+30
		t1=(xcor1,ycor1)
		barriercheck(t1)
		
	def down():
		p2=J.pos()
		xcor2=p2[0]
		ycor2=p2[1]
		ycor2=ycor2-30
		t2=(xcor2,ycor2)
		barriercheck(t2)
	def right():
		p3=J.pos()
		xcor3=p3[0]
		ycor3=p3[1]
		xcor3=xcor3+60
		t3=(xcor3,ycor3)
		barriercheck(t3)
	def left():
		p4=J.pos()
		xcor4=p4[0]
		ycor4=p4[1]
		xcor4=xcor4-60
		t4=(xcor4,ycor4)
		barriercheck(t4)
	########################################################################################################################
	bob=turtle.Turtle()
	sc=turtle.Screen()
	
	J_list = []
	E_list = []
	movable = []
	coin=[]
	barrier=[]
	bounds=[]
	########################################################################################################
	board = [
	"+--------------------------------------------------------------------+",
	"|                                                                    |",
	"|                                                                    |",
	"| 	  #################################   ##################          |",
	"|                   ###                               ###            |",
	"|                   ###                               ###            |",
	"|                                                     ###            |",
	"|                   ###                               ###            |",
	"|                   ###              #############################   |",
	"|                   ###                       ###           #        |",
	"|        #   E      ###                        #            #        |",
	"|       ###         ###                                     #        |",
	"|      #####        ###                                     #        |",
	"|############## #############################               #        |",
	"|                             ##                            #        |",
	"|                             ##                            #        |",
	"|      #                                #############                |",
	"|      #                            J   ##         ##                |",
	"|      #                      ##                   ###########       |",
	"| 	    #                      ##        ##                           |",
	"| 	    #                      ##        ##                           |",
	"| 	    #     ####################### ################    ############|",
	"| 	    #     ####################### ################     ###########|",
	"| 	    #                                          ##                 |",
	"| 	    #                                          ##                 |",
	"| 	    #                                          ##                 |",
	"|    #######################  ######################         #       |",
	"| 	                                                         ###      |",
	"| 	                                                        #####     |",
	"+--------------------------------------------------------------------+"]

	###########################################################################################
	printboard(board,bob,sc,movable,coin,J_list,E_list,bounds,barrier)
	
	E=turtle.Turtle()
	sc.register_shape("E.gif")
	E.shape("E.gif")
	E.pu()
	E.setpos(E_list[0][0],E_list[0][1])
	E.pd()
	E.speed(1)
		
	for time in range(1,500):
		
		sc.ontimer(jfind,300*time)
		
		

	J=turtle.Turtle()
	sc.register_shape("J.gif")
	J.shape("J.gif")
	J.pu()
	J.setpos(J_list[0][0],J_list[0][1])

	J.speed(10)
	J.pd()
	J.pu()
	J.color("White")
	aldreadydone=[]
	turt=turtle.Turtle()
	turt.pu()
	turt.ht()
	bob.undo()

	sc.listen()
	sc.onkey(up,"w")
	sc.onkey(down,"s")
	sc.onkey(right,"d")
	sc.onkey(left,"a")
	
###############################################################################	
	
def round_b():
	import turtle
	import random

	#######################################################
	def segregate(charc,tuptoadd,movable,coin,J_list,E_list,bounds,barrier):
		if (charc == ' ') or (charc == '\t') or (charc == '.'):
			movable.append(tuptoadd)
			
			if (charc == '.'):
				coin.append(tuptoadd)
			
		if (charc == 'J'):
			J_list.append(tuptoadd)
			
		if (charc == 'E'):
			E_list.append(tuptoadd)
			
		if (charc == '+') or (charc=='-')or (charc=='|'):
			bounds.append(tuptoadd)
			
		if (charc == '#'):
			barrier.append(tuptoadd)
	############################################################
	def printboard(board,bob,sc,movable,coin,J_list,E_list,bounds,barrier):
		
		sc.setworldcoordinates(0,-1020,7200,100)
		bob.ht()
		bob.color('blue')
		bob.speed(10)
		sc.tracer(0,0)
		
		for i in range(len(board)):
			for j in range(len(board[i])):
				chartoseg=0
				bob.pu()
				bob.setpos(int(j*60),-int(i*30))
				bob.pd()
				chartoseg=board[i][j]
				if (board[i][j] == ' ') and ((i % j) not in [3,8,12]) and ((j % i) not in [3,8,12]):
					bob.write('.')
					chartoseg='.'
					segregate(chartoseg,(int(j*60),-int(i*30)),movable,coin,J_list,E_list,bounds,barrier)
					continue
				
				segregate(chartoseg,(int(j*60),-int(i*30)),movable,coin,J_list,E_list,bounds,barrier)
				bob.write(board[i][j])
				
		bob.pu()
		bob.setpos(0,-900)
		bob.pd()
		bob.write("SCORE:")
		bob.pu()
		bob.setpos(400,-900)
		bob.write(score)
		sc.update()
		sc.tracer(1)
	###############################################################################################################
	def jfind():
		global score
		E.pu()
		jpos=J.pos()
		epos=E.pos()
		if (epos==jpos) or (score == 1135):
			
			sc.bye()
			
		if jpos[0]-epos[0]>0:
			E.fd(60)
		elif jpos[0]-epos[0]<0:
			E.bk(60)
		else:
			pass
		fpos=E.pos()
		if fpos in barrier or fpos in bounds:
			num1=random.randint(1,1133)
			E.setpos(coin[num1])
				
			
		if jpos[1]-epos[1]>0:
			E.lt(90)
			E.fd(30)
			E.rt(90)
		elif jpos[1]-epos[1]<0:
			E.rt(90)
			E.fd(30)
			E.lt(90)
		else:
			pass	
		gpos=E.pos()
		if gpos in barrier or gpos in bounds:
			num2=random.randint(1,1133)
			E.setpos(coin[num2])
	################################################################################################################
	###############################################################################################################
	def jfind2():
		global score
		F.pu()
		jpos=J.pos()
		fpos=F.pos()
		if (fpos==jpos) or (score == 1135):
			
			sc.bye()
			
		if jpos[0]-fpos[0]>0:
			F.fd(60)
		elif jpos[0]-fpos[0]<0:
			F.bk(60)
		else:
			pass
		tpos=F.pos()
		if tpos in barrier or tpos in bounds:
			num1=random.randint(1,1133)
			F.setpos(coin[num1])
				
			
		if jpos[1]-fpos[1]>0:
			F.lt(90)
			F.fd(30)
			F.rt(90)
		elif jpos[1]-fpos[1]<0:
			F.rt(90)
			F.fd(30)
			F.lt(90)
		else:
			pass	
		upos=F.pos()
		if upos in barrier or upos in bounds:
			num2=random.randint(1,1133)
			F.setpos(coin[num2])
	################################################################################################################
		#####################################################################################################################
	def barriercheck(tuptobechecked):
		
		global score
		if (tuptobechecked not in bounds) and (tuptobechecked not in barrier) and (tuptobechecked in movable):
			J.setpos(tuptobechecked[0],tuptobechecked[1])
			if  (tuptobechecked not in aldreadydone) and (tuptobechecked in coin):
				
				
				J.write("z")
				
				aldreadydone.append(tuptobechecked)
				score = score+1
				
				turt.clear()
				turt.setpos(400,-900)
				turt.write(score)
				
	
				
			
	def up():
		p1=J.pos()
		xcor1=p1[0]
		ycor1=p1[1]
		ycor1=ycor1+30
		t1=(xcor1,ycor1)
		barriercheck(t1)
		
	def down():
		p2=J.pos()
		xcor2=p2[0]
		ycor2=p2[1]
		ycor2=ycor2-30
		t2=(xcor2,ycor2)
		barriercheck(t2)
	def right():
		p3=J.pos()
		xcor3=p3[0]
		ycor3=p3[1]
		xcor3=xcor3+60
		t3=(xcor3,ycor3)
		barriercheck(t3)
	def left():
		p4=J.pos()
		xcor4=p4[0]
		ycor4=p4[1]
		xcor4=xcor4-60
		t4=(xcor4,ycor4)
		barriercheck(t4)
	########################################################################################################################
	bob=turtle.Turtle()
	sc=turtle.Screen()
	
	J_list = []
	E_list = []
	movable = []
	coin=[]
	barrier=[]
	bounds=[]
	########################################################################################################
	board = [
	"+--------------------------------------------------------------------+",
	"|                                                                    |",
	"|                                                                    |",
	"| 	  #################################   ##################          |",
	"|                   ###                               ###            |",
	"|                   ###                               ###            |",
	"|                                                     ###            |",
	"|                   ###                               ###            |",
	"|                   ###              #############################   |",
	"|                   ###                       ###           #        |",
	"|        #   E      ###                        #            #        |",
	"|       ###         ###                                     #        |",
	"|      #####        ###                                     #        |",
	"|############## #############################               #        |",
	"|                             ##                            #        |",
	"|                             ##                            #        |",
	"|      #                                #############                |",
	"|      #                            J   ##         ##                |",
	"|      #                      ##                   ###########       |",
	"| 	    #                      ##        ##                           |",
	"| 	    #                      ##        ##                           |",
	"| 	    #     ####################### ################    ############|",
	"| 	    #     ####################### ################     ###########|",
	"| 	    #                                          ##                 |",
	"| 	    #                                          ##                 |",
	"| 	    #                                          ##                 |",
	"|    #######################  ######################         #       |",
	"| 	                                                         ###      |",
	"| 	                                                        #####     |",
	"+--------------------------------------------------------------------+"]

	###########################################################################################
	printboard(board,bob,sc,movable,coin,J_list,E_list,bounds,barrier)
	
	E=turtle.Turtle()
	sc.register_shape("E.gif")
	E.shape("E.gif")
	E.pu()
	E.setpos(E_list[0][0],E_list[0][1])
	E.pd()
	E.speed(1)
		
	for time in range(1,500):
		
		sc.ontimer(jfind,300*time)
	#########################################################
	F=turtle.Turtle()
	sc.register_shape("F.gif")
	F.shape("F.gif")
	F.pu()
	F.setpos(E_list[0][0],E_list[0][1])
	F.pd()
	F.speed(1)
		
	for time in range(1,500):
		
		sc.ontimer(jfind2,300*time)
	#########################################################

	J=turtle.Turtle()
	sc.register_shape("J.gif")
	J.shape("J.gif")
	J.pu()
	J.setpos(J_list[0][0],J_list[0][1])

	J.speed(10)
	J.pd()
	J.pu()
	J.color("White")
	aldreadydone=[]
	turt=turtle.Turtle()
	turt.pu()
	turt.ht()
	bob.undo()

	sc.listen()
	sc.onkey(up,"w")
	sc.onkey(down,"s")
	sc.onkey(right,"d")
	sc.onkey(left,"a")
	
###############################################################################	
	
def round_c():
	import turtle
	import random

	#######################################################
	def segregate(charc,tuptoadd,movable,coin,J_list,E_list,bounds,barrier):
		if (charc == ' ') or (charc == '\t') or (charc == '.'):
			movable.append(tuptoadd)
			
			if (charc == '.'):
				coin.append(tuptoadd)
			
		if (charc == 'J'):
			J_list.append(tuptoadd)
			
		if (charc == 'E'):
			E_list.append(tuptoadd)
			
		if (charc == '+') or (charc=='-')or (charc=='|'):
			bounds.append(tuptoadd)
			
		if (charc == '#'):
			barrier.append(tuptoadd)
	############################################################
	def printboard(board,bob,sc,movable,coin,J_list,E_list,bounds,barrier):
		
		sc.setworldcoordinates(0,-1020,7200,100)
		bob.ht()
		bob.color('blue')
		bob.speed(10)
		sc.tracer(0,0)
		
		for i in range(len(board)):
			for j in range(len(board[i])):
				chartoseg=0
				bob.pu()
				bob.setpos(int(j*60),-int(i*30))
				bob.pd()
				chartoseg=board[i][j]
				if (board[i][j] == ' ') and ((i % j) not in [3,8,12]) and ((j % i) not in [3,8,12]):
					bob.write('.')
					chartoseg='.'
					segregate(chartoseg,(int(j*60),-int(i*30)),movable,coin,J_list,E_list,bounds,barrier)
					continue
				
				segregate(chartoseg,(int(j*60),-int(i*30)),movable,coin,J_list,E_list,bounds,barrier)
				bob.write(board[i][j])
				
		bob.pu()
		bob.setpos(0,-900)
		bob.pd()
		bob.write("SCORE:")
		bob.pu()
		bob.setpos(400,-900)
		bob.write(score)
		sc.update()
		sc.tracer(1)
	###############################################################################################################
	def jfind():
		global score
		E.pu()
		jpos=J.pos()
		epos=E.pos()
		if (epos==jpos) or (score == 1135):
			
			sc.bye()
			
		if jpos[0]-epos[0]>0:
			E.fd(60)
		elif jpos[0]-epos[0]<0:
			E.bk(60)
		else:
			pass
		fpos=E.pos()
		if fpos in barrier or fpos in bounds:
			num1=random.randint(1,1133)
			E.setpos(coin[num1])
				
			
		if jpos[1]-epos[1]>0:
			E.lt(90)
			E.fd(30)
			E.rt(90)
		elif jpos[1]-epos[1]<0:
			E.rt(90)
			E.fd(30)
			E.lt(90)
		else:
			pass	
		gpos=E.pos()
		if gpos in barrier or gpos in bounds:
			num2=random.randint(1,1133)
			E.setpos(coin[num2])
	################################################################################################################
		#####################################################################################################################
	def barriercheck(tuptobechecked):
		
		global score
		if (tuptobechecked not in bounds) and (tuptobechecked not in barrier) and (tuptobechecked in movable):
			J.setpos(tuptobechecked[0],tuptobechecked[1])
			if  (tuptobechecked not in aldreadydone) and (tuptobechecked in coin):
				
				
				J.write("z")
				
				aldreadydone.append(tuptobechecked)
				score = score+1
				
				turt.clear()
				turt.setpos(400,-900)
				turt.write(score)
				
	
				
			
	def up():
		p1=J.pos()
		xcor1=p1[0]
		ycor1=p1[1]
		ycor1=ycor1+30
		t1=(xcor1,ycor1)
		barriercheck(t1)
		
	def down():
		p2=J.pos()
		xcor2=p2[0]
		ycor2=p2[1]
		ycor2=ycor2-30
		t2=(xcor2,ycor2)
		barriercheck(t2)
	def right():
		p3=J.pos()
		xcor3=p3[0]
		ycor3=p3[1]
		xcor3=xcor3+60
		t3=(xcor3,ycor3)
		barriercheck(t3)
	def left():
		p4=J.pos()
		xcor4=p4[0]
		ycor4=p4[1]
		xcor4=xcor4-60
		t4=(xcor4,ycor4)
		barriercheck(t4)
	########################################################################################################################
	bob=turtle.Turtle()
	sc=turtle.Screen()
	
	J_list = []
	E_list = []
	movable = []
	coin=[]
	barrier=[]
	bounds=[]
	########################################################################################################
	board = [
	"+--------------------------------------------------------------------+",
	"|                                                                    |",
	"|                                                                    |",
	"| 	  #################################   ##################          |",
	"|                   ###                               ###            |",
	"|                   ###                               ###            |",
	"|                                                     ###            |",
	"|                   ###                               ###            |",
	"|                   ###              #############################   |",
	"|                   ###                       ###           #        |",
	"|        #   E      ###                        #            #        |",
	"|       ###         ###                                     #        |",
	"|      #####        ###                                     #        |",
	"|############## #############################               #        |",
	"|                             ##                            #        |",
	"|                             ##                            #        |",
	"|      #                                #############                |",
	"|      #                            J   ##         ##                |",
	"|      #                      ##                   ###########       |",
	"| 	    #                      ##        ##                           |",
	"| 	    #                      ##        ##                           |",
	"| 	    #     ####################### ################    ############|",
	"| 	    #     ####################### ################     ###########|",
	"| 	    #                                          ##                 |",
	"| 	    #                                          ##                 |",
	"| 	    #                                          ##                 |",
	"|    #######################  ######################         #       |",
	"| 	                                                         ###      |",
	"| 	                                                        #####     |",
	"+--------------------------------------------------------------------+"]

	###########################################################################################
	printboard(board,bob,sc,movable,coin,J_list,E_list,bounds,barrier)
	
	E=turtle.Turtle()
	sc.register_shape("E.gif")
	E.shape("E.gif")
	E.pu()
	E.setpos(E_list[0][0],E_list[0][1])
	E.pd()
	E.speed(10)
		
	for time in range(1,600):
		
		sc.ontimer(jfind,100*time)
		
		

	J=turtle.Turtle()
	sc.register_shape("J.gif")
	J.shape("J.gif")
	J.pu()
	J.setpos(J_list[0][0],J_list[0][1])

	J.speed(10)
	J.pd()
	J.pu()
	J.color("White")
	aldreadydone=[]
	turt=turtle.Turtle()
	turt.pu()
	turt.ht()
	bob.undo()

	sc.listen()
	sc.onkey(up,"w")
	sc.onkey(down,"s")
	sc.onkey(right,"d")
	sc.onkey(left,"a")
	
###############################################################################	
	
def round_d():
	import turtle
	import random

	#######################################################
	def segregate(charc,tuptoadd,movable,coin,J_list,E_list,bounds,barrier):
		if (charc == ' ') or (charc == '\t') or (charc == '.'):
			movable.append(tuptoadd)
			
			if (charc == '.'):
				coin.append(tuptoadd)
			
		if (charc == 'J'):
			J_list.append(tuptoadd)
			
		if (charc == 'E'):
			E_list.append(tuptoadd)
			
		if (charc == '+') or (charc=='-')or (charc=='|'):
			bounds.append(tuptoadd)
			
		if (charc == '#'):
			barrier.append(tuptoadd)
	############################################################
	def printboard(board,bob,sc,movable,coin,J_list,E_list,bounds,barrier):
		
		sc.setworldcoordinates(0,-1020,7200,100)
		bob.ht()
		bob.color('blue')
		bob.speed(10)
		sc.tracer(0,0)
		
		for i in range(len(board)):
			for j in range(len(board[i])):
				chartoseg=0
				bob.pu()
				bob.setpos(int(j*60),-int(i*30))
				bob.pd()
				chartoseg=board[i][j]
				if (board[i][j] == ' ') and ((i % j) not in [3,8,12]) and ((j % i) not in [3,8,12]):
					bob.write('.')
					chartoseg='.'
					segregate(chartoseg,(int(j*60),-int(i*30)),movable,coin,J_list,E_list,bounds,barrier)
					continue
				
				segregate(chartoseg,(int(j*60),-int(i*30)),movable,coin,J_list,E_list,bounds,barrier)
				bob.write(board[i][j])
				
		bob.pu()
		bob.setpos(0,-900)
		bob.pd()
		bob.write("SCORE:")
		bob.pu()
		bob.setpos(400,-900)
		bob.write(score)
		sc.update()
		sc.tracer(1)
	###############################################################################################################
	def jfind():
		global score
		E.pu()
		jpos=J.pos()
		epos=E.pos()
		if (epos==jpos) or (score == 1135):
			
			sc.bye()
			
		if jpos[0]-epos[0]>0:
			E.fd(60)
		elif jpos[0]-epos[0]<0:
			E.bk(60)
		else:
			pass
		fpos=E.pos()
		if fpos in barrier or fpos in bounds:
			num1=random.randint(1,800)
			
			E.setpos(coin[num1])
		if fpos in coin:
			coin.remove(fpos)
		if fpos in movable:
			movable.remove(fpos)
			
			
		if jpos[1]-epos[1]>0:
			E.lt(90)
			E.fd(30)
			E.rt(90)
		elif jpos[1]-epos[1]<0:
			E.rt(90)
			E.fd(30)
			E.lt(90)
		else:
			pass	
		gpos=E.pos()
		if gpos in barrier or gpos in bounds:
			num2=random.randint(1,800)
			E.setpos(coin[num2])
		if gpos in coin:
			coin.remove(gpos)
		if gpos in movable:
			movable.remove(gpos)
	################################################################################################################
		#####################################################################################################################
	def barriercheck(tuptobechecked):
		
		global score
		if (tuptobechecked not in bounds) and (tuptobechecked not in barrier) and (tuptobechecked in movable):
			J.setpos(tuptobechecked[0],tuptobechecked[1])
			if  (tuptobechecked not in aldreadydone) and (tuptobechecked in coin):
				
				
				J.write("z")
				
				aldreadydone.append(tuptobechecked)
				score = score+1
				
				turt.clear()
				turt.setpos(400,-900)
				turt.write(score)
				
	
				
			
	def up():
		p1=J.pos()
		xcor1=p1[0]
		ycor1=p1[1]
		ycor1=ycor1+30
		t1=(xcor1,ycor1)
		barriercheck(t1)
		
	def down():
		p2=J.pos()
		xcor2=p2[0]
		ycor2=p2[1]
		ycor2=ycor2-30
		t2=(xcor2,ycor2)
		barriercheck(t2)
	def right():
		p3=J.pos()
		xcor3=p3[0]
		ycor3=p3[1]
		xcor3=xcor3+60
		t3=(xcor3,ycor3)
		barriercheck(t3)
	def left():
		p4=J.pos()
		xcor4=p4[0]
		ycor4=p4[1]
		xcor4=xcor4-60
		t4=(xcor4,ycor4)
		barriercheck(t4)
	########################################################################################################################
	bob=turtle.Turtle()
	sc=turtle.Screen()
	
	J_list = []
	E_list = []
	movable = []
	coin=[]
	barrier=[]
	bounds=[]
	########################################################################################################
	board = [
	"+--------------------------------------------------------------------+",
	"|                                                                    |",
	"|                                                                    |",
	"| 	  #################################   ##################          |",
	"|                   ###                               ###            |",
	"|                   ###                               ###            |",
	"|                                                     ###            |",
	"|                   ###                               ###            |",
	"|                   ###              #############################   |",
	"|                   ###                       ###           #        |",
	"|        #   E      ###                        #            #        |",
	"|       ###         ###                                     #        |",
	"|      #####        ###                                     #        |",
	"|############## #############################               #        |",
	"|                             ##                            #        |",
	"|                             ##                            #        |",
	"|      #                                #############                |",
	"|      #                            J   ##         ##                |",
	"|      #                      ##                   ###########       |",
	"| 	    #                      ##        ##                           |",
	"| 	    #                      ##        ##                           |",
	"| 	    #     ####################### ################    ############|",
	"| 	    #     ####################### ################     ###########|",
	"| 	    #                                          ##                 |",
	"| 	    #                                          ##                 |",
	"| 	    #                                          ##                 |",
	"|    #######################  ######################         #       |",
	"| 	                                                         ###      |",
	"| 	                                                        #####     |",
	"+--------------------------------------------------------------------+"]

	###########################################################################################
	printboard(board,bob,sc,movable,coin,J_list,E_list,bounds,barrier)
	
	E=turtle.Turtle()
	sc.register_shape("E.gif")
	E.shape("E.gif")
	E.pu()
	E.setpos(E_list[0][0],E_list[0][1])
	E.pd()
	E.speed(1)
		
	for time in range(1,500):
		
		sc.ontimer(jfind,300*time)
		
		

	J=turtle.Turtle()
	sc.register_shape("J.gif")
	J.shape("J.gif")
	J.pu()
	J.setpos(J_list[0][0],J_list[0][1])

	J.speed(10)
	J.pd()
	J.pu()
	J.color("White")
	aldreadydone=[]
	turt=turtle.Turtle()
	turt.pu()
	turt.ht()
	bob.undo()

	sc.listen()
	sc.onkey(up,"w")
	sc.onkey(down,"s")
	sc.onkey(right,"d")
	sc.onkey(left,"a")
	
###############################################################################	
	
	

import turtle



sc1=turtle.Screen()
sc1.screensize(660,250,bg="light yellow")
sc1.setworldcoordinates(-400,-120,260,130)
t1=turtle.Turtle()
t1.pu()
t1.ht()
######################################
t1.pencolor("blue")
t1.setpos(-10,0)
t1.write("Welcome to KIZPSZI's game of \n     'Catch me , If you can'",align="center",font=("calibri",23,"bold"))
############################################
sc1.delay(100)
t1.speed(10)
t1.pencolor("green")
t1.setpos(-290,-100)
t1.write("#NOTE: ELY has superpowers\nhe can appear from anywhere .\nBut GOOD NEWS He till now does not \nknows where is your precise location...\nSo lets begin the fun...",move=True,align="center",font=("calibri",17,"normal"))
#############################################
t1.pencolor("red")
t1.setpos(220,-100)
t1.write("Choose :- \n a for single catcher(ELY),\n b for double cathcher(ELY and FELY),\n c for faster catcher(FASTELY),\n d for catcher who destroys coins.(DESTROYELY)",move=True,align="center",font=("calibri",17,"normal"))
choice=sc1.textinput("CHOOSE", "Your choice of catcher:")
if choice == "a":
	t1.reset()
	round_a()
if choice == "b":
	t1.reset()
	round_b()
if choice == "c":
	t1.reset()
	round_c()
if choice == "d":
	t1.reset()
	round_d()
sc1.exitonclick()




