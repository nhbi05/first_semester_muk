marks={"2201":30,"2202":80,"2203":45,"2204":27,"2205":31,
 "2206":31,"2207":32,"2208":90,"2209":45,"2210":45}



mean =sum(marks.values())/len(marks)
#mode
#print(f"the best student is {best_student}")
#print(f"the best student is {mean}")
#print(f"the best student is {mode}")
import statistics
#best_performance = max(marks.values())
best_student = max(marks,key=marks.get)
print(best_student,mean)
mean_mark = statistics.mean(marks.values())
print("mean mark:",mean_mark)
mode_mark = statistics.mode(marks.values())
print("modemark",mode_mark)

mode_mark1 = max(set(marks.values()),key=lambda x:
list(marks.values()).count(x))
print("Mode mark", mode_mark)
print(dir(tuple))