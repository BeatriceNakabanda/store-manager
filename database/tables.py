from werkzeug.security import generate_password_hash

# password = generate_password_hash("password123")
tables_list =(
    """
    CREATE TABLE IF NOT EXISTS users(
        user_id SERIAL PRIMARY KEY, 
        username VARCHAR(150) UNIQUE NOT NULL,
        email VARCHAR(150) UNIQUE NOT NULL,
        password VARCHAR(190) NOT NULL,
        role  VARCHAR(100),
        registered_at TIMESTAMPTZ DEFAULT NOW()  
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS categories(
        category_id SERIAL PRIMARY KEY,
        category_name VARCHAR(35) UNIQUE
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS products(
        product_id SERIAL PRIMARY KEY,
        product_name VARCHAR(150) UNIQUE,
        price INTEGER,
        quantity INTEGER,
        category_id INT references categories(category_id), 
        date_added TIMESTAMPTZ DEFAULT NOW()
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS sales(
        sale_id SERIAL PRIMARY KEY,
        product_id INT references products(product_id),
        user_id INT references users(user_id),
        quantity INTEGER,
        total INTEGER
    )
    """,
    # """
    # INSERT INTO users (username, email,password, role) 
    # VALUES ('admin', 'admin@gmail.com', '{}', 'admin')
    # """.format(password)
    
)