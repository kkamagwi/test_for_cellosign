# ABOUT

Here should be everything about the project

## OPEN PROJECT

### Docker

make image 
```
 % docker build -t cellosign .
```
make container
```
% docker-compose up -d --build
% docker-compose up
```
stop 
```
% docker-compose down -v   
```


## Description of methods
BASIC_URI
`http://127.0.0.1:8000/api/v1/statistic/`
### GET
To get all data
`statistic/get/`

To get timedelta between start date and end date
`get/?timestamp=&start_date=2021-06-11&end_date=2021-06-14`
as example 2021-06-11 is start date and 2021-06-14 is end date

To order you can use any field and -field to reverse `get/?end_date=2021-06-14&ordering=views&start_date=2021-06-11&timestamp=`
here is ordering by views, but you can make any
### POST
to create new instance 
`statistic/create/`
### DELETE
Use delete request to flash all instances
`statistic/delete/`

### mistakes/no mistake

**.gitignore** - to show every step of project you need to see files which should originally be hiden, such as .env 