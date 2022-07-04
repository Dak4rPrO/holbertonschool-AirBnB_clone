# holbertonschool-AirBnB_clone

1models directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
2tests directory will contain all unit tests.
console.py file is the entry point of our command interpreter.
3models/base_model.py file is the base class of all our models. It contains common elements:
attributes: id, created_at and updated_at
methods: save() and to_json()
4models/engine directory will contain all storage classes (using the same prototype)