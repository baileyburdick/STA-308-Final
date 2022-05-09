# STA-308-Final
The purpose of this assignment is to calculate the difference in unemployment between March 2021 and March 2022. Then, I am calculating the mean, standard deviation, and coefficient of variation for this difference. Lastly I put this information into a table. I uploaded this assignment in R and in Python. 

A- The coefficient of variation is the standard deviation divided by the mean. This represents the relative dispersion of data around the mean, or the ratio between standard deviation and the mean. 

B- The average unemployment rate is highest for West (2.15), followed by Northeast (2.11), South (1.54), and Midwest(1.34). The average unemployment rate is lowest in the midwest. This could be due to the amount of farms and industry that supply jobs. Also, the midwest draws people due to the average cost of living and central location. The largest coefficient of variation is West (0.42) followed by Northeast (0.35), Midwest (0.34), and South (0.32). In this case, a lower CV is ideal because it means the unemployment in the states of each region is more condensed. In this case. south has the best CV. It has the most condensed unemployment rates while West has the mleast condensed unemployment rates. Since midwest has the lowest mean and the second lowest CV, it is the best region to live in (not at all biased).


C-

| Functionality              	| R                	| Python                              	|
|----------------------------	|------------------	|-------------------------------------	|
| Import a package           	| library(package) 	| import 'package'                    	|
| Filter out data            	| filter()         	| newdf = df[df ['Column'] != "data"] 	|
| Merge data frames together 	| merge()          	| df.merge()                          	|
| Remove columns from data   	| select(-column)  	| df.loc()                            	|
| Group by certain data      	| group_by         	| df.groupby                          	|
| Summarize                  	| summarize()      	| ['column'].agg('statistics')        	|
| standard deviation         	| sd()             	| std()                               	|
| Average or mean            	| mean()           	| mean()                              	|
| Read in data               	| read_csv('')     	| read_csv('')                        	|

D- I really enjoyed everything we did with the COVID data. I enjoyed this because it was easy to understand and it was really relevant. It helped me understand what was happening with COVID in Ohio. Additionally, what we learned was really fun and it made me excited for my career in analytics. 
