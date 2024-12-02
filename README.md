
# Backend Docs

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



