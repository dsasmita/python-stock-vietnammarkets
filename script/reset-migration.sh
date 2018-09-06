#!/usr/bin/env bash
alembic downgrade base
rm -rf migrations/versions/*
alembic revision --autogenerate -m "initial DB"
alembic upgrade head