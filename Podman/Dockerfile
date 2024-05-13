FROM ubuntu:20.04

RUN apt-get update && apt-get install -y sysbench && rm -rf /var/lib/apt/lists/* && apt-get clean

ENTRYPOINT sysbench cpu --num-threads=1 --cpu-max-prime=20000 run > /Results/resultsCPU1.txt \
&& sysbench cpu --num-threads=2 --cpu-max-prime=20000 run > /Results/resultsCPU2.txt \
&& sysbench memory --memory-block-size=1G --memory-total-size=20G --memory-oper=write run > /Results/resultsRAMwrite.txt \
&& sysbench memory --memory-block-size=1G --memory-total-size=20G --memory-oper=read run > /Results/resultsRAMread.txt \
&& sysbench fileio --file-total-size=4G --file-test-mode=rndrw --time=120 --max-requests=0 prepare \
&& sysbench fileio --file-total-size=4G --file-test-mode=rndrw --time=120 --max-requests=0 run > /Results/resultsMEM.txt \
&& sysbench fileio --file-total-size=4G --file-test-mode=rndrw --time=120 --max-requests=0 cleanup \
&& exit \
&& /bin/bash