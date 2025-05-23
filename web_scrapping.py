"""
This Project is Assignment task given by XPCover Technologies
Position: Cloud-Based Web Data Scripting internship
Name: Vishal Jadhav
Email ID: vishalj2805@gmail.com
Mobile Number: +91 8888882328
"""


import bs4
import requests

web_page = requests.get("https://internshala.com/internships/software-testing-internship/")

soup = bs4.BeautifulSoup(web_page.text, "lxml")

scrapped_data = []
data = soup.select(".internship_meta")

for info in data:
    work_info = {'job_title': info.select("a.job-title-href")[0].text,
                 'company_name': info.select("p.company-name")[0].text.strip(),
                 'location': info.select("div.detail-row-1 div.row-1-item.locations span a")[0].text,
                 'duration': info.select("div.detail-row-1 div.row-1-item i.ic-16-calendar + span")[0].text,
                 'stipend': info.select("div.detail-row-1 span.stipend")[0].text
                 }
    scrapped_data.append(work_info)

for work_data in scrapped_data:
    print("------------------------------------")
    print("Job Title: " + work_data['job_title'] + '\n'
          "Company Name: " + work_data['company_name'] + '\n'
          "Location: " + work_data['location'] +
          " | Duration: " + work_data['duration'] +
          " | Stipend: " + work_data['stipend']
          )
