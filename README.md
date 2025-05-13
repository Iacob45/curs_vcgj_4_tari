Aici va fii descrierea individuala

Lucrul cu docker
-afisare containere: docker ps -a
-creare container: docker build -t tari:v1 /home/user/SCC/curs_vcgj_4_tari
-rulare container: docker run -d --name tari_cont -p 8020:5011 tari:v1
-oprire container: docker stop tari_cont
-stergere container: docker rm tari_cont
-accesare container: docker exec -it tari_cont /bin/sh       ///iesire cu exit