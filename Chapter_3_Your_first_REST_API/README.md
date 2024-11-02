# Overview of your first REST API

In this section we will make a simple REST API that allows us to:
* Create a store, with a name AND add a list of stocked items
* Create an item in a store, with a name and a price
* Retrieve a list of stores and their items
* Given its name, retrieve an individual store and all its items
* Given a store name, retrieve only a list of its items within it.

#### Install Environment
```bash
python3.10 -m venv .venv
source .venv/bin/activate
pip install Flask
```

This is how the interaction will go !!

### Create store
Request:
```
POST /store {name: 'My Store'}
```
Response:
```
{
  "name": "My Store",
  "items": []
}
```

### Create item
Request:
```
POST /store/My Store/item {name: 'Chair', price: 15.99}
```
Response:
```
{
  "name": "Chair",
  "price": 15.99
}
```

### Retrieve list of stores
Request:
```
GET /stores
```
Response:
```
{
  "stores": [
    {
      "name": "My Store",
      "items": [
        {
          "name": "Chair",
          "price": 15.99
        }
      ]
    }
  ]
}
```

### Get particular store

Request:
``` 
GET /store/My Store
```
Response:
```
{
  "name": "My Store",
  "items": [
    {
      "name": "Chair",
      "price": 15.99
    }
  ]
}
```

### Get items of a particular store

Request:
```
GET /store/My Store/items
```
Response:
```
{
  "items": [
    {
      "name": "Chair",
      "price": 15.99
    }
  ]
}
```