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

This is how the interaction will go:

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

---

# What is JSON?

JSON is just a (usually long) string whose contents follow a specific format. 
One example of JSON is the following:

```json
{
    "key": "value",
    "author": "John Doe",
    "list_data": [1, 2, 3],
    "sub_object": {
        "name": "Jane Doe",
        "age": 25
    }
}
```

So at its core, you've got:

* String
* Number
* Boolean (true/false)
* Lists
* Objects (akin to dictionaries in Python)
        * Note that objects are not ordered, so the key could come back in any order. This is not a problem.

At the top level of pieces of JSON, you can have an object or a list. So this is valid JSON:

```json
[
        {
            "Name": "John Doe",
            "age": 25
        },
        {
            "Name": "Anne Smith",
            "age": 24
        },
        {
            "Name": "Adam Doe",
            "age": 26
        }
]
```
When we return a Python dictionary in a Flask route, Flask automatically turns it into JSON for us, so we don't have to.

Remember that "turning it into JSON" means two things:

1. Change Python keywords and values so they match the JSON standard (e.g. True to true).
2. Turn the whole thing into a single string that our API can return.

:::tip
Note that JSON can be "prettified" (as the above examples), although usually it is returned by our API "not-prettified":

```json
[{"name":"Rolf","age":25},{"name":"Anne","age":27},{"name":"Adam","age":23}]
```
This removal of newlines and spaces, believe it or not, adds up and can save a lot of bandwidth since there is less data to transfer between the API server and the client.
:::