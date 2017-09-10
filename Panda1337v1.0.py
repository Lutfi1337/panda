def clear ():
    import os
    os.system('cls')
def IPK():
    def daftar():
        print ("")
        print ("")
        print ("\tPanel Count IPK")
        print ("\n=================================")
        print ("")
        print ("\nChoose : ")
        for IPK in ["1. Count Your Ipk (D4)","2. Count Your Ipk (D3)","3. Back","4. Exit"]:
            print IPK
        print ("")
        
    def back_menu():
        print ('Do you want to try again? [Y/N] :')
        back = raw_input().upper()
        if back == "Y":        #<LUTFI HARIDHA>
            try:
                clear()
                daftar()
                pilihan()
            except:
                print "Please Input Number Only!!"
                back_menu()
        elif back == "N":
            exit
        else:
            print "Pilih Y [untuk mencoba lagi], Pilih N [exit]"
            back_menu()    
        
    def pilihan():
        x = input ("Input Your Choose : ")
        if x == 1:
        #<LUTFI HARIDHA>
			opoiki = raw_input("What Your Name: ")
			a = input("Input Your IP Value Semester 1: ")
			b = input("Input Your IP Value Semester 2: ")
			c = input("Input Your IP Value Semester 3: ")
			d = input("Input Your IP Value Semester 4: ")
			e = input("Input Your IP Value Semester 5: ")
			f = input("Input Your IP Value Semester 6: ")
			g = input("Input Your IP Value Semester 7: ")
			h = input("Input Your IP Value Semester 8: ")
			kkm = input("Dah berapa semseter : ")
			l = a+b+c+d+e+f+g+h
			p = l / kkm
			if p > 3.50:
				print "Selamat, untuk", opoiki, "dapat cumlaude karena IPK mu ", p
				if kkm < 8:
						print("sementara ya")
			elif p > 3.20 and p <=3.50:
				print ("Lumayan lah karena IPK mu "), p
				if kkm < 8:
					print("sementara ya")
			elif p > 3.00 and p <=3.20: 
				print ("Standar karena IPK mu "), p
				if kkm < 8:
						print("sementara ya")
			elif p > 2.70 and p <=3.00:
				print ("Jauh bed IPK mu karena IPK mu "), p
				if kkm < 8:
						print("sementara ya")
			else:
				print ("Gak usah kuliah lagi aja cuk karena IPK mu "), p
				if kkm < 8:
						print("sementara ya")
			back_menu()
        if x == 2:

			opoiki = raw_input("What Your Name: ")
			a = input("Input Your IP Value Semester 1: ")
			b = input("Input Your IP Value Semester 2: ")        #<LUTFI HARIDHA>
			c = input("Input Your IP Value Semester 3: ")
			d = input("Input Your IP Value Semester 4: ")
			e = input("Input Your IP Value Semester 5: ")
			f = input("Input Your IP Value Semester 6: ")
			kkm = input("Dah berapa semseter : ")
			l = a+b+c+d+e+f
			p = l / kkm
			if p > 3.50:
				print "Selamat, untuk", opoiki, "dapat cumlaude karena IPK mu ", p
				if kkm < 8:
						print("sementara ya")
			elif p > 3.20 and p <=3.50:
				print ("Lumayan lah karena IPK mu "), p
				if kkm < 8:
					print("sementara ya")
			elif p > 3.00 and p <=3.20: 
				print ("Standar karena IPK mu "), p
				if kkm < 8:
						print("sementara ya")
			elif p > 2.70 and p <=3.00:
				print ("Jauh bed IPK mu karena IPK mu "), p
				if kkm < 8:
						print("sementara ya")
			else:
				print ("Gak usah kuliah lagi aja cuk karena IPK mu "), p
				if kkm < 8:
						print("sementara ya")        #<LUTFI HARIDHA>
			back_menu()
            
        elif x==3:
            clear()
            back_utama()
    
        elif x==4:
            exit


        else:
            print "You input nothing found in choose !!"
            print ("")
            back_menu()


    try:        
        daftar()
        pilihan()
    except:
        print "Please Input Number Only!!"
        back_menu()
def mtk():
    def daftar2():
        print ("")
        print ("")
        print ("\tPanel Panda1337")
        print ("\n=================================================")
        print ("")
        print ("\nChoose : ")
        for MataUang in ["1. Increment (+)","2. Reduction (-)","3. Multiplication (*)","4. Division (/)","5. Back","6. Exit"]:
            print MataUang
        print ("")        #<LUTFI HARIDHA>
        
	def back_menu2():
		print ('Do you want to try again? [Y/N] :')
		back = raw_input().upper()
		if back == "Y":
			try:
				clear()
				daftar2()
				pilihan2()
			except:
				print "Please Input Number Only!!"
				back_menu2()
		elif back == "N":
			exit
		else:
			print "Pilih Y [untuk mencoba lagi], Pilih N [exit]"
			back_menu2()   
		
    def pilihan2():
        p = input ("Input Your Choose : ")
        if p == 1:
			a = input("Input Your Value: ")
			b = input("Input Your Value: ")
			hasil = a + b
			print ("Your increment Result : "), hasil
			print ("\n=================================================")
			print ("")
			back_menu2()


        elif p == 2:
			a = input ("Input Your Value: ")
			b = input ("Input Your Value: ")
			hasil = a - b
			print ("Your Reduction Result : "), hasil
			print ("\n=================================================")
			print ("")
			back_menu2()
        #<LUTFI HARIDHA>

        elif p == 3:
			a = input ("Input Your Value: ")
			b = input ("Input Your Value: ")
			hasil = a * b
			print ("Your Multiplication Result : "), hasil
			print ("\n=================================================")
			print ("")
			back_menu2()


        elif p == 4:
			a = input ("Input Your Value: ")
			b = input ("Input Your Value: ")
			hasil = a / b
			print ("Your Division Result : "), hasil
			print ("\n=================================================")
			print ("")
			back_menu2()
            
        elif p==5:
            clear()
            back_utama()


        elif p==6:
            exit


        else:
            print "You input nothing found in choose !!"
            print ("")
            back_menu2()


    try:
        daftar2()
        pilihan2()
    except:
        print "Please Input Number Only!!"
        back_menu2()
def KonversiPanjang():
    def daftar3():
        print ('')
        print ('')
        print ('\t\tTranslate')
        print ('\n========================================================')
        print ('')
        print ('\nChoose : ')
        for panjang in ('1. IND - ENG','2. IND - JPN','3. Back To First Menu','4. Exit'):
            print panjang
        print ('')

    def back_menu3():
        print ('Do you want to try again? [Y/N] :')
        back = raw_input().upper()
        if back == "Y":
            try:
                clear()
                daftar3()
                pilihan3()
            except:
                print "Please Input Number Only!!"
                back_menu3()
        elif back == "N":
            exit
        else:
            print "Pilih Y [untuk mencoba lagi], Pilih N [exit]"
            print ('')
            back_menu3()


    def pilihan3():    
        p = input ("Input Your Choose : ")
        if p == 1:
			x = int(input(' Masukan Angka Yang Mau di Artikan : '))
			sokinggris = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 
					11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 
					21: 'twenty-one', 22: 'twenty-two', 23: 'twenty-three', 24: 'twenty-four', 25: 'twenty-five', 26: 'twenty-six', 27: 'twenty-seven', 28: 'twenty-eight', 29: 'twenty-nine', 30: 'thirty', 
					31: 'thirty-one', 32: 'thirty-two', 33: 'thirty-three', 34: 'thirty-four', 35: 'thirty-five', 36: 'thirty-six', 37: 'thirty-seven', 38: 'thirty-eight', 39: 'thirty-nine', 40: 'forty', 
					41: 'forty-one', 42: 'forty-two', 43: 'forty-three', 44: 'forty-four', 45: 'forty-five', 46: 'forty-six', 47: 'forty-seven', 48: 'forty-eight', 49: 'forty-nine', 50: 'fifty', 
					51: 'fifty-one', 52: 'fifty-two', 53: 'fifty-three', 54: 'fifty-four', 55: 'fifty-five', 56: 'fifty-six', 57: 'fifty-seven', 58: 'fifty-eight', 59: 'fifty-nine', 60: 'sixty', 
					61: 'sixty-one', 62: 'sixty-two', 63: 'sixty-three', 64: 'sixty-four', 65: 'sixty-five', 66: 'sixty-six', 67: 'sixty-seven', 68: 'sixty-eight', 69: 'sixty-nine', 70: 'seventy', 
					71: 'seventy-one', 72: 'seventy-two', 73: 'seventy-three', 74: 'seventy-four', 75: 'seventy-five', 76: 'seventy-six', 77: 'seventy-seven', 78: 'seventy-eight', 79: 'seventy-nine', 80: 'eighty', 
					81: 'eighty-one', 82: 'eighty-two', 83: 'eighty-three', 84: 'eighty-four', 85: 'eighty-five', 86: 'eighty-six', 87: 'eighty-seven', 88: 'eighty-eight', 89: 'eighty-nine', 90: 'ninety', 
					91: 'ninety-one', 92: 'ninety-two', 93: 'ninety-three', 94: 'ninety-four', 95: 'ninety-five', 96: 'ninety-six', 97: 'ninety-seven', 98: 'ninety-eight', 99: 'ninety-nine', 100: 'one hundred'}
			x in sokinggris
			print ("")
			print (sokinggris.get(x))
			print ("\n=================================================")
			print ("")
			back_menu3()
        #<LUTFI HARIDHA>
        elif p == 2:
			x = int(input(' Masukan Angka Yang Mau di Artikan : '))
			wibu = {1: 'Ichi', 2: 'Ni', 3: 'San', 4: 'Shi/yon', 5: 'Go', 6: 'Roku', 7: 'Shichi', 8: 'Hachi', 9: 'Kyuu/ku', 10: 'juu', 
					11: 'juu ichi', 12: 'juu ni', 13: 'juu san ', 14: 'juu yon ', 15: 'juu go ', 16: 'juu roku ', 17: 'juu nana ', 18: 'juu hachi ', 19: 'juu kyuu ', 20: 'ni juu ', 
					21: 'ni juu ichi ', 22: 'ni juu ni ', 23: 'ni juu san', 24: 'ni juu yon ', 25: 'ni juu go', 26: 'ni juu roku', 27: 'ni juu nana ', 28: 'ni juu hachi ', 29: 'ni juu kyuu ', 30: 'san juu ', 
					31: 'san juu ichi ', 32: 'san juu ni ', 33: 'san juu san ', 34: 'san juu yon ', 35: 'san juu go ', 36: 'san juu roku ', 37: 'san juu nana ', 38: 'san juu hachi ', 39: 'san juu kyuu ', 40: 'yon juu ', 
					41: 'yon juu ichi ', 42: 'yon juu ni ', 43: 'yon juu san ', 44: 'yon juu yon ', 45: 'yon juu go ', 46: 'yon juu roku ', 47: 'yon juu nana', 48: 'yon juu hachi', 49: 'yon juu kyuu ', 50: 'go juu ', 
					51: 'Go juu ichi ', 52: 'Go ju ni ', 53: 'Go juu san ', 54: 'Go juu yon ', 55: 'Go juu go ', 56: 'Go juu roku ', 57: 'Go juu nana ', 58: 'Go juu hachi ', 59: 'Go juu kyuu ', 60: 'Roku juu ', 
					61: 'Roku juu ichi', 62: 'Roku juu ni', 63: 'Roku juu san', 64: 'Roku juu yon', 65: 'Roku juu go ', 66: 'Roku juu roku ', 67: 'Roku juu nana ', 68: 'Roku juu hachi ', 69: 'Roku juu kyuu ', 70: 'Nana juu ', 
					71: 'Nana juu ichi ', 72: 'Nana juu ni ', 73: 'Nana juu san ', 74: 'Nana juu yon ', 75: 'Nana juu go ', 76: 'Nana juu roku ', 77: 'Nana juu nana', 78: 'Nana juu hachi ', 79: 'Nana juu kyuu ', 
					80: 'Hachi juu ', 81: 'Hachi juu ichi ', 82: 'Hachi juu ni', 83: 'Hachi juu san', 84: 'Hachi juu yon', 85: 'Hachi juu go', 86: 'Hachi juu roku', 87: 'Hachi juu nana', 88: 'Hachi juu hachi', 89: 'Hachi juu kyuu', 
					90: 'Kyuu juu', 91: 'Kyuu juu ichi', 92: 'Kyuu juu ni', 93: 'Kyuu juu san',  94: 'Kyuu juu yon', 95: 'Kyuu juu go', 96: 'Kyuu juu roku', 97: 'Kyuu juu nana', 98: 'Kyuu juu hachi', 99: 'Kyuu juu kyuu', 100: 'Hyaku'}
			x in wibu
			print ("")
			print (wibu.get(x))
			print ("\n=================================================")
			print ("")
			back_menu3()
            
        elif p == 3:
            clear()
            back_utama()


        elif p==4:
            exit
        
        else:
            print "You input nothing found in choose !!"
            print ("")
            back_menu3()
        
    try:
        daftar3()
        pilihan3()
    except:
        print "Please Input Number Only!!"
        back_menu3()


def daftar_utama():
    print ("")        #<LUTFI HARIDHA>
    print ("")
    print ("\tPanel Panda1337")
    print ("\n============================")
    print ("")
    print ("\nChoose : ")
    for Menu_Utama in ["1. Count IPK","2. Calculators","3. Translation","4. Exit"]:
        print Menu_Utama
    print ("")
    
def back_utama():
    print ('Do you want to first menu? [Y/N] :')
    back2= raw_input().upper()
    if back2=="Y":   
        try:        #<LUTFI HARIDHA>
            clear()
            daftar_utama()
            pilihan_utama()
        except:
            clear()
            print "Please Input Number Only!!"
            back_utama()
    elif back2=="N":
        exit
    else:
        print "Pilih Y [untuk mencoba lagi], Pilih N [exit]"
        back_utama()
        
def pilihan_utama():
    q=input ("Input Your Choose : ")
    if q==1:
        IPK()
    elif q==2:
        mtk()
    elif q==3:
        KonversiPanjang()
    elif q==4:
        exit
    else:        #<LUTFI HARIDHA>
        clear()
        print "You input nothing found in choose !!"
        print ""
        back_utama()
            


try:
    daftar_utama()
    pilihan_utama()
except:
    print "Please Input Number Only!!"
    back_utama()
