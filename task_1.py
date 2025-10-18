def get_index_of_sum(nums, target):
    for l in range(len(nums)):
        for r in range(l + 1, len(nums)):
            if nums[l] + nums[r] > target:
                break
            if nums[l] + nums[r] == target:
                return f'Indexes: [{l}, {r}]'

    return "No indexes found"


try:
    a = list(map(int, input("Write your array with elements divided by commas: ").split(',')))
    target = int(input("Write your target number: "))
    print(get_index_of_sum(a, target))
except Exception:
    print("Invalid input")

