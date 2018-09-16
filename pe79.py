

def func(lst1, lst2):
  lst = lst1 + lst2
  lst = [i for i in lst if i not in lst[i:]]

def main():
    trials = [425, 125, 145, 142]
    #  trials = [str(trials) for trial in trials]
    lst1, lst2 = list(str(trials[0])), list(str(trials[1]))
    for trial in trials:
         trial = list(str(trial))
         new_lst = func(lst1, lst2)
         lst1 = lst2
         lst2 = new_lst
    return new_lst


answer = main()
print answer
