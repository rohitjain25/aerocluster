import os
import subprocess
print("Running tiny proxy")
os.system('export https_proxy="http://tinyproxy:8888"')
os.system('export http_proxy="http://tinyproxy:8888"')
os.system('ansible-playbook purge.yaml')
os.system('wget http://cor-mirror101.phonepe.nm5/aerospike-E4.8.0.6.tgz')
os.system('wget http://cor-mirror101.phonepe.nm5/aerospike-amc-e4.0.24.deb')
os.system('ansible-playbook aero.yaml')
os.system('rm -rf aerospike-E4.8.0.6.tgz')
os.system('rm -rf aerospike-amc-e4.0.24.deb')