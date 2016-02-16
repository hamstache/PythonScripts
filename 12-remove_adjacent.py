def remove_adjacent(nums):
	if len(nums)>1:
		if nums[0] != nums[1]:
			return [nums[0]] + remove_adjacent(nums[1:])
		del nums[1]
		return remove_adjacent(nums)
	else:
		return nums



if __name__ == '__main__':
    print('remove_adjacent')
    print(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    print(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    print(remove_adjacent([]), [])
