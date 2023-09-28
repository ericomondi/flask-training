from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)   

# Database connection function
def get_connection():
    return psycopg2.connect(
        host='127.0.0.1',
        database='duka',
        user='postgres',
        password='2345'
    )
# get table data

def get_data():
        
        conn = get_connection()
        # Create a cursor
        cursor = conn.cursor()

        # here we etrieve data from the table and return them as records
        
        cursor.execute(f"SELECT * FROM products")
        products = cursor.fetchall()
        conn.close

        return products


# Function to insert a new product into the database
def insert_product(product_name, buying_price, selling_price, stock_quantity):
    conn = get_connection()
    cursor = conn.cursor()
    
    # SQL query to insert data
    insert_query = "INSERT INTO products (product_name, buying_price, selling_price, stock_quantity) VALUES (%s, %s, %s, %s)"
    
    # Tuple containing values to insert
    data = (product_name, buying_price, selling_price, stock_quantity)
    
    try:
        cursor.execute(insert_query, data)
        conn.commit()
    except Exception as e:
        # Handle any errors here
        print("Error:", e)
        conn.rollback()
    finally:
        conn.close()

# Route for handling form submission
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Retrieve form data
        product_name = request.form["product_name"]
        buying_price = float(request.form["buying_price"])
        selling_price = float(request.form["selling_price"])
        stock_quantity = int(request.form["stock_quantity"])

        # Insert the product into the database
        insert_product(product_name, buying_price, selling_price, stock_quantity)

        # Redirect to the index page to show the updated product list
        return redirect(url_for("index"))

    # Fetch product data from the database
    records = get_data()
    
    return render_template("bootstrap.html", products=records)

if __name__ == '__main__':
    app.run(debug=True)


    