tables_list =(
    """
    CREATE TABLE IF NOT EXISTS users(
        user_id SERIAL PRIMARY KEY, 
        username VARCHAR(150) UNIQUE NOT NULL,
        email VARCHAR(150) UNIQUE NOT NULL,
        password VARCHAR(190) NOT NULL,
        admin_status BOOL DEFAULT False,
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
    
)