import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

sns.set(style="ticks", color_codes=True)

response = ["Stress", "No Stress"]

df = pd.read_csv("./pseudo.csv")
length = 200

times = df.time.values.tolist()
new_t = []
new_act = []
new_f = []
intended = []
i = 0
val = 200
index = 0
on = True
while i < len(times)/3:
	#new_f.append("mean_IBI")
	adddingg = random.uniform(val, val+150)
	new_t.append(adddingg)
	new_f.append("mean_IBI")
	if adddingg > 310:
		if int(adddingg) % 22 == 0 or int(adddingg) % 13 == 0:
			intended.append(response[1])
		else:
			intended.append(response[0])
	elif adddingg >= 260:
		if int(adddingg) % 7 == 0 or int(adddingg) % 11 == 0:
			intended.append(response[1])
		else:
			intended.append(response[0])
	else:
		if int(adddingg) % 22 == 0 and int(adddingg) % 8 == 0:
			intended.append(response[0])
		else:
			intended.append(response[1])
	i = i + 1
	'''
	if i + length < len(times)/3:
		end = i + length
		while i < end and on:
			adddingg = random.uniform(val, val+50)
			new_t.append(adddingg)

			new_f.append("mean_IBI")
			if int(adddingg) % 4 == 0:
				#new_ind = random.randint(0, len(acts)-1)
				#while new_ind == index:
				#	new_ind = random.randint(0, len(acts)-1)
				#new_act.append(acts[new_ind])
				intended.append(response[1])
			else:
				#new_act.append(acts[index])
				intended.append(response[0])

			i = i + 1
		while i < end and not on:
			adddingg = random.uniform(val, val+50)
			new_t.append(adddingg)

			new_f.append("mean_IBI")
			if int(adddingg) % 4 == 0:
				#new_ind = random.randint(0, len(acts)-1)
				#while new_ind == index:
				#	new_ind = random.randint(0, len(acts)-1)
				#new_act.append(acts[new_ind])
				intended.append(response[0])
			else:
				#new_act.append(acts[index])
				intended.append(response[1])

			i = i + 1
		val = val + 50
		#index = index + 1
		on = False
	else:
		while i < len(times)/3:
			adddingg = random.uniform(val, val+50)
			new_t.append(adddingg)
			new_f.append("mean_IBI")
			if int(adddingg) % 4 == 0:
				#new_ind = random.randint(0, len(acts)-1)
				#while new_ind == index:
				#	new_ind = random.randint(0, len(acts)-1)
				#new_act.append(acts[new_ind])
				intended.append(response[1])
			else:
				#new_act.append(acts[index])
				intended.append(response[0])

			i = i + 1
		break
'''
print("Done1")
val = 200
index = 0
on = True
while i < 2* (len(times)/3):
	#new_f.append("max_IBI")
	adddingg = random.uniform(val, val+150)
	new_t.append(adddingg)
	new_f.append("min_IBI")
	if adddingg >= 325:
		intended.append(response[0])
	elif adddingg >= 290:
		if int(adddingg) % 5 == 0 or int(adddingg) % 7 == 0 or int(adddingg) % 6 == 0:
			intended.append(response[0])
		else:
			intended.append(response[1])
	else:
		if (int(adddingg)**2) %23 == 0:
			intended.append(response[0])
		else:
			intended.append(response[1])
	i = i + 1
	'''
	if i + length < 2* (len(times)/3):
		end = i + length
		while i < end and on:
			adddingg = random.uniform(val, val+50)
			new_t.append(adddingg)
			new_f.append("min_IBI")
			if int(adddingg) % 3 == 0:
				#new_ind = random.randint(0, len(acts)-1)
				#while new_ind == index:
				#	new_ind = random.randint(0, len(acts)-1)
				#new_act.append(acts[new_ind])
				intended.append(response[1])
			else:
				#new_act.append(acts[index])
				intended.append(response[0])

			i = i + 1
		while i < end and not on:
			adddingg = random.uniform(val, val+50)
			new_t.append(adddingg)
			new_f.append("min_IBI")
			if int(adddingg) % 3 == 0:
				#new_ind = random.randint(0, len(acts)-1)
				#while new_ind == index:
				#	new_ind = random.randint(0, len(acts)-1)
				#new_act.append(acts[new_ind])
				intended.append(response[0])
			else:
				#new_act.append(acts[index])
				intended.append(response[1])

			i = i + 1
		val = val + 50
		#index = index + 1
		on = False
	else:
		while i < 2* (len(times)/3):
			adddingg = random.uniform(val, val+50)
			new_t.append(adddingg)
			new_f.append("min_IBI")
			if int(adddingg) % 3 == 0:
				#new_ind = random.randint(0, len(acts)-1)
				#while new_ind == index:
				#	new_ind = random.randint(0, len(acts)-1)
				#new_act.append(acts[new_ind])
				intended.append(response[1])
			else:
				#new_act.append(acts[index])
				intended.append(response[0])
			i = i + 1
		break'''
print("Done2")
val = 200
index = 0
while i < 3* (len(times)/3):
	#new_f.append("min_IBI")
	adddingg = random.uniform(val, val+150)
	new_t.append(adddingg)
	new_f.append("max_IBI")
	if int(adddingg) % 5 == 0 or int(adddingg) % 3 == 0:
		intended.append(response[0])
	else:
		intended.append(response[1])
	i = i + 1
	'''
	if i + length < 3* (len(times)/3):
		end = i + length
		while i < end:
			adddingg = random.uniform(val, val+50)
			new_t.append(adddingg)
			new_f.append("max_IBI")
			if int(adddingg) % 4 == 0 or int(adddingg) %3 == 0:
				#new_ind = random.randint(0, len(acts)-1)
				#while new_ind == index:
				#	new_ind = random.randint(0, len(acts)-1)
				#new_act.append(acts[new_ind])
				intended.append(response[1])
			else:
				#new_act.append(acts[index])
				intended.append(response[0])

			i = i + 1
		val = val + 50
		#index = index + 1
	else:
		while i < 3* (len(times)/3):
			adddingg = random.uniform(val, val+50)
			new_t.append(adddingg)
			new_f.append("max_IBI")			
			
			if int(adddingg) % 4 == 0 or int(adddingg) %3 == 0:
				#new_ind = random.randint(0, len(acts)-1)
				#while new_ind == index:
				#	new_ind = random.randint(0, len(acts)-1)
				#new_act.append(acts[new_ind])
				intended.append(response[0])
			else:
				#new_act.append(acts[index])
				intended.append(response[1])
			i = i + 1
		break'''
print("Done3")

#print(len(times))
#print(len(new_t))
#print(len(new_f))

df['Feature Value (IBI in ms)'] = new_t
#df['Activity'] = new_act
df['Feature'] = new_f

df["Intended Stress"] = intended

#lab = ["","Sing-A-Song","", "Rest","", "ColdPressor",""]
sns.catplot(x='Feature Value (IBI in ms)', y='Feature', hue='Intended Stress', kind = "swarm", data=df)
plt.xticks([200,250, 300, 350])#np.arange(min(new_t), max(new_t)+1, 100), labels= lab
#plt.axvline(x=250, color = "grey", linestyle = "--")
#plt.axvline(x=300, color = "grey", linestyle = "--")
props = dict(boxstyle='round', facecolor='lightsteelblue', alpha=0.8)
plt.text(200, -0.4, "Good separability", bbox = props)
plt.text(295, 2.4, "Poor separability",bbox = props)
plt.show()



