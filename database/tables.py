tables_list =(
    """
    CREATE TABLE IF NOT EXISTS users(
        user_id SERIAL PRIMARY KEY, 
        username VARCHAR(150),
        email VARCHAR(150) UNIQUE,
        password VARCHAR(190),
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