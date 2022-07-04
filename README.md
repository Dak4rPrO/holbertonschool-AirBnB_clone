# holbertonschool-AirBnB_clone
-------------------------------------------------------
BaseModel
__init__ -> key is a update and created set a datetime

Save -> update the update_at and created_at set datetime
To_Dict -> set a isoformat at update_at and create_at
---------------------------------------------------------
MODELS
ENGINE
FILESOTRAGE, to manage correctly serializaiton and deseroalization of all classes, place, city, state, review, amenity

FileStorage -> class to store objects in JSON strings file_path
    (str): path of the JSON file objects
    (dict): stores all objects by class
all -> save all the objects
new -> sotre all objects by class name.id
save -> serialized objects to the JSON file (path: file_path)
  In this method serlized object of python for share files more easly.
  From a DataBase an develpoment can share a file in this format JSON for later...
reload -> deserealized the JSON file to objects
-------------------------------------------------------
CONSOLE
eof -> quit the command to exit
quit -> quit the program
emptyline -> display menssage to help

ACTIONS OF CONSOLE TO FILESTORAGE
---------
do_create -> create an new instance of class of basemodel and save in JSON

do_updated -> updated an insntance based on the class name and id by adding or updating attribute

do_destroy -> deletes an instance based on the class name and id, sabe thechange into de JSON file

do_show -> print the string representation of an instance based on the class name  and id

do_all -> print all string epresentation of all instances based or not in theclass name
-------------------------------------------------------
Class inherit from BaseModel
-state
-city
-amenity
-place
-review
