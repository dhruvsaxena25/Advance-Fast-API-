# **Fast API Notes**

# **HTTP Methods**

| **Method** | **Action** | **Idempotent** | **Use Case**        |
| ---------------- | ---------------- | -------------------- | ------------------------- |
| GET              | Read data        | ✅ Yes               | Fetch data from server    |
| POST             | Create data      | ❌ No                | Submit forms, create item |
| PUT              | Update data      | ✅ Yes               | Full update of a resource |
| DELETE           | Delete data      | ✅ Yes               | Remove a resource         |

# **HTTP Methods Code**

| **Category**      | **Code** | **Meaning**               | **Description**                               |
| ----------------------- | -------------- | ------------------------------- | --------------------------------------------------- |
| **Informational** | 100            | Continue                        | Request received, continuing process.               |
|                         | 101            | Switching Protocols             | Protocol switching requested by client.             |
|                         | 102            | Processing                      | Server has received and is processing the request.  |
|                         | 103            | Early Hints                     | Hints user agent to preload resources.              |
| **Success**       | 200            | OK                              | Request succeeded.                                  |
|                         | 201            | Created                         | Resource created successfully.                      |
|                         | 202            | Accepted                        | Request accepted but not yet processed.             |
|                         | 203            | Non-Authoritative Information   | Returned meta-information not from origin server.   |
|                         | 204            | No Content                      | Request succeeded but no content to return.         |
|                         | 205            | Reset Content                   | Request succeeded, client should reset view.        |
|                         | 206            | Partial Content                 | Partial content returned (used for range requests). |
| **Redirection**   | 300            | Multiple Choices                | Multiple response options.                          |
|                         | 301            | Moved Permanently               | Resource moved permanently.                         |
|                         | 302            | Found                           | Resource temporarily moved.                         |
|                         | 303            | See Other                       | Response can be found under a different URI.        |
|                         | 304            | Not Modified                    | Resource not modified since last request.           |
|                         | 307            | Temporary Redirect              | Resource temporarily moved, same method.            |
|                         | 308            | Permanent Redirect              | Resource permanently moved, same method.            |
| **Client Errors** | 400            | Bad Request                     | Malformed request.                                  |
|                         | 401            | Unauthorized                    | Authentication required.                            |
|                         | 402            | Payment Required                | Reserved for future use.                            |
|                         | 403            | Forbidden                       | Server refuses to authorize.                        |
|                         | 404            | Not Found                       | Resource not found.                                 |
|                         | 405            | Method Not Allowed              | HTTP method not supported.                          |
|                         | 406            | Not Acceptable                  | Cannot produce content requested.                   |
|                         | 407            | Proxy Authentication Required   | Proxy authentication needed.                        |
|                         | 408            | Request Timeout                 | Request took too long.                              |
|                         | 409            | Conflict                        | Request conflict with server state.                 |
|                         | 410            | Gone                            | Resource no longer available.                       |
|                         | 411            | Length Required                 | Content-Length header required.                     |
|                         | 412            | Precondition Failed             | Preconditions in headers not met.                   |
|                         | 413            | Payload Too Large               | Request body too large.                             |
|                         | 414            | URI Too Long                    | URI too long to process.                            |
|                         | 415            | Unsupported Media Type          | Media type not supported.                           |
|                         | 416            | Range Not Satisfiable           | Requested range not satisfiable.                    |
|                         | 417            | Expectation Failed              | Expectation header not met.                         |
|                         | 418            | I'm a teapot                    | April Fools' joke from RFC 2324.                    |
|                         | 422            | Unprocessable Entity            | Semantic errors in request.                         |
|                         | 425            | Too Early                       | Request sent too early.                             |
|                         | 426            | Upgrade Required                | Client must switch to a different protocol.         |
|                         | 429            | Too Many Requests               | Rate limiting applied.                              |
| **Server Errors** | 500            | Internal Server Error           | Generic server error.                               |
|                         | 501            | Not Implemented                 | Server lacks functionality to fulfill request.      |
|                         | 502            | Bad Gateway                     | Invalid response from upstream server.              |
|                         | 503            | Service Unavailable             | Server is temporarily overloaded or down.           |
|                         | 504            | Gateway Timeout                 | Upstream server did not respond in time.            |
|                         | 505            | HTTP Version Not Supported      | Server does not support requested HTTP version.     |
|                         | 511            | Network Authentication Required | Client must authenticate to gain network access.    |

# **Fast API**

- FastAPI is a high-performance, modern web framework for building APIs with Python, based on standard Python type hints.
- **The key features are**

  - **Fast:** Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). One of the fastest Python frameworks available.
  - **Fast to code:** Increase the speed to develop features by about 200% to 300%. *
  - **Fewer bugs:** Reduce about 40% of human (developer) induced errors. *
  - **Intuitive:** Great editor support. Completion everywhere. Less time debugging.
  - **Easy:** Designed to be easy to use and learn. Less time reading docs.
  - **Short:** Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
  - **Robust:** Get production-ready code. With automatic interactive documentation.

# Wokring of Fast API:

![Alt text](fastapi-1.png "fastapi wokring")

1) **Web Server**

- **Purpose:** Acts as the first point of contact for incoming HTTP requests.
- **Functionality:** Receives client requests (like a browser or another server making an API call) and forwards them to the ASGI application.
- **Example:** Popular web servers include Nginx, Apache, or Caddy. In Python, this is often handled by Uvicorn or Hypercorn for ASGI applications.

```bash
POST /predict HTTP/1.1
Host: api.example.com
Content-Type: application/json
Content-Length: 45

{
    "feature1": 5.2,
    "feature2": 3.1
}
```

- **Role in FastAPI:** The web server listens on a port (e.g., 8000) and routes incoming HTTP requests to the ASGI layer.

2) **ASGI (Asynchronous Server Gateway Interface)**

- **Purpose:** Bridges the web server and the application code, handling the lifecycle of each request.
- **Why ASGI:** It is the asynchronous evolution of WSGI (Web Server Gateway Interface), designed to handle long-lived connections like WebSockets alongside regular HTTP traffic.
- **Flow (from above image):**

  * Receives the incoming HTTP request.
  * Converts it into a structured format that the FastAPI application can understand.
  * Passes it to the API code for processing.
  * Collects the response and sends it back to the web server for final delivery to the client.
  * **Benefits:** Non-blocking, scalable, and allows background tasks and real-time functionality.

3) **API Code (FastAPI)**

- **Purpose:** Contains the actual logic for processing incoming requests and returning appropriate responses.
- **Key Features:**

  * **Request Parsing:** Extracts JSON data into a Pydantic model (Features).
  * **Processing:** Runs the machine learning model or business logic.
  * **Response:** Returns a JSON response to the client.
- **Response (from above image):**

```bash
HTTP/1.1 200 OK
Content-Type: application/json

{
    "prediction": 8.3
}
```

## End-to-End Flow in the Image:

- **Client Request:** A client sends a POST request to /predict with JSON payload.
- **ASGI Processing:** ASGI server (like Uvicorn) accepts the request and passes it to the FastAPI application.
- **API Logic:** FastAPI processes the data, runs the prediction, and generates a response.
- **Response Delivery:** The ASGI server sends the response back to the client.

# Fast API vs. Flask

![Alt text](fasiapi-2.png "fastapi wokring")

# **Get Method**

## **Path Parameters**

- Path parameters are part of the URL path itself. They are used to capture dynamic values from the URL and pass them to your API function.

```bash
/items/{item_id}
```

- **Purpose:** Capture parts of the URL as variables.
- **Data Type:** You can enforce the data type (e.g., int, str, float) by specifying it in the function signature.
- **Required:** Always required as they are part of the URL.

## **Query Parameters**

- Query parameters are the key-value pairs in the URL, typically found after the ? in the URL. They are used for optional data, filtering, or additional parameters.

```bash
/items?name=book&price=20
```

- **Purpose:** Add optional parameters to your API without changing the URL structure.
- **Data Type:** Can also have type hints like strings, integers, booleans, lists, etc.
- **Optional:** Typically optional, and you can define default values.

## **Key Differences:**

| **Path Parameters**        | **Query Parameters**               |
| -------------------------------- | ---------------------------------------- |
| Required in URL                  | Typically optional                       |
| Part of the URL structure        | After the`?` in the URL                |
| Used for resource identification | Used for filtering or additional details |
| Fixed position in URL            | Can be unordered                         |

# **Post Method**

- Used to create or submit data to the server (e.g., creating a user, submitting a form).

## **Key Concepts:**

- 1. **Pydantic Models**

  * Used to define and validate request body.
  * Automatically converts and checks types.
- 2. **@app.post("/path/")**

  * Defines a route that listens for POST requests at /path/.
- 3. **Request Body Handling**

  * FastAPI reads and parses the JSON body into a Pydantic model.
- 4. **Response**

  * Returns any serializable object (e.g., dict, list, model).
  * Can be customized with response_model.

## **Request body**

- A request body is the portion of an HTTP request that contains data sent by the client to the server. It is typically used in HTTP methods such as POST, or PUT to transmit structured data (e.g., JSON, XML, form-data) for the purpose of creating or updating resources on the server. The server parses the request body to extract the necessary information and perform the intended operation.

# **Put Method**

- Used to update an existing resource (e.g., a record in a database).
- @app.put() declares this is a PUT route.

## **Key Concepts**

1) Usually expects complete or partial data in the request body.
2) Often used with a path parameter to identify which resource to update (e.g., /edit/{id}).
3) Ideal for modifying fields without replacing the entire object.

# **Delete Method**

- Used to remove a resource from the system (e.g., delete a user or record).
- @app.delete() declares this is a DELETE route.

## **Key Concepts**

1) Often includes a path parameter to identify which resource to delete.
2) No request body is usually needed.
3) Should return a success message or appropriate error.
