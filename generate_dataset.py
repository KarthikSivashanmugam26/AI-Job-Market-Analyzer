import pandas as pd
import random

job_titles = [
    "Data Scientist","Data Analyst","ML Engineer","AI Engineer",
    "Data Engineer","NLP Engineer","Computer Vision Engineer",
    "Business Analyst","Research Scientist"
]

locations = [
    "Bangalore","Hyderabad","Chennai","Pune","Delhi",
    "Mumbai","Remote","Kolkata"
]

skills_list = [
    "Python","SQL","Machine Learning","Deep Learning",
    "TensorFlow","PyTorch","Power BI","Tableau",
    "Spark","AWS","NLP","Computer Vision"
]

data = []

for i in range(10000):

    job = random.choice(job_titles)
    location = random.choice(locations)

    skills = ",".join(random.sample(skills_list,3))

    salary = random.randint(60000,180000)

    data.append([job,location,skills,salary])

df = pd.DataFrame(
    data,
    columns=["job_title","location","skills","salary"]
)

df.to_csv("jobs.csv",index=False)

print("Dataset created with 10,000 rows")