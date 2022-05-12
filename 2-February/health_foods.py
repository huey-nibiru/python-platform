# 1. create a dictionary of foods
foods = {}


# 2. add healthy foods
foods["apple"]="healthy"
foods["carrot"]="healthy"
foods["beet"]="healthy"
foods["ginger"]="healthy"
foods["turnip"]="healthy"
foods[""]="healthy"


# 3. add unhealthy foods
foods["chips"]="unhealthy"
foods["hot dog"]="unhealthy"
foods["pudding"]="unhealthy"
foods["soda"]="unhealthy"



# 4. Count number of healthy foods
num_healthy = 0
num_unhealthy = 0

for f in foods:
  value = foods[f]
  if value=="healthy":
    num_healthy+=1
  if value=="unhealthy":
    num_unhealthy+=1






print("I have",num_healthy,"healthy foods")
print("I have",num_unhealthy,"unhealthy foods")





# 5. print healthy foods
print("\n...Healthy Foods...")
for f in foods:
  value = foods[f]
  if value=="healthy": print(f)
  
  
# 6. print unhealthy foods
print("\n...Unhealthy Foods...")
for f in foods:
  value = foods[f]
  if value=="unhealthy": print(f)
   
  















