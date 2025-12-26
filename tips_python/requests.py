'''
Common HTTP methods in REST APIs
-------------------------------------------------------------------------------------------------


POST  -  Create new resource

PUT   -  Update (replace) entire existing resource

PATCH -  Update only resource partially (only specific fields)


-----------------------------------------------------------------------------------------------

POST is Not Idempotent

PUT, PATCH are Idempotent

-------------------------------------------------------------------------------------------------


For a successfull api call 

    200 OK for GET, PUT, PATCH
    201 Created  for POST


'''