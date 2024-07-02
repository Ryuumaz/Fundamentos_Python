txt = ''
nums = [10, 11]

if nums:
    print("Um")
if not txt:
    print("Dois")
    txt = 'abc'
    nums = []
else:
    print("Três")
    txt = 'xey'
    nums[-1:] = [12]
        
txt = txt.replace('a', '').replace('e', '')
print("Quatro" if len(nums) else "Cinco")
print(txt if len(nums) == 0 else nums)
