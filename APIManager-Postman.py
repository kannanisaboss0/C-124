#--------------------------------------------------------------APIManager-Postman.py--------------------------------------------------------------#

'''
Importing modules:
-jsonify :-flask
-request :-flask
-Flask   :-flask
-datetime
-time (tm)
'''

from flask import jsonify,request,Flask
import datetime
import time as tm

#Printing the welcoming message
print("Welcome to APIManager-Postman.py. We provide services for managing API requests and logistics through Postman")
tm.sleep(2.3)


input_API_boolean=input("Don't know what APIs are?(:- I Know or I Don't Know)")

#Verifying the user's knowledge of APIs
#Case-1
if(input_API_boolean=="I Don't Know" or input_API_boolean=="I don't know" or input_API_boolean=="I don't Know" or input_API_boolean=="I DON'T KNOW" or input_API_boolean=="I Don't know" or input_API_boolean=="i Don't Know" or input_API_boolean=="i don't know" or input_API_boolean=="i don't Know" or input_API_boolean=="i DON'T KNOW" or input_API_boolean=="i Don't know"):
    print("An API, or Application Progamming Interface, is a type of software interface that provides services of softwares.")
    tm.sleep(2.1)

    print("APIs are also capable of facilitating connection between computers or software apparatus.")
    tm.sleep(2.1)

    print("While user interface enables a communicability between a computer and a human, APIs are used for computer-computer interaction.")
    tm.sleep(2.3)

    print("Any document or data that desrcibes the process of building APIs is called an API Specification")
    tm.sleep(1.5)

    print("APIs can be of several types, in several perspectives, such as on the basis of privacy and equivocacy, APIs are of four main types")
    tm.sleep(1.9)

    print("1. Open/Public APIs")
    tm.sleep(0.5)
    print("2. Partner APIs")
    tm.sleep(0.5)
    print("3. Internal/Private APIs")
    tm.sleep(0.5)
    print("4. Composite APIs")
    tm.sleep(1.4)

    print("Many applications and software empower users to model and deploy their own APIs for commercial usage, mostly for free.")
    tm.sleep(2.3)

    print("A prime example is the API hosting and deployment software, Postman.")
    tm.sleep(1.2)

    print("To know more about APIs, visit 'https://en.wikipedia.org/wiki/API'")
    print("To gain access to some of the best examples of APIs, visit 'https://any-api.com/'")

input_postman_boolean=input("Don't know what Postman is(:- I Know or I Don't Know)?")

#Verifying the user's knowledge of Postman
#Case-1
if(input_postman_boolean=="I Don't Know" or input_postman_boolean=="I don't know" or input_postman_boolean=="I don't Know" or input_postman_boolean=="I DON'T KNOW" or input_postman_boolean=="I Don't know" or input_postman_boolean=="i Don't Know" or input_postman_boolean=="i don't know" or input_postman_boolean=="i don't Know" or input_postman_boolean=="i DON'T KNOW" or input_postman_boolean=="i Don't know"):
    print("Postman is an Indian tech start-up developed by software engineers Abhinav Asthana, Ankit Sobti, and Abhijit Kane.")
    tm.sleep(2.3)

    print("Postman was only recently founded in 2014, and hence, is still growing.")
    tm.sleep(1.2)

    print("Postman integrates full support for the life cycle of API management, testing, hosting, and deployment.")
    tm.sleep(2.4)

    print("It is currently being used by over 6 million users and by about 100 thousand organisations worldwide, for assessing and generating APIs.")
    tm.sleep(3.4)

    print("All services in Postman are offered for no price at all, but some are provided in limited capacities.")
    tm.sleep(2.5)

    print("Limitless services can be enabled through a payment of 6-18 USD (445-1135 INR) per user.")
    tm.sleep(1.2)

    print("To know more about Postman, visit 'https://www.postman.com/'")
    print("To download Postman, visit 'https://www.postman.com/downloads/'")

#Pre-usage instructions
print("Before creating an API, knowing a couple of the application functions is integral:")
tm.sleep(1.2)
print("1. The link extension 'add_data', enables the addition of data to the API through postman")
tm.sleep(2.7)
print("2. The link extension 'clear_data', deletes all data groups of the API, except the first one.")
tm.sleep(2.5)
print("3. The link extension 'view_deleted_data', will redirect the output to the deleted data groups.")

print("Loading Data...")
tm.sleep(2.3)

#Asking inputs from the user
number_of_fields=int(input("Please enter the number of fields the initial first API data group should possess(:-data can be added after throught Postman):"))
profile=[]
restored_profile=[]

dict1={}
field_names=[]

dict1.update({"ID":1})

for field_add in range(1,(number_of_fields+1)):
    example_field_label=""
    example_field_value=""

    #Verifying whether the value of the number fields is 1
    #Case-1
    if(field_add==1):
        example_field_label="(Eg. Name)"
        example_field_value="(Eg. Marcus)"
            
    field_label=input("Please enter the label of field name-{}:{}".format(field_add,example_field_label))
    field_names.append(field_label)

    field_value=input("Please enter the value:{}".format(example_field_value))
    dict1.update({field_label:field_value})

    dict1.update({"time":datetime.datetime.now()})

profile.append(dict1)        
         
app=Flask(__name__)

@app.route("/")
def RenderInitialDataDictionary():
    return jsonify({"data":profile})

@app.route("/add_data",methods=["POST"])
def RenderAppendedDictionary():
    dict2={}
    for name in field_names:

        dict2[name]=request.json.get(name,"")
        dict2["time"]=datetime.datetime.now()
        dict2["ID"]=profile[-1]["ID"]+1

    profile.append(dict2) 
    
    return jsonify({
        "message":"Dataset functioned successfully.JSON data appended.",
        "status":"Success",
        "Here is the link updated data set:":profile,
    }) 

@app.route("/clear_data",methods=["POST"])
def RenderDeletedDictionary():
    for element in range(0,(len(profile)-1)):
        pop_element=profile.pop(element)
        restored_profile.append(pop_element)

    return jsonify({
        "Data deleted":"True",
        "data":profile,
        "status":"Success",
        "message":"The data has been deleted. The deleted heirarchy can be viewd in the sub-root 'restored'"
    })

@app.route("/view_deleted_data",methods=["POST"])
def ViewResotredDictionary():
    
    return jsonify({
        "data":[restored_profile]
    })

#Verifying whether the name of the application is "__main__"
if(__name__=="__main__"):
 run=app.run()

#Since, it is not possible to print the ending message, it will be commented below, here:
#Printng the ending message 
#Thank You for using APIManager-Postman.py

#--------------------------------------------------------------APIManager-Postman.py--------------------------------------------------------------#