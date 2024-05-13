echo
echo
echo " --------------- Benchmark has STARTED"
echo
echo

mkdir 1Baremetal
mkdir 1Docker
mkdir 1Podman
mkdir 1Singularity
mkdir 2Baremetal
mkdir 2Docker
mkdir 2Podman
mkdir 2Singularity
mkdir 3Baremetal
mkdir 3Docker
mkdir 3Podman
mkdir 3Singularity
mkdir 4Baremetal
mkdir 4Docker
mkdir 4Podman
mkdir 4Singularity
mkdir 5Baremetal
mkdir 5Docker
mkdir 5Podman
mkdir 5Singularity

echo "-------------------WARMUP-------------------"
echo
echo " --------------- BARE METAL --------------- "

# CLEAN SYSTEM CACHE
apt-get autoremove -y --purge
apt-get clean

echo
echo
echo " --------------- Running BARE METAL Benchmark"
echo
echo

sensors > ./Baremetal/1temp.txt

sysbench cpu --num-threads=1 --cpu-max-prime=20000 run > ./Baremetal/resultsCPU1.txt
sysbench cpu --num-threads=2 --cpu-max-prime=20000 run > ./Baremetal/resultsCPU2.txt
sysbench memory --memory-block-size=1G --memory-total-size=20G --memory-oper=write run > ./Baremetal/resultsRAMwrite.txt
sysbench memory --memory-block-size=1G --memory-total-size=20G --memory-oper=read run > ./Baremetal/resultsRAMread.txt
sysbench fileio --file-total-size=4G --file-test-mode=rndrw --time=120 --max-requests=0 prepare
sysbench fileio --file-total-size=4G --file-test-mode=rndrw --time=120 --max-requests=0 run > ./Baremetal/resultsMEM.txt
sysbench fileio --file-total-size=4G --file-test-mode=rndrw --time=120 --max-requests=0 cleanup

sensors > ./Baremetal/2temp.txt

echo
echo
echo " --------------- BARE METAL Benchmark Finished"
echo
echo


# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------


echo " --------------- DOCKER --------------- "

sleep 300s
# CLEAN SYSTEM CACHE AND DOCKER CACHE
apt-get autoremove -y --purge
apt-get clean
yes | docker builder prune

echo
echo
echo " --------------- Building Benchy image"
echo
echo

sensors > ./Docker/Results/1temp.txt

(time docker build -t benchy:1.0 ./Docker) 2>&1 | tee ./Docker/Results/ImageTime.txt
docker image list > ./Docker/Results/ImageSize.txt
sleep 2s


echo
echo
echo " --------------- Running container Benchy"
echo
echo

(time docker run -it --name DockerBenchy -v $(pwd)/Docker/Results:/Results benchy:1.0) 2>&1 | tee ./Docker/Results/ContainerTime.txt
sensors > ./Docker/Results/2temp.txt
sleep 2s

echo
echo
echo " --------------- Removing Benchy container"
echo
echo

docker container rm DockerBenchy
sleep 2s

echo
echo
echo " --------------- Removing Benchy image"
echo
echo

(time docker image rm -f benchy:1.0 ) 2>&1 | tee ./Docker/Results/ImageTimeRemove.txt
sleep 2s

echo 
echo
echo " --------------- DOCKER Benchmark has FINISHED"
echo
echo


# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------


echo " --------------- PODMAN --------------- "

sleep 300s
# CLEAN SYSTEM CACHE AND PODMAN CACHE
apt-get autoremove -y --purge
apt-get clean
yes | podman builder prune

echo
echo
echo " --------------- Building Benchy image"
echo
echo

sensors > ./Podman/Results/1temp.txt

(time podman --storage-driver=overlay build -t benchy:1.0 ./Podman) 2>&1 | tee ./Podman/Results/ImageTime.txt
podman image list > ./Podman/Results/ImageSize.txt
sleep 2s


echo
echo
echo " --------------- Running container Benchy"
echo
echo

(time podman --storage-driver=overlay run -it --name PodmanBenchy -v $(pwd)/Podman/Results:/Results localhost/benchy:1.0) 2>&1 | tee ./Podman/Results/ContainerTime.txt
sensors > ./Podman/Results/2temp.txt
sleep 2s

echo
echo
echo " --------------- Removing Benchy container"
echo
echo

podman container rm PodmanBenchy
sleep 2s

echo
echo
echo " --------------- Removing Benchy image"
echo
echo

(time podman image rm -f benchy:1.0 ) 2>&1 | tee ./Podman/Results/ImageTimeRemove.txt
sleep 2s

echo 
echo
echo " --------------- PODMAN Benchmark has FINISHED"
echo
echo


# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------


echo " --------------- SINGULARITY --------------- "

sleep 300s
# CLEAN SYSTEM CACHE AND SINGULARITY CACHE
apt-get autoremove -y --purge
apt-get clean
yes | singularity cache clean

echo
echo
echo " --------------- Building Benchy image"
echo
echo

sensors > ./Singularity/Results/1temp.txt

(time singularity build ./Singularity/Benchy ./Singularity/Singularity.recipe) 2>&1 | tee ./Singularity/Results/ImageTime.txt
du -h ./Singularity/Benchy > ./Singularity/Results/ImageSize.txt

sleep 2s

echo
echo
echo " --------------- Running container Benchy"
echo
echo

(time singularity run --bind ./Singularity/Results:$(pwd)/Singularity/Results ./Singularity/Benchy) 2>&1 | tee ./Singularity/Results/ContainerTime.txt
sensors > ./Singularity/Results/2temp.txt
mv -t ./Singularity/Results resultsCPU1.txt resultsCPU2.txt resultsRAMread.txt resultsRAMwrite.txt resultsMEM.txt
sleep 2s

echo
echo
echo " --------------- Removing Benchy image"
echo
echo

(time rm ./Singularity/Benchy) 2>&1 | tee ./Singularity/Results/ImageTimeRemove.txt
sleep 2s

echo 
echo
echo " --------------- SINGULARITY Benchmark has FINISHED"
echo
echo

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

echo "----------------------1---------------------"
echo
echo " --------------- BARE METAL --------------- "

sleep 300s
# CLEAN SYSTEM CACHE
apt-get autoremove -y --purge
apt-get clean

echo
echo
echo " --------------- Running BARE METAL Benchmark"
echo
echo

sensors > ./Baremetal/1temp.txt

sysbench cpu --num-threads=1 --cpu-max-prime=20000 run > ./Baremetal/resultsCPU1.txt
sysbench cpu --num-threads=2 --cpu-max-prime=20000 run > ./Baremetal/resultsCPU2.txt
sysbench memory --memory-block-size=1G --memory-total-size=20G --memory-oper=write run > ./Baremetal/resultsRAMwrite.txt
sysbench memory --memory-block-size=1G --memory-total-size=20G --memory-oper=read run > ./Baremetal/resultsRAMread.txt
sysbench fileio --file-total-size=4G --file-test-mode=rndrw --time=120 --max-requests=0 prepare
sysbench fileio --file-total-size=4G --file-test-mode=rndrw --time=120 --max-requests=0 run > ./Baremetal/resultsMEM.txt
sysbench fileio --file-total-size=4G --file-test-mode=rndrw --time=120 --max-requests=0 cleanup

sensors > ./Baremetal/2temp.txt

echo
echo
echo " --------------- BARE METAL Benchmark Finished"
echo
echo


# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------


echo " --------------- DOCKER --------------- "

sleep 300s
# CLEAN SYSTEM CACHE AND DOCKER CACHE
apt-get autoremove -y --purge
apt-get clean
yes | docker builder prune

echo
echo
echo " --------------- Building Benchy image"
echo
echo

sensors > ./Docker/Results/1temp.txt

(time docker build -t benchy:1.0 ./Docker) 2>&1 | tee ./Docker/Results/ImageTime.txt
docker image list > ./Docker/Results/ImageSize.txt
sleep 2s


echo
echo
echo " --------------- Running container Benchy"
echo
echo

(time docker run -it --name DockerBenchy -v $(pwd)/Docker/Results:/Results benchy:1.0) 2>&1 | tee ./Docker/Results/ContainerTime.txt
sensors > ./Docker/Results/2temp.txt
sleep 2s

echo
echo
echo " --------------- Removing Benchy container"
echo
echo

docker container rm DockerBenchy
sleep 2s

echo
echo
echo " --------------- Removing Benchy image"
echo
echo

(time docker image rm -f benchy:1.0 ) 2>&1 | tee ./Docker/Results/ImageTimeRemove.txt
sleep 2s

echo 
echo
echo " --------------- DOCKER Benchmark has FINISHED"
echo
echo


# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------


echo " --------------- PODMAN --------------- "

sleep 300s
# CLEAN SYSTEM CACHE AND PODMAN CACHE
apt-get autoremove -y --purge
apt-get clean
yes | podman builder prune

echo
echo
echo " --------------- Building Benchy image"
echo
echo

sensors > ./Podman/Results/1temp.txt

(time podman --storage-driver=overlay build -t benchy:1.0 ./Podman) 2>&1 | tee ./Podman/Results/ImageTime.txt
podman image list > ./Podman/Results/ImageSize.txt
sleep 2s


echo
echo
echo " --------------- Running container Benchy"
echo
echo

(time podman --storage-driver=overlay run -it --name PodmanBenchy -v $(pwd)/Podman/Results:/Results localhost/benchy:1.0) 2>&1 | tee ./Podman/Results/ContainerTime.txt
sensors > ./Podman/Results/2temp.txt
sleep 2s

echo
echo
echo " --------------- Removing Benchy container"
echo
echo

podman container rm PodmanBenchy
sleep 2s

echo
echo
echo " --------------- Removing Benchy image"
echo
echo

(time podman image rm -f benchy:1.0 ) 2>&1 | tee ./Podman/Results/ImageTimeRemove.txt
sleep 2s

echo 
echo
echo " --------------- PODMAN Benchmark has FINISHED"
echo
echo


# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------


echo " --------------- SINGULARITY --------------- "

sleep 300s
# CLEAN SYSTEM CACHE AND SINGULARITY CACHE
apt-get autoremove -y --purge
apt-get clean
yes | singularity cache clean

echo
echo
echo " --------------- Building Benchy image"
echo
echo

sensors > ./Singularity/Results/1temp.txt

(time singularity build ./Singularity/Benchy ./Singularity/Singularity.recipe) 2>&1 | tee ./Singularity/Results/ImageTime.txt
du -h ./Singularity/Benchy > ./Singularity/Results/ImageSize.txt

sleep 2s

echo
echo
echo " --------------- Running container Benchy"
echo
echo

(time singularity run --bind ./Singularity/Results:$(pwd)/Singularity/Results ./Singularity/Benchy) 2>&1 | tee ./Singularity/Results/ContainerTime.txt
sensors > ./Singularity/Results/2temp.txt
mv -t ./Singularity/Results resultsCPU1.txt resultsCPU2.txt resultsRAMread.txt resultsRAMwrite.txt resultsMEM.txt
sleep 2s

echo
echo
echo " --------------- Removing Benchy image"
echo
echo

(time rm ./Singularity/Benchy) 2>&1 | tee ./Singularity/Results/ImageTimeRemove.txt
sleep 2s

echo 
echo
echo " --------------- SINGULARITY Benchmark has FINISHED"
echo
echo

mv ./Baremetal/1temp.txt ./1Baremetal
mv ./Baremetal/2temp.txt ./1Baremetal
mv ./Baremetal/resultsCPU1.txt ./1Baremetal
mv ./Baremetal/resultsCPU2.txt ./1Baremetal
mv ./Baremetal/resultsMEM.txt ./1Baremetal
mv ./Baremetal/resultsRAMread.txt ./1Baremetal
mv ./Baremetal/resultsRAMwrite.txt ./1Baremetal

mv ./Docker/Results/1temp.txt ./1Docker
mv ./Docker/Results/2temp.txt ./1Docker
mv ./Docker/Results/resultsCPU1.txt ./1Docker
mv ./Docker/Results/resultsCPU2.txt ./1Docker
mv ./Docker/Results/resultsMEM.txt ./1Docker
mv ./Docker/Results/resultsRAMread.txt ./1Docker
mv ./Docker/Results/resultsRAMwrite.txt ./1Docker
mv ./Docker/Results/ContainerTime.txt ./1Docker
mv ./Docker/Results/ImageSize.txt ./1Docker
mv ./Docker/Results/ImageTime.txt ./1Docker
mv ./Docker/Results/ImageTimeRemove.txt ./1Docker

mv ./Podman/Results/1temp.txt ./1Podman
mv ./Podman/Results/2temp.txt ./1Podman
mv ./Podman/Results/resultsCPU1.txt ./1Podman
mv ./Podman/Results/resultsCPU2.txt ./1Podman
mv ./Podman/Results/resultsMEM.txt ./1Podman
mv ./Podman/Results/resultsRAMread.txt ./1Podman
mv ./Podman/Results/resultsRAMwrite.txt ./1Podman
mv ./Podman/Results/ContainerTime.txt ./1Podman
mv ./Podman/Results/ImageSize.txt ./1Podman
mv ./Podman/Results/ImageTime.txt ./1Podman
mv ./Podman/Results/ImageTimeRemove.txt ./1Podman

mv ./Singularity/Results/1temp.txt ./1Singularity
mv ./Singularity/Results/2temp.txt ./1Singularity
mv ./Singularity/Results/resultsCPU1.txt ./1Singularity
mv ./Singularity/Results/resultsCPU2.txt ./1Singularity
mv ./Singularity/Results/resultsMEM.txt ./1Singularity
mv ./Singularity/Results/resultsRAMread.txt ./1Singularity
mv ./Singularity/Results/resultsRAMwrite.txt ./1Singularity
mv ./Singularity/Results/ContainerTime.txt ./1Singularity
mv ./Singularity/Results/ImageSize.txt ./1Singularity
mv ./Singularity/Results/ImageTime.txt ./1Singularity
mv ./Singularity/Results/ImageTimeRemove.txt ./1Singularity

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

echo "----------------------2---------------------"
echo
echo " --------------- BARE METAL --------------- "

sleep 300s
# CLEAN SYSTEM CACHE
apt-get autoremove -y --purge
apt-get clean

echo
echo
echo " --------------- Running BARE METAL Benchmark"
echo
echo

sensors > ./Baremetal/1temp.txt

sysbench cpu --num-threads=1 --cpu-max-prime=20000 run > ./Baremetal/resultsCPU1.txt
sysbench cpu --num-threads=2 --cpu-max-prime=20000 run > ./Baremetal/resultsCPU2.txt
sysbench memory --memory-block-size=1G --memory-total-size=20G --memory-oper=write run > ./Baremetal/resultsRAMwrite.txt
sysbench memory --memory-block-size=1G --memory-total-size=20G --memory-oper=read run > ./Baremetal/resultsRAMread.txt
sysbench fileio --file-total-size=4G --file-test-mode=rndrw --time=120 --max-requests=0 prepare
sysbench fileio --file-total-size=4G --file-test-mode=rndrw --time=120 --max-requests=0 run > ./Baremetal/resultsMEM.txt
sysbench fileio --file-total-size=4G --file-test-mode=rndrw --time=120 --max-requests=0 cleanup

sensors > ./Baremetal/2temp.txt

echo
echo
echo " --------------- BARE METAL Benchmark Finished"
echo
echo

# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------


echo " --------------- DOCKER --------------- "

sleep 300s
# CLEAN SYSTEM CACHE AND DOCKER CACHE
apt-get autoremove -y --purge
apt-get clean
yes | docker builder prune

echo
echo
echo " --------------- Building Benchy image"
echo
echo

sensors > ./Docker/Results/1temp.txt

(time docker build -t benchy:1.0 ./Docker) 2>&1 | tee ./Docker/Results/ImageTime.txt
docker image list > ./Docker/Results/ImageSize.txt
sleep 2s


echo
echo
echo " --------------- Running container Benchy"
echo
echo

(time docker run -it --name DockerBenchy -v $(pwd)/Docker/Results:/Results benchy:1.0) 2>&1 | tee ./Docker/Results/ContainerTime.txt
sensors > ./Docker/Results/2temp.txt
sleep 2s

echo
echo
echo " --------------- Removing Benchy container"
echo
echo

docker container rm DockerBenchy
sleep 2s

echo
echo
echo " --------------- Removing Benchy image"
echo
echo

(time docker image rm -f benchy:1.0 ) 2>&1 | tee ./Docker/Results/ImageTimeRemove.txt
sleep 2s

echo 
echo
echo " --------------- DOCKER Benchmark has FINISHED"
echo
echo

# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------


echo " --------------- PODMAN --------------- "

sleep 300s
# CLEAN SYSTEM CACHE AND PODMAN CACHE
apt-get autoremove -y --purge
apt-get clean
yes | podman builder prune

echo
echo
echo " --------------- Building Benchy image"
echo
echo

sensors > ./Podman/Results/1temp.txt

(time podman --storage-driver=overlay build -t benchy:1.0 ./Podman) 2>&1 | tee ./Podman/Results/ImageTime.txt
podman image list > ./Podman/Results/ImageSize.txt
sleep 2s


echo
echo
echo " --------------- Running container Benchy"
echo
echo

(time podman --storage-driver=overlay run -it --name PodmanBenchy -v $(pwd)/Podman/Results:/Results localhost/benchy:1.0) 2>&1 | tee ./Podman/Results/ContainerTime.txt
sensors > ./Podman/Results/2temp.txt
sleep 2s

echo
echo
echo " --------------- Removing Benchy container"
echo
echo

podman container rm PodmanBenchy
sleep 2s

echo
echo
echo " --------------- Removing Benchy image"
echo
echo

(time podman image rm -f benchy:1.0 ) 2>&1 | tee ./Podman/Results/ImageTimeRemove.txt
sleep 2s

echo 
echo
echo " --------------- PODMAN Benchmark has FINISHED"
echo
echo

# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------


echo " --------------- SINGULARITY --------------- "

sleep 300s
# CLEAN SYSTEM CACHE AND SINGULARITY CACHE
apt-get autoremove -y --purge
apt-get clean
yes | singularity cache clean

echo
echo
echo " --------------- Building Benchy image"
echo
echo

sensors > ./Singularity/Results/1temp.txt

(time singularity build ./Singularity/Benchy ./Singularity/Singularity.recipe) 2>&1 | tee ./Singularity/Results/ImageTime.txt
du -h ./Singularity/Benchy > ./Singularity/Results/ImageSize.txt

sleep 2s

echo
echo
echo " --------------- Running container Benchy"
echo
echo

(time singularity run --bind ./Singularity/Results:$(pwd)/Singularity/Results ./Singularity/Benchy) 2>&1 | tee ./Singularity/Results/ContainerTime.txt
sensors > ./Singularity/Results/2temp.txt
mv -t ./Singularity/Results resultsCPU1.txt resultsCPU2.txt resultsRAMread.txt resultsRAMwrite.txt resultsMEM.txt
sleep 2s

echo
echo
echo " --------------- Removing Benchy image"
echo
echo

(time rm ./Singularity/Benchy) 2>&1 | tee ./Singularity/Results/ImageTimeRemove.txt
sleep 2s

echo 
echo
echo " --------------- SINGULARITY Benchmark has FINISHED"
echo
echo

mv ./Baremetal/1temp.txt ./2Baremetal
mv ./Baremetal/2temp.txt ./2Baremetal
mv ./Baremetal/resultsCPU1.txt ./2Baremetal
mv ./Baremetal/resultsCPU2.txt ./2Baremetal
mv ./Baremetal/resultsMEM.txt ./2Baremetal
mv ./Baremetal/resultsRAMread.txt ./2Baremetal
mv ./Baremetal/resultsRAMwrite.txt ./2Baremetal

mv ./Docker/Results/1temp.txt ./2Docker
mv ./Docker/Results/2temp.txt ./2Docker
mv ./Docker/Results/resultsCPU1.txt ./2Docker
mv ./Docker/Results/resultsCPU2.txt ./2Docker
mv ./Docker/Results/resultsMEM.txt ./2Docker
mv ./Docker/Results/resultsRAMread.txt ./2Docker
mv ./Docker/Results/resultsRAMwrite.txt ./2Docker
mv ./Docker/Results/ContainerTime.txt ./2Docker
mv ./Docker/Results/ImageSize.txt ./2Docker
mv ./Docker/Results/ImageTime.txt ./2Docker
mv ./Docker/Results/ImageTimeRemove.txt ./2Docker

mv ./Podman/Results/1temp.txt ./2Podman
mv ./Podman/Results/2temp.txt ./2Podman
mv ./Podman/Results/resultsCPU1.txt ./2Podman
mv ./Podman/Results/resultsCPU2.txt ./2Podman
mv ./Podman/Results/resultsMEM.txt ./2Podman
mv ./Podman/Results/resultsRAMread.txt ./2Podman
mv ./Podman/Results/resultsRAMwrite.txt ./2Podman
mv ./Podman/Results/ContainerTime.txt ./2Podman
mv ./Podman/Results/ImageSize.txt ./2Podman
mv ./Podman/Results/ImageTime.txt ./2Podman
mv ./Podman/Results/ImageTimeRemove.txt ./2Podman

mv ./Singularity/Results/1temp.txt ./2Singularity
mv ./Singularity/Results/2temp.txt ./2Singularity
mv ./Singularity/Results/resultsCPU1.txt ./2Singularity
mv ./Singularity/Results/resultsCPU2.txt ./2Singularity
mv ./Singularity/Results/resultsMEM.txt ./2Singularity
mv ./Singularity/Results/resultsRAMread.txt ./2Singularity
mv ./Singularity/Results/resultsRAMwrite.txt ./2Singularity
mv ./Singularity/Results/ContainerTime.txt ./2Singularity
mv ./Singularity/Results/ImageSize.txt ./2Singularity
mv ./Singularity/Results/ImageTime.txt ./2Singularity
mv ./Singularity/Results/ImageTimeRemove.txt ./2Singularity


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

echo "----------------------3---------------------"
echo
echo " --------------- BARE METAL --------------- "

sleep 300s
# CLEAN SYSTEM CACHE
apt-get autoremove -y --purge
apt-get clean

echo
echo
echo " --------------- Running BARE METAL Benchmark"
echo
echo

sensors > ./Baremetal/1temp.txt

sysbench cpu --num-threads=1 --cpu-max-prime=20000 run > ./Baremetal/resultsCPU1.txt
sysbench cpu --num-threads=2 --cpu-max-prime=20000 run > ./Baremetal/resultsCPU2.txt
sysbench memory --memory-block-size=1G --memory-total-size=20G --memory-oper=write run > ./Baremetal/resultsRAMwrite.txt
sysbench memory --memory-block-size=1G --memory-total-size=20G --memory-oper=read run > ./Baremetal/resultsRAMread.txt
sysbench fileio --file-total-size=4G --file-test-mode=rndrw --time=120 --max-requests=0 prepare
sysbench fileio --file-total-size=4G --file-test-mode=rndrw --time=120 --max-requests=0 run > ./Baremetal/resultsMEM.txt
sysbench fileio --file-total-size=4G --file-test-mode=rndrw --time=120 --max-requests=0 cleanup

sensors > ./Baremetal/2temp.txt

echo
echo
echo " --------------- BARE METAL Benchmark Finished"
echo
echo


# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------


echo " --------------- DOCKER --------------- "

sleep 300s
# CLEAN SYSTEM CACHE AND DOCKER CACHE
apt-get autoremove -y --purge
apt-get clean
yes | docker builder prune

echo
echo
echo " --------------- Building Benchy image"
echo
echo

sensors > ./Docker/Results/1temp.txt

(time docker build -t benchy:1.0 ./Docker) 2>&1 | tee ./Docker/Results/ImageTime.txt
docker image list > ./Docker/Results/ImageSize.txt
sleep 2s


echo
echo
echo " --------------- Running container Benchy"
echo
echo

(time docker run -it --name DockerBenchy -v $(pwd)/Docker/Results:/Results benchy:1.0) 2>&1 | tee ./Docker/Results/ContainerTime.txt
sensors > ./Docker/Results/2temp.txt
sleep 2s

echo
echo
echo " --------------- Removing Benchy container"
echo
echo

docker container rm DockerBenchy
sleep 2s

echo
echo
echo " --------------- Removing Benchy image"
echo
echo

(time docker image rm -f benchy:1.0 ) 2>&1 | tee ./Docker/Results/ImageTimeRemove.txt
sleep 2s

echo 
echo
echo " --------------- DOCKER Benchmark has FINISHED"
echo
echo


# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------


echo " --------------- PODMAN --------------- "

sleep 300s
# CLEAN SYSTEM CACHE AND PODMAN CACHE
apt-get autoremove -y --purge
apt-get clean
yes | podman builder prune

echo
echo
echo " --------------- Building Benchy image"
echo
echo

sensors > ./Podman/Results/1temp.txt

(time podman --storage-driver=overlay build -t benchy:1.0 ./Podman) 2>&1 | tee ./Podman/Results/ImageTime.txt
podman image list > ./Podman/Results/ImageSize.txt
sleep 2s


echo
echo
echo " --------------- Running container Benchy"
echo
echo

(time podman --storage-driver=overlay run -it --name PodmanBenchy -v $(pwd)/Podman/Results:/Results localhost/benchy:1.0) 2>&1 | tee ./Podman/Results/ContainerTime.txt
sensors > ./Podman/Results/2temp.txt
sleep 2s

echo
echo
echo " --------------- Removing Benchy container"
echo
echo

podman container rm PodmanBenchy
sleep 2s

echo
echo
echo " --------------- Removing Benchy image"
echo
echo

(time podman image rm -f benchy:1.0 ) 2>&1 | tee ./Podman/Results/ImageTimeRemove.txt
sleep 2s

echo 
echo
echo " --------------- PODMAN Benchmark has FINISHED"
echo
echo


# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------


echo " --------------- SINGULARITY --------------- "

sleep 300s
# CLEAN SYSTEM CACHE AND SINGULARITY CACHE
apt-get autoremove -y --purge
apt-get clean
yes | singularity cache clean

echo
echo
echo " --------------- Building Benchy image"
echo
echo

sensors > ./Singularity/Results/1temp.txt

(time singularity build ./Singularity/Benchy ./Singularity/Singularity.recipe) 2>&1 | tee ./Singularity/Results/ImageTime.txt
du -h ./Singularity/Benchy > ./Singularity/Results/ImageSize.txt

sleep 2s

echo
echo
echo " --------------- Running container Benchy"
echo
echo

(time singularity run --bind ./Singularity/Results:$(pwd)/Singularity/Results ./Singularity/Benchy) 2>&1 | tee ./Singularity/Results/ContainerTime.txt
sensors > ./Singularity/Results/2temp.txt
mv -t ./Singularity/Results resultsCPU1.txt resultsCPU2.txt resultsRAMread.txt resultsRAMwrite.txt resultsMEM.txt
sleep 2s

echo
echo
echo " --------------- Removing Benchy image"
echo
echo

(time rm ./Singularity/Benchy) 2>&1 | tee ./Singularity/Results/ImageTimeRemove.txt
sleep 2s

echo 
echo
echo " --------------- SINGULARITY Benchmark has FINISHED"
echo
echo

mv ./Baremetal/1temp.txt ./3Baremetal
mv ./Baremetal/2temp.txt ./3Baremetal
mv ./Baremetal/resultsCPU1.txt ./3Baremetal
mv ./Baremetal/resultsCPU2.txt ./3Baremetal
mv ./Baremetal/resultsMEM.txt ./3Baremetal
mv ./Baremetal/resultsRAMread.txt ./3Baremetal
mv ./Baremetal/resultsRAMwrite.txt ./3Baremetal

mv ./Docker/Results/1temp.txt ./3Docker
mv ./Docker/Results/2temp.txt ./3Docker
mv ./Docker/Results/resultsCPU1.txt ./3Docker
mv ./Docker/Results/resultsCPU2.txt ./3Docker
mv ./Docker/Results/resultsMEM.txt ./3Docker
mv ./Docker/Results/resultsRAMread.txt ./3Docker
mv ./Docker/Results/resultsRAMwrite.txt ./3Docker
mv ./Docker/Results/ContainerTime.txt ./3Docker
mv ./Docker/Results/ImageSize.txt ./3Docker
mv ./Docker/Results/ImageTime.txt ./3Docker
mv ./Docker/Results/ImageTimeRemove.txt ./3Docker

mv ./Podman/Results/1temp.txt ./3Podman
mv ./Podman/Results/2temp.txt ./3Podman
mv ./Podman/Results/resultsCPU1.txt ./3Podman
mv ./Podman/Results/resultsCPU2.txt ./3Podman
mv ./Podman/Results/resultsMEM.txt ./3Podman
mv ./Podman/Results/resultsRAMread.txt ./3Podman
mv ./Podman/Results/resultsRAMwrite.txt ./3Podman
mv ./Podman/Results/ContainerTime.txt ./3Podman
mv ./Podman/Results/ImageSize.txt ./3Podman
mv ./Podman/Results/ImageTime.txt ./3Podman
mv ./Podman/Results/ImageTimeRemove.txt ./3Podman

mv ./Singularity/Results/1temp.txt ./3Singularity
mv ./Singularity/Results/2temp.txt ./3Singularity
mv ./Singularity/Results/resultsCPU1.txt ./3Singularity
mv ./Singularity/Results/resultsCPU2.txt ./3Singularity
mv ./Singularity/Results/resultsMEM.txt ./3Singularity
mv ./Singularity/Results/resultsRAMread.txt ./3Singularity
mv ./Singularity/Results/resultsRAMwrite.txt ./3Singularity
mv ./Singularity/Results/ContainerTime.txt ./3Singularity
mv ./Singularity/Results/ImageSize.txt ./3Singularity
mv ./Singularity/Results/ImageTime.txt ./3Singularity
mv ./Singularity/Results/ImageTimeRemove.txt ./3Singularity


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

echo "----------------------4---------------------"
echo
echo " --------------- BARE METAL --------------- "

sleep 300s
# CLEAN SYSTEM CACHE
apt-get autoremove -y --purge
apt-get clean

echo
echo
echo " --------------- Running BARE METAL Benchmark"
echo
echo

sensors > ./Baremetal/1temp.txt

sysbench cpu --num-threads=1 --cpu-max-prime=20000 run > ./Baremetal/resultsCPU1.txt
sysbench cpu --num-threads=2 --cpu-max-prime=20000 run > ./Baremetal/resultsCPU2.txt
sysbench memory --memory-block-size=1G --memory-total-size=20G --memory-oper=write run > ./Baremetal/resultsRAMwrite.txt
sysbench memory --memory-block-size=1G --memory-total-size=20G --memory-oper=read run > ./Baremetal/resultsRAMread.txt
sysbench fileio --file-total-size=4G --file-test-mode=rndrw --time=120 --max-requests=0 prepare
sysbench fileio --file-total-size=4G --file-test-mode=rndrw --time=120 --max-requests=0 run > ./Baremetal/resultsMEM.txt
sysbench fileio --file-total-size=4G --file-test-mode=rndrw --time=120 --max-requests=0 cleanup

sensors > ./Baremetal/2temp.txt

echo
echo
echo " --------------- BARE METAL Benchmark Finished"
echo
echo

# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------


echo " --------------- DOCKER --------------- "

sleep 300s
# CLEAN SYSTEM CACHE AND DOCKER CACHE
apt-get autoremove -y --purge
apt-get clean
yes | docker builder prune

echo
echo
echo " --------------- Building Benchy image"
echo
echo

sensors > ./Docker/Results/1temp.txt

(time docker build -t benchy:1.0 ./Docker) 2>&1 | tee ./Docker/Results/ImageTime.txt
docker image list > ./Docker/Results/ImageSize.txt
sleep 2s


echo
echo
echo " --------------- Running container Benchy"
echo
echo

(time docker run -it --name DockerBenchy -v $(pwd)/Docker/Results:/Results benchy:1.0) 2>&1 | tee ./Docker/Results/ContainerTime.txt
sensors > ./Docker/Results/2temp.txt
sleep 2s

echo
echo
echo " --------------- Removing Benchy container"
echo
echo

docker container rm DockerBenchy
sleep 2s

echo
echo
echo " --------------- Removing Benchy image"
echo
echo

(time docker image rm -f benchy:1.0 ) 2>&1 | tee ./Docker/Results/ImageTimeRemove.txt
sleep 2s

echo 
echo
echo " --------------- DOCKER Benchmark has FINISHED"
echo
echo


# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------


echo " --------------- PODMAN --------------- "

sleep 300s
# CLEAN SYSTEM CACHE AND PODMAN CACHE
apt-get autoremove -y --purge
apt-get clean
yes | podman builder prune

echo
echo
echo " --------------- Building Benchy image"
echo
echo

sensors > ./Podman/Results/1temp.txt

(time podman --storage-driver=overlay build -t benchy:1.0 ./Podman) 2>&1 | tee ./Podman/Results/ImageTime.txt
podman image list > ./Podman/Results/ImageSize.txt
sleep 2s


echo
echo
echo " --------------- Running container Benchy"
echo
echo

(time podman --storage-driver=overlay run -it --name PodmanBenchy -v $(pwd)/Podman/Results:/Results localhost/benchy:1.0) 2>&1 | tee ./Podman/Results/ContainerTime.txt
sensors > ./Podman/Results/2temp.txt
sleep 2s

echo
echo
echo " --------------- Removing Benchy container"
echo
echo

podman container rm PodmanBenchy
sleep 2s

echo
echo
echo " --------------- Removing Benchy image"
echo
echo

(time podman image rm -f benchy:1.0 ) 2>&1 | tee ./Podman/Results/ImageTimeRemove.txt
sleep 2s

echo 
echo
echo " --------------- PODMAN Benchmark has FINISHED"
echo
echo


# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------


echo " --------------- SINGULARITY --------------- "

sleep 300s
# CLEAN SYSTEM CACHE AND SINGULARITY CACHE
apt-get autoremove -y --purge
apt-get clean
yes | singularity cache clean

echo
echo
echo " --------------- Building Benchy image"
echo
echo

sensors > ./Singularity/Results/1temp.txt

(time singularity build ./Singularity/Benchy ./Singularity/Singularity.recipe) 2>&1 | tee ./Singularity/Results/ImageTime.txt
du -h ./Singularity/Benchy > ./Singularity/Results/ImageSize.txt

sleep 2s

echo
echo
echo " --------------- Running container Benchy"
echo
echo

(time singularity run --bind ./Singularity/Results:$(pwd)/Singularity/Results ./Singularity/Benchy) 2>&1 | tee ./Singularity/Results/ContainerTime.txt
sensors > ./Singularity/Results/2temp.txt
mv -t ./Singularity/Results resultsCPU1.txt resultsCPU2.txt resultsRAMread.txt resultsRAMwrite.txt resultsMEM.txt
sleep 2s

echo
echo
echo " --------------- Removing Benchy image"
echo
echo

(time rm ./Singularity/Benchy) 2>&1 | tee ./Singularity/Results/ImageTimeRemove.txt
sleep 2s

echo 
echo
echo " --------------- SINGULARITY Benchmark has FINISHED"
echo
echo

mv ./Baremetal/1temp.txt ./4Baremetal
mv ./Baremetal/2temp.txt ./4Baremetal
mv ./Baremetal/resultsCPU1.txt ./4Baremetal
mv ./Baremetal/resultsCPU2.txt ./4Baremetal
mv ./Baremetal/resultsMEM.txt ./4Baremetal
mv ./Baremetal/resultsRAMread.txt ./4Baremetal
mv ./Baremetal/resultsRAMwrite.txt ./4Baremetal

mv ./Docker/Results/1temp.txt ./4Docker
mv ./Docker/Results/2temp.txt ./4Docker
mv ./Docker/Results/resultsCPU1.txt ./4Docker
mv ./Docker/Results/resultsCPU2.txt ./4Docker
mv ./Docker/Results/resultsMEM.txt ./4Docker
mv ./Docker/Results/resultsRAMread.txt ./4Docker
mv ./Docker/Results/resultsRAMwrite.txt ./4Docker
mv ./Docker/Results/ContainerTime.txt ./4Docker
mv ./Docker/Results/ImageSize.txt ./4Docker
mv ./Docker/Results/ImageTime.txt ./4Docker
mv ./Docker/Results/ImageTimeRemove.txt ./4Docker

mv ./Podman/Results/1temp.txt ./4Podman
mv ./Podman/Results/2temp.txt ./4Podman
mv ./Podman/Results/resultsCPU1.txt ./4Podman
mv ./Podman/Results/resultsCPU2.txt ./4Podman
mv ./Podman/Results/resultsMEM.txt ./4Podman
mv ./Podman/Results/resultsRAMread.txt ./4Podman
mv ./Podman/Results/resultsRAMwrite.txt ./4Podman
mv ./Podman/Results/ContainerTime.txt ./4Podman
mv ./Podman/Results/ImageSize.txt ./4Podman
mv ./Podman/Results/ImageTime.txt ./4Podman
mv ./Podman/Results/ImageTimeRemove.txt ./4Podman

mv ./Singularity/Results/1temp.txt ./4Singularity
mv ./Singularity/Results/2temp.txt ./4Singularity
mv ./Singularity/Results/resultsCPU1.txt ./4Singularity
mv ./Singularity/Results/resultsCPU2.txt ./4Singularity
mv ./Singularity/Results/resultsMEM.txt ./4Singularity
mv ./Singularity/Results/resultsRAMread.txt ./4Singularity
mv ./Singularity/Results/resultsRAMwrite.txt ./4Singularity
mv ./Singularity/Results/ContainerTime.txt ./4Singularity
mv ./Singularity/Results/ImageSize.txt ./4Singularity
mv ./Singularity/Results/ImageTime.txt ./4Singularity
mv ./Singularity/Results/ImageTimeRemove.txt ./4Singularity


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

echo "----------------------5---------------------"
echo
echo " --------------- BARE METAL --------------- "

sleep 300s
# CLEAN SYSTEM CACHE
apt-get autoremove -y --purge
apt-get clean

echo
echo
echo " --------------- Running BARE METAL Benchmark"
echo
echo

sensors > ./Baremetal/1temp.txt

sysbench cpu --num-threads=1 --cpu-max-prime=20000 run > ./Baremetal/resultsCPU1.txt
sysbench cpu --num-threads=2 --cpu-max-prime=20000 run > ./Baremetal/resultsCPU2.txt
sysbench memory --memory-block-size=1G --memory-total-size=20G --memory-oper=write run > ./Baremetal/resultsRAMwrite.txt
sysbench memory --memory-block-size=1G --memory-total-size=20G --memory-oper=read run > ./Baremetal/resultsRAMread.txt
sysbench fileio --file-total-size=4G --file-test-mode=rndrw --time=120 --max-requests=0 prepare
sysbench fileio --file-total-size=4G --file-test-mode=rndrw --time=120 --max-requests=0 run > ./Baremetal/resultsMEM.txt
sysbench fileio --file-total-size=4G --file-test-mode=rndrw --time=120 --max-requests=0 cleanup

sensors > ./Baremetal/2temp.txt

echo
echo
echo " --------------- BARE METAL Benchmark Finished"
echo
echo


# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------


echo " --------------- DOCKER --------------- "

sleep 300s
# CLEAN SYSTEM CACHE AND DOCKER CACHE
apt-get autoremove -y --purge
apt-get clean
yes | docker builder prune

echo
echo
echo " --------------- Building Benchy image"
echo
echo

sensors > ./Docker/Results/1temp.txt

(time docker build -t benchy:1.0 ./Docker) 2>&1 | tee ./Docker/Results/ImageTime.txt
docker image list > ./Docker/Results/ImageSize.txt
sleep 2s


echo
echo
echo " --------------- Running container Benchy"
echo
echo

(time docker run -it --name DockerBenchy -v $(pwd)/Docker/Results:/Results benchy:1.0) 2>&1 | tee ./Docker/Results/ContainerTime.txt
sensors > ./Docker/Results/2temp.txt
sleep 2s

echo
echo
echo " --------------- Removing Benchy container"
echo
echo

docker container rm DockerBenchy
sleep 2s

echo
echo
echo " --------------- Removing Benchy image"
echo
echo

(time docker image rm -f benchy:1.0 ) 2>&1 | tee ./Docker/Results/ImageTimeRemove.txt
sleep 2s

echo 
echo
echo " --------------- DOCKER Benchmark has FINISHED"
echo
echo


# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------


echo " --------------- PODMAN --------------- "

sleep 300s
# CLEAN SYSTEM CACHE AND PODMAN CACHE
apt-get autoremove -y --purge
apt-get clean
yes | podman builder prune

echo
echo
echo " --------------- Building Benchy image"
echo
echo

sensors > ./Podman/Results/1temp.txt

(time podman --storage-driver=overlay build -t benchy:1.0 ./Podman) 2>&1 | tee ./Podman/Results/ImageTime.txt
podman image list > ./Podman/Results/ImageSize.txt
sleep 2s


echo
echo
echo " --------------- Running container Benchy"
echo
echo

(time podman --storage-driver=overlay run -it --name PodmanBenchy -v $(pwd)/Podman/Results:/Results localhost/benchy:1.0) 2>&1 | tee ./Podman/Results/ContainerTime.txt
sensors > ./Podman/Results/2temp.txt
sleep 2s

echo
echo
echo " --------------- Removing Benchy container"
echo
echo

podman container rm PodmanBenchy
sleep 2s

echo
echo
echo " --------------- Removing Benchy image"
echo
echo

(time podman image rm -f benchy:1.0 ) 2>&1 | tee ./Podman/Results/ImageTimeRemove.txt
sleep 2s

echo 
echo
echo " --------------- PODMAN Benchmark has FINISHED"
echo
echo


# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------


echo " --------------- SINGULARITY --------------- "

sleep 300s
# CLEAN SYSTEM CACHE AND SINGULARITY CACHE
apt-get autoremove -y --purge
apt-get clean
yes | singularity cache clean

echo
echo
echo " --------------- Building Benchy image"
echo
echo

sensors > ./Singularity/Results/1temp.txt

(time singularity build ./Singularity/Benchy ./Singularity/Singularity.recipe) 2>&1 | tee ./Singularity/Results/ImageTime.txt
du -h ./Singularity/Benchy > ./Singularity/Results/ImageSize.txt

sleep 2s

echo
echo
echo " --------------- Running container Benchy"
echo
echo

(time singularity run --bind ./Singularity/Results:$(pwd)/Singularity/Results ./Singularity/Benchy) 2>&1 | tee ./Singularity/Results/ContainerTime.txt
sensors > ./Singularity/Results/2temp.txt
mv -t ./Singularity/Results resultsCPU1.txt resultsCPU2.txt resultsRAMread.txt resultsRAMwrite.txt resultsMEM.txt
sleep 2s

echo
echo
echo " --------------- Removing Benchy image"
echo
echo

(time rm ./Singularity/Benchy) 2>&1 | tee ./Singularity/Results/ImageTimeRemove.txt
sleep 2s

echo 
echo
echo " --------------- SINGULARITY Benchmark has FINISHED"
echo
echo

mv ./Baremetal/1temp.txt ./5Baremetal
mv ./Baremetal/2temp.txt ./5Baremetal
mv ./Baremetal/resultsCPU1.txt ./5Baremetal
mv ./Baremetal/resultsCPU2.txt ./5Baremetal
mv ./Baremetal/resultsMEM.txt ./5Baremetal
mv ./Baremetal/resultsRAMread.txt ./5Baremetal
mv ./Baremetal/resultsRAMwrite.txt ./5Baremetal

mv ./Docker/Results/1temp.txt ./5Docker
mv ./Docker/Results/2temp.txt ./5Docker
mv ./Docker/Results/resultsCPU1.txt ./5Docker
mv ./Docker/Results/resultsCPU2.txt ./5Docker
mv ./Docker/Results/resultsMEM.txt ./5Docker
mv ./Docker/Results/resultsRAMread.txt ./5Docker
mv ./Docker/Results/resultsRAMwrite.txt ./5Docker
mv ./Docker/Results/ContainerTime.txt ./5Docker
mv ./Docker/Results/ImageSize.txt ./5Docker
mv ./Docker/Results/ImageTime.txt ./5Docker
mv ./Docker/Results/ImageTimeRemove.txt ./5Docker

mv ./Podman/Results/1temp.txt ./5Podman
mv ./Podman/Results/2temp.txt ./5Podman
mv ./Podman/Results/resultsCPU1.txt ./5Podman
mv ./Podman/Results/resultsCPU2.txt ./5Podman
mv ./Podman/Results/resultsMEM.txt ./5Podman
mv ./Podman/Results/resultsRAMread.txt ./5Podman
mv ./Podman/Results/resultsRAMwrite.txt ./5Podman
mv ./Podman/Results/ContainerTime.txt ./5Podman
mv ./Podman/Results/ImageSize.txt ./5Podman
mv ./Podman/Results/ImageTime.txt ./5Podman
mv ./Podman/Results/ImageTimeRemove.txt ./5Podman

mv ./Singularity/Results/1temp.txt ./5Singularity
mv ./Singularity/Results/2temp.txt ./5Singularity
mv ./Singularity/Results/resultsCPU1.txt ./5Singularity
mv ./Singularity/Results/resultsCPU2.txt ./5Singularity
mv ./Singularity/Results/resultsMEM.txt ./5Singularity
mv ./Singularity/Results/resultsRAMread.txt ./5Singularity
mv ./Singularity/Results/resultsRAMwrite.txt ./5Singularity
mv ./Singularity/Results/ContainerTime.txt ./5Singularity
mv ./Singularity/Results/ImageSize.txt ./5Singularity
mv ./Singularity/Results/ImageTime.txt ./5Singularity
mv ./Singularity/Results/ImageTimeRemove.txt ./5Singularity

echo
echo
echo
echo
echo " --------------- Benchmark has FINISHED ---------------  "
echo

mv 1Baremetal   .Results
mv 1Docker      .Results
mv 1Podman      .Results
mv 1Singularity .Results
mv 2Baremetal   .Results
mv 2Docker      .Results
mv 2Podman      .Results
mv 2Singularity .Results
mv 3Baremetal   .Results
mv 3Docker      .Results
mv 3Podman      .Results
mv 3Singularity .Results
mv 4Baremetal   .Results
mv 4Docker      .Results
mv 4Podman      .Results
mv 4Singularity .Results
mv 5Baremetal   .Results
mv 5Docker      .Results
mv 5Podman      .Results
mv 5Singularity .Results

sudo python3 graficos.py

