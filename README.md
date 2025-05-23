# XPCover Technologies Internship Assignement
## - By Vishal Jadhav
### Software Tester | vishalj2805@gmail.com | +91 8888882328

XPCoverWebScrappingProject Project scrapes data from Internshala website. The data scrapped is Intership details with 
- Title
- Company Name
- Location
- Duration
- Stipend

Libraries used for this Project is:
- bs4 (Beautiful Soup)
   bs4 library is used to scrape the data from web page
- requests
   requests library is used to get the page data
- lxml
   lxml library is used to parse the data

Here the Flow of scrapping the data:
1. Use requests library to get the data of a web page
2. Store the web page data from step 1 in Beautiful Soup object with  passing 'lxml' as a feature in argument
3. Declare a List Variable
4. Scrape the data and store it in List Variable, each data will be stored as dictionary
5. Print the data in a neat format



