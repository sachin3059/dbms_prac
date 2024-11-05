from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# Establish the connection to MongoDB
def create_connection():
    try:
        client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.3.3")
        client.admin.command('ping')
        print("Connected to MongoDB successfully!")
        return client
    except ConnectionFailure as e:
        print("Could not connect to MongoDB:", e)
        return None

# CRUD Operations
def add_document(collection, data):
    """Add a document to the collection, ensuring no duplicates."""
    try:
        existing_document = collection.find_one({"name": data["name"], "city": data["city"]})
        if existing_document:
            print("Duplicate document found. No new document added.")
        else:
            result = collection.insert_one(data)
            print(f"Document added with id: {result.inserted_id}")
    except Exception as e:
        print(f"An error occurred while adding the document: {e}")

def delete_document(collection, query):
    """Delete a document matching the query."""
    try:
        result = collection.delete_one(query)
        if result.deleted_count > 0:
            print("Document deleted.")
        else:
            print("No document found matching the query.")
    except Exception as e:
        print(f"An error occurred while deleting the document: {e}")

def update_document(collection, query, new_values):
    """Update a document matching the query."""
    try:
        result = collection.update_one(query, {"$set": new_values})
        if result.modified_count > 0:
            print("Document updated.")
        else:
            print("No document found matching the query.")
    except Exception as e:
        print(f"An error occurred while updating the document: {e}")

def show_all_documents(collection):
    """Show all documents in the collection."""
    try:
        documents = collection.find()
        for doc in documents:
            print(doc)
    except Exception as e:
        print(f"An error occurred while showing documents: {e}")

# Menu Display and Execution
def menu():
    print("\nMenu:")
    print("1. Add Document")
    print("2. Show All Documents")
    print("3. Update Document")
    print("4. Delete Document")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

if __name__ == "__main__":
    client = create_connection()
    
    if client:
        db = client["practical"]
        collection = db["Sample"]
        
        while True:
            choice = menu()

            if choice == '1':
                name = input("Enter name: ")
                age = int(input("Enter age: "))
                city = input("Enter city: ")
                add_document(collection, {"name": name, "age": age, "city": city})

            elif choice == '2':
                print("All documents in the collection:")
                show_all_documents(collection)

            elif choice == '3':
                name = input("Enter the name of the document to update: ")
                field = input("Enter the field to update (e.g., age, city): ")
                new_value = input("Enter the new value: ")
                
                # Convert the value to int if updating age
                if field == "age":
                    new_value = int(new_value)
                
                update_document(collection, {"name": name}, {field: new_value})

            elif choice == '4':
                name = input("Enter the name of the document to delete: ")
                delete_document(collection, {"name": name})

            elif choice == '5':
                print("Exiting program.")
                break

            else:
                print("Invalid choice. Please enter a valid option.")
        
        client.close()



# use practical;

# db.createCollection("Sample");
# db.Sample.find();



#python -m pip install pymongo


