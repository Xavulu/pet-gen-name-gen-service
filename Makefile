build:
	docker build -t myimage .

log: 
	 docker run -a stdin -a stdout -a stderr --name mycontainer -p 80:80 myimage

kill: 
	docker stop mycontainer 
	docker rm mycontainer 

