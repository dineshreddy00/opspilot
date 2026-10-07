#!/bin/bash

echo "======================================"
echo "        OpsPilot Health Check"
echo "======================================"

echo
echo "[1] Docker Container"
docker ps --filter "name=opspilot-app"

echo
echo "[2] Nginx Status"
systemctl is-active nginx

echo
echo "[3] Application Health"
curl -s http://localhost/health

echo
echo
echo "[4] Nginx HTTP Status"
curl -I -s http://localhost | head -n 1

echo
echo "======================================"
echo "        Health Check Complete"
echo "======================================"
