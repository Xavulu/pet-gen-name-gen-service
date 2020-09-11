build:
	docker build -t myimage .

log: 
	 docker run -a stdin -a stdout -a stderr --name mycontainer -p 80:80 myimage
run:
	docker run -d --name mycontainer -p 80:80 myimage 
	timeout 5 
	docker ps

kill: 
	docker stop mycontainer 
	docker rm mycontainer
