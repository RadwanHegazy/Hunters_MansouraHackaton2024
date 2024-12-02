# Carpooling Project

### Description
`Carpooling` is a sustainable transportation solution that encourages individuals to share rides, reducing the number of vehicles on the road. By coordinating travel with others who have similar routes and schedules, carpooling helps decrease traffic congestion, lower fuel costs, and minimize carbon emissions. It fosters community connections while providing a cost-effective and eco-friendly alternative to solo driving. Whether for daily commutes, school runs, or long-distance travel, carpooling promotes efficient use of resources and contributes to a cleaner environment.


### Persnetation
- [F-sktk Persentation View](https://prezi.com/view/i0FpoxTT7lMX5VGJ8oak/)

### Analysis
- [Google Survey](https://docs.google.com/spreadsheets/d/1N9Gxzo62dyyiPtymEXxngxGjWLPHBKk18L_zb-VyPDE/edit?gid=0#gid=0)
- [Google Survey Form Link](https://tally.so/r/n0bKrQ)



# UI/UX

F-SKTK web application aims to reduce the number of cars on the streets by enabling car owners to share rides with passengers heading to the same destination, promoting safety, reliability, and environmental sustainability by reducing carbon emissions by 20-30%. Designed using Figma and Photoshop, the platform offers a user-friendly interface with features like elders-only and female-only rides, ensuring accessibility for diverse users. The blue color represents trust and reliability, while green symbolizes eco-friendliness, aligning with the application's goal of fostering sustainable transportation solutions.

### User Experince
We ensured the user experience is intuitive and accessible to a broad audience. After signing in, users can choose their role as either a `car owner` or a `passenger` and then complete a verification process specific to their selection, guaranteeing security and reliability.

### Colors
We chose blue to represent **trust and reliability, fostering user confidence, and green to symbolize** **environmental sustainability**, reflecting the app's goal of reducing car usage and lowering carbon emissions by 20-30%.

### Tools
- Figma
- Photoshop
- Google Survey

### Overview
[Figma Design](https://www.figma.com/design/cQoW44Uin7efeIvBjsWEsH/F-Sktk?node-id=0-1&t=imfluyVtUae9mmh3-1)

# Frontend
Working on a carpooling web app, I use React (Next.js) for building the web app, Tailwind CSS for responsive design, and ShadCn components for a styling. My goal is to create an easy-to-use, fast, and good-looking web platform.

### Stack
- Tailwind Css (Styling)
- Shad Cn (Components)
- Typescript
- React ( Next.js )

### Screens
- `/` Landing Page
- `/home` Home
- `/passenger` Passenger
- `/profile` User Profile Page
- `/premium` Premium Features

### CI/CD
- git
- github

### Production
- Vercel


### Server Link
- [Frontend Server URL](https://hunters-mansoura-hackathon2024-uy1b.vercel.app/)



# Backend
In this project i starts for analysis the idea with the team,Then i start to create the db schema in [Drawsql](https://drawsql.app/teams/test-1748/diagrams/f-sktk#), After that I starts to create the db tables and handle relations in my Django project,And I use Sqlite3 as a database, And then i starts to implement the endpoints,Then i test this endpoints and write test cases, Then i push to github and connect to railway.

### Stack:
- `Python` (Programming Language)
- `Django` (Backend Framework)
- `Django Rest Framework` ( APIs )

### Database
- Sqlite3

### Database Schema 
- [Fsktk Schema](https://drawsql.app/teams/test-1748/diagrams/f-sktk#)


### CI/CD
- Git
- Github

### Production
- Railway

### Server Link
- [Backend Server URL](https://web-production-b837.up.railway.app/)


### Endpoints
> Main Feature
- `/journey/get/`
- - For getting all avaliable journies
- - submiited params : from, to

Example Response for `/journey/get?from=cairo&to=alex`

```json
[
    {
        "id": 6,
        "from_place": "cairo",
        "to_place": "alex",
        "start_at": "2024-12-10T10:27:50+02:00",
        "driver": {
            "full_name": "Yasser Ali",
            "picture": "/media/user-pics/profile.png"
        },
        "passengers_count": [
            2
        ],
        "car": {
            "max_passengers_count": 3,
            "car_name": "BMW",
            "car_id": "eee-111",
            "riders": [
                "Khaled Ali",
                "Test User"
            ]
        }
    }
]
```


