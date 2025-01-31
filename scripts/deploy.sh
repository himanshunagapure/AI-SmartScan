#!/bin/bash
cd /home/ec2-user/app
docker stop $(docker ps -q) || true
docker pull 061051258974.dkr.ecr.ap-south-1.amazonaws.com/ai-smartscan:latest 
docker run -d -p 80:8501 061051258974.dkr.ecr.ap-south-1.amazonaws.com/ai-smartscan:latest