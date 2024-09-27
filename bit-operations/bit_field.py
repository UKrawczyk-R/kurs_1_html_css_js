#!/usr/bin/env python3



def mask(bit_field, field_size):
	mask =((1<< len(bit_field))-1)
	mask= mask << int(field_size[0]) -1
	mask=bin(mask).replace("0b","")
	
	mask=str(mask).rjust(8,'0')
	
	print('mask: ',mask)
	return mask
	

def answers():
	while True:
		bits = input('enter a 8-bit sequence: ')
		for i in bits:
			if i not in {'1','0'}:
				print("must only contains 0's and 1's ")
				break
			
		if len(bits) != 8:
			print("must be an 8 bit")
		else:
			break
	valid=False
	while valid is False:
		field_size =input('Enter bit numbers of the bit field that interested you (counting from 1 from the right): ')
		is_first=True
		prev_digit=''
		for i in field_size:
			if i.isdigit() is not True:
				print('Enter only numbers.')
				print('')
				break 	
			elif int(i) <= 0 or int(i) > 8:
				print('The digits must be between 1 and 8.')
				print('')
				break 
			elif is_first is True:
				is_first = False
			elif (int(i) != (int(prev_digit)+1)) and is_first is False:
				print('Enter digits in ascending order for example: 123.')
				break
			else:
			valid = True
			prev_digit=i
	return field_size, bits	
#end def answer

def revers_mask(mask):
	print('')
	print('cleaning filed to exchanging the bit fields')
	print('')
	mask=int(mask, 2)
	revers_mask= 255^mask
	revers_mask=bin(revers_mask).replace("0b","")
	revers_mask=str(revers_mask).rjust(8,'0')
	print('revers mask:    ',revers_mask)
	
	return revers_mask
	
def new_field(field_size):
	while True:
		chosen_field=input('enter new bits sequence to replace old chosen bit field: ')
		for i in bits:
			if i not in {'1','0'}:
				print("must only contains 0's and 1's ")
				break
			
		if len(chosen_field) != len(field_size):
			print("must be exactly the same digits length like in your original bit field")
		else:
			break
	chosen_field= int(chosen_field, 2)
	return chosen_field
		
	


bit_field=[]
field_size, bits = answers()
for i in field_size:
	reverse_bits= bits[::-1]
	i=int(i)
	i=reverse_bits[i-1]
	bit_field.append(i)

bit_field= ''.join(bit_field) # join list to one number
bit_field=bit_field[::-1] #reverse number
print('bit field:  ',bit_field)
print('for:  ', bits)

bits=''.join(bits)

mask=mask(bit_field, field_size)
camuflage= int(bits, 2) & int(mask, 2)
camuflage=bin(camuflage)

print('extracted field:' , camuflage)

revers_mask= revers_mask(mask)

camuflage_revers_mask= int(bits, 2) & int(revers_mask, 2)
camuflage_revers_mask=bin(camuflage_revers_mask)
print('for byte:       ', bits)
print('cleaned field:' , camuflage_revers_mask)

	
chosen_field= new_field(field_size)

chosen_field =chosen_field << int(field_size[0]) -1
chosen_field=bin(chosen_field)


new_bits= int(chosen_field, 2) | int(camuflage_revers_mask, 2)
new_bits=bin(new_bits)[2:]
print('chosen field on position'+field_size+': '+chosen_field)
print('old bit sequence: ', bits)
print('new bit sequence: ',new_bits)

