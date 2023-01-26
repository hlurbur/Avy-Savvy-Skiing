# Avy-Savvy-Skiing

                                                - AVY SAVVY SKIING - 
This program scrapes the avalanche forecast from the Northwest Avalanche Center (NWAC) website and analyzes backcountry ski routes to pick the safest ski route for the day given the avalanche forecast. The program then sends the chosen routes along with the daily avalanche forecast in an automated email to program users. 

This program aims to increase safety in the backcoutry by ruling out dangerous routes when conditions are unsafe and automatically suggesting safe alternative routes from a database of routes. 

This program analyzes the most basic element of the avalanche forecast provided by NWAC: below treeline danger level, near treeline danger level, and above treeline danger level. 

The avalanche danger scale is: low (1) moderate (2) considerable (3) high (4) extreme (4)

Each treeline level is given a danger forecast for the day which indicates the likelihood of an avalanche occurring in avalanche terrain given the snowpack. So, the decision to ski a route is based upon wether or not the route enters an elevation band with a high danger level, and more importantly wether or not the route enters avalanche terrain (a slope with an angle of 30 degrees or higher). Routes logged by users in a google sheet are used to create skiRoute objects which contain attributes indicating what treeline bands they enter as well as if they enter avalanche terrain. This data is used to choose the safest routes for a given forecast. 


PROJECT DETAILS:

This project has four main components:

1.) Webscraping
2.) Data Management
3.) Route Analysis
4.) Email Automation

1.) WEBSCRAPING:

scraper.py executes the webscraping and uses selenium chromedriver to open a chrome webpage and scrape the avalanche forecast for a specific region of the north cascades using beautiful soup. Scraper contains one main scraping method which takes a URL to scrape and can be used to to scrape each region's NWAC forecast page when passed the URL. The scraper searches the soup to locate the forecast for each elevation level, below, near and above, and returns a list of the forecasted danger levels as strings.

2.) DATA MANAGEMENT:
Data for the program consists of user data and route data, both of which are stored in a public google sheet. Using the unique google sheet ID and URL, the program creates a pandas data frame from the sheet csv which can then be read line by line. Sheets.py has two methods, readInRoutes() and readInUsers(). ReadInRoutes reads in the users google sheet data row by row, creating a user object from each row of data. Each user has a name, associated region they want to ski in, and email address. 

ReadInRoutes() reads from the routes google sheet and creates a skiRoute object from each row of data. Each route has boolean and integer data fields indicating which treeline bands it enters, if it enters avalanche terrain, and integer values for fun and risk. ReadInRoutes() and readInUsers return a list of skiRoute objects, and a list of user objects, respectively. 

3.) ROUTE ANALYSIS:
The route analysis component of this program happens in analyzeRoutes.py. To choose routes to ski, first we must get the forecast for a region given the name of a region. This happens in get_regionForecast(). This calls a specific scraper method and returns the forecast. Next, makeForecastNumerical() converts the string forecast into a numerical forecast for easy analysis.

ChooseRoutes() brings together these helper methods to choose the best ski routes for the day by following a set of criteria:
    1.)Never ski a route which crosses though a treeline band with a danger level of considerable or above if the route enters avalanche terrain. 
    2.)If the danger level is moderate, do not ski a route with a risk level above 6, or a route in which avalanche terrain is unavoidable. 
    3.) Of the remaining safe routes, suggest routes with the highest fun rating. 

Choose routes functions by adding all routes in the users region to a list called goodRoutes. If a route is unsafe (eg. meets on of the un skiable criteria above) it is removed from goodRoutes. After removing all of the unsafe routes given the forecast at each treeline band, return the top three most fun of the remaining routes in a list called top3. 

4.) EMAIL AUTOMATION:
The final component of the this project was setting up an email account and sending automatic emails from the account. Emailer.py uses the SMTP library which provides methods to automatically send emails. Additionally, MIMEText and MIMEMultipart libraries provide methods to populate the receiver and subject lines of an email, as well as to format the body of the email. 

Google's two factor authentification presented a challenge because it prevents outside applications from logging into the gmail account. Instead of a regular password, emailer.py uses an app password to log in to the account and get around two factor authentification. 

SendEmail() takes in the route suggestion as well as a link to an NWAC region's forecast page. After formatting the body of the email, sendEmail() creates a secure SMTP connection, logs into the AvyScraper@gmail.com account, and send the email with the message. 


Finally main.py simply brings everything together by iterating through the users of the program, scraping the forecast from the users region, choosing routes for them, and sending the user an email. And Voila! now you know what to ski to go on today! 


#######
HOW TO RUN THE PROGRAM:
1.) Download necessary packages:
    * selenium
    * bs4
    * pandas
    * email.mime.text
    * email.mime.multipart
    * smtplib
2.) Download a chrome driver and customize the pathname in scraper.py to your chromedriver path (line 15)
3.) Add yourself as a user in the google sheet and add your ski routes to the routes sheet!
    
    google sheet link: https://docs.google.com/spreadsheets/d/1M4zSa9Osun8BaQos3dhi97FRa74uo5EJjaIh3NV7-3U/edit#gid=744851719


#######
IMPORTANT NOTES
1.) When entering data in the google sheet, each route and user row must be complete (every cell is filled with the correct data type)
2.) Region names are not caps sensitive but MUST be spelled correctly
