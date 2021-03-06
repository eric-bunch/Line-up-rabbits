def answer(x, y, n):

	import math
	import scipy
	from scipy import special
	import gc
	
	def grow_tree(tr, level_num, max_level):
		tree_level_list = tr[level_num - 1]
		
		if level_num < max_level:
			for index_l, l in enumerate(tree_level_list):
				number_left = l[2]
				if number_left != 0 and len(l[0]) !=1:
					for index_count, count in enumerate(l[0]):
						if index_count == 0:
							gc.disable()
							tr[level_num].append( [ [0], 
											 	 scipy.special.binom(number_left - 1, count) * math.factorial(number_left - 1 - count), 
											  	 0,  index_l] )				
							gc.enable()
						else:
							if count > max_level - level_num:
								gc.disable()
								tr[level_num].append( [ range(max_level - level_num - 1, count), 
												 	 scipy.special.binom(number_left - 1, count) * math.factorial(number_left - 1 - count), 
												  	 count,  index_l] )	
					  	 		gc.enable()
					  	 	
		elif level_num == max_level:
			for index_l, l in enumerate(tree_level_list):
				number_left = l[2]
				if number_left != 0:
					gc.disable()
					tr[level_num].append( [ [0], math.factorial(number_left - 1), 
										   0, index_l ] )
				   	gc.enable()
	
	def count_tree(tr):
		tr = [l for l in tr if l]
		tree_len = len(tr)
		for i in range(0, tree_len - 1)[::-1]:
			for node_index, node in enumerate(tr[i]):
				child_node_count_list = [l[1] for l in tr[i + 1] if l[3] == node_index]
				if child_node_count_list:
					child_sum = sum( child_node_count_list )
					node[1] *= child_sum
		
		return tr[0][0][1]

	
	def one_side(num, z):
		tree = []
		for i in range(0, z + 1):
			tree.append([])

		if z == 1:
			tree[0] = [ [ [0], 1, num, 0 ] ]
		else:
			tree[0] = [ [ range(z - 1, num), 1, num, 0  ] ]
		
		for i in range(1, z + 1):
			print i
			grow_tree(tree, i, z)
		
		return count_tree(tree)
		

	arrangements = []			
		
	if x + y > n + 1:
		return str(0)
		
	if x == 1 and y != 1:
		ans = one_side(n - 1, y - 1)
		ans = str(int(ans))
		return ans
	elif y == 1 and x != 1:
		ans = one_side(n - 1, x - 1)
		ans = str(int(ans))
		return ans
	elif x == 1 and y == 1 and n != 1:
		return str(0)
	else:	
		for j in range(x - 1, n - y + 1):
#			print j
			left_arrs = one_side(j, x - 1)
			right_arrs = one_side(n - 1 - j, y -1)
			arrangements.append(left_arrs * right_arrs * scipy.special.binom(n - 1, j))
		
		ans = str(int(sum(arrangements)))
		return ans
	

#print answer(9, 10, 20)

"""
def answer2(x, y, n):
	import itertools
	perms = list(itertools.permutations(range(0, n)))
	
	counter = 0


	for p in perms:
		visible_x = 1
		visible_y = 1
	
		for i in range(1, n):
			if p[i] > max(p[:i]):
				visible_x += 1
			
		for j in range(0, n - 1)[::-1]:
			if p[j] > max(p[j + 1:]):
				visible_y += 1
	
		if visible_x == x and visible_y == y:
			counter += 1
	
	counter = str(counter)
	return counter

for n in range(3, 8):
	for x in range(1, 8):
		for y in range(1, 8):
			if answer(x, y, n) != answer2(x, y, n):
				print "Does not match on (x, y, n): ",x,y,n,'\t',"ans1, ans2(correct): ",answer(x,y,n),answer2(x,y,n)
"""

