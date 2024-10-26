from azure.cosmos import CosmosClient, exceptions, PartitionKey

#Obtener las variables de entorno
Cosmos_endpoint = 'https://dbjafdev.documents.azure.com:443/'
cosmos_key = 'chFx77YDSmgHgVtHlo4C9gtk1U7nfwHu6sZne5uMNUd6wIayaLTAxD4i3ZtxIdFB3mEp0ciBY2uPACDbzWyHkw=='
database_name = 'Test_db'
Container_Name = 'retail'

#inicializar el cliente de Cosmos DB
client= CosmosClient(Cosmos_endpoint, cosmos_key)


#Crear o obtener la base de datos
database = client.create_database_if_not_exists(id=database_name)


#Crear o obtener el contenedor
container = database.create_container_if_not_exists(
    id=Container_Name,
    partition_key=PartitionKey(path="/id"),
    offer_throughput=400

)