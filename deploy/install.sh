#!/usr/bin/env bash
# Install Smart Support Bot on Ubuntu (dedicated tiny VPS, runs as root).
set -euo pipefail

INSTALL_DIR="/opt/Smart Support Bot"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

echo "==> Installing system packages"
apt-get update -qq
apt-get install -y python3 python3-venv python3-pip

echo "==> Preparing ${INSTALL_DIR}"
mkdir -p "${INSTALL_DIR}"

if [[ "${SOURCE_DIR}" != "${INSTALL_DIR}" ]]; then
  cp -a "${SOURCE_DIR}/." "${INSTALL_DIR}/"
fi

mkdir -p "${INSTALL_DIR}/data"

echo "==> Creating Python virtualenv and installing dependencies"
cd "${INSTALL_DIR}"
python3 -m venv .venv
.venv/bin/pip install -U pip
.venv/bin/pip install -r requirements.txt

echo "==> Preparing safety store"
mkdir -p /opt/smart-support-bot-safety/backups /opt/smart-support-bot-safety/staging

echo "==> Installing systemd units"
install -m 644 "${INSTALL_DIR}/deploy/smart-support-bot.service" /etc/systemd/system/smart-support-bot.service
install -m 644 "${INSTALL_DIR}/deploy/smart-support-bot-watchdog.service" /etc/systemd/system/smart-support-bot-watchdog.service
systemctl daemon-reload
systemctl enable --now smart-support-bot.service
systemctl enable --now smart-support-bot-watchdog.service

echo "==> Done. Status:"
systemctl status smart-support-bot.service --no-pager || true
systemctl status smart-support-bot-watchdog.service --no-pager || true
