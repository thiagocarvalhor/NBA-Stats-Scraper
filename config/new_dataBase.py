from sshtunnel import SSHTunnelForwarder
import psycopg2 as pg


def connectionDataBase():
    # Configurações da conexão SSH
    ssh_host = '52.72.84.46'
    ssh_port = 22
    ssh_username = 'ubuntu'
    ssh_private_key_path = '/home/maya/maya-energy-scraping/config/oem-key.pem'
    #ssh_private_key_path=r"C:\\Users\\saulo\\Downloads\\oem-key.pem"

    # Configurações da conexão PostgreSQL
    db_host = 'maya-db-pg-02.cxucpmthnikd.us-east-1.rds.amazonaws.com'
    db_port = 5432

    # Criar o túnel SSH
    tunnel = SSHTunnelForwarder(
        (ssh_host, ssh_port),
        ssh_username=ssh_username,
        ssh_private_key=ssh_private_key_path,
        remote_bind_address=(db_host, db_port)
    )

    # Iniciar o túnel SSH
    tunnel.start()

    db_user = 'postgres'
    db_password = 'uD631lWZwULeMqafusBs'
    db_name = 'Maya_energy2'
    conn = pg.connect(
        host='localhost',
        port=tunnel.local_bind_port,
        user=db_user,
        password=db_password,
        database=db_name
    )

    print(conn)
    return conn

# def connectionDataBase():
#     connection = pg.connect(user="postgres", password="2023@Tag", host="159.65.42.225", port=5432, database="Maya_energy2")
#     #connection = pg.connect(user="postgres", password="uD631lWZwULeMqafusBs", host="maya-db-pg-02.cxucpmthnikd.us-east-1.rds.amazonaws.com", port=5432, database="maya_energy")
#     #connection = pg.connect(user="postgres", password="postgres", host="localhost", port=5432, database="maya_energy")
#     print(connection)
#     return connection