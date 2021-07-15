###########
# CLIENT/ #
###########

##########
# Task 3 #
##########
Endpoint - /client/

Request - GET
Data Return -  [
                  {
                      "fullname": "Himzy Khandelwaal",
                      "client_details": "http://localhost:8000/client/4555785955/"
                  }
               ] 

Request  - POST
Data Posted - { 
	            "first_name" : "Shubhanshu",
	            "last_name"  : "Jayker",
	            "email"      : "shubh@gmail.com",
	            "mobile_number" : 4556785955
              }
              
Endpoint - /client/<int:pk>/   # here pk is mobile_number

Request - GET
Data Return - {
                 "mobile_number": 4555785955,
                 "first_name": "Himzy",
                 "last_name": "Khandelwaal",
                 "email": "him@gmail.com",
                 "registration_date": "2021-07-13"
              } 


--x----x----x----x----x----x----x----x----x----x----x----x----x----x---


############
# VEHICLE/ #
############

ENDPOINT - /vehicle/

Request - GET
Data Return -     {
                      "vehicle_number": "mu2221",
                      "license_status": false,
                      "vehicle_owner": "http://localhost:8000/client/4556785955/",
                      "gps_imei": 4562856483,
                      "license_start": "2021-07-13",
                      "license_end": "2022-07-13",
                      "vehicle_category": "Stockyard",
                      "vehicle_type": "Tractor",
                      "total_permits": 0,
                      "installation_type": "Renewal with existing hardware",
                      "registration_date": "2021-07-13"
                  }
Request - POST
Data Posted - {
                       "vehicle_number": "mu2221",
                       "vehicle_owner_id" : 4555785955 ,   # mobile number
                       "gps_imei": 4562856483,
                       "license_start": "2021-07-13",
                       "vehicle_category": "Stockyard",
                       "vehicle_type": "Tractor",
                       "installation_type": "Renewal with existing hardware",
                   }
##########
# Task 3 #
##########

ENDPOINT - /vehicle/permits/
Request - GET
Data Reutrn - 	[ 
	              {
	                   "vehicle_number": "my4880",
	                   "vehicle_owner": "Shubhanshu Jayker",
	                   "vechicle_permits": [
	                       {
	                           "permit_date": "2021-07-13T10:43:26.358847Z",
	                           "permit_number": "asdf4569df"
	                       }
	                   ],
	                   "gps_imei": 123456799,
	                   "license_start": "2021-07-13",
	                   "license_end": "2022-07-13",
	                   "vehicle_category": "DMG",
	                   "vehicle_type": "Tipper",
	                   "total_permits": 1,
	                   "installation_type": "Migration",
	                   "registration_date": "2021-07-13"
	              }
               	]

ENDPOINT - /vehicle/<int:pk>/   # here pk is vehicle_number
Request - GET

Data Return - {
                 "vehicle_number": "my1234",
                 "license_status": true,
                 "vehicle_owner": {
                     "mobile_number": 4556785955,
                     "first_name": "Shubhanshu",
                     "last_name": "Jayker",
                     "email": "shubh@gmail.com",
                     "registration_date": "2021-07-13"
                 },
                 "gps_imei": 123456779,
                 "license_start": "2021-07-13",
                 "license_end": "2022-07-13",
                 "vehicle_category": "DMG",
                 "vehicle_type": "Tipper",
                 "total_permits": 0,
                 "installation_type": "Migration",
                 "registration_date": "2021-07-13"
              }

Request - PUT
Data Posted - {
                  "vehicle_number": "mu2221",
                  "vehicle_owner_id" : 4555785955 ,   # mobile number
                  "gps_imei": 4562856483,
                  "license_start": "2021-07-13",
                  "vehicle_category": "Stockyard",
                  "vehicle_type": "Tractor",
                  "installation_type": "Renewal with existing hardware",
              }

Request - DELETE
Data Returns - Status 204 No Content


--x----x----x----x----x----x----x----x----x----x----x----x----x----x---


###########
# Task 6a #
###########
ENDPOINT - /vehicle/csv/   
Request - GET

Data Returns - Downloadable Csv file.


--x----x----x----x----x----x----x----x----x----x----x----x----x----x---
###########
# PERMIT/ #
###########

ENDPOINT - /permit/

Request - GET
Data Return  - [
                  {
                      "permit_number": "asdf4568df",
                      "vehicle": {
                          "vehicle_number": "mu2221",
                          "vehicle_owner": "Shubhanshu Jayker",
                          "gps_imei": 4562856483,
                          "vehicle_category": "Stockyard",
                          "vehicle_type": "Tractor"
                      },
                      "loading_point": "Civil Lines",
                      "unloading_point": "Indira Market",
                      "quanity": 85.4,
                      "permit_date": "2021-07-13T10:23:54.728242Z"
                  }
               ]

Request - POST
Data Posted -   {
                    "permit_number": "asdf4569df",
                    "vehicle_id" : "kk4880",
                    "loading_point": "Civil Lines",
                    "unloading_point": "Indira Market",
                    "quanity": 90.4
                } 

ENDPOINT - /vehicle/<int:pk>/   # here pk is permit_number 

Request - GET
Data Return - {
                 "permit_number": "asdf4569df",
                 "vehicle": {
                     "vehicle_number": "kk4880",
                     "vehicle_owner": "Himzy Khandelwaal",
                     "gps_imei": 1232856583,
                     "vehicle_category": "Stockyard",
                     "vehicle_type": "Lorry"
                 },
                 "loading_point": "Civil Lines",
                 "unloading_point": "Indira Market",
                 "quanity": 90.4,
                 "permit_date": "2021-07-13T10:34:04.940107Z"
              }

Request - PUT
Data Posted - {
                 "permit_number": "asdf4569df",
                 "vehicle_id": "my4880",
                 "loading_point": "Civil Lines",
                 "unloading_point": "Indira Market",
                 "quanity": 90.4
              } 
Request - DELETE
Data Returns - Status 204 No Content

##########
# Task 5 #
##########

Endpoint - api/rest-auth/login/
Data Returns - Tokens and extra user information.

Data - {
          "key": "39d23d77794ef5ad1bd26db75c34b070d07edba4",
          "user": {
              "id": 1,
              "last_login": "2021-07-13T16:10:18.802672Z",
              "username": "process",
              "email": "",
              "first_name": "",
              "last_name": ""
          }
       }



