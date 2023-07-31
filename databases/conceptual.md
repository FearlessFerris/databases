### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?

    PostgreSQL is an open source relational database system

- What is the difference between SQL and PostgreSQL?

    PostgreSQL has most of the same capabilities as SQL but also adds in many nice additional features and has an easier working syntax. 

- In `psql`, how do you connect to a database?

    Once the database server is running you simply type 'psql' into the terminal and from there you should be directed into the postgres shell

- What is the difference between `HAVING` and `WHERE`?

    'WHERE' is applied to rows wheras 'HAVING' is applied to groups of rows 

- What is the difference between an `INNER` and `OUTER` join?

    'INNER' join will return all matched records from both the left and right side of the table, wheras 'OUTER' join will return all records from the right table and all matched records from the left side 

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?

    'LEFT OUTER' join will only give you rows from the left table, and 'RIGHT OUTER' will only give you rows from the right table

- What is an ORM? What do they do?  

    ORM is a technique used to 'bridge' object-oriented programs and usually relational databases 

- What are some differences between making HTTP requests using AJAX 

  and from the server side using a library like `requests`?

    AJAX will allow you to make requests to and from a webserver asynchronously without a refresh or a reload required 

- What is CSRF? What is the purpose of the CSRF token?

    CSRF stands for Cross Site Request Forgery, this will provide the requesting user with a unique and secret 'token' when issuing a request such as a form submission, this token is hidden within the form which allows a user to make valid requests to a server. Without this, a users requests would be invalid. 

- What is the purpose of `form.hidden_tag()`?

  This tag will generate a hidden field used to prevent unwanted hacks or attacks on a webpage/server 
