# given bytes in hexadecimal
hex_bytes = input('write hexadecimal number in 2 nibble set(example: aa 12 3b..)')
bytes_list = [int(x, 16) for x in hex_bytes.split()]

#initialize variables
decoded_numbers =[]
current_number = 0
shift_amount = 0

#decode each byte
for byte in bytes_list:
	value= byte & 0x7f #bit mask
	current_number |= (value << shift_amount) #bit shift
	shift_amount += 7 #move to the next 7 bits
	
	if (byte & 0x80) == 0: # chcek if the top-most bit is 0
		decoded_numbers.append(current_number)
		current_number = 0 #reset the current number
		shift_amount = 0 #reset the shift amount
		
print(decoded_numbers)
