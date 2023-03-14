1.  获取用户token
    To get a token make a request to the auth resource:
    ```bash
    POST /auth HTTP/1.1
    Host: localhost:5000
    Content-Type: application/json

    {
        "username": "joe",
        "password": "pass"
    }
    ```
    The response should look similar to:
    ```bash
    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MSwiaWF0IjoxNDQ0OTE3NjQwLCJuYmYiOjE0NDQ5MTc2NDAsImV4cCI6MTQ0NDkxNzk0MH0.KPmI6WSjRjlpzecPvs3q_T3cJQvAgJvaQAPtk1abC_E"
    }
    ```
2. 使用token请求资源  
    This token can then be used to make requests against protected `chatgpt` endpoints:
    ```bash
    GET /chatgpt HTTP/1.1
    Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MSwiaWF0IjoxNDQ0OTE3NjQwLCJuYmYiOjE0NDQ5MTc2NDAsImV4cCI6MTQ0NDkxNzk0MH0.KPmI6WSjRjlpzecPvs3q_T
    Content-Type: application/json

    {
        "question": "xxxx"
    }
    ```