def longest(seq):
	max_char = ''
	prev_char = ''
	max_count = 0
	for current in seq:
		if prev_char == current:
			count += 1
		else:
			count = 1
		if count > max_count:
			max_count = count
			max_char = current
		prev_char = current
	dict = {max_char: max_count}
	print (max_char)
	print(max_count)
longest('AABCCDEEDDDDBBBBB')