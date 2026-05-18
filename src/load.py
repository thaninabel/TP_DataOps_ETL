import pandas as pd
import psycopg2

from sqlalchemy import create_engine


def get_engine(database_url: str):
    return create_engine(database_url)


def create_tables(conn):

    with conn.cursor() as cur:

        cur.execute("""
        CREATE TABLE IF NOT EXISTS ventes_propres (
            id INTEGER,
            client_email TEXT,
            date_vente DATE,
            montant NUMERIC,
            categorie TEXT
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS ca_par_mois (
            mois TEXT,
            chiffre_affaires NUMERIC,
            nb_transactions INTEGER
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS run_log (
            id SERIAL PRIMARY KEY,
            run_at TIMESTAMP DEFAULT NOW(),
            etape TEXT,
            statut TEXT,
            nb_lignes INTEGER,
            message TEXT
        );
        """)

    conn.commit()


def load_ventes(df, engine):

    df.to_sql(
        "ventes_propres",
        engine,
        if_exists="replace",
        index=False,
        method="multi"
    )

    return len(df)


def load_mart(df, engine):

    df.to_sql(
        "ca_par_mois",
        engine,
        if_exists="replace",
        index=False,
        method="multi"
    )

    return len(df)


def log_etape(conn, etape, statut, nb_lignes=None, message=None):

    with conn.cursor() as cur:

        cur.execute("""
        INSERT INTO run_log (etape, statut, nb_lignes, message)
        VALUES (%s, %s, %s, %s)
        """, (etape, statut, nb_lignes, message))

    conn.commit()