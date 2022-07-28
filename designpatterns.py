# Notes on Design Patterns
# Creational Patterns
# Abstract Factory - Provide an interface for creating families of related or dependent objects without specifying their concrete classes.
# Builder - Separate the construction of a complex object from its representation so that the
# same construction process can create different representations
# Factory Method - Define an interface for creating an object, but let subclasses decide which class to instantiate. Factory Method
# lets a class defer instantiation to subclasses.
# Prototype - Specify the kinds of objects to create using a prototypical instance, and
# create new objects by copying this prototype.
# Singleton - Ensure a class only has one instance, and provide a global point of access to it.

# Structural Patterns
# Adapter - Convert the interface of a class into another interface clients expect. Adapter 
# lets classes work together that couldn't otherwise because of incompatible interfaces
# Bridge decouple an abstraction from its implementation so that the two can vary independently
# Composite - Compose objects into tree structures to represent part-whole hierarychies.
# composite lets clients treat individuals objects and composition of objects uniformly
# Decorator - Attach additional reposibilities to an object dynammically, decorators 
# provide a flexible alternative to subclassing for extending functionality
# Facade - Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level
# interface making the subsystem easier to use.
# Flyweight - Use sharing to support large numbers of fine-grained objects efficiently
# Proxy - Provide a surrogate or placeholder for another object to control access to it.

# Behavioral Patterns
# Chain of Responsibility - Avoid coupling the sender of a request to its reciever by giving
# more than one object a chance to handle the request. Chain the recieving objects
# and pass the request along the chain until an object handles it.
# Command - Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue
# or log requests, and support undoable operations.
# Interpreter - given a language, define a representationfor its grammar along with an interpreter that uses the representation to
# interpret sentences in the language
# Mediator - Define an object that encapsulates how a set of objects interact. Mediator promots loose coupling by keeping objects from referring to
# each other explicitly, and it lets you vary their interaction independently
# Memento - without violating encapsulation, capture and externalize an object's internal state so that the object can be restored to this state later
# Observer - Define a one-to-many dependency between objects so that when one object changes state,
# all its dependents are notified and updated automatically
# State - Allow an object to alter its behavior when its internal state changes. The object will appear to change its class.
# Strategy - Define a family of algorithms, encapsulate each one, and make them interchangable. Strategy lets the algorithm vary independently
# from clients that use it
# Template Method - Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. redefine certain steps of an algorithm
# without changing the algorithm's structure
# Visitor - Represent an operation to be performed on the elements of an object structure. Visitor lets you define the new operation without changing
# the classes of the elements on which it operates

#Pascal Case for Classes and Inheritance
