-- Database: asx_eod

-- DROP DATABASE asx_eod;

CREATE DATABASE asx_eod
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_AU.UTF-8'
    LC_CTYPE = 'en_AU.UTF-8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

DROP TABLE IF EXISTS "marketdata";
CREATE TABLE "marketdata"(
    Ticker    TEXT,
    Date     DATE,
    Open  NUMERIC,
    High    NUMERIC,
    Low     NUMERIC,
    Close  NUMERIC,
    Volume  INT
);

CREATE INDEX ON "marketdata"(Date DESC);
CREATE INDEX ON "marketdata"(Ticker);

ALTER TABLE public.marketdata
    ADD CONSTRAINT "Constraint_Data_code" UNIQUE (date, ticker);


psql -c "copy marketdata from '/tmp/20191029.txt' csv" asx_eod;

