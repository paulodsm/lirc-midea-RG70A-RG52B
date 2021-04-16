# -*- coding: utf-8 -*-
import sys

# This script generates lirc raw codes for Midea remote controls RG70A / RG52B
#####################################

#fan, cool, heat, auto 
mode_list=['fan','cool','heat']

#auto, low, med, max
fan_list=['low','med','max']

#17 to 30 + 'off' for fan and off commands
temp_list=[17,18,19,20,21,22,23,24,25,26,27,28,29,30]

#generating signals for state=ON (turn on or modify settings)
state='on'

#####################################

for mode in mode_list:

	for fan in fan_list :
	
		j=0
		while j < len(temp_list):
		
			temp = temp_list[j]

			header='10110010'
			_mode={'fan':'0100','cool':'0000','heat':'1100','auto':'1000'}
			_fan={'auto':'1011','low':'1001','med':'0101','max':'0011'}
			_temp={17:'0000',18:'0001',19:'0011',20:'0010',21:'0110',22:'0111',23:'0101',24:'0100',25:'1100',26:'1101',27:'1001',28:'1000',29:'1010',30:'1011','off':'1110'}
			_state={'on':'1111','off':'1011'}

			if state=='off': temp='off'
			
			if mode=='fan':
				temp='off'
				j=len(temp_list)  #takes a value out of range to run once, as fan has no temperature
			

			data=header+_fan[fan]+_state[state]+_temp[temp]+_mode[mode]

			#print (data)

			raw=''

			for k in range(2):
				raw=raw+'4421 4421 '

				#1o byte
				i=0
				while i <= 7:
					if data[i] == '1': raw=raw+'553 1658 '
					if data[i] == '0': raw=raw+'553 553 '
					i+=1
					
				#1o byte invertido
				i=0
				while i <= 7:
					if data[i] == '0': raw=raw+'553 1658 '
					if data[i] == '1': raw=raw+'553 553 '
					i+=1

				#2o byte
				i=8
				while i <= 15:
					if data[i] == '1': raw=raw+'553 1658 '
					if data[i] == '0': raw=raw+'553 553 '
					i+=1

				#2o byte invertido
				i=8
				while i <= 15:
					if data[i] == '0': raw=raw+'553 1658 '
					if data[i] == '1': raw=raw+'553 553 '
					i+=1

				#3o byte
				i=16
				while i <= 23:
					if data[i] == '1': raw=raw+'553 1658 '
					if data[i] == '0': raw=raw+'553 553 '
					i+=1

				#2o byte invertido
				i=16
				while i <= 23:
					if data[i] == '0': raw=raw+'553 1658 '
					if data[i] == '1': raw=raw+'553 553 '
					i+=1

				#trail_pulse
				raw=raw+'553 '

				#repeat_gap
				raw=raw+'5220 '

			raw=raw[:-6]
				
			print ('name S.' + state + '-M.' + mode + '-F.' + fan + '-T.' + str(temp) + '\n\t' + raw + '\n')
			
			j+=1

#signals for toggle silent/LEDs off button
raw_silent='4421 4421 553 1658 553 553 553 1658 553 1658 553 553 553 1658 553 553 553 1658 553 553 553 1658 553 553 553 553 553 1658 553 553 553 1658 553 553 553 1658 553 1658 553 1658 553 1658 553 553 553 1658 553 553 553 1658 553 553 553 553 553 553 553 553 553 1658 553 553 553 1658 553 553 553 1658 553 553 553 553 553 553 553 553 553 1658 553 1658 553 553 553 553 553 1658 553 1658 553 1658 553 1658 553 553 553 553 553 1658 553 5220 4421 4421 553 1658 553 553 553 1658 553 1658 553 553 553 1658 553 553 553 1658 553 553 553 1658 553 553 553 553 553 1658 553 553 553 1658 553 553 553 1658 553 1658 553 1658 553 1658 553 553 553 1658 553 553 553 1577 553 553 553 553 553 553 553 553 553 1658 553 553 553 1658 553 553 553 1578 553 553 553 553 553 553 553 553 553 1658 553 1658 553 553 553 553 553 1576 553 1658 553 1658 553 1658 553 553 553 553 553 1658 553'
print ('name silent\n\t' + raw_silent + '\n')

#signals for state=OFF
raw_off='4421 4421 553 1658 553 553 553 1658 553 1658 553 553 553 553 553 1658 553 553 553 553 553 1658 553 553 553 553 553 1658 553 1658 553 553 553 1658 553 553 553 1658 553 1658 553 1658 553 1658 553 553 553 1658 553 1658 553 1658 553 553 553 553 553 553 553 553 553 1658 553 553 553 553 553 1658 553 1658 553 1658 553 553 553 553 553 553 553 553 553 553 553 553 553 553 553 553 553 1658 553 1658 553 1658 553 1658 553 1658 553 5220 4421 4421 553 1658 553 553 553 1658 553 1658 553 553 553 553 553 1658 553 553 553 553 553 1658 553 553 553 553 553 1658 553 1658 553 553 553 1658 553 553 553 1658 553 1658 553 1658 553 1658 553 553 553 1658 553 1658 553 1658 553 553 553 553 553 553 553 553 553 1658 553 553 553 553 553 1658 553 1658 553 1658 553 553 553 553 553 553 553 553 553 553 553 553 553 553 553 553 553 1658 553 1658 553 1658 553 1658 553 1658 553'
print ('name off\n\t' + raw_off + '\n')
