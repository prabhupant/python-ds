#python3
#program to calculate roots of a polynomial with error of .0001 

#function for polynomial x*x - x -1
def f(number):
	return number*number - number - 1
	
print("Enter values of first_no and second_no on separate line ")
first_no = float(input())
second_no = float(input())
error = .0001

if f(first_no)*f(second_no)>0:
	print("Invalid internal, Root does not exist in it")
else:
		middle = (first_no+second_no)/2
		iteration=1
		print (first_no,second_no,middle,f(middle),f(first_no)*f(middle),iteration)
		while abs(f(middle))>error :
			
			if f(first_no)*f(middle)>0:
				first_no = middle
			else:
				second_no = middle
			middle = (first_no+second_no)/2
			iteration= iteration+1
			print ("first_no = ",first_no,"second_no = ",second_no,"middle = ",middle,"f(middle) = ",f(middle),"f(first_no)*f(middle) = ",f(first_no)*f(middle),"iteration = ",iteration)
		print ("Root of polynomial :",middle)
		
		
'''
Enter values of first_no and second_no on separate line 
1
2
1.0 2.0 1.5 -0.25 0.25 1
first_no =  1.5 second_no =  2.0 middle =  1.75 f(middle) =  0.3125 f(first_no)*f(middle) =  -0.078125 iteration =  2
first_no =  1.5 second_no =  1.75 middle =  1.625 f(middle) =  0.015625 f(first_no)*f(middle) =  -0.00390625 iteration =  3
first_no =  1.5 second_no =  1.625 middle =  1.5625 f(middle) =  -0.12109375 f(first_no)*f(middle) =  0.0302734375 iteration =  4
first_no =  1.5625 second_no =  1.625 middle =  1.59375 f(middle) =  -0.0537109375 f(first_no)*f(middle) =  0.006504058837890625 iteration =  5
first_no =  1.59375 second_no =  1.625 middle =  1.609375 f(middle) =  -0.019287109375 f(first_no)*f(middle) =  0.001035928726196289 iteration =  6
first_no =  1.609375 second_no =  1.625 middle =  1.6171875 f(middle) =  -0.00189208984375 f(first_no)*f(middle) =  3.649294376373291e-05 iteration =  7
first_no =  1.6171875 second_no =  1.625 middle =  1.62109375 f(middle) =  0.0068511962890625 f(first_no)*f(middle) =  -1.2963078916072845e-05 iteration =  8
first_no =  1.6171875 second_no =  1.62109375 middle =  1.619140625 f(middle) =  0.002475738525390625 f(first_no)*f(middle) =  -4.684319719672203e-06 iteration =  9
first_no =  1.6171875 second_no =  1.619140625 middle =  1.6181640625 f(middle) =  0.00029087066650390625 f(first_no)*f(middle) =  -5.503534339368343e-07 iteration =  10
first_no =  1.6171875 second_no =  1.6181640625 middle =  1.61767578125 f(middle) =  -0.0008008480072021484 f(first_no)*f(middle) =  1.515276380814612e-06 iteration =  11
first_no =  1.61767578125 second_no =  1.6181640625 middle =  1.617919921875 f(middle) =  -0.0002550482749938965 f(first_no)*f(middle) =  2.0425490276920755e-07 iteration =  12
first_no =  1.617919921875 second_no =  1.6181640625 middle =  1.6180419921875 f(middle) =  1.7896294593811035e-05 f(first_no)*f(middle) =  -4.5644190649341e-09 iteration =  13
Root of polynomial : 1.6180419921875

'''
