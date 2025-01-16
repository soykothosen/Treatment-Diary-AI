import mysql.connector

# Step 1: Establish a Connection to the MySQL Database
def connect_to_db():
    connection = mysql.connector.connect(
        host="localhost",  # Replace with your MySQL host
        user="root",       # Replace with your MySQL username
        password="",  # Replace with your MySQL password
        database="DiseaseMedicineDB"
    )
    return connection

# Step 2: Fetch Medicines for a Given Disease
def get_medicines_by_disease(disease_name):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()

        # SQL Query to Fetch Medicines
        query = "SELECT medicine_name FROM DiseaseMedicine WHERE disease_name = %s"
        cursor.execute(query, (disease_name,))

        # Fetch Results
        results = cursor.fetchall()
        medicines = [row[0] for row in results]

        if medicines:
            return medicines
        else:
            return f"No medicines found for the disease '{disease_name}'."

    except mysql.connector.Error as error:
        return f"Error: {error}"
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Step 3: Test the Functionality
if __name__ == "__main__":
    print("Welcome to the Disease-Medicine Finder!")
    disease = input("Enter the disease name: ").strip()

    # Fetch Medicines
    medicines = get_medicines_by_disease(disease)

    # Display Results
    if isinstance(medicines, list):
        print(f"Medicines for {disease}: {', '.join(medicines)}")
    else:
        print(medicines)
