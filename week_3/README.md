Dockerfile run commands
1.docker run --name mydba --network mynetwork -p 8081:80  -d my_dba
2. docker run --name mydb --network mynetwork -itd -p5432:5432 my_db
3. docker run -it -p8000:8000 --network mynetwork -v $(pwd)/app:/app my_django 
