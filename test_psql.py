from http import HTTPStatus

def test_create_request(client):
    data = {
        "table": "student",
        "columns":{
            "id": "serial primary key",
            "title": "varchar(100)"
          }
    }
    url = "/tables/create"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.OK

def test_create_fail_request(client):
    data = {
        "table": "",
        "columns":{
            "id": "serial primary key",
            "title": "varchar(100)"
          }
    }
    url = "/tables/create"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR


def test_insert_request(client):
    data = {
        "table": "student",
        "values":{
             "id": "21",
             "title": "john"
             }
    }
    url = "/insert"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.OK     

def test_insert_request_fail(client):
    data = {
        "table": "",
        "values": {
            "id": "21",
            "title": "john"
            }
    }
    url = "/insert"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR  

def test_update_request(client):
    data = {
        "table": "student",
        "values": {
            "id": "21",
            "title": "makhay"
            },
        "where": {
            "id": "21"
            }
    }
    url = "/update"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.OK

def test_update_fail_request(client):
    data = {
        "table": "",
        "values": {
            "id": "21",
            "title": "makhay"
            },
        "where": {
            "id": "21"
            }
    }
    url = "/update"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR  
    
def test_execute_request(client):
    data = {
        "query": "select * from student where name=%(username)s",
        "data": {
            "title": "john"
            }
    }
    url = "/execute"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR  
        
        
def test_execute_fail_request(client):
    data = {
        "query": "select * from student12 where name=%(username)s",
        "data": {
            "title": "john"
            }
    }
    url = "/execute"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR  

def test_delete_request(client):
    data = {
        "table": "student",
        "where": {
            "id": "21"
            }
    }
    url = "/delete"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.OK

def test_delete_fail_request(client):
    data = {
        "table": "",
        "where": {
            "id": "21"
            }
    }
    url = "/delete"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR     

def test_select_request(client):
    data = {
        "table": "student",
        "where": {
            "id": "21"
            }
    }
    url = "/select"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.OK  

def test_select_fail_request(client):
    data = {
        "table": "",
        "where":{
            "id": ""
            }
    }
    url = "/select"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR  

def test_drop_request(client):
    data = {
        "table": "student",
    }
    url = "/tables/drop"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.OK   

def test_drop_fail_request(client):
    data = {
        "table": "",
      
    }
    url = "/tables/drop"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR      