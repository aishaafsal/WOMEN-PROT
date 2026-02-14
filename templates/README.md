<p align="center">
  <img src="./img.png" alt="Project Banner" width="100%">
</p>

# [Safetour kerala] 🎯

## Basic Details

### Team Name: Amigos

### Team Members
- Member 1: Aisha.A - College of engineering and management punnapra
- Member 2: Anaswara Sheejo - College of engineering and management punnapra

### Hosted Project Link
[mention your project hosted link here]

### Project Description
Displays popular tourist attractions in Kerala.
Includes details about the location, timings, and safety tips.
Restaurants Page:
Lists verified and hygienic restaurants.
Provides contact info, location, and safety ratings.
Homestays & Resorts Page:
Shows safe and budget-friendly accommodation options in Alappuzha.
Includes contact numbers, budget, and type of stay.
Safety Page:
Provides tourist safety guidelines.
Emergency contacts like police, ambulance, and tourist helpline.
Women safety tips and nearest police station information.
SOS Page:
One-click emergency call to police.
WhatsApp alert message for emergencies.
Accessible from mobile and desktop.
Budget Page:
Shows approximate travel and accommodation costs.
Helps tourists plan their budget effectively.
Responsive Navigation:
Easy access to Home, Destinations, Restaurants, Homestays, Budget, Safety, and SOS pages.
Professional and mobile-friendly design.
Technology Stack:
Frontend: HTML, CSS (Responsive and modern layout)
Backend: Python Flask framework
Static Assets: Images, icons, CSS stored in Flask static folder
Deployment (Optional): Can be deployed using platforms like Heroku, PythonAnywhere, or Netlify for static pages.
Significance:
Tourist Safety: Ensures tourists know emergency numbers, safe restaurants, and verified homestays.
Ease of Use: One-stop platform for tourists without searching multiple sources.
Promotes Local Tourism: Showcases verified local accommodations, restaurants, and attractions.
Quick Emergency Response: SOS feature helps tourists during emergencies.
Conclusion:
The SafeTour Kerala website is a practical, user-friendly, and safety-oriented solution for tourists visiting Kerala. It combines travel guidance with emergency services, making it a unique platform for tourists to travel safely, plan better, and enjoy their trip with peace of mind.

### The Problem statement
 Problem Statement – Tourist Safety in Kerala
Tourism is one of the major attractions of Kerala, especially in regions like Alappuzha, which is famous for its backwaters, houseboats, homestays, and cultural experiences. However, tourists often face several challenges:
Lack of Reliable Information:
Tourists struggle to find verified information about safe restaurants, homestays, resorts, and destinations.
Many online sources are outdated, incomplete, or unreliable.
Safety Concerns:
Tourists, especially newcomers, may not know emergency contacts, local police stations, or safety tips.
Women and solo travelers often feel unsafe without proper guidance.
Difficulty in Planning:
Tourists find it difficult to plan budgets, accommodations, and travel routes.
Unorganized information increases the chances of overspending or facing inconvenience.
Emergency Response Issues:
In case of emergencies, tourists may not have quick access to SOS numbers or ways to alert authorities immediately.
Therefore, there is a clear need for a centralized, user-friendly platform that provides:
Verified information about destinations, restaurants, homestays, and resorts
Emergency safety guidelines and contacts
Budget planning assistance
Quick SOS alert feature
 Goal
To create a Tourist Safety Website that addresses these challenges by combining travel information, safety guidance, and emergency support into a single platform for a safe and convenient tourist experience.

### The Solution
Solution – Tourist Safety Website
To address the problems faced by tourists in Kerala, especially in Alappuzha, we propose the development of a centralized, user-friendly website that combines travel information, safety guidance, and emergency support.
 Key Features of the Solution
Verified Tourist Information:
List of popular destinations, restaurants, homestays, and resorts with verified details.
Includes location, contact information, budget range, and safety ratings.
Safety Guidelines & SOS:
Emergency numbers: police, ambulance, tourist helpline.
Women safety tips and nearest police station details.
SOS feature: one-click call to authorities and WhatsApp emergency alert.
Budget Planning Assistance:
Helps tourists estimate travel costs, accommodation expenses, and meal budgets.
User-Friendly Navigation:
Easy access to Home, Destinations, Restaurants, Homestays, Budget, Safety, and SOS pages.
Responsive design for both desktop and mobile users.
Professional and Modern Design:
Cards, images, and hover effects for better readability.
Background images, overlays, and clear headings to improve user experience.
 Benefits of the Solution
Enhances Tourist Safety: Tourists have quick access to emergency contacts and safety tips.
Simplifies Trip Planning: Budget, accommodations, and attractions information in one place.
Promotes Local Tourism: Verified restaurants, homestays, and resorts help local businesses.
Quick Emergency Response: SOS feature provides instant help when needed.

---

## Technical Details

### Technologies
- Languages used: Python, html
- Frameworks used: Flask
- Libraries used: Flask
- Tools used: VS Code, Git

---

## Features
- 1Feature : [DescriptionHTML5 – For creating the structure and content of webpages.
CSS3 – For styling pages, layout, colors, background images, and responsive design.
Bootstrap  – For professional-looking navigation bar, cards, and responsive layout.
2️ Backend:
Python 3 – Programming language used for building the backend logic.
Flask Framework – Lightweight Python web framework to serve pages and handle routing.
Handles page requests like /home, /restaurants, /homestays, /safety, /sos.
Renders HTML templates using render_template.
3️ Static Assets:
Images – Used for background, destinations, homestays, restaurants, and houseboats.
Icons – For SOS, emergency contacts, and navigation buttons.
CSS Files – Stored in Flask static folder for styling and layout.
4️ Development Tools:
VS Code – Code editor used to write Python, HTML, and CSS.
Terminal / Command Line – For running the Flask server using python app.py.
Browser (Chrome, Firefox, etc.) – To view and test the website locally.]

---

## Implementation

#### Installation
```bash
pip install flask
```

#### Run
```bash
python app.py
```

---

## Project Documentation

#### Screenshots (Add at least 3)

![Screenshot1]https://drive.google.com/file/d/1UZAT7FpxsiA5hliaU5-rkiBU0HrP8IYQ/view?usp=drive_link
*Add caption explaining what this shows*

![Screenshot2]https://drive.google.com/file/d/1QdQALXHqtU5MTN8S_PWLOqcKqUFkHNcN/view?usp=drive_link
*Add caption explaining what this shows*

![Screenshot3]https://drive.google.com/file/d/1nwGaE1GpVTiiRyjqyVXDkzsxvJjgY8C8/view?usp=drive_link
*Add caption explaining what this shows*

#### Diagrams

**System Architecture:**

![+------------------+
|      User        |
| (Browser / Mobile)|
+--------+---------+
         |
         v
+------------------+
|   Presentation   |
|  HTML, CSS, JS   |
| Templates folder |
+--------+---------+
         |
         v
+------------------+
|    Backend       |
|   Python Flask   |
|  Routing & Logic |
+--------+---------+
         |
         v
+------------------+
|     Data Layer   |
|  Static / DB     |
+--------+---------+
         |
         v
+------------------+
| External Services|
| Maps, SOS API    |
+------------------+]
1️⃣ Components
A. User / Client Layer
Users access the website via web browsers on desktops or mobile devices.
Interaction points include:
Navigation through Home, Destinations, Restaurants, Homestays, Budget, Safety, SOS pages.
Clicking buttons, submitting forms, and triggering SOS alerts.
B. Presentation Layer (Frontend)
Built using HTML, CSS, and optionally Bootstrap.
Responsible for:
Page layout and structure (home.html, safety.html, etc.)
Styling, images, backgrounds, cards, hover effects
Responsive design for mobile devices
Optional JavaScript for interactive elements (alerts, popups, scroll effects)
C. Application Layer (Backend)
Powered by Python Flask framework.
Responsibilities:
Handles routing: e.g., /home, /restaurants, /homestays, /budget, /safety, /sos.
Renders templates with render_template() function.
Processes dynamic content if data is stored in variables or a database.
Optional logic for SOS alerts and external API calls.
D. Data Layer
Stores all project data:
Static Data: Hardcoded in templates or Python dictionaries (homestays, restaurants, safety contacts).
Dynamic Data (Optional): Can be stored in databases like SQLite, MySQL, or Firebase for scalability.
Data includes: destinations, restaurants, homestays, resorts, emergency contacts, and budget info.
E. External Services (Optional)
Google Maps API – To link locations for destinations, restaurants, and homestays.
WhatsApp / tel: – For SOS alerts in emergencies.
2️⃣ Data Flow
User Request: User opens the website and clicks a link.
Frontend Interaction: The browser sends an HTTP request to the Flask server.
Backend Processing: Flask receives the request and identifies the route.
Data Fetching:
If static: Data is fetched from templates or Python variables.
If dynamic: Data is queried from the database.
Template Rendering: Flask populates the HTML template with the requested data.
Response to User: The browser receives the HTML page and displays it.
External Services: If SOS or maps are triggered, the backend communicates with APIs.
Data Flow Diagram (Text Version):
Copy code

User (Browser)
     │
     ▼
Frontend (HTML, CSS, JS)
     │
     ▼
Backend (Python Flask)
     │
     ├─ Routing: /home, /restaurants, /homestays, /budget, /safety, /sos
     │
     ▼
Data Layer (Static or DB)
     │
     ▼
External Services (Google Maps API, SOS Alerts)
3️⃣ Tech Stack Interaction
Layer / Component
Technology / Framework
Interaction / Role
Frontend
HTML, CSS, Bootstrap, JS
Presents data, handles user interactions
Backend
Python Flask
Receives requests, processes logic, renders templates
Data Layer
Python Variables / DB (SQLite/MySQL)
Stores destinations, homestays, restaurants, safety info
External Services
Google Maps API, WhatsApp/tel
Provides maps, emergency alerts
Development Tools
VS Code, Terminal, Browser
For coding, testing, and running the app
Interaction Flow:
User → Frontend → Backend → Data → Frontend → User
SOS / Maps → Backend → External API → Frontend → User

**Application Workflow:**

![+------------------+
          |   Start / User   |
          | Visits Website   |
          +--------+---------+
                   |
                   v
           +----------------+
           |    Home Page   |
           | Navigation Bar |
           +--------+-------+
                    |
      +-------------+--------------+
      |             |              |
      v             v              v
+-----------+  +-----------+  +-----------+
| Destinations|  | Restaurants|  | Homestays|
+-----------+  +-----------+  +-----------+
      |             |              |
      v             v              v
+-----------+  +-----------+  +-----------+
| Safety Tips|  | Menu Info |  | Contact &|
| & Safety   |  | & Budget  |  | Budget  |
+-----------+  +-----------+  +-----------+
      |
      v
+-----------+
|   SOS     |
| Page      |
+-----------+
      |
      v
    +-------+
    |  End  |
    +-------+](docs/workflow.png)
The flowchart illustrates the structure and workflow of the SafeTour Kerala website, designed to provide a safe and convenient experience for tourists visiting Kerala, especially Alappuzha.
The Start represents the user accessing the website.
The Home Page serves as the central hub with a navigation bar linking to all key sections: Destinations, Restaurants, Homestays, Budget, Safety, and SOS.
Each page displays relevant, verified information:
Destinations: Tourist attractions, descriptions, and safety tips.
Restaurants: Verified dining options with contact and budget info.
Homestays & Resorts: Accommodation details including contact, type, and budget.
Budget: Estimated travel, food, and stay costs.
Safety: Emergency contacts, tips, and SOS link.
SOS: Quick access to emergency services via call or WhatsApp alert.
Users interact with each page to access information or emergency features.
The flow ends when the user exits the website.
This flowchart provides a clear visualization of how users navigate the website and how information is organized to enhance safety, planning, and convenience for tourists.

---

## Project Demo

### Video
https://drive.google.com/file/d/1aDLC6rItWfrR8I8kHLmkyXvgCBklW5vH/view?usp=drive_link

*Explain what the video demonstrates - key features, user flow, technical highlights*

---

## Team Contributions

- Aisha A: Frontend development, API integration,documentation
- Anaswara sheejo:  Backend development, Database design

---

## License

This project is licensed under the [MIT] License - see the [LICENSE](LICENSE) file for details.

---

Made with ❤️ at TinkerHub
