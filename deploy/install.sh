#!/usr/bin/env bash
# Smart Support Bot — Linux installer (Ubuntu/Debian)
# Usage:
#   1) Clone this repository on the VPS
#   2) cp .env.example .env && nano .env
#   3) sudo bash deploy/install.sh
set -euo pipefail

INSTALL_DIR="${INSTALL_DIR:-/opt/smart-support-bot}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

if [[ "${EUID}" -ne 0 ]]; then
  echo "Please run as root: sudo bash deploy/install.sh"
  exit 1
fi

echo "==> Installing system packages"
export DEBIAN_FRONTEND=noninteractive
apt-get update -qq
apt-get install -y python3 python3-venv python3-pip curl rsync

echo "==> Preparing ${INSTALL_DIR}"
mkdir -p "${INSTALL_DIR}"

if [[ "${SOURCE_DIR}" != "${INSTALL_DIR}" ]]; then
  if command -v rsync >/dev/null 2>&1; then
    rsync -a \
      --exclude '.venv' \
      --exclude '__pycache__' \
      --exclude '.git' \
      --exclude 'data/*.json' \
      "${SOURCE_DIR}/" "${INSTALL_DIR}/"
  else
    cp -a "${SOURCE_DIR}/." "${INSTALL_DIR}/"
  fi
fi

mkdir -p "${INSTALL_DIR}/data" \
  /opt/smart-support-bot-safety/backups \
  /opt/smart-support-bot-safety/staging

# Compatibility symlink for older path references
ln -sfn /opt/smart-support-bot-safety /opt/blackfox-bot-safety || true

if [[ ! -f "${INSTALL_DIR}/.env" ]]; then
  if [[ -f "${INSTALL_DIR}/.env.example" ]]; then
    cp "${INSTALL_DIR}/.env.example" "${INSTALL_DIR}/.env"
    echo "==> Created ${INSTALL_DIR}/.env from .env.example"
    echo "    Edit TELEGRAM_BOT_TOKEN, AI_API_KEY, BOT_ADMIN_IDS before start."
  else
    echo "Missing .env.example — cannot continue."
    exit 1
  fi
fi

if grep -q "replace-with-botfather-token\|sk-replace-me\|YOUR_TELEGRAM_USER_ID" "${INSTALL_DIR}/.env"; then
  echo "==> WARNING: .env still has placeholder values."
fi

echo "==> Creating Python virtualenv and installing dependencies"
cd "${INSTALL_DIR}"
python3 -m venv .venv
.venv/bin/pip install -U pip
.venv/bin/pip install -r requirements.txt

echo "==> Installing systemd units"
install -m 644 "${INSTALL_DIR}/deploy/smart-support-bot.service" /etc/systemd/system/smart-support-bot.service
install -m 644 "${INSTALL_DIR}/deploy/smart-support-bot-watchdog.service" /etc/systemd/system/smart-support-bot-watchdog.service
systemctl daemon-reload
systemctl enable smart-support-bot.service smart-support-bot-watchdog.service

if grep -Eq '^TELEGRAM_BOT_TOKEN=.+:.+' "${INSTALL_DIR}/.env" \
  && ! grep -q 'replace-with-botfather-token' "${INSTALL_DIR}/.env" \
  && grep -Eq '^AI_API_KEY=.+' "${INSTALL_DIR}/.env" \
  && ! grep -q 'sk-replace-me' "${INSTALL_DIR}/.env"; then
  systemctl restart smart-support-bot.service
  systemctl restart smart-support-bot-watchdog.service
  echo "==> Services started"
else
  echo "==> Services enabled but not started (fill .env first)"
fi

echo "==> Done. Status:"
systemctl status smart-support-bot.service --no-pager || true
systemctl status smart-support-bot-watchdog.service --no-pager || true
echo
echo "Next:"
echo "  1) nano ${INSTALL_DIR}/.env"
echo "  2) systemctl restart smart-support-bot.service"
echo "  3) Telegram → admin menu → Chat with Bot / گفتگو با ربات"
