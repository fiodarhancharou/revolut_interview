Commands:
    - to build the container:
        docker build -t rev_interview .
    - to run the container:
        docker run -d --name rev_container -p 8000:8000 rev_interview
App will be available at:
    localhost:8000