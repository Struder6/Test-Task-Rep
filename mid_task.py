# ЗАДАНИЕ: Поиск дубликатов в массиве
# Напишите функцию, которая принимает список чисел и возвращает количество повторений каждого элемента.
def main(lst):
  nums = []
  answer = dict()
  for i in lst:
    if i not in nums and lst.count(i) > 1:
      nums.append(i)
      answer[i] = lst.count(i)
  
